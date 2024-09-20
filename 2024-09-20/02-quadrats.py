import turtle

mida = 100

j = 1
while j <= 36:

    i = 1
    while i <= 4:
        turtle.forward(mida)
        turtle.right(90)
        i = i + 1

    turtle.right(10)
    j = j + 1

turtle.done()
