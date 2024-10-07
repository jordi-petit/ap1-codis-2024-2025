"""
Comptar el nombre de pics en una seqüència de nombres enters. Un nombre és un pic si és més gran que els dos nombres entre els quals es troba.
"""


import yogi

pics = 0

x = yogi.scan(int)
if  x != None:
    y = yogi.scan(int)
    if y != None:
        z = yogi.scan(int)
        while z != None:
            if x < y > z:
                pics = pics + 1
            x,y,z = y,z,yogi.scan(int)

print(pics)