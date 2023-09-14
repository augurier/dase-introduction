x = input("x=")
y = input("y=")
z = input("z=")
w = input("w=")
l1 = [x,y,z,w]
l1 = sorted(l1,reverse=True)
for i in l1:
    print(i,end=' ')