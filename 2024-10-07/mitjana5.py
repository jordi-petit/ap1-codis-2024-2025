"""
Calcular la mitana d'una seqüència de nombres reals.
Versió amb tokens.
"""


import yogi

s = 0
n = 0
for x in yogi.tokens(float):
    s = s + x
    n = n + 1
print(s / n)