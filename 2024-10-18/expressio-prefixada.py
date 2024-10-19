from yogi import read


def avalua() -> int:
    """Llegeix una expressió aritmètica prefixada i en calcula el resultat"""

    element = read(str)
    if "0" <= element <= "9":
        return int(element)
    else:
        op1 = avalua()
        op2 = avalua()
        if element == "+":
            return op1 + op2
        elif element == "-":
            return op1 - op2
        elif element == "*":
            return op1 * op2
        else:
            assert False, "Mal operador"


def main() -> None:
    print(avalua())


if __name__ == "__main__":
    main()
