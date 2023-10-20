from matplotlib import pyplot as plt
import numpy as np
data = np.random.normal(0, 1, size = 100)
print(data)

fig, ax = plt.subplots()
ax.hist(data, bins = 30)
ax.set_ylim(ymin = 0, ymax = 20)
ax.set_xlim(xmin = -5, xmax = 5)
plt.show(block = True)
