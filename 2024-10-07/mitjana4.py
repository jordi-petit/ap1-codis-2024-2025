"""
Calcular la mitana d'una seqüència de nombres reals.
Versió amb scan.

Redirecció de l'entrada i de la sortida:
python3 mitjana4.py < dades.txt > mitana.txt
"""


import yogi

s = 0
n = 0
x = yogi.scan(float)
while x != None:
    s = s + x
    n = n + 1
    x = yogi.scan(float)
print(s / n)