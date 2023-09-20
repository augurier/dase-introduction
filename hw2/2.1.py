numList = [1,2,3]
numLine = [[1],[2],[3]]
def maxMult(num):
    if(num <= len(numList)):
        return numList[num - 1]
    maxNum = 0
    m = 0
    n = 0
    for first in range(1,int(num/2) + 1):
        second = num - first
        if(maxMult(first) * maxMult(second) > maxNum):
            maxNum = maxMult(first) * maxMult(second)
            m = first
            n = second
    numList.append(maxNum)
    numLine.append(numLine[m - 1] + numLine[n - 1])
    return maxNum
#动态规划思想：从小到大记录每个数的正数数列，这样大的数就可以拆分成两个子问题递归解决

n = int(input("请输入一个数: "))
for i in range(1,n+1):
    a = maxMult(i)
print(numLine[n - 1])
