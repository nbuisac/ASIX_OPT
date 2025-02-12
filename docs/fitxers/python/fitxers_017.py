nom_fitxer = input("Nom del fitxer -> ")
try:
    fi = open(nom_fitxer, "r", encoding="utf8")
    # Creem l'array on guardarem les dades
    array_quantes = []
    # hi posem tants 0s com lletres hi ha
    for a in range(ord('z') - ord('a') + 1):
        array_quantes.append(0)
    lletra = fi.read(1)
    while lletra != "":
        if ord('a') <= ord(lletra.lower()) <= ord('z'):
            array_quantes[ord(lletra.lower()) - ord('a')] += 1
        lletra = fi.read(1)
    fi.close()
    ## Mostrem els resultats
    for index, valor in enumerate(array_quantes):
        print(chr(ord('a') + index), valor, end="  -  ")

except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
