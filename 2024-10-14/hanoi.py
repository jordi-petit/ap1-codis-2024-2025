def hanoi(n: int, ori: str, dst: str, aux: str ) ->  None:
    """Escriu com moure n discos de la torre ori a la torre dst passant per la torre aux. Prec: n >= 0."""

    if n > 0:
        hanoi(n - 1, ori, aux, dst)
        print(ori, '->', dst)
        hanoi(n - 1, aux, dst, ori)


if __name__ == "__main__":
    hanoi(8, 'A', 'C', 'B')
