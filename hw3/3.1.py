num = float(input("请输入一个小数："))
a = int(num)
b = num - a
ans = bin(a)[2:]
str_b = "."
while(b != 0):
    b *= 2
    if(b >= 1):
        str_b += "1"
        b -= 1
    else:
        str_b += "0"
ans += str_b
print(ans)