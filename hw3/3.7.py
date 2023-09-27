a,b = input("请输入两个数：").split(' ')
a = int(a)
b = int(b)
if(a < b):
    a,b = b,a
while(a % b != 0):
    a,b = b,a%b
print(b)