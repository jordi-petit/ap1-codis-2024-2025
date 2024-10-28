import yogi


def valor(c: str) -> int:
    """Retorna el codi del caràcter c. Prec: c és un sol caràcter."""
    return ord(c) - ord("a") + 1


def car(n: int) -> str:
    """Retorna el caràcter amb code n. Prec: c és un codi de caràcter."""
    return chr(n + ord("a") - 1)


def anterior(c: str) -> str:
    """
    Retorna el caràcter anterior al caràcter c. Per exemple, l'anterior de 'b' és 'a'.
    Prec: c és un sol caràcter.
    """
    return car(valor(c) - 1)


def escriure_patro(c: str) -> None:
    """Escriu (sense salt de línia) el patró descrit a l'enunciat a partir del caràcter c."""
    if c == "a":
        print("a", end="")
    else:
        v = valor(c)
        for _ in range(v - 1):
            print(c, end="")
            escriure_patro(anterior(c))
        print(c, end="")


def main() -> None:
    escriure_patro(yogi.read(str))
    print()


if __name__ == "__main__":
    main()
