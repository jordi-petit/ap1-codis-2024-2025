def minim_i_maxim(a: int, b: int) -> tuple[int, int]:
    """Funció que retorna el mínim i el màxim dels dos nombres a i b."""

    if a < b:
        return a, b
    else:
        return b, a


def descomposicio_horaria(n: int) -> tuple[int, int, int]:
    """Descompon el nombre de segons n en (hores, minuts, segons)."""

    h = n // 3600
    m = (n % 3600) // 60
    s = n % 60
    return h, m, s


def un_segon_mes_tard(h: int, m: int, s: int) -> tuple[int, int, int]:
    """Calcula l'hora un segon més tard de l'hora h:m:s."""

    s = s + 1
    if s == 60:
        s = 0
        m = m + 1
        if m == 60:
            m = 0
            h = h + 1
            if h == 24:
                h = 0
    return h, m, s


def escriure_hora(h: int, m: int, s: int) -> None:
    """Escriu l'hora h:m:s amb el format 00:00:00."""

    if h < 10:
        print(0, end="")
    print(h, end=":")
    if m < 10:
        print(0, end="")
    print(m, end=":")
    if s < 10:
        print(0, end="")
    print(s)


hh, mm, ss = 23, 59, 59
nh, nm, ns = un_segon_mes_tard(hh, mm, ss)
escriure_hora(nh, nm, ns)
escriure_hora(hh, mm, ss)
