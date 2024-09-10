# Python - Exercicis

## La magnífica Lassanya

Escriu un codi per ajudar-te a cuinar una lasanya magnífica del teu llibre de cuina preferit.

Tens cinc **tasques**, totes relacionades amb la cuina de la teva recepta.

### 1. Defineix el temps de cocció previst en minuts

Defineix una constant `#!py TEMPS_PREVIST_COCCIO` que emmagatzemi quants minuts ha de coure la lasanya al forn. Segons el teu llibre de cuina, la lasanya ha d'estar al forn durant **40 minuts**:

!!!question "Possible execució"

    ```py
    TEMPS_PREVIST_COCCIO
    40
    ```

???example "Possible solució"

    ```py
    TEMPS_PREVIST_COCCIO = 40

    ```

### 2. Calcula el temps de cocció restant en minuts

Implementa la funció `#!py temps_de_coccio_restant()` que rebrà els minuts reals que la lasanya ha estat al forn com a argument i retorna quants minuts necessita encara per acabar de coure's en funció del `#!py TEMPS_PREVIST_COCCIO`.

!!!question "Possible execució"

    ```py
    temps_de_coccio_restant(10)
    30
    ```

???example "Possible solució"

    ```py
    def temps_de_coccio_restant(temps):
        return TEMPS_PREVIST_COCCIO - temps

    ```


### 3. Calcula el temps de preparació en minuts

Implementeu la funcio `#!py temps_de_preparacio_en_minuts(nombre_de_capes)` que pren com a argument el nombre de capes que vols afegir a la lasanya i retorna quants minuts cal dedicar a fer-les. Suposem que cada capa triga 2 minuts a preparar-se.

!!!question "Possible execució"

    ```py
    temps_de_preparacio_en_minuts(2)
    4
    ```

???example "Possible solució"

    ```py
    def temps_de_preparacio_en_minuts(capes):
        return capes * 2

    ```

### 4. Calcula el temps total de cocció transcorregut (preparació + forn) en minuts

Implementa la funció `#!py temps_total_en_minuts(nombre_de_capes, temps_al_forn)` que té dos paràmetres: nombre_de_capes( el nombre de capes afegides a la lasanya ) i temps_al_forn( el nombre de minuts que la lasanya ha estat coent al forn ). Aquesta funció ha de retornar el nombre total de minuts que has estat cuinant, que és la suma del temps de preparació i del temps que la lasanya ja ha passat al forn.

!!!question "Possible execució"

    ```py
    temps_total_en_minuts(3, 15)
    21
    ```

???example "Possible solució"

    ```py
    def temps_total_en_minuts(nombre_de_capes, temps_al_forn):
        return temps_de_preparacio_en_minuts(nombre_de_capes) + temps_al_forn

    ```

### 5. Actualitza la recepta amb notes

Torna a la recepta, afegint "notes" en forma de **docstrings** de funció.

!!!question "Possible execució"

    ```py hl_lines="1"
    print(temps_total_en_minuts.__doc__)
    Calcula el temps que portem cuinant.

        :param nombre_de_capes: int - el nombre de capes de la lassanya.
        :param temps_al_forn: int - temps que porta al forn coent.
        :return: int - temps total en minuts des de que hem començat a preparar la lassanya.

        Aquesta funció rep dos paràmetres que representen el nombre de capes de la lassanya i
        el temps que porta a l forn coent i calcula el temps total que portem cuinant la nostra
        lassanya.

    ```

???example "Possible solució"

    ```py
    def temps_total_en_minuts(nombre_de_capes, temps_al_forn):
        """Calcula el temps que portem cuinant.

        :param nombre_de_capes: int - el nombre de capes de la lassanya.
        :param temps_al_forn: int - temps que porta al forn coent.
        :return: int - temps total en minuts des de que hem començat a preparar la lassanya.

        Aquesta funció rep dos paràmetres que representen el nombre de capes de la lassanya i
        el temps que porta a l forn coent i calcula el temps total que portem cuinant la nostra
        lassanya.
        """
        return temps_de_preparacio_en_minuts(nombre_de_capes) + temps_al_forn

    ```

[Extret de ...][]{target="_blank}

[Extret de ...]:        https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna "Extret de ..."
--8<-- ".acronims.txt"
