def suma(llista: list[int]) -> int:
    """retorna la suma dels elements de llista"""

    s = 0
    for element in llista:
        s += element
    return s


def suma2(llista: list[int]) -> int:
    """retorna la suma dels elements de llista"""

    s = 0
    for i in range(len(llista)):
        s += llista[i]
    return s


def producte_escalar(vector1: list[float], vector2: list[float]) -> float:
    """Retorna el producte escalar de vector1 i vector2. Prec: vector1 i vector2 tenen la mateixa mida."""

    s = 0.0
    for i in range(len(vector1)):
        s += vector1[i] * vector2[i]
    return s


def producte_escalar2(vector1: list[float], vector2: list[float]) -> float:
    """Retorna el producte escalar de vector1 i vector2. Prec: vector1 i vector2 tenen la mateixa mida."""

    s = 0.0
    for a, b in zip(vector1, vector2):
        s += a * b
    return s


def doblar_elements(llista: list[int]) -> None:
    """Dobla cada element de la llista"""

    for x in llista:
        x *= 2


def doblar_enter(x: int) -> None:
    x *= 2


def es_capicua(L: list[int]) -> bool:
    for i in range(len(L) // 2):
        if L[i] != L[len(L) - i - 1]:
            return False
    return True


L = [1, 2, 3]
doblar_elements(L)
print(L)

i = 3
doblar_enter(i)
print(i)
