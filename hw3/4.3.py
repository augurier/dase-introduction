def insertsort(list1):
    l = len(list1)
    for i in range(l):
        for j in range(i):
            if(list1[j] > list1[i]):
                num = list1[i]
                for k in range(i,j,-1):
                    list1[k] = list1[k-1]
                list1[j] = num
                break
    return list1
            
datalist = [int(x) for x in input("请输入一串数，用逗号分隔：").split(',')]
datalist = insertsort(datalist)
for i in datalist:
    print(i,end=" ")