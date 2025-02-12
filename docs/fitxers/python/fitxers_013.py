nom_fitxer = "dades.txt"
nom_fitxer = "poema.txt"
try:
    with open(nom_fitxer, encoding="utf8") as f:
        for linia in f:
            for posicio, lletra in enumerate(linia):
                if not lletra.isalpha():
                    print(lletra, end="")
                else:
                    print(lletra.upper(), end="")
                    print(linia[posicio + 1:].lower(), end="")
                    break
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
