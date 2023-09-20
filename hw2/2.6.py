c = int(input("请输入一个数："))
g = c/4
i = 0
print("g = c/4: ")
while(abs(g * g - c) > 0.00000001):
    g = (g + c/g)/2
    i += 1
    print("%d: %.13f" %(i,g))
#由于精度问题，g初始值略微影响逼近后的结果