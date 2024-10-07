"""
Calcular la mitana d'una seqüència de nombres reals.
El nombre d'elements es dóna com a primer nombre de la seqüència.
"""


import yogi

n = yogi.read(int)
s = 0
for i in range(n):
    x = yogi.read(float)
    s = s + x
print(s / n)