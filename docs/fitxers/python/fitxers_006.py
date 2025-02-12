## A partir d'un nom de fitxer ens diu quants caracters te. Si el fitxer no existeix diu 0.
nom_fitxer = input("Entra el nom del fitxer -> ")
try:
    q = 0
    with open(nom_fitxer, "r") as f:
        for linia in f:
            for c in linia:
                q += 1
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
finally:
    print(f"El fitxer {nom_fitxer} conte {q} caracters")