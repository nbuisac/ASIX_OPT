nom_fitxer = "dades.txt"
edat_maxima = -1
try:
    f = open(nom_fitxer, "r")
    nom = f.readline().rstrip()
    while nom != '':
        edat = int(f.readline())
        print(f"nom: {nom}, edat : {edat}")
        if edat > edat_maxima:
            edat_maxima = edat
            nom_major = nom
        nom = f.readline().rstrip()
    f.close()
    print(f"El/La més gran és en/la {nom_major}")
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
