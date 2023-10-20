import numpy as np
x = np.array([1, -1, 4])
y = np.array([2, 1, 3])
z = np.array([1, 3, -1])
ans = np.cov([x,y,z])
print(ans)

a0 = np.matrix([[1],[0],[0]])
max1 = 0
max2 = np.linalg.norm(a0, 2)
while(abs(max2-max1) > 0.0000001):
    v = a0 / max2
    a0 = ans * v
    max1 = max2
    max2 = np.linalg.norm(a0, 2)
print(int(max2),v)
