# Python

## Exercici d'escriptures i assignacions

Ajuda de [print()][]{target="_blank}.

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


[Extret de ...][]{target="_blank}

[print()]:              https://docs.python.org/3/library/functions.html#print  "print()"
[Extret de ...]:        https://thinkinfi.com/python-print-function-exercises-with-solutions-for-beginners/ "Extret de ..."
--8<-- ".acronims.txt"
