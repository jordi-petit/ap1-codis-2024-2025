from typing import TypeVar, Optional
import random
import time

T = TypeVar("T")


def ordena_per_seleccio(L: list[T]) -> None:
    """Ordena la llista L en ordre creixent."""

    n = len(L)
    for i in range(n - 1):
        p = pos_minim(L, i)
        L[i], L[p] = L[p], L[i]


def pos_minim(L: list[T], i: int) -> int:
    """Retorna la posició de l'element més petit en L[i:]. Prec: 0<=i<n."""
    n = len(L)
    p = i
    for j in range(i + 1, n):
        if L[j] < L[p]:
            p = j
    return p


n = 20000
L = [random.randint(0, n) for i in range(n)]
t0 = time.time()
ordena_per_seleccio(L)
t1 = time.time()
print(n, t1 - t0)
n *= 2
