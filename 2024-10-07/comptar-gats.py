"""
Comptar quants cops apareix la paraula 'gat' a l'entrada.
"""


import yogi


gats = 0

for paraula in yogi.tokens(str):
    if paraula == 'gat':
        gats = gats + 1

print(gats)