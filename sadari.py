# -*- coding: utf-8 -*-
import random
def sadari(text):
    print text
    arr = text.split(",")
    random.shuffle(arr)
    res = ""
    for i in range(len(arr)):
        res += arr[i]+"           "+"\\n"

    return res


