import math
def func(a):
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i == 0):
            print("不是质数")
            return
    print("是质数")
    
a = int(input("请输入一个数： "))
func(a)

        