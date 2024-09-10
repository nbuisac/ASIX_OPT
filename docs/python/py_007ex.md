# Python - Exercicis

## Blackjack

En aquest exercici implementareu algunes regles del [blackjack][]{target="_blank"}, com ara la manera de jugar i puntuar el joc.

Nota : En aquest exercici, **A** significa **as**, **J** significa **jota**, **Q** significa **reina** i **K** significa **rei**. S'assumeix una [baralla francesa][]{target="_blank"} de 52 cartes.


### 1. Calcula el valor d'una carta

Al *blackjack* les cartes amb cares (J, Q, K) es puntuen amb **deu** punts cadascuna, l'**as** de vegades val 1 i altres 11, segons com vulguio el jugador i qualsevol altra targeta val el seu valor numèric.

Defineix la funció `#!py valor_de_carta(<carta>)` amb el paràmetre `carta`. La funció ha de retornar el valor numèric de l'string de carta que s'ha passat. 

!!!question "Possible execució"

    ```py
    valor_de_carta("A") # Retorna 1
    valor_de_carta("4") # Retorna 4
    valor_de_carta("J") # Retorna 10
    ```

!!!note "De moment assumim que l'As val un punt 1."

### 2. Determina quina carta té un valor més alt

Defineix la funció `#!py carta_alta(<carta1>, <carta2>)` amb els paràmetres `#!py carta1` i `#!py carta2`. A efectes de puntuació, el valor és el que ha s'ha explicat. La funció ha de retornar quina carta té el valor més alt per puntuar. Si les dues cartes tenen el mateix valor, retorna les dues. La devolució de les dues cartes es pot fer utilitzant una coma a la clàusula `#!py return`:

!!!question "Possible execució"

    ```py
    carta_alta("4", "8") # Retorna "8"
    carta_alta("3", "A") # Retorna "3"
    carta_alta("A", "Q") # Retorna "Q"
    carta_alta("J", "Q") # Retorna ("J", "Q")
    ```

!!!note "De moment assumim que l'As val un punt 1."

### 3. Calculem el valor d'un as

Com s'ha dit abans, un as pot valer 1 o 11 punts. Els jugadors intenten apropar-se el més possible a una puntuació de 21, sense passar per sobre de 21 (anar a "perdre").

Defineix la funció `valor_del_as(<carta1>, <carta2>)` amb els paràmetres `#!py carta1` i `#!py carta2`, que són un parell de cartes que ja estan a la mà abans d'aconseguir la carta as. La funció ha de decidir si el proper as obtindrà un valor d'1 o un valor d'11 i tornarà aquest valor. Recorda: el valor de la mà amb l'as ha de ser el més alt possible sense passar de 21.

!!!tip "Pista : si ja tenim un as a la mà, el valor del proper as seria 1."

!!!question "Possible execució"

    ```py
    valor_del_as('6', 'K') # ha de retornar 1
    valor_del_as('7', '3') # ha de retornar 11
    valor_del_as('A', '3') # ha de retornar 1
    valor_del_as('6', '3') # ha de retornar 11
    ```

### 4. Determina si la mà és *Natural* o *Blackjack*.

Si les dues primeres cartes que reben un jugador són un **as** (**A**) i una carta de 10 punts (**10**, **K**, **Q** o **J** ), aleshores el jugador té una puntuació de 21. Això es coneix com a mà de *blackjack*.

Defineix la funcio `es_blackjack(<carta1>, <carta2>)` amb els paràmetres `#!py carta1` i `#!py carta2`, que són un parell de cartes. Determina si la mà de dues cartes és un *blackjack*, i retorna el booleà `True` si ho és o `False` en cas contrari.

Nota : el càlcul de la puntuació es pot fer de moltes maneres. Però si és possible, comprova si hi ha un as i una carta de deu punts a la mà (o en una posició determinada), en lloc de sumar els valors de la mà.

!!!question "Possible execució"

    ```py
    es_blackjack('A', 'K')  # ha de retornar True
    es_blackjack('10', '9') # ha de retornar False
    es_blackjack('10', 'A') # ha de retornar True
    ```

### 5. Divisió de parelles

Si les dues primeres cartes dels jugadors tenen el mateix valor, com ara dos **sis**, o una **Q** i **K**,  un jugador pot optar per tractar-les com dues mans separades. Això es coneix com **dividir parelles**.

Defineix la funció `puc_dividir_parelles(<carta1>, <carta2>)` amb els paràmetres `#!py carta1` i `#!py carta2`, que són un parell de cartes. Determina si aquesta mà de dues cartes es pot dividir en dos parelles. Si la mà es pot dividir, retorna el booleà `True` en cas contrari, torna `False`.

!!!question "Possible execució"

    ```py
    puc_dividir_parelles('Q', 'J')  # ha de retornar True
    puc_dividir_parelles('10', '9') # ha de retornar False
    puc_dividir_parelles('10', 'Q') # ha de retornar True
    ```

### 6. Doblar

Quan les dues cartes originals repartides sumen 9, 10 o 11 punts, un jugador pot fer una aposta addicional igual a la seva aposta original. Això es coneix com a *doblament*.

Defineix la funció `puc_doblar(<carta1>, <carta2>)` amb els paràmetres `#!py carta1` i `#!py carta2`, que són un parell de cartes. Determina si la mà de dues cartes es pot *doblar* i retorna el booleà `True` quan sigui possible, `False` en cas contrari.

!!!question "Possible execució"

    ```py
    puc_doblar('A', '9')  # ha de retornar True
    puc_doblar('10', '2') # ha de retornar False
    ```

[Extret de ...][]{target="_blank}

[Extret de ...]:        https://exercism.org/tracks/python/exercises/black-jack                 "Extret de ..."
[blackjack]:            https://bicyclecards.com/how-to-play/blackjack/                         "blackjack"
[baralla francesa]:     https://es.wikipedia.org/wiki/Baraja_francesa                           "Baralla francesa"
[Set i mig]:            https://ca.wikipedia.org/wiki/Set_i_mig                                 "Set i mig"
[baralla espanyola]:    https://es.wikipedia.org/wiki/Baraja_espa%C3%B1ola                      "Baralla espanyola"
--8<-- ".acronims.txt"
