# Python - Exercicis d'iteracions amb seqüències

Resol aquests exercicis d'iteracions amb [`for`][for] i/o [`while`][while].

pots utilitzar aquells [mètodes d'strings][] que vegis interessants.

## Seqüències (1 a 10) i Recorreguts (11 a 18)

1. Escriu un programa que demani una frase i digui quantes lletres `a` hi ha.

    ???example "Possible solució"

        ```py
        LLETRA_BUSCADA = 'a'.lower()
        frase = input("Entra una frase -> ")
        lletres = 0
        for lletra in frase.lower():
            if lletra == LLETRA_BUSCADA:
                lletres += 1
        print(f"Hi ha {lletres} '{LLETRA_BUSCADA}'")
        ```

2. Escriu un programa que demani una frase i digui si hi ha alguna lletra `a`.

    ???example "Possible solució"

        ```py title="Versió més Python, amb in"
        LLETRA_BUSCADA = 'a'.lower()
        frase = input("Entra una frase -> ")
        if LLETRA_BUSCADA in frase.lower():
            print(f"Hi ha alguna '{LLETRA_BUSCADA}'")
        else:
            print(f"No hi ha cap '{LLETRA_BUSCADA}'")
        ```

        ```py title="Versió menys Python"
        LLETRA_BUSCADA = 'a'.lower()
        frase = input("Entra una frase -> ")
        for lletra in frase.lower():
            if lletra == LLETRA_BUSCADA:
                trobada = True
                break
        else:
            trobada = False
        if trobada:
            print(f"Hi ha alguna '{LLETRA_BUSCADA}'")
        else:
            print(f"No hi ha cap '{LLETRA_BUSCADA}'")
        ```

3. Escriu un programa que vagi demanant números fins trobar el zero i digui quants valors s'han introduït.

    ???example "Possible solució"

        ```py
        quants = 0
        numero = float(input("Entra un nombre (0 per acabar) -> "))
        while numero != 0:
            quants += 1
            numero = float(input("Entra un nombre (0 per acabar) -> "))
        print(f"Has entrat {quants} nombres")
        ```

4. Escriu un programa que vagi demanant números fins trobar el zero i calculi la suma dels valors introduïts.

    ???example "Possible solució"

        ```py
        suma = 0
        numero = float(input("Entra un nombre (0 per acabar) -> "))
        while numero != 0:
            suma += numero
            numero = float(input("Entra un nombre (0 per acabar) -> "))
        print(f"La suma és {suma}")
        ```

5. Escriu un programa que vagi demanant números fins trobar el zero i calculi la mitjana aritmètica dels valors introduïts.

    ???example "Possible solució"

        ```py
        suma = 0
        quants = 0
        numero = float(input("Entra un nombre (0 per acabar) -> "))
        while numero != 0:
            quants += 1
            suma += numero
            numero = float(input("Entra un nombre (0 per acabar) -> "))
        print(f"La mitjana és {suma/quants}")
        ```

6. Escriu un programa que vagi demanant números fins trobar el zero i mostri en pantalla el valor més gran.

    ???example "Possible solució"

        ```py
        numero = float(input("Entra un nombre (0 per acabar) -> "))
        gran = numero
        while numero != 0:
            if numero > gran:
                gran = numero
            numero = float(input("Entra un nombre (0 per acabar) -> "))
        print(f"El més gran és {gran}")
        ```

7. Escriu un programa que demani una llista de números positius acabada en -1 i mostri la diferència entre el major i el menor.

    ???example "Possible solució"

        ```py
        numero = float(input("Entra un nombre (0 per acabar) -> "))
        menor = numero
        major = numero
        while numero != 0:
            if numero > major:
                major = numero
            elif numero < menor:
                menor = numero
            numero = float(input("Entra un nombre (0 per acabar) -> "))
        print(f"La diferència entre {major} i {menor} és {major - menor}")
        ```

8. Escriu un programa que demani números fins trobar el zero i digui si la sèrie era creixent.

    ???example "Possible solució"

        ```py title="Només farem la comprovació a partir de saber que teni m dos nombres entrats"
        numero_anterior = float(input("Entra un nombre (0 per acabar) -> "))
        if numero_anterior != 0:
            numero = float(input("Entra un nombre (0 per acabar) -> "))
            if numero != 0:
                es_creixent = numero > numero_anterior
                while numero != 0: ## Podem afegir-hi -> and es_creixent
                    if numero <= numero_anterior:
                        es_creixent = False
                        ## Si no volem demanar més nombres podem fer un break
                    numero_anterior = numero
                    numero = float(input("Entra un nombre (0 per acabar) -> "))
                if es_creixent:
                    print(f"La sèrie SÍ és creixent")
                else:
                    print(f"La sèrie NO és creixent")
            else:
                print(f"Només has entrat un nombre")
        else:
            print(f"No has entrat cap nombre")
        ```

9. Escriu un programa que demani números fins trobar el zero i digui si la sèrie era creixent, decreixent o res.

    ???example "Possible solució"

        ```py
        numero_anterior = float(input("Entra un nombre (0 per acabar) -> "))
        if numero_anterior != 0:
            numero = float(input("Entra un nombre (0 per acabar) -> "))
            if numero != 0:
                es_creixent = numero > numero_anterior
                es_decreixent = numero < numero_anterior
                while numero != 0: ## Podem afegir-hi -> and (es_creixent or es_decreixent)
                    if numero <= numero_anterior:
                        es_creixent = False
                    if numero >= numero_anterior:
                        es_decreixent = False
                    numero_anterior = numero
                    numero = float(input("Entra un nombre (0 per acabar) -> "))
                if es_creixent:
                    print(f"La sèrie és creixent")
                elif es_decreixent:
                    print(f"La sèrie és decreixent")
                else:
                    print(f"La sèrie NO és creixent NI decreixent")
            else:
                print(f"Només has entrat un nombre")
        else:
            print(f"No has entrat cap nombre")
        ```

10. Escriu un programa que demani una sèrie de números positius acabada en 0 y digui si és o no una progressió aritmètica. 12 16 20 24 28 32 0 sí que ho és doncs entre cada dos termes hi ha una diferència constant (en aquest cas 4)

    ???example "Possible solució"

        ```py title="Primer cal demanar els dos primers nombres per calcular-ne la diferència"
        numero_anterior = float(input("Entra un nombre (0 per acabar) -> "))
        if numero_anterior != 0:
            numero = float(input("Entra un nombre (0 per acabar) -> "))
            if numero != 0:
                diferencia = numero - numero_anterior
                es_progressio = True
                while numero != 0: ## Podem afegir-hi -> and es_progressio
                    if (numero - numero_anterior) != diferencia:
                        es_progressio = False
                    numero_anterior = numero
                    numero = float(input("Entra un nombre (0 per acabar) -> "))
                if es_progressio:
                    print(f"La sèrie té una progressió aritmètica de {diferencia}")
                else:
                    print(f"La sèrie NO té una progressió aritmètica")
            else:
                print(f"Només has entrat un nombre")
        else:
            print(f"No has entrat cap nombre")
        ```

11. Fes un programa que demani una llista de números positius acabada en ‐1 i digui si el primer es repeteix.

    ???example "Possible solució"

        ```py title="També podriem comptar quants cops apareix el primer a la resta de la sèrie"
        primer = float(input("Entra un nombre (0 per acabar) -> "))
        if primer != 0:
            numero = float(input("Entra un nombre (0 per acabar) -> "))
            if numero != 0:
                es_repeteix = primer == numero
                while numero != 0:
                    if numero == primer:
                        es_repeteix = True
                    numero = float(input("Entra un nombre (0 per acabar) -> "))
                if es_repeteix:
                    print(f"El número {primer} s'ha entrat al principi i al mig")
                else:
                    print(f"El número {primer}, s'ha entrat al principi, no s'ha repetit")
            else:
                print(f"Només has entrat un nombre")
        else:
            print(f"No has entrat cap nombre")
        ```

12. Fes un programa que demani una frase i digui quantes vocals té.

    ???example "Possible solució"

        ```py title="Utilitzarem in i una constant amb totes les vocals"
        VOCALS = "aeiouAEIOUàèiòùáéíóúÀÈÌÒÙÀÉÍÓÚäëïöüÄËÏÖÜâêîôûÂÊÎÔÛãõÃÕ"
        frase = input("Entra una frase -> ")
        quantes = 0
        for lletra in frase:
            if lletra in VOCALS:
                quantes += 1
        print(f"La frase té {quantes} vocals")
        ```

13. Fes un programa que demani una frase i escrigui el percentatge de vocals respecte al de consonants.

    ???example "Possible solució"

        ```py
        VOCALS = "aeiouAEIOUàèiòùáéíóúÀÈÌÒÙÀÉÍÓÚäëïöüÄËÏÖÜâêîôûÂÊÎÔÛãõÃÕ"
        frase = input("Entra una frase -> ")
        vocals = 0
        consonants = 0
        for lletra in frase:
            if lletra.isalpha():
                print(lletra, end="") ## Aquesta linia es pot treure. És per saber el que compta!
                if lletra in VOCALS:
                    vocals += 1
                else:
                    consonants += 1
        print(f"\nLa frase té {vocals} vocals i {consonants} consonants. {vocals / consonants * 100:.2f}%")
        ```

14. Fes un programa que demani una frase i digui quantes paraules hi ha.

    a. Versió 1. Suposeu que no hi ha espais innecessaris.

    b. Versió 2. Suposeu que pot haver espais al principi, al final, espais dobles, ...

    ???example "Possible solució"

        ```py title="Fem directament la versió 2."
        frase = input("Entra una frase -> ")
        paraules = 0
        ## Estem indicant que l'anterior al primer no era lletra
        #  per tal que compti la primera lletra com a inici de paraula
        anterior_es_lletra = False
        for lletra in frase:
            if lletra.isalpha():
                if not anterior_es_lletra:
                    paraules += 1
                    anterior_es_lletra = True
            else:
                anterior_es_lletra = False

        print(f"\nLa frase té {paraules} paraules")
        ```

        !!!note "Suposem que cada vegada que trobem una lletra i l'anterior no er lletra, comença una nova paraula"

            Al principi cal indicar que l'anterior no és lletra

15. Fes un programa que demani una frase i l'escrigui sense espais múltiples

    ???example "Possible solució"

        ```py
        ```

16. Escriu un programa que demani una frase i compti els diftongs. Són diftongs els grups de vocal més vocal feble (i, u) excepte ii.

    ???example "Possible solució"

        ```py
        ```

17. Demana una frase i codifica‐la, fent correspondre a cada lletra el següent caràcter de l'alfabet. A la '`a`' la '`b`', a la '`b`' la '`c`', a la `c` la `d`, ... , a la `x` la `y`, a la `y` la `z` i finalment a la `z` la `a`. Prova de fer-lo de manera que l'increment de la lletra per la que canviem la demanem per teclat, i sempre funcioni. *No tinguis en compte accents ni dièresis ni `ç` ni `ñ`*.

    ???example "Possible solució"

        ```py
        ```

18. Escriu un programa que vagi demanant números fins trobar el zero i digui si són tots parells.

    ???example "Possible solució"

        ```py
        ```


[while]:                https://docs.python.org/reference/compound_stmts.html#the-while-statement       "while"
[for]:                  https://docs.python.org/reference/compound_stmts.html#the-for-statement         "for"
[mètodes d'strings]:    https://docs.python.org/3/library/stdtypes.html#string-methods                  "mètodes d'strings"

--8<-- ".acronims.txt"
