from typing import TypeVar, Optional
import random
import time

T = TypeVar("T")


def ordena_per_insercio(L: list[T]) -> None:
    """Ordena la llista L en ordre creixent."""

    n = len(L)
    for i in range(1, n):
        insercio_ordenada(L, i)


def insercio_ordenada(L: list[T], i: int) -> None:
    x = L[i]
    j = i - 1
    while j >= 0 and L[j] > x:
        L[j + 1] = L[j]
        j -= 1
    L[j + 1] = x


n = 1000
while n < 1000000:
    L = [random.randint(0, n) for i in range(n)]
    t0 = time.time()
    ordena_per_insercio(L)
    t1 = time.time()
    print(n, t1 - t0)
    n *= 2
