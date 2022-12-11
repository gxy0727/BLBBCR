import torch
import torch.nn as nn
import torch.nn.functional as F

from fastNLP.models.base_model import BaseModel
from fastNLP.core.const import Const as C
from fastNLP.core.utils import seq_len_to_mask
from fastNLP.embeddings.utils import get_embeddings
from fastNLP.modules.decoder import ConditionalRandomField
from fastNLP.modules.encoder import LSTM,VarLSTM,SelfAttention,VarGRU,TransformerEncoder,MultiHeadAttention,TransformerEncoder,BiAttention,star_transformer
from fastNLP.modules import decoder, encoder
from fastNLP.modules.decoder.crf import allowed_transitions

#
# class BetterBiLSTMCRF(BaseModel):
#
#
#     def __init__(self, embed, num_classes, num_layers=1, hidden_size=100, dropout=0.5,
#                  target_vocab=None):
#
#         super().__init__()
#         self.embed = get_embeddings(embed)
#         self.norm = torch.nn.LayerNorm(self.embed.embedding_dim)
#
#         if num_layers > 1:
#             self.lstm = LSTM(self.embed.embedding_dim, num_layers=num_layers, hidden_size=hidden_size,
#                              bidirectional=True,
#                              batch_first=True, dropout=dropout)
#         else:
#             self.lstm = LSTM(self.embed.embedding_dim, num_layers=num_layers, hidden_size=hidden_size,
#                              bidirectional=True,
#                              batch_first=True)
#         self.liner = nn.Linear(hidden_size * 2, hidden_size * 2 // 3)
#         self.norm2 = torch.nn.LayerNorm(hidden_size * 2 // 3)
#
#         self.SelfAttention = SelfAttention(hidden_size * 2 // 3)
#
#         self.dropout = nn.Dropout(dropout)
#         self.relu = torch.nn.LeakyReLU()
#         self.fc = nn.Linear(hidden_size * 2//3, num_classes)
#
#         trans = None
#         if target_vocab is not None:
#             assert len(
#                 target_vocab) == num_classes, "The number of classes should be same with the length of target vocabulary."
#             trans = allowed_transitions(target_vocab.idx2word, include_start_end=True)
#
#         self.crf = ConditionalRandomField(num_classes, include_start_end_trans=True, allowed_transitions=trans)
#
#     def _forward(self, words, seq_len=None, target=None):
#         words = self.embed(words)
#         words = self.norm(words)
#         feats, _ = self.lstm(words, seq_len=seq_len)
#         feats = self.liner(feats)
#         feats = self.norm2(feats)
#         feats = self.SelfAttention(feats)
#         feats = self.fc(feats)
#         feats = self.dropout(feats)
#         logits = F.log_softmax(feats, dim=-1)
#         mask = seq_len_to_mask(seq_len)
#         if target is None:
#             pred, _ = self.crf.viterbi_decode(logits, mask)
#             return {C.OUTPUT: pred}
#         else:
#             loss = self.crf(logits, target, mask).mean()
#             return {C.LOSS: loss}
#
#     def forward(self, words, seq_len, target):
#         return self._forward(words, seq_len, target)
#
#     def predict(self, words, seq_len):
#         return self._forward(words, seq_len)
class BiVarLSTMSeqLabel(nn.Module):
    r"""
    更复杂的Sequence Labelling模型。结构为Embedding, LayerNorm, 双向LSTM(两层)，FC，LayerNorm，DropOut，FC，CRF。
    """

    def __init__(self, embed, hidden_size, num_classes, dropout=0.3, id2words=None, encoding_type='bmes'):
        r"""

        :param tuple(int,int),torch.FloatTensor,nn.Embedding,numpy.ndarray embed: Embedding的大小(传入tuple(int, int),
            第一个int为vocab_zie, 第二个int为embed_dim); 如果为Tensor, Embedding, ndarray等则直接使用该值初始化Embedding
        :param int hidden_size: LSTM的隐层大小
        :param int num_classes: 有多少个类
        :param float dropout: LSTM中以及DropOut层的drop概率
        :param dict id2words: tag id转为其tag word的表。用于在CRF解码时防止解出非法的顺序，比如'BMES'这个标签规范中，'S'
            不能出现在'B'之后。这里也支持类似与'B-NN'，即'-'前为标签类型的指示，后面为具体的tag的情况。这里不但会保证
            'B-NN'后面不为'S-NN'还会保证'B-NN'后面不会出现'M-xx'(任何非'M-NN'和'E-NN'的情况。)
        :param str encoding_type: 支持"BIO", "BMES", "BEMSO", 只有在id2words不为None的情况有用。
        """
        super().__init__()

        self.Embedding = get_embeddings(embed)
        self.norm1 = torch.nn.LayerNorm(self.Embedding.embedding_dim)
        hidden_size = 384
        self.Rnn = encoder.LSTM(input_size=self.Embedding.embedding_dim, hidden_size=hidden_size, num_layers=2,
                                bidirectional=True, batch_first=True)
        hidden_size = 384
        self.Linear1 = nn.Linear(hidden_size * 2, hidden_size * 2 // 3)
        self.norm2 = torch.nn.LayerNorm(hidden_size * 2 // 3)
        self.TransformerEncoder = TransformerEncoder(num_layers=5,d_model=768,n_head=4)
        # self.starTransformer = star_transformer.StarTransformer(num_layers=5,hidden_size=768,num_head=4,head_dim=768)
        self.relu = torch.nn.LeakyReLU()
        self.drop = torch.nn.Dropout(dropout)
        self.Linear2 = nn.Linear(hidden_size * 2 // 3, num_classes)

        if id2words is None:
            self.Crf = decoder.crf.ConditionalRandomField(num_classes, include_start_end_trans=False)
        else:
            self.Crf = decoder.crf.ConditionalRandomField(num_classes, include_start_end_trans=False,
                                                          allowed_transitions=allowed_transitions(id2words,
                                                                                                  encoding_type=encoding_type))

    def _decode(self, x, mask):
        r"""
        :param torch.FloatTensor x: [batch_size, max_len, tag_size]
        :param torch.ByteTensor mask: [batch_size, max_len]
        :return torch.LongTensor, [batch_size, max_len]
        """
        tag_seq, _ = self.Crf.viterbi_decode(x, mask)
        return tag_seq

    def _internal_loss(self, x, y, mask):
        r"""
        Negative log likelihood loss.
        :param x: Tensor, [batch_size, max_len, tag_size]
        :param y: Tensor, [batch_size, max_len]
        :param mask: Tensor, [batch_size, max_len]
        :return loss: a scalar Tensor

        """
        x = x.float()
        y = y.long()
        total_loss = self.Crf(x, y, mask)
        return torch.mean(total_loss)

    def _forward(self, words, seq_len, target=None):
        r"""
        :param torch.LongTensor words: [batch_size, mex_len]
        :param torch.LongTensor seq_len:[batch_size, ]
        :param torch.LongTensor target: [batch_size, max_len]
        :return y: If truth is None, return list of [decode path(list)]. Used in testing and predicting.
                   If truth is not None, return loss, a scalar. Used in training.
        """
        words = words.long()
        seq_len = seq_len.long()
        mask = seq_len_to_mask(seq_len, max_len=words.size(1))

        target = target.long() if target is not None else None

        if next(self.parameters()).is_cuda:
            words = words.cuda()
        x = self.Embedding(words)
        x = self.norm1(x)
        x = self.TransformerEncoder(x)
        y = x
        y,_ = self.Rnn(y)
        x = x+y
        x = self.Linear1(x)
        x = self.norm2(x)
        x = self.relu(x)
        x = self.drop(x)
        x = self.Linear2(x)
        if target is not None:
            return {"loss": self._internal_loss(x, target, mask)}
        else:
            return {"pred": self._decode(x, mask)}

    def forward(self, words, seq_len, target):
        r"""

        :param torch.LongTensor words: [batch_size, mex_len]
        :param torch.LongTensor seq_len: [batch_size, ]
        :param torch.LongTensor target: [batch_size, max_len], 目标
        :return torch.Tensor: a scalar loss
        """
        return self._forward(words, seq_len, target)

    def predict(self, words, seq_len):
        r"""

        :param torch.LongTensor words: [batch_size, mex_len]
        :param torch.LongTensor seq_len: [batch_size, ]
        :return torch.LongTensor: [batch_size, max_len]
        """
        return self._forward(words, seq_len)