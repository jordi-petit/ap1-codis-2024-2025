"""
Comptar el nombre de vegades que es repeteix consecutivament un nombre en una seqüència de nombres enters.
"""

import yogi

n = 0

x = yogi.scan(int)
if x != None:
    y = yogi.scan(int)
    while y != None:
        if x == y:
            n = n + 1
        x, y = y, yogi.scan(int)

print(n)
