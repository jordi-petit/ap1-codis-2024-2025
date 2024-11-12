"""
Trobar la llista de tots els nombres primers de 0 a m.
"""


def es_primer(n: int) -> bool:
    """Indica si el natural n és primer o no."""

    if n <= 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True


def primers(m: int) -> list[int]:
    """Donat un natural m, retorna la llista ordenada de tots els nombres primers de 0 a m."""

    return [n for n in range(m + 1) if es_primer(n)]


def primers2(m: int) -> list[int]:
    """Donat un natural m, retorna la llista ordenada de tots els nombres primers de 0 a m."""

    bs = garbell(m)
    return [n for n in range(m + 1) if bs[n]]


def garbell(m: int) -> list[bool]:
    """Retorna una llista de m+1 booleans on a la pos i es diu si i és primer o no"""

    bs = [False, False] + [True] * (m - 1)
    i = 0
    while i * i <= m:
        if bs[i]:
            j = i * i
            while j <= m:
                if bs[j]:
                    bs[j] = False
                j += i
        i += 1
    return bs


def main() -> None:
    print(len(primers2(1000000)))


if __name__ == "__main__":
    main()
