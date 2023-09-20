import random
import math
def pi1(times):
    sum = 0
    for i in range(times):
        x = random.random()
        y = random.random()
        d = x*x + y*y
        if(d <= 1):
            sum += 1
    return sum/times*4

def pi2(times):
    sum = 0
    for i in range(times):
        mid = (i+0.5)/times
        sum += 1/times * math.sqrt(1 - mid ** 2)
    return sum*4

def pi3(times):
    sum = 1
    for i in range(1,times):
        sum += (-1) ** i / (2 * i + 1)
    return sum*4

print("pi1=%.10f" %pi1(1000000))
print("pi2=%.10f" %pi2(1000000))
print("pi3=%.10f" %pi3(1000000))