import random
import time
def makelist(cnt):
    numlist = []
    for i in range(cnt):
        numlist.append(random.randint(1,100))
    return numlist

def selectsort(numlist):
    print("选择排序：")
    start = time.time()
    l = len(numlist)
    for i in range(l):
        min = i
        for j in range(i+1,l):
            if(numlist[j] < numlist[min]):
                min = j
        numlist[min],numlist[i] = numlist[i],numlist[min]
    end = time.time()
    print("执行时间：%s 秒"%(end-start))
    print("归并排序：")
#时间复杂度O(N^2),运行时间较长，且随数据量增加涨幅大

def mergesort(numlist):
    l = len(numlist)
    if(l <= 1):
        return numlist
    list1 = mergesort(numlist[0:int(l/2):])
    list2 = mergesort(numlist[int(l/2):l:])
    list3 = []
    l1 = len(list1)
    l2 = len(list2)
    i = 0
    j = 0
    while(i < l1 and j < l2):
        if(list1[i] < list2[j]):
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1    
    if(i < l1):
        list3.extend(list1[i::])
    else:
        list3.extend(list2[j::])
    return list3       
#时间复杂度O(NlgN),运行时间较短，且随数据量增加涨幅小     
        

for i in range(1000,5000,1000):
    print("数据量：%d"%i)
    numlist = makelist(i)
    selectsort(numlist[::])
    start = time.time()
    newlist = mergesort(numlist)
    end = time.time()
    print("执行时间：%s 秒"%(end-start))
    print()

    