# Python - Exercicis d'iteracions amb seqüències

Resol aquests exercicis d'iteracions amb [`for`][for] i/o [`while`][while].

pots utilitzar aquells [mètodes d'strings][] que vegis interessants.

## Seqüències (1 a 10) i Recorreguts (11 a 19)

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
        ```

7. Escriu un programa que demani una llista de números positius acabada en -1 i mostri la diferència entre el major i el menor.

    ???example "Possible solució"

        ```py
        ```

8. Escriu un programa que demani números fins trobar el zero i digui si la sèrie era creixent.

    ???example "Possible solució"

        ```py
        ```

9. Escriu un programa que demani números fins trobar el zero i digui si la sèrie era creixent, decreixent o res.

    ???example "Possible solució"

        ```py
        ```

10. Escriu un programa que demani una sèrie de números positius acabada en 0 y digui si és o no una progressió aritmètica. 12 16 20 24 28 32 0 sí que ho és doncs entre cada dos termes hi ha una diferència constant (en aquest cas 4)

    ???example "Possible solució"

        ```py
        ```

11. Fes un programa que demani una llista de números positius acabada en ‐1 i digui si el primer es repeteix.

    ???example "Possible solució"

        ```py
        ```

12. Fes un programa que demani una frase i digui quantes vocals té.

    ???example "Possible solució"

        ```py
        ```

13. Fes un programa que demani una frase i escrigui el percentatge de vocals respecte al de consonants.

    ???example "Possible solució"

        ```py
        ```

14. Fes un programa que demani una frase i digui quantes paraules hi ha.

    a. Versió 1. Suposeu que no hi ha espais innecessaris.

    b. Versió 2. Suposeu que pot haver espais al principi, al final, espais dobles, ...

    ???example "Possible solució"

        ```py
        ```

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
