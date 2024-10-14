"""
Pintar un arbre fractal.
"""


from yogi import *
from turtle import *


def pintar_arbre(n: int, d: float) -> None:
    if n == 0:
        forward(d)
        backward(d)
    else:
        forward(d/3)
        left(60)
        pintar_arbre(n - 1, d * 2 / 3)
        right(120)
        pintar_arbre(n - 1, d * 2 / 3)
        left(60)
        backward(d/3)



def main() -> None:
    n = read(int)
    d = read(float)
    left(90)
    # hideturtle()
    pintar_arbre(n, d)
    done()


if __name__ == "__main__":
    main()
