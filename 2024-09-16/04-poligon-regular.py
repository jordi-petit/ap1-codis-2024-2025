# programa que pinta un poligon regular

import yogi
import turtle

mida = yogi.read(int)
costats = yogi.read(int)
gir = 360 / costats

i = 1
while i <= costats:
    turtle.forward(mida)
    turtle.right(gir)
    i = i + 1

turtle.done()
