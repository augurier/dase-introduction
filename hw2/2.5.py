c = int(input("请输入一个数："))
g = c/2
i = 0
while(abs(g * g - c) > 0.00000001):
    g = (g + c/g)/2
    i += 1
    print("%d: %.13f" %(i,g))