nom_fitxer = "dades.txt"
try:
    f = open(nom_fitxer)
    print(f.read().upper())
    f.close()
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
