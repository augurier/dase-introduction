g = 1
c = 2
while(abs(g ** 2 - c) > 0.0001):
    g += 0.00001
print("g=%.7f" %g)