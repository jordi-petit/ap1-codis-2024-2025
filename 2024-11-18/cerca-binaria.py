from typing import TypeVar, Optional

T = TypeVar("T")


def cerca(L: list[T], x: T) -> int | None:
    """
    Si x ∈ L, retorna una posició p tal que L[p] == x.
    Si x ∉ L, retorna None.
    Prec: L es troba ordenada creixentment.
    """

    n = len(L)
    e, d = 0, n - 1
    while e <= d:
        m = (e + d) // 2
        if L[m] > x:
            d = m - 1
        elif L[m] < x:
            e = m + 1
        else:
            return m
    return None
