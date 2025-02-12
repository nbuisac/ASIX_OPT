nom_fitxer = "passwd"
try:
    with open(nom_fitxer, "r") as f:
        for linia in f:
            llista = linia.split(":")
            print(f"usuari: {llista[0]}, id : {llista[2]}")
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
