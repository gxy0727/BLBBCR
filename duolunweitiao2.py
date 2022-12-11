from fastNLP import Tester
from fastNLP.models import STSeqLabel



# import os
# os.environ['CUDA_VISIBLE_DEVICES'] = '2'
all = []
word = []
with open('fencinaole.txt','r',encoding='gbk') as f:
    a = f.read()
    words= []
    targets = []
    for i in a.split("\n"):
        try:
            a,b = i.split(" ")
            word.append(a)
            words.append(a)
            targets.append(b)
        except:
            all.append((words,targets))
            words = []
            targets = []
# print(all)
word = set(word)
word_dict = dict()
j = 0
for i in word:
    word_dict[i] = j
    j += 1
from fastNLP import DataSet,Instance
dataset2 = DataSet()
for i in all:
    t = []
    e = ""
    ww = []
    for a in i[0]:
        t.append(word_dict[a])
        e += a
        ww.append(a)
    # words = jieba.lcut(e, cut_all=False)
    # print(words)
    if len(i[0])<=510:
        pass
        instance = Instance(
            raw_chars = ww,
            chars=i[0],
                            target=i[1],


                            seq_len=len(i[0]),

                            # words=ww
        )
        # print(instance)
        if len(i[0]) != 0:
            dataset2.append(instance)
        else:
            pass
    else:
        pass







all = []
word = []
with open('naozuzhong333.txt','r',encoding='gbk') as f:
    a = f.read()
    words= []
    targets = []
    for i in a.split("\n"):
        try:
            a,b = i.split(" ")
            word.append(a)
            words.append(a)
            targets.append(b)
        except:
            all.append((words,targets))
            words = []
            targets = []
# print(all)
word = set(word)
word_dict = dict()
j = 0
for i in word:
    word_dict[i] = j
    j += 1
from fastNLP import DataSet,Instance
dataset = DataSet()
for i in all:
    t = []
    e = ""
    ww = []
    for a in i[0]:
        t.append(word_dict[a])
        e += a
        ww.append(a)
    # words = jieba.lcut(e, cut_all=False)
    # print(words)
    if len(i[0])<=510:
        pass
        instance = Instance(
            raw_chars = ww,
            chars=i[0],
                            target=i[1],


                            seq_len=len(i[0]),

                            # words=ww
        )
        # print(instance)
        if len(i[0]) != 0:
            dataset.append(instance)
        else:
            pass
    else:
        pass














temp = dataset
dataset = dataset2
dataset2 = temp




























from fastNLP import Vocabulary
vocab = Vocabulary()
vocab1 = Vocabulary()

vocab.from_dataset(dataset, field_name='chars',no_create_entry_dataset=dataset2)
vocab.index_dataset(dataset, field_name='chars')
vocab.index_dataset(dataset2, field_name='chars')
vocab1.from_dataset(dataset, field_name='target',no_create_entry_dataset=dataset2)
vocab1.index_dataset(dataset, field_name='target')
vocab1.index_dataset(dataset2, field_name='target')
print(vocab1.word2idx)
dataset.rename_field('chars', 'words')
# dataset.set_input('chars')
dataset.set_input('seq_len')
dataset.set_input('words')
dataset.set_target('target')
dataset.set_target('seq_len')
dataset.set_input('target')


dataset.print_field_meta()
train_data = dataset
dev_data = dataset
test_data =dataset



train_data, test_data = dataset.split(0.15)
train_data, dev_data = train_data.split(0.15)
train_data = dataset
train_data.set_input('seq_len')
train_data.set_input('words')
train_data.set_target('target')
train_data.set_target('seq_len')
train_data.set_input('target')
test_data.set_input('seq_len')
test_data.set_input('words')
test_data.set_target('target')
test_data.set_target('seq_len')
test_data.set_input('target')
dev_data.set_input('seq_len')
dev_data.set_input('words')
dev_data.set_target('target')
dev_data.set_target('seq_len')
dev_data.set_input('target')
from fastNLP.embeddings import BertEmbedding,StaticEmbedding
from lstm import BiVarLSTMSeqLabel

embed = BertEmbedding(vocab, model_dir_or_name='cn-wwm-ext',requires_grad=True)

model = BiVarLSTMSeqLabel(embed=embed, num_classes=len(vocab1), hidden_size=200,
              encoding_type="bio")
from fastNLP import SpanFPreRecMetric
from torch.optim import Adam
from fastNLP import LossInForward
metric = SpanFPreRecMetric(tag_vocab=vocab1,only_gross=False)
optimizer = Adam(model.parameters(), lr=2e-5)
loss = LossInForward()

from fastNLP import Trainer
import torch
device= 0 if torch.cuda.is_available() else 'cpu'
# device = 'cpu'
trainer = Trainer(train_data=train_data, model=model, loss=loss, optimizer=optimizer, batch_size=8 ,
                    dev_data=dev_data, metrics=metric, device=device,n_epochs=20)
trainer.train()

#
# from fastNLP import Tester
# tester = Tester(test_data, model, metrics=metric)
# tester.test()


embed.save('bertwww8')
# model.to('cpu')
# torch.save(model, 'model.pkl')
# vocab.save('vocab')
# vocab1.save('vocab1')
#
# from fastNLP import Tester
# tester = Tester(test_data, model, metrics=metric)
# tester.test()






# from fastNLP.io.model_io import ModelSaver
# saver = ModelSaver("mox.pkl")
# saver.save_pytorch(model)






#
# model.to('cpu')
#

# torch.cuda.empty_cache()
# import time
# time.sleep(10)
# print('oooooooooooooooooooooo')
#



#
#
# dataset2.rename_field('chars', 'words')
# # dataset.set_input('chars')
# dataset2.set_input('seq_len')
# dataset2.set_input('words')
# dataset2.set_target('target')
# dataset2.set_target('seq_len')
# dataset2.set_input('target')
#
#
# dataset2.print_field_meta()
# train_data, test_data = dataset2.split(0.10)
# train_data, dev_data = train_data.split(0.10)
# train_data.set_input('seq_len')
# train_data.set_input('words')
# train_data.set_target('target')
# train_data.set_target('seq_len')
# train_data.set_input('target')
# test_data.set_input('seq_len')
# test_data.set_input('words')
# test_data.set_target('target')
# test_data.set_target('seq_len')
# test_data.set_input('target')
# dev_data.set_input('seq_len')
# dev_data.set_input('words')
# dev_data.set_target('target')
# dev_data.set_target('seq_len')
# dev_data.set_input('target')
#
#
#
# model = BiVarLSTMSeqLabel(embed=embed, num_classes=len(vocab1), hidden_size=200,
#               encoding_type="bio")
# from fastNLP import SpanFPreRecMetric
# from torch.optim import Adam
# from fastNLP import LossInForward
# metric = SpanFPreRecMetric(tag_vocab=vocab1,only_gross=False)
# optimizer = Adam(model.parameters(), lr=2e-5)
# loss = LossInForward()
#
# from fastNLP import Trainer
# import torch
# device= 0 if torch.cuda.is_available() else 'cpu'
# # device = 'cpu'
# trainer = Trainer(train_data=train_data, model=model, loss=loss, optimizer=optimizer, batch_size=1 ,
#                     dev_data=dev_data, metrics=metric, device=device,n_epochs=10)
# trainer.train()
#
# from fastNLP import Tester
# tester = Tester(test_data, model, metrics=metric)
# tester.test()
