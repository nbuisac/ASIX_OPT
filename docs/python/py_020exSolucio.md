# Python - Exercicis

## Procediments i Funcions

1. Fes una funció `es_nota_valida` que validi una nota (valor admès de 0 a 10). Ha de retornar *`cert`* o *`fals`*.

    ???example "Possible solucio"

        ```py title="Opció simple"
        def es_nota_valida(nota):
            if 0 <= nota <= 10:
                return True
            else:
                return False
        ```

        ```py title="Opció simple"
        def es_nota_valida(nota):
            return 0 <= nota <= 10
        ```

        ```py title="Opció indicant valors mínim i màxim opcionals"
        def es_nota_valida(nota, valor_minim = 0, valor_maxim = 10):
            return valor_minim <= nota <= valor_maxim
        ```

2. Fes una funció *`es_resposta_valida`* que validi una resposta (valors admesos s n). Ha de retornar *`cert`* o *`fals`*.

    ???example "Possible solucio"

        ```py title="Opció simple"
        def es_resposta_valida(siono):
            siono = siono.strip()
            if len(siono) != 1:
                return False
            if siono.lower() in "sn":
                return True
            else:
                return False
        ```

        ```py title="Opció en una linia"
        def es_resposta_valida(siono):
            return len(siono.strip()) == 1 and siono.strip().lower() in "sn"
        ```

        ```py title="Opció indicant valors valids opcional"
        def es_resposta_valida(siono, valors_valids="sn"):
            if siono in valors_valids:
                return True
            if siono.strip().lower() in valors_valids:
                return True
            return False
        ```

3. Fes una funció *`demana_nota`* que retorni una nota vàlida (valor admès de 0 a 10). Ha de
retornar un valor de 0 a 10. Demanarà la dada a l’usuari i quan sigui correcte la retornarà.

4. Fes una funció *`es_parell`* que retorni si un número és parell.

5. Fes una funció *`suma`* que sumi dos números passats com a paràmetres i en retorni el
resultat.

6. Fes una funció *`multiplica`* que calculi el producte de dos números a base de sumes. Per
exemple 5*3=5 + 5 + 5

    ???example "Possible solucio"

        ```py title="Opció simple"
        def multiplica(a, b):
            m = 0
            for i in range(a):
                # print(f"({i + 1}) Sumo {b}")
                m = m + b
            return m
        ```
        


7. Fes una funció *`divideix`* que retorni la divisió entera calculant-la a base de restes. 20 / 3 = 6*3+2. Quocient 3 i sobren 2, doncs puc restar 6 vegades el 3

8. Fes una funció *`suma_1_N`* que donat un número retorni la suma del 1 al N. Per exemple si donem el 4 ha de retornar 10 (1+2+3+4)

9. Fes una funció *`factorial`* que donat un número retorni el producte del 1 al N (N!)
Per exemple si passem el 4 ha de retornar 24 (1*2*3*4)

10. Fes un procediment *`mostra_dividors`* que donat un número N mostri els seus divisors.
Per exemple si passem el 12 ha de mostar: 1 2 3 4 6 12

11. Fes una funció *`quants_divisors`* que donat un número N retorni el nombre de divisors que té.
Per exemple si donem el 12 ha de retornar: 6

12. Fes una funció *`es_primer`* que donat un número N retorni si un número és primer.
Són primers els que tenen només dos divisors, el 1 i ell mateix.

13. Fes una funció *`maxim_comu_divisor`* que passats dos números retorni el màxim comú divisor.
El màxim comú divisor és el divisor de tots dos més gran que hi hagi. Si no trobem cap divisor, el 1 sempre ho serà.

14. Fes una funció *`minim_comu_multiple`* que passats dos números retorni el mínim comú múltiple.
El mínim comú múltiple és el múltiple de tots dos més petit que hi hagi. Com a molt, el producte de tots dos ho serà.

--8<-- ".acronims.txt"
