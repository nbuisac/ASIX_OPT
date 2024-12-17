# Python

## Exercici d'alternatives

Ajuda de [print()][]{target="_blank}.

Ajuda de [input()][]{target="_blank}.

Ajuda de [if][]{target="_blank}.

1. Fes un programa en c# que calculi la solució de l'equació de primer grau $a x + b = 0$. Ha de controlar quan la $a$ és zero. $x = -b / a$.

    ???example "Possible solució"

        ```py
        print("Anem a resoldre una equació de 1r grau\nax + b = 0\n")
        a = int(input("Entra el valor per la a -> "))
        b = int(input("Entra el valor per la b -> "))
        if a == 0:
            print("No és una equació de 1r grau. No té solució")
        else:
            x = -b / a
            print(f"En {a}x + {b} = 0, x val {x}")
        ```

2. Fes un programa que calculi les solucions d'una equació de segon grau i que no falli mai. No es poden fer arrels de valors negatius ni divisions per 0.

    $$
    ax^2 + bx + c = 0 \longrightarrow x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    $$

    ???example "Possible solució"

        ```py
        import math
        print("Anem a resoldre una equació de 2n grau\nax\u00b2 + bx + c= 0\n")
        a = int(input("Entra el valor per la a -> "))
        b = int(input("Entra el valor per la b -> "))
        c = int(input("Entra el valor per la c -> "))
        if a == 0:
            print("No és una equació de 2n grau.")
        else:
            discriminant = b ** 2 - 4 * a * c
            if discriminant < 0:
                print("No té solucions")
            elif discriminant == 0:
                x = -b / (2 * a)
                print(f"Té una solució\n\tx = {x}")
            else:
                x1 = (-b + math.sqrt(discriminant)) / (2 * a)
                x2 = (-b - math.sqrt(discriminant)) / (2 * a)
                print(f"Té dues solucins\n\tx = {x1}\n\tx = {x2}")
        ```

3. Calcula el valor absolut d'un número. $|3| = 3$ i  $|-3| = 3$. (sempre positiu)
    
    ???example "Possible solució"

        ```py
        print("Calculem el valor absolut d'un nombre: | n |")
        n = float(input("Entra el valor de n -> "))
        if n > 0:
            absolut_n = n
        else:
            absolut_n = -n
        print(f"|{n}| = {absolut_n}")
        ```

4. Fes un programa que ens digui si un número és parell o senar. Cal dividir per 2 i mirar el residu. Si el residu és 0 el nombre és parell i si el residu és 1 el nombre és senar.

    ???example "Possible solució"

        ```py
        n = int(input("Parell o senar? Entra un nombre -> "))
        if n % 2 == 0:
            print(f"{n} és parell")
        else:
            print(f"{n} és senar")
        ```

5. Fes un programa que ens digui si dos números, introduïts pel teclat, han estat introduïts en ordre creixent.

    ???example "Possible solució"

        ```py
        print("Valors creixents?")
        a = float(input("Entra un nombre -> "))
        b = float(input("Entra un altre nombre -> "))
        if a < b:
            print(f"Els valors SÍ s'han introduït en ordre creixent")
        else:
            print(f"Els valors NO s'han introduït en ordre creixent")
        ```

6. Fes un programa que ens digui en quin ordre s'han introduït dos nombres pel teclat (creixent, decreixent o bé són iguals)

    ???example "Possible solució"

        ```py
        print("Ordre de valors")
        a = float(input("Entra un nombre -> "))
        b = float(input("Entra un altre nombre -> "))
        if a < b:
            print(f"El primer valor {a}, és menor que el segon valor {b}")
        elif a == b:
            print(f"El primer valor {a}, és igual que el segon valor {b}")
        else:
            print(f"El primer valor {a}, és major que el segon valor {b}")
        ```

7. Fes un programa que passi d'euros a pessetes i/o al revés. Ens ha de demanar quina operació volem fer i l'import pertinent. Cal aplicar el canvi que toqui (1€ = 166'386 ptes)

    ???example "Possible solució"

        ```py
        CANVI = 166.386
        que = input("De Euros a Pessetes (1) o de Pessetes a Euros (2)")
        if que == "1":
            euros = float(input("Entra la quantitat d'euros -> "))
            pessetes = int(euros * CANVI)
            print(f"{euros} € són {pessetes} pts")
        elif  que == "2":
            pessetes = int(input("Entra la quantitat de pessetes -> "))
            euros = float(pessetes / CANVI)
            print(f"{pessetes} pts són {euros} € ")
        else:
            print("Opció incorrecta")
        ```

8. Fes un programa que ens demani la operació que volem fer (+, -, * ó /), dos valors i mostri el resultat pertinent.

    ???example "Possible solució"

        === "Primera solució"
        
            ```py
            que = input("Quina operació vols fer? (S)uma, (R)esta, (M)ultiplicació o (D)ivisió ? -> ")
            if que == "S":
                n1 = float(input("Entra el primer nombre -> "))
                n2 = float(input("Entra el segon  nombre -> "))
                resultat = n1 + n2
                print(f"{n1} + {n2} = {resultat}")
            elif que == "R":
                n1 = float(input("Entra el primer nombre -> "))
                n2 = float(input("Entra el segon  nombre -> "))
                resultat = n1 - n2
                print(f"{n1} - {n2} = {resultat}")
            elif que == "M":
                n1 = float(input("Entra el primer nombre -> "))
                n2 = float(input("Entra el segon  nombre -> "))
                resultat = n1 * n2
                print(f"{n1} * {n2} = {resultat}")
            elif que == "D":
                n1 = float(input("Entra el primer nombre -> "))
                n2 = float(input("Entra el segon  nombre -> "))
                if n2 == 0:
                    print("No es pot dividir per zero")
                else:
                    resultat = n1 / n2
                    print(f"{n1} / {n2} = {resultat}")
            else:
                print("Opció incorrecta")
            ```

        === "Segona solució"
        
            ```py
            que = input("Quina operació vols fer? (S)uma, (R)esta, (M)ultiplicació o (D)ivisió ? -> ")
            if que in "SRMDsrmd":
                n1 = float(input("Entra el primer nombre -> "))
                n2 = float(input("Entra el segon  nombre -> "))
                ok = True
                if que in "Ss":
                    resultat = n1 + n2
                    op = "+"
                elif que in "Rr":
                    resultat = n1 - n2
                    op = "-"
                elif que in "Mm":
                    resultat = n1 * n2
                    op = "*"
                elif que in "Dd":
                    if n2 == 0:
                        print("No es pot dividir per zero")
                        ok = False
                    else:
                        resultat = n1 / n2
                        op = "/"
                if ok:
                    print(f"{n1} {op} {n2} = {resultat}")
            else:
                print("Opció incorrecta")
            ```

9. Fes un programa que demani un angle en graus (0-360) i ens indiqui a quin quadrant es troba. Controla que l'angle que s'introdueixi sigui vàlid. Suposarem [0,90) és el 1rQ, [90,180) és el 2nQ, [180,270) és el 3rQ i [270,360) és el 4tQ. Pots fer l'exercici per qualsevol valor positiu (si és major que 360 també funcioni).

    ???example "Possible solució"

        ```py
        grausTotals = float(input("Entra els graus -> "))
        # Posem els graus enrte 0 i 360
        graus = grausTotals % 360
        # Posem els graus en valor positiu
        if graus < 0:
            graus = 360 + graus;
        if graus < 90:
            quadrant = "primer"
        elif graus < 180:
            quadrant = "segon"
        elif graus < 270:
            quadrant = "tercer"
        else:
            quadrant = "quart"
        print(f"{grausTotals} graus es troben al {quadrant} quadrant")
        ```

10. Fes un programa que demani una lletra i digui si és majúscula, minúscula o no és lletra. 

    ???example "Possible solució"

        === "Sense contemplar accents ni ç ni ñ"
            ```py
            lletra = input("Entra una lletra -> "))
            # Posem els graus en valor positiu
            if 'a' <= lletra[0] < ='z' < 0:
                print(f"{a[0]} és minúscula")
            elif 'A' <= lletra[0] < ='Z' < 0:
                print(f"{a[0]} és majúscula")
            else:
                print(f"{a[0]} no és lletra")
            ```

        === "Contemplant accents i ç i ñ"
            ```py
            lletra = input("Entra una lletra -> "))
            # Posem els graus en valor positiu
            if 'a' <= lletra[0] < ='z' < 0 or a[0] in "àèìòùáéíóúäëïöüçñ":
                print(f"{a[0]} és minúscula")
            elif 'A' <= lletra[0] < ='Z' < 0 or a[0] in "ÀÈÌÒÙÁÉÍÓÚÄËÏÖÜÇÑ":
                print(f"{a[0]} és majúscula")
            else:
                print(f"{a[0]} no és lletra")
            ```

        === "amb mètodes islower() i isupper() i comprovant una lletra"
            ```py
            lletra = input("Entra una lletra -> ")
            if len(lletra) != 1:
                print("No has entrat un caràcter")
            elif lletra.islower():
                print("És minúscula")
            elif lletra.isupper():
                print("És MASJÚSCULA")
            else:
                print("No és lletra")
            ```

11. Fes un programa que demani una lletra i digui si és o no una vocal.

    ???example "Possible solució"

        ```py
        VOCALS = "aeiouAEIOUáéíóúÁÉÍÚÓàèìòùÀÈÌÒÙäëïöüÄËÏÖÜÂÊÎÔÛ"
        lletra = input("Entra una lletra -> ")

        if len(lletra) != 1:        # Comprovem que només hagin entrat un caràcter
            print("He demanat un sol caràcter")
        elif lletra[0] in VOCALS:
            print(f"{lletra[0]} SÍ és una vocal")
        else:
            print(f"{lletra[0]} NO és una vocal")
        ```

12. Fes un programa que demani un caràcter i digui si és o no lletra.

    ???example "Possible solució"

        ```py
        lletra = input("Entra una lletra -> ")

        if len(lletra) != 1:        # Comprovem que només hagin entrat un caràcter
            print("He demanat un sol caràcter")
        elif lletra.isalpha():
            print(f"{lletra} SÍ és una lletra")
        else:
            print(f"{lletra} NO és una lletra")
        ```

13. Fes un programa que passi una lletra a majúscules. Si no és minúscula no ha de fer res.

    ???example "Possible solució"

        ```py
        lletra = input("Entra una lletra -> ")

        if len(lletra) != 1:        # Comprovem que només hagin entrat un caràcter
            print("He demanat un sol caràcter")
        elif lletra.islower():
            lletra = lletra.upper()
        print(f"En majúscula -> {lletra}")
        ```

14. Fes un programa que digui si un any és de traspàs o no. Ho serà quan sigui múltiple de 4, com el 2020. Compte, els múltiples de 100 no són tots de traspàs, només aquells que són múltiples de 400 com el 2000 (1900 no va ser de traspàs).

    ???example "Possible solució"

        ```py
        anyy = int(input("Entra un any -> "))

        if anyy % 400 == 0 or anyy % 100 != 0 and anyy % 4 == 0 :
            print(f"{anyy} SÍ és de traspàs")
        else:
            print(f"{anyy} NO és de traspàs")
        ```

15. Fes un programa que demani dos números qualssevol i després els mostri en ordre creixent. Demana `a` i `b`, i escriu `a` i `b`. Ha de permutar el valor de les variables si cal.

    ???example "Possible solució"

        === "Amb variable d'ajuda"

            ```py
            valor1 = input("Entra un valor -> ")
            valor2 = input("Entra un altre valor -> ")

            ajuda = valor1
            valor1 = valor2
            valor2 = ajuda

            print(f"Els valors permutats són {valor1} i {valor2}"")
            ```

        === "Sense variable d'ajuda. Més Python"

            ```py
            valor1 = input("Entra un valor -> ")
            valor2 = input("Entra un altre valor -> ")

            valor1, valor2 = valor2, valor1

            print(f"Els valors permutats són {valor1} i {valor2}")
            ```

16. Fes un programa que demani tres números introduïts per teclat i digui si estan ordenats. (dos nombres entrats consecutivament iguals considerarem que no trenquen l'ordre).

17. Fes un programa que demani tres números introduïts per teclat i ens digui quin és el més gran.

18. Fes un programa que a partir d'una nota numèrica entera entre 0 i 10 indiqui si correspon a:

    * [0 .. 4] → suspès

    * [5 .. 8] → aprovat

    * 9 → excel·lent

    * 10 → MATRÍCULA D'HONOR

    * altrament: error

19. Fes un programa que donades dues notes amb decimals entre 0 i 10, corresponents a pràctiques (30%) i a teoria (70%), calculi la mitjana i expressi el resultat en lletres, tenint en compte la següent taula, i que si una nota qualsevol és inferior a 3 ja no fa mitjana (suspèn automàticament):

    * [0 .. 5) 	 suspès

    * [5 .. 7) 	 aprovat

    * [7 .. 9) 	 notable

    * [9  .. 10) 	 excel·lent

    * 10 	 matrícula d'honor 

20. Volem calcular el preu d'una entrada de cinema:
    
    * Sabem que una entrada estàndard val 5 €.
    
    * Si tens carnet jove et fan un 15% de descompte.
    
    * Els dimarts fan un 20%.
    
    * El cap de setmana no fan cap descompte a ningú.
    
    * Només et poden fer un descompte.

    Fes un programa que demani per cada opció si es compleix o no (resposta s/n) i ens digui el preu que hem de pagar. (escull l'ordre de preguntes correcte)

21. Fes un programa que donada una hora, minut i segon, incrementi un segon i mostri l'hora resultant. Cal verificar que l'hora estigui entre 0 i 23, els minuts entre 0 i 59 i els segons entre 0 i 59.

22. Fes un programa que calculi la tarifa d'un pàrquing, sabent que val 1€ la hora o fracció, és a dir que si estic 3 hores pago 3€, i si estic 3 hores i cinc minuts pago 4€. Per simplificar, per entrar les dades demana  separadament  l'hora  d'entrada,  el  minut  d'entrada,  hora  de sortida  i  minut  de  sortida. Suposem que tarifiquem dintre del mateix dia.

23. Fes un programa que donat un nombre de 2 xifres (té 2 xifres), digui si és cap-i-cua.

24. Fes un programa que donat un nombre de fins a 3 xifres (té 1, 2 ó 3 xifres), digui si és cap-i-cua.

25. Fes un programa que donats tres números, els ordeni creixentment. Ha de permutar el valor de les variables si cal.

26. Fes un programa que demani un número de màxim 4 xifres i escrigui les xifres per separat.

27. Fes un programa que demani un número (1-7) i escrigui a quin dia de la setmana correspon (dilluns-diumenge). En cas de no entrar una dada correcta, mostra un error.

28. Fes un programa que ens demani el número de DNI i ens calculi la lletra del NIF. Per calcular-la simplement dividim el número per 23 i segons el residu escollim la lletra corresponent dins la següent llista: TRWAGMYFPDXBNJZSQVHLCKE el 0 és la T, el 1 la R, ... Utilitza el que s'ha fet a classe fins el moment.

29. Fes un programa que demani un número de 2 xifres màxim i l'escrigui en nombres romans. Per exemple el 49 s'escriu ajuntant el 40 i el 9: XLIX. 

30. Fes un programa que donada una data, digui a quina estació de l'any correspon:

    | Període | Estació |
    |:-------:|:------- |
    | 21/03 – 20/06 | Primavera |
    | 21/06 – 20/09 | Estiu  |
    | 21/09 – 20/12 | Tardor |
    | 21/12 – 20/03 | Hivern |

31. (Dificultat ++) Fes un programa per validar una data. L'entrada de la data serà un número enter en format `ddmmaaaa` i cal controlar 

    * Que el mes estigui entre 1 i 12

    * Que  el  dia  sigui  correcte  per  al  mes  corresponent  (incloent  el  mes  de  febrer  i  els anys  de traspàs)


[print()]:          https://docs.python.org/library/functions.html#print  "print()"
[input()]:          https://docs.python.org/library/functions.html#input  "input()"
[if]:               https://docs.python.org/reference/compound_stmts.html#the-if-statement  "if"



--8<-- ".acronims.txt"
