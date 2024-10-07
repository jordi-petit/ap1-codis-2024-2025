"""
Esbrinar si apareix la paraula 'gat' a l'entrada.
"""

import yogi

hi_ha_gats = False
paraula = yogi.scan(str)
while paraula != None and not hi_ha_gats:
    if paraula == 'gat':
        hi_ha_gats = True
    paraula = yogi.scan(str)

if hi_ha_gats:
    print("hi ha gats")
else:
    print("no hi ha gats")
