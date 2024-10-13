"""
Escriure un nombre en binari (del dret).
"""


def escriu_en_binari(n: int) -> None:
    """Escriu un número n en binari. Precondició: n >= 0"""

    if n < 2:
        print(n, end='')
    else:
        escriu_en_binari(n // 2)
        print(n % 2, end='')


def main() -> None:
    for i in range(32):
        print(i, end=': ')
        escriu_en_binari(i)
        print()


if __name__ == '__main__':
    main()