import re
import numpy as np
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt

fibonacci = [0, 1]
lemmikjada = []
i = 1
while True:
    f = open('fibonacci.txt', 'a')

    j22gid = "01"
    print("jagamine toimub", i, "ga")
    for j in range(0, 20 * i):
        a = (fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]) % i
        fibonacci.append(a)
        j22gid = j22gid + str(a)
    for k in range(len(fibonacci) // 2):
        jaotised = re.findall(j22gid[:k], j22gid)
        if len(j22gid) - len(jaotised) * k < k:
            paarike = [int(len(jaotised[0])), i]
            lemmikjada.append(paarike)
            f.write("%s\n" % paarike)
            f.close()
            break
    fibonacci = [0, 1]
    i = i + 1




