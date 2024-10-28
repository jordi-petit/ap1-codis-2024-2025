def tres_digits_seguits_iguals(n: int, b: int) -> bool:
    """Indica si el natural n té tres dígits iguals consecutius en base b. Prec: n >= 0 i b >= 2."""
    if n < b**2:
        return False
    elif tres_digits_finals_iguals(n, b):
        return True
    else:
        return tres_digits_seguits_iguals(n // b, b)


def tres_digits_seguits_iguals_alternatiu(n: int, b: int) -> bool:
    """Indica si el natural n té tres dígits iguals consecutius en base b. Prec: n >= 0 i b >= 2."""
    return n >= b**2 and (tres_digits_finals_iguals(n, b) or tres_digits_seguits_iguals(n // b, b))
    # nota: A or B ja no avalua B si A és cert (igualment, A and B ja no avalua B si A és fals)


def tres_digits_finals_iguals(n: int, b: int) -> bool:
    """Indica si els tres dígits finals de n són iguals en base b. Prec: n >= 0 i b >= 2."""
    d1 = n % b
    d2 = (n // b) % b
    d3 = (n // (b**2)) % b
    return d1 == d2 == d3  # això vol dir d1 == d2 and d2 == d3


if __name__ == "__main__":
    # algunes proves
    print(tres_digits_seguits_iguals(44344, 10))
    print(tres_digits_seguits_iguals(6444344, 10))
