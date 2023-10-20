import numpy as np
import pandas as pd

def statistic(file):
    f = open(file)
    dictionary = {}
    for line in f.readlines():
        if(len(line) > 10):
            mark = [',','.',':','\'s',';','?','(',')']
            for m in mark:
                line = line.replace(m,' ')
            linearrt = line.strip().split(" ")
            for char in linearrt:
                if(char not in dictionary):
                    dictionary[char] = 1
                else:
                    dictionary[char] += 1

    a = sorted(dictionary.items(),key = lambda x:x[1],reverse=True)
    return a

def printwords(file,n):
    a = statistic(file)
    for i in range(n):
        print(a[i])

printwords("poem.txt",10)
