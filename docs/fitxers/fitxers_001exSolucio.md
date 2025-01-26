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

6. A partir d'un nom de fitxer ens diu quants caràcters té. Si el fitxer no existeix diu 0.

7. A partir d'un fitxer amb format `/etc/password` ens mostra el nom dels usuaris amb el seu *`id`*.

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

9. A partir d'un fitxer com el de l'exercici 8, ens diu el nom de l'usuari menor.
(Si dos usuaris tenen la mateixa edat, només en mostra un).

10. A partir d'un fitxer com el de l'exercici 8, ens diu la mitjana de les edats.

11. A partir d'un fitxer com el de l'exercici 8, ens diu el nom del major, el nom
del menor i la mitjana de les edats de tots.

12. A partir d'un fitxer de text el mostrem tot en majúscules.

13. A partir d'un fitxer de text el mostrem de forma que la primera lletra (primer caràcter) de cada línia estigui en majúscula i les altres en minúscula.

14. A partir d'un fitxer i una paraula, mostrem totes les línies del fitxer que contenen la paraula simulant la comanda grep.

15. A partir d'un fitxer en generem un altre amb el mateix nom afegint-hi .cesar amb el mateix text però canviant cada lletra per la següent (en cas de ser z posarem a).

16. Fes que el programa de inventar-se un número i endevinar-lo. Et demana el nom abans de començar cada partida, i afegeixi el teu nom i el temps que has trigat a un arxiu on hi consta l'historial de partides.

17. Donat un arxiu de text, que conté un text, dir quantes vegades apareix cada lletra. Quantes a's, quantes b's, .....

--8<-- ".acronims.txt"
