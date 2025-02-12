# Python - Exercicis de fitxers

Resol aquests exercicis de fitxers amb llenguatge Python

1. Crea un arxiu, amb un *editor de text*, amb un missatge i, fes un programa que obri aquest arxiu i mostri el missatge per pantalla.

    ???example "Possible solució a l'exercici"

        ```py title="Llegint linia a linia"
        try:
            f = open("fitxer01.txt")
            for linia in f:
                print(linia, end="")
        except Exception as e:
            print("Error:", e)
        ```

        ```py title="Amb with"
        try:
            with open("fitxer01.txt") as f:
                print(f.read())
        except Exception as e:
            print("Error:", e)
        ```


2. Fes un programa que vagi demanant números enters positius per teclat fins trobar el -1 i els vagi escrivint en un arxiu. El -1 no s'ha d'escriure a l'arxiu.

    ???example "Possible solució a l'exercici"

        ```py title="Escrivim nombre a nombre"
        def demana_numero():
            while True:
                try:
                    n = int(input("Entra un número enter -> "))
                    if n == -1 or n > 0:
                        return n
                except Exception:
                    pass

        f = open("fitxer02.txt", "wt")
        n = demana_numero()
        while n != -1:
            f.write(str(n) + "\n")
            n = demana_numero()
        f.close()
        ```

3. Fes un programa que llegeixi números enters positius d'un arxiu i mostri: el major, el menor i la mitjana per pantalla. *Pots utilitzar el fitxer creat a l'exercici anterior*.

    ???example "Possible solució a l'exercici"

        ```py title="Compte al llegir strings i passar-lo a enter i saber que estem al final"
        f = open("fitxer02.txt", "rt")
        quants = 0
        suma = 0
        numero_str = f.readline()
        ## Per si el fitxer estigués buit fem el següent en un if
        if numero_str != "":
            if numero_str.strip() != "":
                petit = int(numero_str)
                gran = int(numero_str)
                quants = 1
                suma = gran
            while numero_str != "":
                if numero_str.strip() != "":
                    numero = int(numero_str)
                    quants = quants + 1
                    suma = suma + numero
                    if numero > gran:
                        gran = numero
                    elif numero < petit:
                        petit = numero
                    numero_str = f.readline()
            print(f"El número més petit és {petit}")
            print(f"El número més gran és {gran}")
            print(f"La mitjana és {round(suma / quants, 2)}")
        f.close()
        ```

4. Fes un programa que s'inventi 1.000.000 de combinacions per la loteria 6/49 (o primitiva) i les escrigui en un arxiu. Cada combinació ha d'aparèixer en una línia diferent. *No comprovarem la repetició de combinacions, però recorda que les combinacions no poden tenir números repetits*.

    ???example "Possible solució a l'exercici"

        ```py title="Loteria 6/49"
        import random
        QUANTIAT = 1000000
        def genera_combinacio():
            combi = []
            while len(combi) < 6:
                n = random.randint(1, 49)
                if n in combi:
                    continue
                combi.append(n)
            return combi

        f = open("fitxer04.txt", "wt")
        q = 0
        while q < QUANTIAT:
            combinacio = genera_combinacio()
            combinacio.sort()
            for n in combinacio:
                f.write(str(n) + " ")
            f.write("\n")
            q = q + 1

        f.close()
        ```

5. A partir d'un nom de fitxer ens diu quantes línies té. Si el fitxer no existeix diu 0.

    ???example "Possible solució a l'exercici"

        ```py title="Numero linies"
        ## A partir d'un nom de fitxer ens diu quantes línies té. Si el fitxer no existeix diu 0.
        nom_fitxer = input("Entra el nom del fitxer -> ")
        try:
            q = 0
            with open(nom_fitxer, "r") as f:
                for linia in f:
                    q += 1
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})") ## Aquesta línia s'ha posat per tal que no peti el programa Podria dir només pass
        finally:
            print(f"El fitxer {nom_fitxer} conté {q} linies")
        ```

6. A partir d'un nom de fitxer ens diu quants caràcters té. Si el fitxer no existeix diu 0.

    ???example "Possible solució a l'exercici"

        ```py title="Numero caràcters"
        ## A partir d'un nom de fitxer ens diu quants caràcters té. Si el fitxer no existeix diu 0.
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
            print(f"El fitxer {nom_fitxer} conté {q} caràcters")
        ```

7. A partir d'un fitxer amb format `/etc/password` ens mostra el nom dels usuaris amb el seu *`id`*.

    ???example "Possible solució a l'exercici"

        ```py title="Dades de /etc/passwd"
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
        ```

8. A partir d'un fitxer del tipus mostrat ens diu el nom de l'usuari major.
(Si dos usuaris tenen la mateixa edat, només en mostra un).
    
    ```txt
    Joan
    12
    Manel
    23
    Pilar
    34
    Maria
    21
    ```

    ???example "Possible solució a l'exercici"

        ```py title="Utilitzem la funció rstrip() per treure els intros del final"
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
            print(f"El més gran és en/la {nom_major}")
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
        except Exception as e:
            print(f"ERROR: Error no tractat. ({e})")
        ```

9. A partir d'un fitxer com el de l'exercici 8, ens diu el nom de l'usuari menor.
(Si dos usuaris tenen la mateixa edat, només en mostra un).

    ???example "Possible solució a l'exercici"

        ```py title="Utilitzem la funció rstrip() per treure els intros del final"
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
                    nom_menor = nom
                nom = f.readline().rstrip()
            f.close()
            print(f"El/La més petit/a és en/la {nom_menor}")
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
        except Exception as e:
            print(f"ERROR: Error no tractat. ({e})")
        ```

10. A partir d'un fitxer com el de l'exercici 8, ens diu la mitjana de les edats.

    ???example "Possible solució a l'exercici"

        ```py title="Utilitzem la funció rstrip() per treure els intros del final"
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
        ```

11. A partir d'un fitxer com el de l'exercici 8, ens diu el nom del major, el nom
del menor i la mitjana de les edats de tots.

    ???example "Possible solució a l'exercici"

        ```py title="Aquesta vegada no suposarem cap edat inicial sinó la del primer"
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
        ```

        !!!question "Què passaria si el fitxer estigués buit?"

12. A partir d'un fitxer de text el mostrem tot en majúscules.

    ???example "Possible solució a l'exercici"

        ```py title="Amb el mínim d'instruccions"
        nom_fitxer = "dades.txt"
        try:
            f = open(nom_fitxer)
            print(f.read().upper())
            f.close()
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
        except Exception as e:
            print(f"ERROR: Error no tractat. ({e})")
        ```

13. A partir d'un fitxer de text el mostrem de forma que la primera lletra (primer caràcter) de cada línia estigui en majúscula i les altres en minúscula.

    ???example "Possible solució a l'exercici"

        ```py title="Línia a línia sense tenir en compte espais inicials"
        nom_fitxer = "dades.txt"
        nom_fitxer = "poema.txt"
        try:
            with open(nom_fitxer, encoding="utf8") as f:
                for linia in f:
                    print(linia[0].lower(), end="")
                    print(linia[1:].upper(), end="")
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
        except Exception as e:
            print(f"ERROR: Error no tractat. ({e})")
        ```


        ```py title="Saltant-nos els caràcters no lletra inicials"
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
        ```

14. A partir d'un fitxer i una paraula, mostrem totes les línies del fitxer que contenen la paraula simulant la comanda grep.

    ???example "Possible solució a l'exercici"

        ```py title="Simulem la comanda grep"
        nom_fitxer = input("Nom del fitxer -> ")
        paraula = input("Paraula a cerca -> ")
        try:
            with open(nom_fitxer, encoding="utf8") as f:
                for linia in f:
                    if paraula in linia:
                        print(linia, end="")
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
        except Exception as e:
            print(f"ERROR: Error no tractat. ({e})")
        ```

        ```py title="Simulem la comanda igrep: sense tenir en compte majúscules/minúscules"
        nom_fitxer = input("Nom del fitxer -> ")
        paraula = input("Paraula a cerca -> ")
        try:
            with open(nom_fitxer, encoding="utf8") as f:
                for linia in f:
                    if paraula.lower() in linia.lower():
                        print(linia, end="")
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
        except Exception as e:
            print(f"ERROR: Error no tractat. ({e})")
        ```

        ```py title="Marquem la primera ocurrència de cada paraula"
        nom_fitxer = input("Nom del fitxer -> ")
        paraula = input("Paraula a cerca -> ")
        try:
            with open(nom_fitxer, encoding="utf8") as f:
                for linia in f:
                    if paraula.lower() in linia.lower():
                        posicio = linia.index(paraula)
                        print(linia[:posicio], end="")
                        print(chr(27)+"[7m", end="")
                        print(linia[posicio:posicio + len(paraula)], end="")
                        print(chr(27)+"[0m", end="")
                        print(linia[posicio + len(paraula):], end="")
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
        except Exception as e:
            print(f"ERROR: Error no tractat. ({e})")
        ```

        ```py title="Marquem totes les ocurrències de cada paraula"
        nom_fitxer = input("Nom del fitxer -> ")
        paraula = input("Paraula a cerca -> ")
        try:
            with open(nom_fitxer, encoding="utf8") as f:
                for linia in f:
                    if paraula.lower() in linia.lower():
                        while paraula.lower() in linia.lower():
                            posicio = linia.index(paraula)
                            print(linia[:posicio], end="")
                            print(chr(27)+"[7m", end="")
                            print(linia[posicio:posicio + len(paraula)], end="")
                            print(chr(27)+"[0m", end="")
                            linia = linia[posicio + len(paraula):]
                        print(linia, end="")
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
        except Exception as e:
            print(f"ERROR: Error no tractat. ({e})")
        ```

15. A partir d'un fitxer en generem un altre amb el mateix nom afegint-hi .cesar amb el mateix text però canviant cada lletra per la següent (en cas de ser z posarem a).

    ???example "Possible solució a l'exercici"

        ```py title="Solució amb nombre de lletres a desplaçar, variable segons CLAU"
        CLAU = 1 ## nombre de caràcters que desplacem
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
        ```

16. Fes que el programa de inventar-se un número i endevinar-lo. Et demana el nom abans de començar cada partida, i afegeixi el teu nom i el temps que has trigat a un arxiu on hi consta l'historial de partides.

    ???example "Possible solució a l'exercici"

        ```py title="fitxer -> puntuacions.txt.Importem la llibreria time pel temps"
        import random
        import time
        MAXIM = 100
        MINIM = 1
        def demana_numero(des_de = 1, fins_a = 10):
            n = input(f"Entra un Numero ({des_de}..{fins_a} -> ")
            while not n.isdigit() or int(n) < des_de or int(n) > fins_a:
                n = input(f"ERROR: Entra un Numero ({des_de}..{fins_a} -> ")
            return int(n)

        nom = input("Entra el teu nom -> ")
        numero_a_encertar = random.randint(MINIM, MAXIM)
        temps_inicial = time.time()
        numero = demana_numero(MINIM, MAXIM)
        intents = 1
        while numero != numero_a_encertar:
            print("Noooooooooo!!!!", end=" ")
            if  numero_a_encertar < numero:
                print("és més petit")
            else:
                print("és més gran")
            numero = demana_numero(MINIM, MAXIM)
            intents += 1
        temps_final = time.time()
        segons = temps_final - temps_inicial
        print(f"Correcte, l'has encertat en {intents} intents i en {segons} segons")

        try:
            nom_fitxer = "puntuacions.txt"
            fi = open(nom_fitxer, "a")
            fi.write(f"{nom}:{MINIM}:{MAXIM}:{numero_a_encertar}:{intents}:{segons}\n")
            fi.close()
        except FileNotFoundError as e:
            print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
        except Exception as e:
            print(f"ERROR: Error no tractat. ({e})")
        ```


17. Donat un arxiu de text, que conté un text, dir quantes vegades apareix cada lletra. Quantes a's, quantes b's, .....

    ???example "Possible solució a l'exercici"

        ```py title="Tractarem majúscules i minúscules de la mateixa manera..."
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
        ```

--8<-- ".acronims.txt"
