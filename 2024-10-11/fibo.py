"""
Nombres de Fibonacci recursius.
"""


def fibo_lent(n: int) -> int:
    """Retorna l'n-èsim número de Fibonnaci per n >= 0."""

    if n <= 1:
        return n
    else:
        return fibo_lent(n-1) + fibo_lent(n-2)


def fibo_rapid(n: int) -> int:
    """Retorna l'n-èsim número de Fibonnaci per n >= 0."""

    f, _ = fibo_rapid_rec(n)
    return f


def fibo_rapid_rec(n: int) -> tuple[int,int]:
    """Retorna (F(n),F(n-1)) per n >= 0."""

    if n == 0:
        return 0, 0       # el segon no està definit, no importa què es posi
    elif n == 1:
        return 1, 0
    else:
        (fn1, fn2) = fibo_rapid_rec(n - 1) # calcula (F(n-1), F(n-2))
        return (fn1 + fn2, fn1)


def main() -> None:
    for n in range(900):
        print(n, fibo_rapid(n))


if __name__ == '__main__':
    main()
