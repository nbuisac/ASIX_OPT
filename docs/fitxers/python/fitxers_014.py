nom_fitxer = input("Nom del fitxer -> ")
paraula = input("Paraula a cerca -> ")
try:
    with open(nom_fitxer, encoding="utf8") as f:
        for linia in f:
            if paraula.lower() in linia.lower():
                while paraula.lower() in linia.lower():
                    posicio = linia.index(paraula)
                    print(linia[:posicio], end="")
                    print(chr(27)+"[7m", end="")
                    print(linia[posicio:posicio + len(paraula)], end="")
                    print(chr(27)+"[0m", end="")
                    linia = linia[posicio + len(paraula):]
                print(linia, end="")
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
