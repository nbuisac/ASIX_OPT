# Python - Exercicis d'iteracions sense seqüències

Resol aquests exercicis d'iteracions amb [`for`][for] i/o [`while`][while].

1. Fes un programa que validi una nota (0..10) amb while. Que demani una nota, i si no està entre 0 i 10 que la torni a demanar, i si no està ....


    ???example "Possible solució"

        ```py
        nota = float(input("Entra una nota (0..10) ->"))
        while nota < 0 or nota > 10:
            nota = float(input("Entra una nota (0..10) ->"))

        print("La nota és", nota)
        ```

2. Fes un programa que validi una resposta `s/n`. Que demani una resposta `s` ó `n`, i si no és `s` ó `n` que la torni a demanar, i si no està ....

    ???example "Possible solució"

        ```py
        continua = input("Vols continuar (s/n)? ")
        while continua not in "sSnN":
            continua = input("Vols continuar (s/n)? ")

        if continua in "sS":
            print("Sí vols continuar")
        else:
            print("No vols continuar")
        ```

3. Fes un programa que escrigui 20 vegades *hola*. Fes-lo dues vegades, una amb [`for`][for] i l'altra amb [`while`][while].

    ???example "Possible solució"

        ```py title="amb for"
        for a in range(20):
            print("Hola")
        ```

        ```py title="amb while"
        i = 0
        while i < 20:
            print("Hola")
            i = i + 1
        ```

4. Escriu un programa que ens demani quantes vegades volem escriure hola, i que ho faci

    ???example "Possible solució"

        ```py
        vegades = int(input("Quantes vegades vols escriure \"Hola\"? "))

        for a in range(vegades):
            print("Hola")
        ```

5. Fes un programa que escrigui els 20 primers números (1, 2, 3, ... 20)

    ???example "Possible solució"

        ```py
        for i in range(1, 21):
                    print(i)
        ```

        ```py
        for i in range(20):
                    print(i + 1)
        ```

6. Fes un programa que escrigui els 20 primers números parells (2, 4, 6, 8, ..., 40)

    ???example "Possible solució"

        ```py
        for i in range(1, 21):
            print(i * 2)
        ```

7. Fes un programa que escrigui els 20 primers quadrats perfectes (0, 1, 4, 9, 16, ...)

    ???example "Possible solució"

        ```py
        for i in range(20):
            print(i * i)
        ```

8. Fes un programa que demani 10 números per teclat i que els sumi i ens mostri el resultat

    ???example "Possible solució"

        ```py
        suma = 0
        for i in range(10):
            suma = suma + float(input("Entra un número -> "))
        
        print(suma)
        ```

9. Fes un programa que demani 10 enters i digui quants eren positius, quants negatius i quantes vegades hi havia el zero

    ???example "Possible solució"

        ```py
        positius = 0
        negatius = 0
        zeros = 0
        for i in range(10):
            numero = float(input("Entra un número -> "))
            if numero > 0:
                positius = positius + 1
            elif numero < 0:
                negatius = negatius + 1
            else:
                zeros = zeros + 1
        
        print(positius, negatius, zeros)
        ```

10. Fes un programa que demani 2 números i calculi el producte a base de sumes. Per exemple **per calcular 5*3 ha de fer 5 + 5 + 5**

    ???example "Possible solució"

        ```py

        ```

11. Fes un programa que calculi la divisió entera a base de restes. Per exemple *per calcular 20 / 3 = 6*3 + 2. Quocient 3 i sobren 2, doncs puc restar 6 vegades el 3*

    ???example "Possible solució"

        ```py

        ```

12. Escriu un programa que demani un número N i calculi la **suma** de l'**1 al N**. Per exemple si donem el 4 ha de calcular 1+2+3+4=10

    ???example "Possible solució"

        ```py

        ```

13. Fes un programa que demani un número N i calculi el factorial del número. **N!** (producte de l'1 al N). Per exemple si donem el 4 ha de calcular 1*2*3*4=24

    ???example "Possible solució"

        ```py

        ```

14. Fes un programa que demani un número N i escrigui els seus divisors. Per exemple si donem el 12 ha d'escriure: 1 2 3 4 6 12 (la divisió entera té residu 0)

    ???example "Possible solució"

        ```py

        ```

15. Fes un programa que compti els divisors d'un número. Per exemple si donem el 12 ha d'escriure: 6

    ???example "Possible solució"

        ```py

        ```

16. Fes un programa que digui si un número és primer. Són primers els que tenen només dos divisors, l'1 i ell mateix.

    ???example "Possible solució"

        ```py

        ```

17. Fes un programa que calculi el màxim comú divisor de dos números. El màxim comú divisor és el divisor de tots dos més gran que hi hagi. Si no trobem cap divisor, el 1 sempre ho serà. Podem fer-ho provant números del 2 al menor d'ells com a molt o a base de restes (el major menys el menor i ara tornem a tenir dos nombres, el menor que teniem i el resultat de la resta i així anem fint fins arribar a tenir dos nombres iguals)

    ???example "Possible solució"

        ```py

        ```

18. Fes un programa que calculi el mínim comú múltiple de dos números. El mínim comú múltiple és el múltiple de tots dos més petit que hi hagi. com a molt, el producte de tots dos ho serà. Es-ho provant tots els números des del major al producte dels dos o fins que en
trobis un.

    ???example "Possible solució"

        ```py

        ```

19. Escriu un programa que indiqui si un número és perfecte. Un número és perfecte si la suma dels divisors excepte ell mateix coincideix amb el número. Per exemple 6 = 1 + 2 + 3
    ???example "Possible solució"

        ```py

        ```

20. Escriu un programa que calculi l'arrel entera d'un número. Arrel (30) = 5. Fem-ho per força bruta anar provant valors fins a passar-nos. n2 (n*n)

    ???example "Possible solució"

        ```py

        ```

21. Fes un programa que compti quantes xifres té un número enter. Hauràs de fer-ho anant treien un dígit cada vegada fins que no te'n quedi cap, o un.

    ???example "Possible solució"

        ```py

        ```

22. Fes un programa que sumi les xifres que té un número enter. Hauràs d'anar extraient les xifres i acumular-les.

    ???example "Possible solució"

        ```py

        ```

23. Escriu un programa que miri si un número enter qualsevol és capicua. Per a resoldre’l crearem un alter nombre amb els dígits al revés i al final els compararem per veure si són iguals.

    ???example "Possible solució"

        ```py

        ```

24. Fes un programa que llanci 1000000 de monedes (s’inventi 0 o 1) i digui quin % de cares i creus ha tret.

    ???example "Possible solució"

        ```py

        ```

25. Fes un programa que digui si un número és apilable: Ho són el 0, 1, 3, 6, 10, 15, 21, ... (els que són la suma de 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + ... fins arribar al número o que ens passem).

    ???example "Possible solució"

        ```py

        ```

26. Fes un programa que escrigui els apilables entre 1 i 1000

    ???example "Possible solució"

        ```py

        ```

27. Fes un programa que escrigui els 20 primers termes de la successió de Fibonacci. La successió és 1, 1, 2, 3, 5, 8, 13, 21, 34, ... (el primer és 1, el segon és 1 i la resta són la suma dels dos anteriors).

    ???example "Possible solució"

        ```py

        ```

28. Fes un programa que calculi el MCD per l’algorisme d’Euclides.

    1. Euclides diu que si un número és múltiple de l’altre, el petit és el MCD: De 24 i 6 el MCD és 6
    
    2. Euclides diu que si no són múltiple un de l’altre, el MCD que hem de buscar és el del petit i el residu de la divisió entera entre tots dos: De 40 i 24 el MCD que hem de buscar és el de 24 i 16

    ???example "Possible solució"

        ```py

        ```

29. Fes un programa que donat un número N i escrigui els seus factors primers.

    ???example "Possible solució"

        ```py

        ```


[while]:                https://docs.python.org/reference/compound_stmts.html#the-while-statement       "while"
[for]:                  https://docs.python.org/reference/compound_stmts.html#the-for-statement         "for"

--8<-- ".acronims.txt"
