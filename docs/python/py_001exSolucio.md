# Python

## Exercici d'escriptures i assignacions

Ajuda de [print()][]{target="_blank}.

Ajuda de [input()][]{target="_blank}.


1. Escriu un programa Python senzill que imprimeixi la frase "Hola, Python!" a la consola.

    ```bash
    Hola, Python!
    ```
    
    ???example "Possible solució"

        ```py
        print("Hola, Python!")
        ```
        
2. Crea un programa Python que defineixi variables pel **`nom`** i l'**`edat`** d'una persona . A continuació, imprimeix aquests detalls a la consola. El programa ha de mostrar la sortida en el format: `Nom: [`nom`] Edat: [`edat`]`. Aquest exercici imprimeix diversos valors, literals i variables, en una sola instrucció.

    ```bash
    Nom: Pilar Edat: 25
    ```
    
    ???example "Possible solució"

        ```py
        nom = "Pilar"
        edat = 25
        print("Nom:", nom, "Edat:", edat)
        ```
        
3. Desenvolupa un codi Python que utilitzi dues variables **`salutacio`** i **`assumpte`**. Concatena aquestes variables i imprimeix el missatge combinat en aquest format: "[`salutacio`] per [`assumpte`]!.

    ```bash
    Et saludo afablement per haver arribat fins aquí!
    ```
    
    ???example "Possible solució"

        ```py
        salutacio = "Et saludo afablement"
        assumpte = "per haver arribat fins aquí"
        print(salutacio + " per " + assumpte + "!")
        ```

        !!!note "Per concatenar hem utilitzar l'operador més `+`"

4. Desenvolupa un programa Python per imprimir diverses línies de text a la consola utilitzant només una instrucció `print()`. El programa hauria de sortir les línies següents:

    ```bash
    Línia 1
    Línia 2
    Línia 3
    ```

    ???example "Possible solució"

        ```py
        print("Línia 1\nLínia 2\nLínia 3")
        ```

        !!!note "Per escriure un salt de línia hem utilitzar `\n`"


5. Escriu un programa que donat el teu nom digui **Bon dia Sr. X** on **X** és el teu nom.

    ???example "Possible solució"

        ```py
        nom = input("Entra el teu nom -> ")
        print("Bon dia Sr.", nom)
        ```

6. Escriu un programa que donat un radi, calculi l'àrea d'un cercle.

    ???example "Possibles solucions"

        ```py
        PI = 3.1415927
        radi = float(input("Entra el radi d'una circumferència -> "))
        area = 2 * PI * radi * radi # o bé 2 * PI * radi ** 2
        print("L'àrea de la circumferència de radi", radi, "és", area)
        ```

        ```py title="Utilitzant la llibreria math"
        import math
        radi = float(input("Entra el radi d'una circumferència -> "))
        area = 2 * math.pi * math.pow(radi, 2)
        print("L'àrea de la circumferència de radi", radi, "és", area)
        ```

7. Escriu un programa que donat el nom i el cognom de l'usuari, els imprimeixi en ordre invers.

    ???example "Possible solució"

        ```py
        nom = input("Entra el teu nom -> ")
        cognom = input("Entra el teu cognom -> ")
        print("Bon dia Sr.", nom, cognom)
        print("Bon dia Sr.", cognom, nom)
        print("Bon dia Sr.", nom[::-1], cognom[::-1])
        print("Bon dia Sr.", cognom[::-1], nom[::-1])
        ```

8. Escriu un programa que donat un enter calculi el valor de n * n

    ???example "Possible solució"

        ```py
        numero = int(input("Entra un número enter -> "))
        nn = numero * numero
        print(numero, "x", numero, "=", nn)
        ```

        ```py title="Sumant n vegades n"
        nn = 0
        for a in range(numero):
            nn = nn + numero
        print(numero, "x", numero, "=", nn)
        ```


9. Escriu un programa que donat una quantitat la desglossi amb bitllets i monedes.

    ???example "Possible solució"

        ```py title="Així hauria d'anar però pot tenir problemes pels decimals"
        quantitat = float(input("Entra una quantitat -> "))
        ## Anirem desglossant començant per bitllets, de 500 acabant amb monedes de 1ct
        bitllets = quantitat // 500
        quantitat = quantitat % 500
        print(bitllets, "bitllets de 500")

        bitllets = quantitat // 200
        quantitat = quantitat % 200
        print(bitllets, "bitllets de 200")

        bitllets = quantitat // 100
        quantitat = quantitat % 100
        print(bitllets, "bitllets de 100")

        bitllets = quantitat // 50
        quantitat = quantitat % 50
        print(bitllets, "bitllets de 50")

        bitllets = quantitat // 20
        quantitat = quantitat % 20
        print(bitllets, "bitllets de 20")

        bitllets = quantitat // 10
        quantitat = quantitat % 10
        print(bitllets, "bitllets de 10")

        bitllets = quantitat // 5
        quantitat = quantitat % 5
        print(bitllets, "bitllets de 5")

        monedes = quantitat // 2
        quantitat = quantitat % 2
        print(monedes, "monedes de 2 €")

        monedes = quantitat // 1
        quantitat = quantitat % 1
        print(monedes, "monedes de 1 €")

        monedes = quantitat // 0.50
        quantitat = quantitat % 0.50
        print(monedes, "monedes de 50 cts")

        monedes = quantitat // 0.20
        quantitat = quantitat % 0.20
        print(monedes, "monedes de 20 cts")

        monedes = quantitat // 0.10
        quantitat = quantitat % 0.10
        print(monedes, "monedes de 10 cts")

        monedes = quantitat // 0.05
        quantitat = quantitat % 0.05
        print(monedes, "monedes de 5 cts")

        monedes = quantitat // 0.02
        quantitat = quantitat % 0.02
        print(monedes, "monedes de 2 cts")

        monedes = quantitat // 0.01
        quantitat = quantitat % 0.01
        print(monedes, "monedes de 1 cts")
        ```

        ```py title="Multipliquem per 100 i treballem amb cèntims"
        quantitat = float(input("Entra una quantitat -> "))
        ## Anirem desglossant començant per bitllets, de 500 acabant amb monedes de 1ct
        bitllets = quantitat // 500
        quantitat = quantitat % 500
        print(bitllets, "bitllets de 500")

        bitllets = quantitat // 200
        quantitat = quantitat % 200
        print(bitllets, "bitllets de 200")

        bitllets = quantitat // 100
        quantitat = quantitat % 100
        print(bitllets, "bitllets de 100")

        bitllets = quantitat // 50
        quantitat = quantitat % 50
        print(bitllets, "bitllets de 50")

        bitllets = quantitat // 20
        quantitat = quantitat % 20
        print(bitllets, "bitllets de 20")

        bitllets = quantitat // 10
        quantitat = quantitat % 10
        print(bitllets, "bitllets de 10")

        bitllets = quantitat // 5
        quantitat = quantitat % 5
        print(bitllets, "bitllets de 5")

        monedes = quantitat // 2
        quantitat = quantitat % 2
        print(monedes, "monedes de 2 €")

        monedes = quantitat // 1
        quantitat = quantitat % 1
        print(monedes, "monedes de 1 €")

        monedes = quantitat // 0.50
        quantitat = quantitat % 0.50
        print(monedes, "monedes de 50 cts")

        monedes = quantitat // 0.20
        quantitat = quantitat % 0.20
        print(monedes, "monedes de 20 cts")

        monedes = quantitat // 0.10
        quantitat = quantitat % 0.10
        print(monedes, "monedes de 10 cts")

        monedes = quantitat // 0.05
        quantitat = quantitat % 0.05
        print(monedes, "monedes de 5 cts")

        monedes = quantitat // 0.02
        quantitat = quantitat % 0.02
        print(monedes, "monedes de 2 cts")

        monedes = quantitat // 0.01
        quantitat = quantitat % 0.01
        print(monedes, "monedes de 1 cts")
        ```


10. Escriu un programa que determini el total d'IVA d'un producte donada una quantitat sense IVA i el % d'IVA.

    ???example "Possible solució"

        ```py
        importt = float(input("Entra l'import sense IVA -> "))
        pct_iva = float(input("Entra el % d'IVA -> "))
        import_iva = round(importt * pct_iva / 100, 2)
        import_total = importt + import_iva
        print(importt)
        print(import_iva, " ( ", pct_iva, "% )")
        print(import_total)
        ```

11. Escriu un programa que et permeti calcular l'àrea i el perímetre d'un quadrat de `X` metres de costat.

    ???example "Possible solució"

        ```py
        costat = float(input("Entra la longitud del costat -> "))
        perimetre = costat * 4
        area = costat * costat
        print("Perimetre -> ", perimetre)
        print("Àrea -> ", area)
        ```

12. Escriu un programa que et permeti calcular l'àrea d'un rectangle i el seu perímetre.

    ???example "Possible solució"

        ```py
        costat1 = float(input("Entra la longitud d'un costat -> "))
        costat2 = float(input("Entra la longitud de l'altre costat -> "))
        perimetre = costat1 * 2 + costat2 * 2
        area = costat1 * costat2
        print("Perimetre -> ", perimetre)
        print("Àrea -> ", area)
        ```

13. Escriu un programa que et permeti calcular l'àrea d'un triangle i el seu perímetre.

    [https://es.wikihow.com/calcular-el-%C3%A1rea-de-un-tri%C3%A1ngulo][]{target="_blank"}

    ???example "Possible solució"

        ```py
        import math

        costat1 = float(input("Entra la longitud d'un costat -> "))
        costat2 = float(input("Entra la longitud de l'altre costat -> "))
        costat3 = float(input("Entra la longitud de l'altre costat -> "))
        perimetre = costat1 + costat2 + costat3
        s = perimetre / 2
        area = math.sqrt(s*(s-costat1)*(s-costat2)*(s-costat3))
        print("Perimetre -> ", perimetre)
        print("Àrea -> ", area)
        ```

14. Escriu un programa que determini aproximadament l'edat de l'usuari en dies, donada la seva data de naixement. Pots considerar que els mesos tenen 30 dies. Fes-ho a a partir del mes i l'any.

    ???example "Possible solució"

        ```py
        import datetime

        avui = datetime.datetime.now()
        dia_avui = avui.day
        mes_avui = avui.month
        any_avui = avui.year

        print("Avui és", dia_avui, "del mes", mes_avui, "de l'any", any_avui)

        avui = input("Entra la data de naixement (DD/MM/AAAA) -> ")
        dia_naixement = int(avui.split("/")[0])
        mes_naixement = int(avui.split("/")[1])
        any_naixement = int(avui.split("/")[2])

        print("Vares néixer el dia", dia_naixement, "del mes", mes_naixement, "de l'any", any_naixement)

        dies = (any_avui - any_naixement) * 365
        dies = dies + (mes_avui - mes_naixement) * 30
        dies = dies + (dia_avui - dia_naixement)

        print("Tens uns", dies, "dies")
        ```

15. La nota final es calcula amb la nota de tres examens. N'hem fet dos. Escriu un programa que em pregunti les dues primeres notes per teclat i em determini quina nota haig de treure per arribar a 5 en la mitjana de tres exàmens.

    ???example "Possible solució"

        ```py
        nota1 = float(input("Entra la primera nota -> "))
        nota2 = float(input("Entra la segona nota -> "))
        nota = 15 - nota1 - nota2
        print("Per arribar al 5 necessites un", nota)
        ```

16. La nota d'una assignatura és calcula en base als exàmens (e) i les proves pràctiques (p), es fa la mitjana ponderada al 40% i 60%. He tret un 7 de pràctiques (p), escriu un programa que em calculi quina és la nota final a patir d'una hipotètica nota d'examen introduïda per teclat.

    ???example "Possible solució"

        ```py
        PCT_EXAMEN = 40
        PCT_PRACTIQUES = 60

        nota_practiques = 7
        nota_examen = float(input("Entra la nota de l'examen -> "))
        nota_final = (nota_practiques * PCT_PRACTIQUES + nota_examen * PCT_EXAMEN) / (PCT_EXAMEN + PCT_PRACTIQUES)
        print("La nota final és ", nota_final)
        ```

17. Escriu un programa que donats els dos costats d'un triangle rectangle en calculi la hipotenusa.

    ???example "Possible solució"

        ```py title="Per fer l'arrel quadrada podem elevar a 0.5"
        catet1 = float(input("Entra la mesura del primer catet -> "))
        catet2 = float(input("Entra la mesura del segon catet -> "))
        hipotenusa = (catet1 ** 2 + catet2 ** 2) ** 0.5
        print("La hipotenusa del triangle és ", hipotenusa)
        ```

18. Et donen un número de 3 dígits. Es tracta d'invertir-lo. Per exemple 345 -> 543

    ???example "Possible solució"

        ```py title="Amb enters"
        numero = int(input("Entra un número de 3 xifres -> "))

        unitats = numero % 10
        centenes = numero // 100
        desenes = (numero // 10) % 10
        invers = unitats * 100 + desenes * 10 + centenes
        print("L'invers de", numero, "és", invers)
        ```

        ```py title="Amb mètodes d'string"
        numero = int(input("Entra un número de 3 xifres -> "))

        invers = int(str(numero)[::-1])
        print("L'invers de", numero, "és", invers)
        ```

De l'1 al 4, [Extrets de ...][]{target="_blank}

[print()]:              https://docs.python.org/3/library/functions.html#print  "print()"
[input()]:              https://docs.python.org/3/library/functions.html#input  "input()"
[Extrets de ...]:        https://thinkinfi.com/python-print-function-exercises-with-solutions-for-beginners/ "Extret de ..."

[https://es.wikihow.com/calcular-el-%C3%A1rea-de-un-tri%C3%A1ngulo]:    https://es.wikihow.com/calcular-el-%C3%A1rea-de-un-tri%C3%A1ngulo   "Àrea d'un triangle"

--8<-- ".acronims.txt"
