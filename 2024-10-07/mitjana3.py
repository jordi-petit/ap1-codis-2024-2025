"""
Calcular la mitana d'una seqüència de nombres reals.
El final de la seqüència es marca amb la paraula 'fi'.
"""


import yogi

s = 0
n = 0
x = yogi.read(str)
while x != 'fi':
    s = s + float(x)
    n = n + 1
    x = yogi.read(str)
print(s / n)
