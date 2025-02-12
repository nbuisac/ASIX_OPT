nom_fitxer = "dades.txt"
edat_minima = 200
try:
    f = open(nom_fitxer, "r")
    nom = f.readline().rstrip()
    while nom != '':
        edat = int(f.readline())
        print(f"nom: {nom}, edat : {edat}")
        if edat < edat_minima:
            edat_minima = edat
            nom_major = nom
        nom = f.readline().rstrip()
    f.close()
    print(f"El/La més petit/a és en/la {nom_major}")
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
