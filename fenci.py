with open('naozuzhongshuffle2.txt','r',encoding='gbk') as f:
    data = f.readlines()
temp = ""
ciku = []
for i in data:
    if "B-" in i:
        if temp != "" and len(temp)>=3:
            ciku.append(temp)
        temp = ""
        temp += i[0]
    elif "I-" in i:
        temp += i[0]
    else:
        if temp != "" and len(temp)>=3:
            ciku.append(temp)
        temp = ""
with open("ciku.txt",'w',encoding='utf-8') as f:
    for i in ciku:
        f.write(i+'\n')


import jieba

all = []
sent = ""
for i in data:
    if i != "\n":
        sent += i[0]
    else:
        if sent != "":
            all.append(sent)
        sent = ""

print(all)
import jieba
jieba.load_userdict('ciku.txt')
with open('fencinaoleha.txt','w') as f:
    for i in all:
        words = jieba.lcut(i, cut_all=False)
        print(words)
        for j in words:

            if len(j) <= 1:
                for s in j:
                    f.write(s + " " + 'O\n')
            if len(j) > 1:
                if j in ciku:
                    print(j)
                    for a in range(0,len(j)):
                        if a == 0:
                            # print(j[a]+" "+"B\n")
                            f.write(j[a]+" "+"B\n")
                        # if a == len(j)-1:
                        #     f.write(j[a]+" "+"I\n")
                        else:
                            f.write(j[a]+" "+"I\n")
                else:
                    for s in j:
                        f.write(s+" "+'O\n')
        f.write("\n")