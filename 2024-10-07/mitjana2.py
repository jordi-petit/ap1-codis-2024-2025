"""
Calcular la mitana d'una seqüència de nombres reals positius.
La seqüència acaba amb un nombre negatiu.
"""


import yogi

s = 0
n = 0
x = yogi.read(float)
while x >= 0:
    s = s + x
    n = n + 1
    x = yogi.read(float)
print(s / n)
