c = int(input("请输入一个数："))
g = c/2
i = 0
while(abs(g * g * g - c) > 0.00000001):
    g = (2*g + c/g/g)/3
    i += 1
    print("%d: %.13f" %(i,g))