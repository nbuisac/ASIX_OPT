nom_fitxer = "dades.txt"
suma_edats = 0
quants = 0
try:
    f = open(nom_fitxer, "r")
    nom = f.readline().rstrip()
    while nom != '':
        edat = int(f.readline())
        print(f"nom: {nom}, edat : {edat}")
        suma_edats += edat
        quants += 1
        nom = f.readline().rstrip()
    f.close()
    mitjana = suma_edats / quants
    print(f"La mitjana de les edats és {mitjana} anys")
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
