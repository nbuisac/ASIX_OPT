# Python - Exercicis

## Joc Arcade Ghost Gobble

En aquest exercici, cal implementar algunes regles de **[Pac-Man][]{target="_blank"}**, el clàssic joc d'arcade dels anys 80.

Hi ha quatre regles per implementar, totes relacionades amb els estats del joc.

No et preocupis de com es deriven els arguments, només centra't en combinar-los arguments per retornar el resultat desitjat.



### 1. Defineix si Pac-Man es menja un fantasma

Defineix la funció `#!py menja_fantasma()` que pren rep paràmetres (si Pac-Man té una pastilla de potència activa i si Pac-Man està tocant un fantasma) i retorna un valor booleà si Pac-Man és capaç de menjar-se un fantasma. La funció només ha de tornar `True` si Pac-Man té una pastilla de potència activa i està tocant un fantasma.

!!!question "Possible execució"

    ```py
    menja_fantasma(False, True)
    False
    ```

???example "Possible solució"

    ```py
    def menja_fantasma(te_pastilla, toca_fantasma):
        return te_pastilla and toca_fantasma

    ```

### 2. Defineix si Pac-Man puntua

Defineix la funció `puntua()` que pren dos paràmetres (si Pac-Man està tocant una pastilla de potència i si Pac-Man està tocant un punt) i retorna un valor booleà si Pac-Man ha obtingut una puntuació. La funció hauria de tornar `True` si Pac-Man toca una pastilla o un punt.

!!!question "Possible execució"

    ```py
    puntua(True, True)
    True
    ```

???example "Possible solució"

    ```py
    def puntua(toca_pastilla, toca_punt):
        return toca_pastilla or toca_punt

    ```

### 3. Defineix si Pac-Man perd

Definiu la funció `perd()` que pren dos paràmetres (si Pac-Man té una pastilla de potència activa i si Pac-Man està tocant un fantasma) i retorna un valor booleà si Pac-Man perd. La funció ha de tornar `True` si Pac-Man està tocant un fantasma i no té cap pastilla de potència activa.

!!!question "Possible execució"

    ```py
    lose(False, True)
    True
    ```

???example "Possible solució"

    ```py
    def lose(te_pastilla, toca_fantasma):
        return not te_pastilla and toca_fantasma

    ```

### Defineix si Pac-Man guanya

Definiu la funció `guanya()` que pren tres paràmetres ( si Pac-Man s'ha menjat tots els punts , si Pac-Man té una pastilla de potència activa i si Pac-Man està tocant un fantasma ) i retorna un valor booleà si Pac-Man guanya. La funció hauria de tornar True si Pac-Man s'ha menjat tots els punts i no ha perdut segons els paràmetres definits a la part 3.

!!!question "Possible execució"

    ```py
    guanya(False, True, False)
    False
    guanya(True, True, False)
    True
    guanya(True, True, True)
    True
    guanya(True, False, True)
    False
    guanya(False, False, True)
    False
    guanya(False, True, True)
    False
    ```

???example "Possible solució"

    ```py
    def guanya(s_ha_menjat_tots_els_punts, te_pastilla, toca_fantasma):
        return s_ha_menjat_tots_els_punts and not lose(te_pastilla, toca_fantasma)

    ```


[Extret de ...][]{target="_blank}

[Extret de ...]:        https://exercism.org/tracks/python/exercises/ghost-gobble-arcade-game   "Extret de ..."
[Pac-Man]:              https://ca.wikipedia.org/wiki/Pac-Man                                   "Pac-Man"
--8<-- ".acronims.txt"
