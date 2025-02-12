CLAU = 2 ## nombre de caràcters que desplacem
nom_fitxer = input("Nom del fitxer -> ")
try:
    fi = open(nom_fitxer, "r", encoding="utf8")
    fo = open(nom_fitxer + ".cesar", "w", encoding="utf8")
    numero_lletres = ord('z') - ord('a') + 1
    lletra = fi.read(1)
    while lletra != "":
        if lletra.islower():
            l = ord(lletra) + CLAU
            if l > ord('z'):
                l = (l - ord('a')) % (numero_lletres) + ord('a')
            lletra = chr(l)
        elif lletra.isupper():
            l = ord(lletra) + CLAU
            if l > ord('Z'):
                l = (l - ord('A')) % (numero_lletres) + ord('A')
            lletra = chr(l)
        fo.write(lletra)
        lletra = fi.read(1)
    fo.close()
    fi.close()

except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
