import random
import time
from typing import TypeVar

T = TypeVar("T")


def ordenacio_per_fusio(L: list[T]) -> list[T]:
    """Retorna la llista L ordenada de menor a major."""

    n = len(L)
    if n <= 1:
        return L
    else:
        m = n // 2
        return fusio(ordenacio_per_fusio(L[:m]), ordenacio_per_fusio(L[m:]))


def fusio(L1: list[T], L2: list[T]) -> list[T]:
    """Retorna la fusió ordenada de les llistes ordenades L1 i L2."""

    R = []
    i1, i2 = 0, 0
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            R.append(L1[i1])
            i1 += 1
        else:
            R.append(L2[i2])
            i2 += 1
    R.extend(L1[i1:])
    R.extend(L2[i2:])
    return R


n = 200000
L = [random.randint(0, n) for i in range(n)]
t0 = time.time()
ordenacio_per_fusio(L)
t1 = time.time()
print(n, t1 - t0)
n *= 2
