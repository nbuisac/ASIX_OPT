# Python - Exercicis

## Les resistències i els seus colors

Si volem construir alguna cosa amb una `Raspberry Pi` o `ESP32`, utilitzarem resistències. Per a aquest exercici, cal saber que:

* Cada resistència té un valor de resistència.

* Les resistències són petites, de fet tan petites que si hi imprimíssim el valor de la resistència, seria difícil de llegir.

Per evitar aquest problema, els fabricants imprimeixen bandes codificades per colors a les resistències per indicar els seus valors de resistència. Cada banda té una posició i un valor numèric.

Les 2 primeres bandes d'una resistència tenen un esquema de codificació senzill: cada color s'assigna a un únic nombre.

En aquest exercici vas a crear un programa útil perquè no hagis de recordar els valors de les bandes.

Aquests colors estan codificats de la següent manera:

* negre: 0

* marró: 1

* vermell: 2

* taronja: 3

* groc: 4

* verd: 5

* blau: 6

* violeta: 7

* gris: 8

* blanc: 9

Els mnemotècnics mapegen els colors als números, que, quan s'emmagatzemen com a matriu, s'assignen al seu índex a la matriu.

Pots trobar més informació sobre la codificació de colors de les resistències a l'[article de la Viquipèdia sobre la identificació de les resistències per bandes de color][resistències]{target="_blank"}.

L'objectiu d'aquest exercici és crear diferents funcions per a :

### Llista de colors

Enumerar els diferents colors de la banda **`#!py colors_resistencia()`**

!!!question "Possible execució"

    ```py
    colors_resistencia() # Ha de retornar ['negre', 'marró', 'vermell', 'taronja', 'groc', 'verd', 'blau', 'violeta', 'gris', 'blanc']
    ```

### Valor d'un color

Cercar el valor numèric associat a una banda de color particular **`#!py codi_color_resistencia(color)`**

!!!question "Possible execució"

    ```py
    codi_color_resistencia('marró')   ## Ha de retornar 1
    codi_color_resistencia('blanc')   ## Ha de retornar 9
    codi_color_resistencia('violeta') ## Ha de retornar 7
    ```

### Valor de dos colors

Cercar el valor numèric, de dos dígits, associat a dues bandes de color particular **`#!py codi_colors_resistencia(colors_separats_per_guio)`**

En cas de posar més de dos colors, s'obviaràn del tercer al final

!!!question "Possible execució"

    ```py
    codi_colors_resistencia("marró-verd") ## Ha de retornar 15
    codi_colors_resistencia("vermell-groc-verd") ## Ha de retornar 24
    ```

* [Extret de ...][]{target="_blank} 


[Extret de ...]:        https://exercism.org/tracks/python/exercises/resistor-color     "Extret de ..."

[resistències]:          https://ca.wikipedia.org/wiki/Resist%C3%A8ncia_el%C3%A8ctrica_(component)#Identificaci%C3%B3_per_bandes_de_color    "Colors de les resistències"



--8<-- ".acronims.txt"
