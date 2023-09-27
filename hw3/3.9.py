n = int(input("请输入一个数："))
import random
numlist = []
for i in range(n):
    num = random.randint(1,10)
    numlist.append(num)
    print(num,end=' ')
print()
bn = []
k = 0
for i in range(n):
    num = 1
    for j in range(n):
        if(j != k):
            num *= numlist[j]
    bn.append(num)
    k += 1
    print(num,end=' ')