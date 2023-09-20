import random
import math
def count(times):
    sum = 0
    for i in range(times):
        x = random.uniform(2,3)
        y = random.uniform(0,21)
        d = x*x + 4*x*math.sin(x)
        if(y <= d):
            sum += 1
    return sum/times*21

print("ans = %.8f" %count(1000000))