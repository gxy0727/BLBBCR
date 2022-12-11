# import spacy
# from spacy.language import Language
# from spacy.matcher import PhraseMatcher
# from spacy.tokens import Span
# from spacy.matcher import Matcher
# import re
# nlp = spacy.load("zh_core_web_trf")
# from fastNLP import Vocabulary
# vocab = Vocabulary()
# vocab1 = Vocabulary()
# vocab = vocab.load('vocab')
# import torch
# vocab1 = vocab1.load('vocab1')
# #1:构建“院前急救药品名称”字典
# #添加用户专有名词
# proper_nouns1 =["rtpA","rt-pa","rt-PA","阿加曲班","阿司匹林","阿司匹林肠溶片","阿替普酶","阿替普酶溶栓","阿替谱酶静",
#             "阿托伐他汀","阿托伐他汀钙","阿托伐他汀钙片","奥拉西坦","奥美拉唑","奥美拉唑钠","奥扎格雷","拜阿司匹林",
#             "倍他司汀","补钾","丹参","丹参多酚","丹红","低分子肝素","地芬尼多","地西泮","碘普罗胺","丁苯酞","复发甘草片",
#             "复方脑肽节苷酯","甘露醇","谷红","红花黄色素","琥珀酸美托洛尔","加巴喷丁胶囊","甲磺酸倍他司汀片",
#             "苦碟子","利伐沙班","硫酸氢氯吡格雷","罗沙替丁","氯吡格雷","脑苷肌肽","脑心通","尼麦角林片","尼莫地平","尿激酶",
#             "泮托拉唑","泮托拉唑钠","瑞舒伐他汀","瑞舒伐他汀片","舒血宁","疏血通","他汀","天麻素","天舒片","乌拉地尔",
#             "硝苯地平","硝苯地平缓释片","缬沙坦氢氯噻嗪","辛伐他汀","醒脑静","醒脑注射液","眩晕片","血清脑颗粒","血栓通",
#             "血栓心脉宁","盐酸倍他司汀", "盐酸川穹","盐酸罗沙班", "盐酸罗沙替丁醋酸酯","盐酸异丙嗪", "养血清脑颗粒", "依达拉奉",
#             "依达拉奉清除自由基","异丙嗪", "银杏", "尤瑞克林", "镇静剂"]
# nlp.tokenizer.pkuseg_update_user_dict(proper_nouns1)
# yqjjypmc = ["rtpA","rt-pa","rt-PA","阿加曲班","阿司匹林","阿司匹林肠溶片","阿替普酶","阿替普酶溶栓","阿替谱酶静",
#             "阿托伐他汀","阿托伐他汀钙","阿托伐他汀钙片","奥拉西坦","奥美拉唑","奥美拉唑钠","奥扎格雷","拜阿司匹林",
#             "倍他司汀","补钾","丹参","丹参多酚","丹红","低分子肝素","地芬尼多","地西泮","碘普罗胺","丁苯酞","复发甘草片",
#             "复方脑肽节苷酯","甘露醇","谷红","红花黄色素","琥珀酸美托洛尔","加巴喷丁胶囊","甲磺酸倍他司汀片",
#             "苦碟子","利伐沙班","硫酸氢氯吡格雷","罗沙替丁","氯吡格雷","脑苷肌肽","脑心通","尼麦角林片","尼莫地平","尿激酶",
#             "泮托拉唑","泮托拉唑钠","瑞舒伐他汀","瑞舒伐他汀片","舒血宁","疏血通","他汀","天麻素","天舒片","乌拉地尔",
#             "硝苯地平","硝苯地平缓释片","缬沙坦氢氯噻嗪","辛伐他汀","醒脑静","醒脑注射液","眩晕片","血清脑颗粒","血栓通",
#             "血栓心脉宁","盐酸倍他司汀", "盐酸川穹","盐酸罗沙班", "盐酸罗沙替丁醋酸酯","盐酸异丙嗪", "养血清脑颗粒", "依达拉奉",
#             "依达拉奉清除自由基","异丙嗪", "银杏", "尤瑞克林", "镇静剂"]
# yqjjypmc_patterns = list(nlp.pipe(yqjjypmc))
# # print("yqjjypmc_patterns:", yqjjypmc_patterns)
# matcher1 = PhraseMatcher(nlp.vocab)
# matcher1.add("YQJJYPMC", yqjjypmc_patterns)
#
# #定义定制化yqjjypmc_ner组件
# @Language.component("yqjjypmc_ner")
# def yqjjypmc_ner_function(doc):
#     # 把matcher应用到doc上
#     matches = matcher1(doc)
#     # 为每一个匹配结果生成一个Span并赋予标签"YQJJYPMC"
#     spans = [Span(doc, start, end, label="YQJJYPMC") for match_id, start, end in matches]
#     # 用匹配到的span覆盖doc.ents
#     doc.ents = spans
#     return doc
#
#
# #2:构建“院前急救给药方式”字典
# #添加用户专有名词
# proper_nouns2 = ["静滴","静滴治疗","静脉","静脉泵入","静脉推注","静推","口服","输液","推注"]
# nlp.tokenizer.pkuseg_update_user_dict(proper_nouns2)
# yqjjgyfs=["静滴","静滴治疗","静脉","静脉泵入","静脉推注","静推","口服","输液","推注"]
# yqjjgyfs_patterns = list(nlp.pipe(yqjjgyfs))
# # print("yqjjgyfs_patterns:", yqjjgyfs_patterns)
# matcher2 = PhraseMatcher(nlp.vocab)
# matcher2.add("YQJJGYFS", yqjjgyfs_patterns)
#
# # 定义定制化yqjjgyfs_ner组件
# @Language.component("yqjjgyfs_ner")
# def yqjjgyfs_ner_function(doc):
#     # 把matcher应用到doc上
#     matches = matcher2(doc)
#     # 为每一个匹配结果生成一个Span并赋予标签"YQJJGYFS"
#     spans = [Span(doc, start, end, label="YQJJGYFS") for match_id, start, end in matches]
#     doc.ents = list(doc.ents)+spans
#     # 用匹配到的span添加到doc.ents
#     return doc
#
# #3:构建“来本院检查项目”字典
# #添加用户专有名词
# proper_nouns3 = ["CT","CTA","CT检查","CT颅脑","CT颅脑平扫","磁共振","磁共振检查","复查CT","颅脑+胸部CT","颅脑CT","颅脑CT平扫",
#                  "头颈CT","头颈CTA","头颅、胸部CT","头颅CT","头颅CTA","头颅CT检查","头颅MRI","膝关节X线","心电图","胸部CT平扫",
#                  "血常规"]
# nlp.tokenizer.pkuseg_update_user_dict(proper_nouns3)
# lbyjcxmjg= ["CT","CTA","CT检查","CT颅脑","CT颅脑平扫","磁共振","磁共振检查","复查CT","颅脑+胸部CT","颅脑CT","颅脑CT平扫",
#                  "头颈CT","头颈CTA","头颅、胸部CT","头颅CT","头颅CTA","头颅CT检查","头颅MRI","膝关节X线","心电图","胸部CT平扫",
#                  "血常规"]
# lbyjcxmjg_patterns = list(nlp.pipe(lbyjcxmjg))
# # print("lbyjcxmjg_patterns:", lbyjcxmjg_patterns)
# matcher3 = PhraseMatcher(nlp.vocab)
# matcher3.add("LBYJCXMJG", lbyjcxmjg_patterns)
#
# # 定义定制化lbyjcxmjg_ner组件
# @Language.component("lbyjcxmjg_ner")
# def lbyjcxmjg_ner_function(doc):
#     # 把matcher应用到doc上
#     matches = matcher3(doc)
#     # 为每一个匹配结果生成一个Span并赋予标签"LBYJCXMJG"
#     spans = [Span(doc, start, end, label="LBYJCXMJG") for match_id, start, end in matches]
#     doc.ents = list(doc.ents)+spans
#     # 用匹配到的span添加到doc.ents
#     return doc
#
# #4:构建“外院治疗方法”字典
# #添加用户专有名词
# proper_nouns4 = ["曾自服药物","对症处理","对症治疗","服用降压药","服用口服药物","规律服用","降糖治疗","介入治疗","禁食","具体诊疗不详",
#                  "具体治疗不详","口服癫痫药物","口服药物识别","扩容","生活方式干预","生活方式干预","输液（具体不详）",
#                  "营养神经等对症处理","长期口服","诊疗情况不详","自服降压药","自服药物"]
# nlp.tokenizer.pkuseg_update_user_dict(proper_nouns4)
# wyzlff= ["曾自服药物","对症处理","对症治疗","服用降压药","服用口服药物","规律服用","降糖治疗","介入治疗","禁食","具体诊疗不详",
#                  "具体治疗不详","口服癫痫药物","口服药物识别","扩容","生活方式干预","生活方式干预","输液（具体不详）",
#                  "营养神经等对症处理","长期口服","诊疗情况不详","自服降压药","自服药物"]
# wyzlff_patterns = list(nlp.pipe(wyzlff))
# # print("wyzlff_patterns:", wyzlff_patterns)
# matcher4 = PhraseMatcher(nlp.vocab)
# matcher4.add("WYZLFF", wyzlff_patterns)
#
# # 定义定制化wyzlff_ner组件
# @Language.component("wyzlff_ner")
# def wyzlff_ner_function(doc):
#     # 把matcher应用到doc上
#     matches = matcher4(doc)
#     # 为每一个匹配结果生成一个Span并赋予标签"WYZLFF"
#     spans = [Span(doc, start, end, label="WYZLFF") for match_id, start, end in matches]
#     doc.ents = list(doc.ents)+spans
#     # 用匹配到的span添加到doc.ents
#     return doc
#
# #5:构建“院前急救方式”字典
# #添加用户专有名词
# proper_nouns5 = ["阿加曲班抗凝","按摩","保守治疗","补钠","补液","持续膀胱冲洗","促醒护脑","改善脑细胞代谢","改善循环","静脉溶栓治疗",
#                  "溶栓治疗","输液治疗","护脑","护胃","换药","活血化瘀","降颅压","降压药物应用","降脂","降脂稳定斑块","抗感染",
#                  "抗凝","抗栓","抗血小板","抗血小板聚集","抗炎","抗炎药物","控制血压","控制血压及血糖","留置尿管","输血",
#                  "调节血脂","调整稳定斑块","调脂","脱水降颅压","稳斑","稳定板块","营养",
#                  "营养神经","针灸"]
# nlp.tokenizer.pkuseg_update_user_dict(proper_nouns5)
# yqjjfs= ["阿加曲班抗凝","按摩","保守治疗","补钠","补液","持续膀胱冲洗","促醒护脑","改善脑细胞代谢","改善循环","静脉溶栓治疗",
#          "溶栓治疗","输液治疗","护脑","护胃","换药","活血化瘀","降颅压","降压药物应用","降脂","降脂稳定斑块","抗感染",
#          "抗凝","抗栓","抗血小板","抗血小板聚集","抗炎","抗炎药物","控制血压","控制血压及血糖","留置尿管","输血",
#          "调节血脂","调整稳定斑块","调脂","脱水降颅压","稳斑","稳定板块","营养",
#          "营养神经","针灸"]
# yqjjfs_patterns = list(nlp.pipe(yqjjfs))
# # print("yqjjfs_patterns:", yqjjfs_patterns)
# matcher5 = PhraseMatcher(nlp.vocab)
# matcher5.add("YQJJFS", yqjjfs_patterns)
#
# # 定义定制化yqjjfs_ner组件
# @Language.component("yqjjfs_ner")
# def yqjjfs_ner_function(doc):
#     # 把matcher应用到doc上
#     matches = matcher5(doc)
#     # 为每一个匹配结果生成一个Span并赋予标签"YQJJFS"
#     spans = [Span(doc, start, end, label="YQJJFS") for match_id, start, end in matches]
#     doc.ents = list(doc.ents)+spans
#     # 用匹配到的span添加到doc.ents
#     return doc
#
# #6:构建“外院治疗药物”字典
# #添加用户专有名词
# proper_nouns6 = ["抗癫痫药物","血塞通","压氏达及缬沙坦","曲克芦丁","胰岛素","二甲双胍","格列美脲","稳心颗粒","通心络","具体不详"]
# nlp.tokenizer.pkuseg_update_user_dict(proper_nouns6)
# wyzlyw= ["抗癫痫药物","血塞通","压氏达及缬沙坦","曲克芦丁","胰岛素","二甲双胍","格列美脲","稳心颗粒","通心络","具体不详"]
# wyzlyw_patterns = list(nlp.pipe(wyzlyw))
# # print("wyzlyw_patterns:", wyzlyw_patterns)
# matcher6 = PhraseMatcher(nlp.vocab)
# matcher6.add("WYZLYW", wyzlyw_patterns)
#
# # 定义定制化wyzlyw_ner组件
# @Language.component("wyzlyw_ner")
# def wyzlyw_ner_function(doc):
#     # 把matcher应用到doc上
#     matches = matcher6(doc)
#     # 为每一个匹配结果生成一个Span并赋予标签"WYZLYW"
#     spans = [Span(doc, start, end, label="WYZLYW") for match_id, start, end in matches]
#     doc.ents = list(doc.ents)+spans
#     # 用匹配到的span添加到doc.ents
#     return doc
#
# #7:构建“NIHSS入院评分”规则
# #添加用户专有名词
# proper_nouns7 = ["NIHSS","评分","：","分"]
# nlp.tokenizer.pkuseg_update_user_dict(proper_nouns7)
# NIHSSRYPF_patterns = [{"ORTH":"NIHSS"},{"ORTH":"评分","OP":"?"},{"ORTH":"：","OP":"?"},{"LIKE_NUM": True},{"ORTH":"分"}]
# matcher7 = Matcher(nlp.vocab)
# matcher7.add("NIHSSRYPF", [NIHSSRYPF_patterns]) #别忘记给模式加[]
#
# # 定义定制化NIHSSRYPF_ner组件
# @Language.component("NIHSSRYPF_ner")
# def NIHSSRYPF_ner_function(doc):
#     # 把matcher应用到doc上
#     matches = matcher7(doc)
#     # 为每一个匹配结果生成一个Span并赋予标签"NIHSSRYPF"
#     spans = [Span(doc, start, end, label="NIHSSRYPF") for match_id, start, end in matches]
#     doc.ents = list(doc.ents)+spans
#     # 用匹配到的span添加到doc.ents
#     return doc
#
# #8:构建“来院交通工具”规则
# #添加用户专有名词
# proper_nouns8 = ["120","私家车","转至","送","送至","我院","医院","本院"]
# nlp.tokenizer.pkuseg_update_user_dict(proper_nouns8)
# lyjtgj_patterns = [{"ORTH": {"IN": ["120","私家车"]}},{"ORTH": {"IN": ["转至","送","送至"]}},{"ORTH":{"IN": ["我院","医院","本院"]}}]
# matcher8 = Matcher(nlp.vocab)
# matcher8.add("LYJTGJ", [lyjtgj_patterns]) #别忘记给模式加[]
# # 定义定制化lyjtgj_ner组件
# @Language.component("lyjtgj_ner")
# def lyjtgj_ner_function(doc):
#     # 把matcher应用到doc上
#     matches = matcher8(doc)
#     # 为每一个匹配结果生成一个Span并赋予标签"LYJTGJ"
#     spans = [Span(doc, start, end, label="LYJTGJ") for match_id, start, end in matches]
#     doc.ents = list(doc.ents)+spans
#     # 用匹配到的span添加到doc.ents
#     return doc
#
# #9:构建“院前急救给药计量”规则
# #添加用户专有名词
# proper_nouns9 = ["mg","g","mg/kg"]
# nlp.tokenizer.pkuseg_update_user_dict(proper_nouns9)
# yqjjgyjl_patterns = [{"TEXT": {"REGEX":"\d+(\.\d+)?"}},{"ORTH":{"IN": ["mg","g","mg/kg"]}}]
# matcher9 = Matcher(nlp.vocab)
# matcher9.add("YQJJGYJL", [yqjjgyjl_patterns]) #别忘记给模式加[]
#
# # 定义定制化yqjjgyjl_ner组件
# @Language.component("yqjjgyjl_ner")
# def yqjjgyjl_ner_function(doc):
#     # 把matcher应用到doc上
#     matches = matcher9(doc)
#     # 为每一个匹配结果生成一个Span并赋予标签"YQJJGYJL"
#     spans = [Span(doc, start, end, label="YQJJGYJL") for match_id, start, end in matches]
#     doc.ents = list(doc.ents)+spans
#     # 用匹配到的span添加到doc.ents
#     return doc
#
# #10:构建“外院诊断名称”规则
# #添加用户专有名词
#
# # 定义定制化wyzdmc_ner组件
# @Language.component("wyzdmc_ner")
# def wyzdmc_ner_function(doc):
#     expression = r"(?<=诊断为“).*?(?=”)|(?<=诊断“).*?(?=”)|(?<=既往有“).*?(?=”)|(?<=既往“).*?(?=”)"
#     for match in re.finditer(expression, doc.text):
#         start, end = match.span()
#         span = doc.char_span(start, end,label="WYZDMC")
#         #spans = [Span(doc, start, end, label="YQJJGYJL")]
#         # This is a Span object or None if match doesn't map to valid token sequence
#         if span is not None:
#             # print("Found match:", span.text,span.label_)
#             doc.ents = list(doc.ents) + [span]
#     return doc
#
# #1：把"wyzlff_ner"组件加入到流程中，紧跟在"ner"组件后面
# nlp.add_pipe("yqjjypmc_ner", after="ner")
# #2：把"yqjjgyfs_ner"组件加入到流程中，紧跟在"yqjjypmc_ner"组件后面
# nlp.add_pipe("yqjjgyfs_ner", after="yqjjypmc_ner")
# #3：把"lbyjcxmjg_ner"组件加入到流程中，紧跟在"yqjjgyfs_ner"组件后面
# nlp.add_pipe("lbyjcxmjg_ner", after="yqjjgyfs_ner")
# #4：把"wyzlff_ner"组件加入到流程中，紧跟在"lbyjcxmjg_ner"组件后面
# nlp.add_pipe("wyzlff_ner", after="lbyjcxmjg_ner")
# #5：把"yqjjfs_ner"组件加入到流程中，紧跟在"wyzlff_ner"组件后面
# nlp.add_pipe("yqjjfs_ner", after="wyzlff_ner")
# #6：把"wyzlyw_ner"组件加入到流程中，紧跟在"yqjjfs_ner"组件后面
# nlp.add_pipe("wyzlyw_ner", after="yqjjfs_ner")
# #7：把"NIHSSRYPF_ner"组件加入到流程中，紧跟在"wyzlyw_ner"组件后面
# nlp.add_pipe("NIHSSRYPF_ner", after="wyzlyw_ner")
# #8：把"lyjtgj_ner"组件加入到流程中，紧跟在"NIHSSRYPF_ner"组件后面
# nlp.add_pipe("lyjtgj_ner", after="NIHSSRYPF_ner")
# #9：把"yqjjgyjl_ner"组件加入到流程中，紧跟在"lyjtgj_ner"组件后面
# nlp.add_pipe("yqjjgyjl_ner", after="lyjtgj_ner")
# #10：把"wyzdmc_ner"组件加入到流程中，紧跟在"yqjjgyjl_ner"组件后面
# nlp.add_pipe("wyzdmc_ner", after="yqjjgyjl_ner")
#
# def guize(batch_x,pred_dict):
#     # print(pred_dict)
#     seq = ""
#     target_guize_all = []
#     for i, o in zip(batch_x['words'].cpu().numpy(), pred_dict['pred'].cpu().numpy()):
#         seq = ""
#         for j in i:
#             seq += vocab.idx2word[j]
#         seq = seq.replace("<pad>", '')
#         # print(guize(seq,o,vocab1=self.vocab1))
#         # target_guize_all.append(guize(seq, o, vocab1=self.vocab1))
#
#     # print(nlp.pipe_names)
#     # 处理文本，打印doc.ents的文本和标签
#         doc = nlp(seq)
#         # print(target)
#         data = []
#         for i in o:
#             data.append(vocab1.idx2word[i])
#
#         ent_list = [(ent.label_, ent.start_char, ent.end_char) for ent in doc.ents]
#         # print("===")
#         # print(ent_list)
#         # print(seq)
#         # print("========================================================================================================")
#         # print(data)
#         for i in ent_list:
#             data[i[1]]="B-"+i[0]
#             for j in range(i[1]+1,i[2]):
#                 data[j] = "I-" + i[0]
#         # print(data)
#         # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#         target_guize = []
#         for i in data:
#             target_guize.append(vocab1.word2idx[i])
#         target_guize_all.append(target_guize)
#     # print(target_guize)
#
#     target_guize_all = torch.tensor(target_guize_all)
#     pred_dict = dict()
#     pred_dict['pred'] = target_guize_all
#     # print(pred_dict)
#
#     return pred_dict
# # print(guize("输液治疗，"))






















import spacy
from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from spacy.matcher import Matcher
import re
nlp = spacy.load("zh_core_web_trf")
from fastNLP import Vocabulary
vocab = Vocabulary()
vocab1 = Vocabulary()
vocab = vocab.load('vocab')
import torch
vocab1 = vocab1.load('vocab1')
#1:构建“院前急救药品名称”字典
#添加用户专有名词
proper_nouns1 =["rtpA","rt-pa","rt-PA","阿加曲班","阿司匹林","阿司匹林肠溶片","阿替普酶","阿替普酶溶栓","阿替谱酶静",
            "阿托伐他汀","阿托伐他汀钙","阿托伐他汀钙片","奥拉西坦","奥美拉唑","奥美拉唑钠","奥扎格雷","拜阿司匹林",
            "倍他司汀","补钾","丹参","丹参多酚","丹红","低分子肝素","地芬尼多","地西泮","碘普罗胺","丁苯酞","复发甘草片",
            "复方脑肽节苷酯","甘露醇","谷红","红花黄色素","琥珀酸美托洛尔","加巴喷丁胶囊","甲磺酸倍他司汀片",
            "苦碟子","利伐沙班","硫酸氢氯吡格雷","罗沙替丁","氯吡格雷","脑苷肌肽","脑心通","尼麦角林片","尼莫地平","尿激酶",
            "泮托拉唑","泮托拉唑钠","瑞舒伐他汀","瑞舒伐他汀片","舒血宁","疏血通","他汀","天麻素","天舒片","乌拉地尔",
            "硝苯地平","硝苯地平缓释片","缬沙坦氢氯噻嗪","辛伐他汀","醒脑静","醒脑注射液","眩晕片","血清脑颗粒","血栓通",
            "血栓心脉宁","盐酸倍他司汀", "盐酸川穹","盐酸罗沙班", "盐酸罗沙替丁醋酸酯","盐酸异丙嗪", "养血清脑颗粒", "依达拉奉",
            "依达拉奉清除自由基","异丙嗪", "银杏", "尤瑞克林", "镇静剂"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns1)
yqjjypmc = ["rtpA","rt-pa","rt-PA","阿加曲班","阿司匹林","阿司匹林肠溶片","阿替普酶","阿替普酶溶栓","阿替谱酶静",
            "阿托伐他汀","阿托伐他汀钙","阿托伐他汀钙片","奥拉西坦","奥美拉唑","奥美拉唑钠","奥扎格雷","拜阿司匹林",
            "倍他司汀","补钾","丹参","丹参多酚","丹红","低分子肝素","地芬尼多","地西泮","碘普罗胺","丁苯酞","复发甘草片",
            "复方脑肽节苷酯","甘露醇","谷红","红花黄色素","琥珀酸美托洛尔","加巴喷丁胶囊","甲磺酸倍他司汀片",
            "苦碟子","利伐沙班","硫酸氢氯吡格雷","罗沙替丁","氯吡格雷","脑苷肌肽","脑心通","尼麦角林片","尼莫地平","尿激酶",
            "泮托拉唑","泮托拉唑钠","瑞舒伐他汀","瑞舒伐他汀片","舒血宁","疏血通","他汀","天麻素","天舒片","乌拉地尔",
            "硝苯地平","硝苯地平缓释片","缬沙坦氢氯噻嗪","辛伐他汀","醒脑静","醒脑注射液","眩晕片","血清脑颗粒","血栓通",
            "血栓心脉宁","盐酸倍他司汀", "盐酸川穹","盐酸罗沙班", "盐酸罗沙替丁醋酸酯","盐酸异丙嗪", "养血清脑颗粒", "依达拉奉",
            "依达拉奉清除自由基","异丙嗪", "银杏", "尤瑞克林", "镇静剂"]
yqjjypmc_patterns = list(nlp.pipe(yqjjypmc))
# print("yqjjypmc_patterns:", yqjjypmc_patterns)
matcher1 = PhraseMatcher(nlp.vocab)
matcher1.add("YQJJYPMC", yqjjypmc_patterns)

#定义定制化yqjjypmc_ner组件
@Language.component("yqjjypmc_ner")
def yqjjypmc_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher1(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"YQJJYPMC"
    spans = [Span(doc, start, end, label="YQJJYPMC") for match_id, start, end in matches]
    # 用匹配到的span覆盖doc.ents
    doc.ents = spans
    return doc


#2:构建“院前急救给药方式”字典
#添加用户专有名词
proper_nouns2 = ["静滴","静滴治疗","静脉","静脉泵入","静脉推注","静推","口服","输液","推注"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns2)
yqjjgyfs=["静滴","静滴治疗","静脉","静脉泵入","静脉推注","静推","口服","输液","推注"]
yqjjgyfs_patterns = list(nlp.pipe(yqjjgyfs))
# print("yqjjgyfs_patterns:", yqjjgyfs_patterns)
matcher2 = PhraseMatcher(nlp.vocab)
matcher2.add("YQJJGYFS", yqjjgyfs_patterns)

# 定义定制化yqjjgyfs_ner组件
@Language.component("yqjjgyfs_ner")
def yqjjgyfs_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher2(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"YQJJGYFS"
    spans = [Span(doc, start, end, label="YQJJGYFS") for match_id, start, end in matches]
    doc.ents = list(doc.ents)+spans
    # 用匹配到的span添加到doc.ents
    return doc

#3:构建“来本院检查项目”字典
#添加用户专有名词
proper_nouns3 = ["CTA","磁共振检查","复查CT","颅脑+胸部CT","头颅、胸部CT","膝关节X线"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns3)
lbyjcxmjg= ["CTA","磁共振检查","复查CT","颅脑+胸部CT","头颅、胸部CT","膝关节X线"]
lbyjcxmjg_patterns = list(nlp.pipe(lbyjcxmjg))
# print("lbyjcxmjg_patterns:", lbyjcxmjg_patterns)
matcher3 = PhraseMatcher(nlp.vocab)
matcher3.add("LBYJCXMJG", lbyjcxmjg_patterns)

# 定义定制化lbyjcxmjg_ner组件
@Language.component("lbyjcxmjg_ner")
def lbyjcxmjg_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher3(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"LBYJCXMJG"
    spans = [Span(doc, start, end, label="LBYJCXMJG") for match_id, start, end in matches]
    doc.ents = list(doc.ents)+spans
    # 用匹配到的span添加到doc.ents
    return doc

#4:构建“外院治疗方法”字典
#添加用户专有名词
proper_nouns4 = ["曾自服药物","对症处理","对症治疗","服用降压药","服用口服药物","规律服用","降糖治疗","介入治疗","禁食","具体诊疗不详",
                 "具体治疗不详","口服癫痫药物","口服药物识别","扩容","生活方式干预","生活方式干预","输液（具体不详）",
                 "营养神经等对症处理","长期口服","诊疗情况不详","自服降压药","自服药物"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns4)
wyzlff= ["曾自服药物","对症处理","对症治疗","服用降压药","服用口服药物","规律服用","降糖治疗","介入治疗","禁食","具体诊疗不详",
                 "具体治疗不详","口服癫痫药物","口服药物识别","扩容","生活方式干预","生活方式干预","输液（具体不详）",
                 "营养神经等对症处理","长期口服","诊疗情况不详","自服降压药","自服药物"]
wyzlff_patterns = list(nlp.pipe(wyzlff))
# print("wyzlff_patterns:", wyzlff_patterns)
matcher4 = PhraseMatcher(nlp.vocab)
matcher4.add("WYZLFF", wyzlff_patterns)

# 定义定制化wyzlff_ner组件
@Language.component("wyzlff_ner")
def wyzlff_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher4(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"WYZLFF"
    spans = [Span(doc, start, end, label="WYZLFF") for match_id, start, end in matches]
    doc.ents = list(doc.ents)+spans
    # 用匹配到的span添加到doc.ents
    return doc

#5:构建“院前急救方式”字典
#添加用户专有名词
proper_nouns5 = ["阿加曲班抗凝","按摩","保守治疗","补钠","补液","持续膀胱冲洗","促醒护脑","改善脑细胞代谢","改善循环","静脉溶栓治疗",
                 "溶栓治疗","输液治疗","护脑","护胃","换药","活血化瘀","降颅压","降压药物应用","降脂","降脂稳定斑块","抗感染",
                 "抗凝","抗栓","抗血小板","抗血小板聚集","抗炎","抗炎药物","控制血压","控制血压及血糖","留置尿管","输血",
                 "调节血脂","调整稳定斑块","调脂","脱水降颅压","稳斑","稳定板块","营养",
                 "营养神经","针灸"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns5)
yqjjfs= ["阿加曲班抗凝","按摩","保守治疗","补钠","补液","持续膀胱冲洗","促醒护脑","改善脑细胞代谢","改善循环","静脉溶栓治疗",
         "溶栓治疗","输液治疗","护脑","护胃","换药","活血化瘀","降颅压","降压药物应用","降脂","降脂稳定斑块","抗感染",
         "抗凝","抗栓","抗血小板","抗血小板聚集","抗炎","抗炎药物","控制血压","控制血压及血糖","留置尿管","输血",
         "调节血脂","调整稳定斑块","调脂","脱水降颅压","稳斑","稳定板块","营养",
         "营养神经","针灸"]
yqjjfs_patterns = list(nlp.pipe(yqjjfs))
# print("yqjjfs_patterns:", yqjjfs_patterns)
matcher5 = PhraseMatcher(nlp.vocab)
matcher5.add("YQJJFS", yqjjfs_patterns)

# 定义定制化yqjjfs_ner组件
@Language.component("yqjjfs_ner")
def yqjjfs_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher5(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"YQJJFS"
    spans = [Span(doc, start, end, label="YQJJFS") for match_id, start, end in matches]
    doc.ents = list(doc.ents)+spans
    # 用匹配到的span添加到doc.ents
    return doc

#6:构建“外院治疗药物”字典
#添加用户专有名词
proper_nouns6 = ["抗癫痫药物","血塞通","压氏达及缬沙坦","曲克芦丁","胰岛素","二甲双胍","格列美脲","稳心颗粒","通心络","具体不详"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns6)
wyzlyw= ["抗癫痫药物","血塞通","压氏达及缬沙坦","曲克芦丁","胰岛素","二甲双胍","格列美脲","稳心颗粒","通心络","具体不详"]
wyzlyw_patterns = list(nlp.pipe(wyzlyw))
# print("wyzlyw_patterns:", wyzlyw_patterns)
matcher6 = PhraseMatcher(nlp.vocab)
matcher6.add("WYZLYW", wyzlyw_patterns)

# 定义定制化wyzlyw_ner组件
@Language.component("wyzlyw_ner")
def wyzlyw_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher6(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"WYZLYW"
    spans = [Span(doc, start, end, label="WYZLYW") for match_id, start, end in matches]
    doc.ents = list(doc.ents)+spans
    # 用匹配到的span添加到doc.ents
    return doc

#7:构建“NIHSS入院评分”规则
#添加用户专有名词
proper_nouns7 = ["NIHSS","评分","：","分"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns7)
NIHSSRYPF_patterns = [{"ORTH":"NIHSS"},{"ORTH":"评分","OP":"?"},{"ORTH":"：","OP":"?"},{"LIKE_NUM": True},{"ORTH":"分"}]
matcher7 = Matcher(nlp.vocab)
matcher7.add("NIHSSRYPF", [NIHSSRYPF_patterns]) #别忘记给模式加[]

# 定义定制化NIHSSRYPF_ner组件
@Language.component("NIHSSRYPF_ner")
def NIHSSRYPF_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher7(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"NIHSSRYPF"
    spans = [Span(doc, start, end, label="NIHSSRYPF") for match_id, start, end in matches]
    doc.ents = list(doc.ents)+spans
    # 用匹配到的span添加到doc.ents
    return doc

#8:构建“来院交通工具”规则
#添加用户专有名词
proper_nouns8 = ["120","私家车","转至","送","送至","我院","医院","本院"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns8)
lyjtgj_patterns = [{"ORTH": {"IN": ["120","私家车"]}},{"ORTH": {"IN": ["转至","送","送至"]}},{"ORTH":{"IN": ["我院","医院","本院"]}}]
matcher8 = Matcher(nlp.vocab)
matcher8.add("LYJTGJ", [lyjtgj_patterns]) #别忘记给模式加[]
# 定义定制化lyjtgj_ner组件
@Language.component("lyjtgj_ner")
def lyjtgj_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher8(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"LYJTGJ"
    spans = [Span(doc, start, end, label="LYJTGJ") for match_id, start, end in matches]
    doc.ents = list(doc.ents)+spans
    # 用匹配到的span添加到doc.ents
    return doc

#9:构建“院前急救给药计量”规则
#添加用户专有名词
proper_nouns9 = ["mg","g","mg/kg"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns9)
yqjjgyjl_patterns = [{"TEXT": {"REGEX":"\d+(\.\d+)?"}},{"ORTH":{"IN": ["mg","g","mg/kg"]}}]
matcher9 = Matcher(nlp.vocab)
matcher9.add("YQJJGYJL", [yqjjgyjl_patterns]) #别忘记给模式加[]

# 定义定制化yqjjgyjl_ner组件
@Language.component("yqjjgyjl_ner")
def yqjjgyjl_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher9(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"YQJJGYJL"
    spans = [Span(doc, start, end, label="YQJJGYJL") for match_id, start, end in matches]
    doc.ents = list(doc.ents)+spans
    # 用匹配到的span添加到doc.ents
    return doc

#10:构建“外院诊断名称”规则
#添加用户专有名词

# 定义定制化wyzdmc_ner组件
@Language.component("wyzdmc_ner")
def wyzdmc_ner_function(doc):
    expression = r"(?<=诊断为“).*?(?=”)|(?<=诊断“).*?(?=”)|(?<=既往有“).*?(?=”)|(?<=既往“).*?(?=”)"
    for match in re.finditer(expression, doc.text):
        start, end = match.span()
        span = doc.char_span(start, end,label="WYZDMC")
        #spans = [Span(doc, start, end, label="YQJJGYJL")]
        # This is a Span object or None if match doesn't map to valid token sequence
        if span is not None:
            # print("Found match:", span.text,span.label_)
            doc.ents = list(doc.ents) + [span]
    return doc



#11:构建“院前检查项目”字典
#添加用户专有名词
proper_nouns11 = ["CRP","CT脑灌注","DSA检查","彩超","测血压","查血压","电子喉镜","妇科B超","肝功能","急诊凝血全套","颈部血管彩超","颈动脉CTA","颈动脉彩超",
                  "颈椎CT","空腹血糖","颅脑、胸部CT","颅脑;颅颈血管MRA","泌尿系B超","脑灌注","脑血管CTA","尿常规","凝血功能","葡萄糖","神经电生理",
                  "头颅CT及头颈CTA","头颅MRI及CTA","头颅磁共振","头颅磁共振及CTA检查","头颅平扫磁共振","头颅腰椎MR","头胸CT","心电检查报告","心梗五连",
                  "心脏彩超","胸椎MRI","血糖和血脂"]
nlp.tokenizer.pkuseg_update_user_dict(proper_nouns11)
yqjcxm= ["CRP","CT脑灌注","DSA检查","彩超","测血压","查血压","电子喉镜","妇科B超","肝功能","急诊凝血全套","颈部血管彩超","颈动脉CTA","颈动脉彩超",
                  "颈椎CT","空腹血糖","颅脑、胸部CT","颅脑;颅颈血管MRA","泌尿系B超","脑灌注","脑血管CTA","尿常规","凝血功能","葡萄糖","神经电生理",
                  "头颅CT及头颈CTA","头颅MRI及CTA","头颅磁共振","头颅磁共振及CTA检查","头颅平扫磁共振","头颅腰椎MR","头胸CT","心电检查报告","心梗五连",
                  "心脏彩超","胸椎MRI","血糖和血脂"]
yqjcxm_patterns = list(nlp.pipe(yqjcxm))
# print("lbyjcxmjg_patterns:", lbyjcxmjg_patterns)
matcher11 = PhraseMatcher(nlp.vocab)
matcher11.add("YQJCXM", yqjcxm_patterns)

# 定义定制化lbyjcxmjg_ner组件
@Language.component("yqjcxm_ner")
def yqjcxm_ner_function(doc):
    # 把matcher应用到doc上
    matches = matcher11(doc)
    # 为每一个匹配结果生成一个Span并赋予标签"LBYJCXMJG"
    spans = [Span(doc, start, end, label="YQJCXM") for match_id, start, end in matches]
    doc.ents = list(doc.ents)+spans
    # 用匹配到的span添加到doc.ents
    return doc


#1：把"wyzlff_ner"组件加入到流程中，紧跟在"ner"组件后面
nlp.add_pipe("yqjjypmc_ner", after="ner")
#2：把"yqjjgyfs_ner"组件加入到流程中，紧跟在"yqjjypmc_ner"组件后面
nlp.add_pipe("yqjjgyfs_ner", after="yqjjypmc_ner")
#3：把"lbyjcxmjg_ner"组件加入到流程中，紧跟在"yqjjgyfs_ner"组件后面
nlp.add_pipe("lbyjcxmjg_ner", after="yqjjgyfs_ner")
#4：把"wyzlff_ner"组件加入到流程中，紧跟在"lbyjcxmjg_ner"组件后面
nlp.add_pipe("wyzlff_ner", after="lbyjcxmjg_ner")
#5：把"yqjjfs_ner"组件加入到流程中，紧跟在"wyzlff_ner"组件后面
nlp.add_pipe("yqjjfs_ner", after="wyzlff_ner")
#6：把"wyzlyw_ner"组件加入到流程中，紧跟在"yqjjfs_ner"组件后面
nlp.add_pipe("wyzlyw_ner", after="yqjjfs_ner")
#7：把"NIHSSRYPF_ner"组件加入到流程中，紧跟在"wyzlyw_ner"组件后面
nlp.add_pipe("NIHSSRYPF_ner", after="wyzlyw_ner")
#8：把"lyjtgj_ner"组件加入到流程中，紧跟在"NIHSSRYPF_ner"组件后面
nlp.add_pipe("lyjtgj_ner", after="NIHSSRYPF_ner")
#9：把"yqjjgyjl_ner"组件加入到流程中，紧跟在"lyjtgj_ner"组件后面
nlp.add_pipe("yqjjgyjl_ner", after="lyjtgj_ner")
#10：把"wyzdmc_ner"组件加入到流程中，紧跟在"yqjjgyjl_ner"组件后面
nlp.add_pipe("wyzdmc_ner", after="yqjjgyjl_ner")
#11：把"yqjcxm_ner"组件加入到流程中，紧跟在"wyzdmc_ner"组件后面
nlp.add_pipe("yqjcxm_ner", after="wyzdmc_ner")


def guize(batch_x,pred_dict):
    # print(pred_dict)
    seq = ""
    target_guize_all = []
    for i, o in zip(batch_x['words'].cpu().numpy(), pred_dict['pred'].cpu().numpy()):
        seq = ""
        for j in i:
            seq += vocab.idx2word[j]
        seq = seq.replace("<pad>", '')
        # print(guize(seq,o,vocab1=self.vocab1))
        # target_guize_all.append(guize(seq, o, vocab1=self.vocab1))

    # print(nlp.pipe_names)
    # 处理文本，打印doc.ents的文本和标签
        doc = nlp(seq)
        # print(target)
        data = []
        for i in o:
            data.append(vocab1.idx2word[i])

        ent_list = [(ent.label_, ent.start_char, ent.end_char) for ent in doc.ents]
        # print("===")
        # print(ent_list)
        # print(seq)
        # # print("========================================================================================================")
        # print(data)
        for i in ent_list:
            data[i[1]]="B-"+i[0]
            for j in range(i[1]+1,i[2]):
                data[j] = "I-" + i[0]
        # print(data)
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        target_guize = []
        for i in data:
            target_guize.append(vocab1.word2idx[i])
        target_guize_all.append(target_guize)
    # print(target_guize)

    target_guize_all = torch.tensor(target_guize_all)
    pred_dict = dict()
    pred_dict['pred'] = target_guize_all
    # print(pred_dict)

    return pred_dict

def predict_guize(text:str,ta):
    doc = nlp(text)
    # print(target)
    data = []
    for i in ta:
        data.append(vocab1.idx2word[i])
    ent_list = [(ent.label_, ent.start_char, ent.end_char) for ent in doc.ents]
    for i in ent_list:
        data[i[1]] = "B-" + i[0]
        for j in range(i[1] + 1, i[2]):
            data[j] = "I-" + i[0]
    ta = []
    for i in data:
        ta.append(vocab1.word2idx[i])
    return ta
# print(guize("输液治疗，"))