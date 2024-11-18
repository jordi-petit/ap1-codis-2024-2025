from typing import TypeVar, Optional

T = TypeVar("T")


def cerca_lineal(L: list[T], x: T) -> int | None:
    """
    Si x ∈ L, retorna una posició p tal que L[p] == x.
    Si x ∉ L, retorna None.
    """

    for i in range(len(L)):
        if L[i] == x:
            return i
    return None
