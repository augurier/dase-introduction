import numpy as np

M = np.matrix([[2,1],[4,5]])
a0 = np.matrix([[1],[0]])
max1 = 0
max2 = np.linalg.norm(a0, 2)
while(abs(max2-max1) > 0.0000001):S
    v = a0 / max2
    a0 = M * v
    max1 = max2
    max2 = np.linalg.norm(a0, 2)
print(int(max2),v)

