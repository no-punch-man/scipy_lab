import matplotlib.pyplot as plt
import numpy as np
import scipy as sc

f = open(r'sources\large.txt', 'r')
lines = f.readlines()
l = []
for line in lines:
    l.append(line.rstrip())
N = int(l[0])
A = np.array([i.split() for i in l[1:N + 1]], dtype = np.float64)
b = np.array(l[-1].split(), dtype = np.float64)
x = np.linalg.solve(A, b)

fig, ax = plt.subplots()
fig.set_figheight(7)
fig.set_figwidth(14)
ax.grid(True)
ax.bar(np.arange(x.size), x, width = 0.5)

fig.savefig("large" + ".png")
