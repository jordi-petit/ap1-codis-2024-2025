from turtle import *


def pintar_quadrat(mida: float) -> None:
    """Pinta un quadrat de la mida donada al punt on es troba la tortuga i la deixa igual."""

    for i in range(4):
        forward(mida)
        right(90)


def pintar_molts_quadrats_rotats(mida: float, quants: int) -> None:
    """Pinta quants quadrats rotats."""

    for i in range(quants):
        pintar_quadrat(mida)
        right(360 / quants)


pintar_molts_quadrats_rotats(100, 10)
done()
