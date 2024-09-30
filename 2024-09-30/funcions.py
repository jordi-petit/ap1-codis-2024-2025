from yogi import read


def maxim2(a: int, b: int) -> int:
    """Retorna el màxim de dos enters."""
    if a > b:
        return a
    return b


def maxim3(a: int, b:int, c:int) -> int:
    """Retorna el màxim de tres enters."""
    return maxim2(a, maxim2(b,c))


def valor_absolut(a: int) -> int:
    """Retorna el el valor absolut d'un enter."""

    if a > 0:
        return a
    return -a


x = read(int)
y = read(int)
print(maxim2(x, y))
