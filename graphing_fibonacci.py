import numpy as np
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt
g = open("fibonacci.txt", "r")
for i, l in enumerate(g):
    pass
ridade_arv = i + 1
g.close()
g = open("fibonacci.txt", "r")
xjada = []
yjada = []
for i in range(ridade_arv):
    paarike = g.readline()
    y1, x1 = paarike.split(",")
    y1 = int(y1.strip("["))
    x1 = int(x1.strip("]\n"))
    xjada.append(x1)
    yjada.append(y1)

g.close()

y = np.array(yjada)
x = np.array(xjada)

b, m = polyfit(x, y, 1)

plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')
plt.show()



