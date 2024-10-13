def factorial(n: int) -> int:
    """Retorna el factorial d'un natural n."""

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(5))  # 120