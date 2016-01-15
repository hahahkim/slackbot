# -*- coding: utf-8 -*-
import random


#load welfare data
f = open("welfare_db")
data = f.read().replace("\n", "")
f.close()
data = eval(data)

def get_yasik(text=""):
    print text
    if text == u"랜덤":
        r = random.randint(0,len(data)-1)
        res = data[r][0]+"\\n"+data[r][1]
    else:
        res_list = []
        for i in range(len(data)):
            if data[i][0].find(text.encode('utf-8')) >= 0:
                res_list += [i]
        if len(res_list) == 1:
            res = data[res_list[0]][0]+"\\n"+data[res_list[0]][1]
        else:
            res = ""
            for i in res_list:
                res += data[i][0]+"\\n"

    if res == "":
        res = u"/야식 : 전체목록\\n/야식 치킨 : 치킨 검색 결과. 결과가 하나면 자세히 나옵니다.\\n/야식 랜덤 : 랜덤 야식"

    return res
