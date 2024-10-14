"""
Pintar una fractal de Koch.
"""


from yogi import *
from turtle import *


def pintar_corba_koch(n: int, d: float) -> None:
    """Pinta una corba de Koch de n nivells i longitud d."""

    if n == 0:
        forward(d)
    else:
        pintar_corba_koch(n-1, d/3)
        left(60)
        pintar_corba_koch(n-1, d/3)
        right(120)
        pintar_corba_koch(n-1, d/3)
        left(60)
        pintar_corba_koch(n-1, d/3)


def pintar_floc_koch(n: int, d: float) -> None:
    """Pinta un floc de Koch de n nivells i longitud d."""

    for _ in range(3):
        pintar_corba_koch(n, d)
        right(120)


def main() -> None:
    n = read(int)
    d = read(float)
    hideturtle()
    speed(0)
    pintar_floc_koch(n, d)
    done()


if __name__ == "__main__":
    main()
