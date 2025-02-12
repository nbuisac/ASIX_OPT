nom_fitxer = "dades.txt"
try:
    f = open(nom_fitxer, "r")
    nom = f.readline().rstrip()
    edat = int(f.readline())
    edat_minima = edat
    edat_maxima = edat
    nom_menor = nom
    nom_major = nom
    suma_edats = edat
    quants = 1
    nom = f.readline().rstrip()
    while nom != '':
        edat = int(f.readline())
        print(f"nom: {nom}, edat : {edat}")
        suma_edats += edat
        quants += 1
        if edat > edat_maxima:
            edat_maxima = edat
            nom_major = nom
        elif edat < edat_minima:
            edat_minima = edat
            nom_menor = nom
        nom = f.readline().rstrip()
    f.close()
    mitjana = suma_edats / quants
    print(f"El/La més petit/a és en/la {nom_menor}")
    print(f"El/La més gran/a és en/la {nom_major}")
    print(f"La mitjana de les edats és {mitjana} anys")
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
