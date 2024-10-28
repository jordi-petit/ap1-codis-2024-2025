import yogi


def escriure_paraules_del_reves() -> None:
    """Llegeix una llista de paraules i les escriu del revés"""

    paraula = yogi.scan(str)
    if paraula is not None:
        escriure_paraules_del_reves()
        print(paraula)


def main() -> None:
    escriure_paraules_del_reves()


if __name__ == "__main__":
    main()
