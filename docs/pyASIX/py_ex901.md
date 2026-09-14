# Exercicis per practicar `#!py break`, `#!py continue` i `#!py else`

## Exercici 1: Escàner de ports amb aturada ràpida (`#!py break` + `#!py else`)

Un script comprova un rang de ports d'un servidor per veure si n'hi ha cap de privat (ex: el port 22 d'SSH).

```py
ports_oberts = [80, 443, 8080, 22, 3306]
```

Fes un script que recorri la llista de ports:

* Si troba el port 22, ha de mostrar "_ALERTA DE SEGURETAT: Port SSH (22) obert! Aturant l'anàlisi..._" i fer un break.

* Si recorre tots els ports i no troba el 22, el bloc else del bucle ha de mostrar "_Anàlisi completat: No s'han trobat ports d'administració crítics._"

???example "Possible Solució"

    ```py
    # --- Solució Exercici 1 ---
    ports_oberts = [80, 443, 8080, 22, 3306]

    for port in ports_oberts:
        if port == 22:
            print("ALERTA DE SEGURETAT: Port SSH (22) obert! Aturant l'anàlisi...")
            break
    else:
        print("Anàlisi completat: No s'han trobat ports d'administració crítics.")
    ```

## Exercici 2: Filtre de línies de registre (`#!py continue`)

Un script llegeix les línies d'un fitxer de configuració o de log. Moltes línies són comentaris que comencen per # o estan buides.

```py
linies_log = ["SERVEI=apache2", "# Això és un comentari", "PORT=80", " ", "TIMEOUT=30"]
```

Fes un script que recorri la llista amb un for:

* Si la línia comença per # o és un espai en blanc " ", utilitza `#!py continue` per ignorar-la i saltar a la següent.

* Per a la resta de línies vàlides, mostra per pantalla: "Processant paràmetre: [línia]".

???example "Possible Solució"

    ```py
    # --- Solució Exercici 2 ---
    linies_log = ["SERVEI=apache2", "# Això és un comentari", "PORT=80", " ", "TIMEOUT=30"]

    for linia in linies_log:
        if linia.startswith("#") or linia == " ":
            continue  # Ignorem comentaris i línies buides
        print(f"Processant paràmetre: {linia}")
    ```

## Exercici 3: Menú d'intents de connexió (`#!py while` + `#!py break`)

Un script intenta connectar-se a un servidor remot en un bucle `#!py while True:` (bucle infinit).

Fes un script que:

1. Utilitzi una variable `#!py intent = 1`.

1. Dins del `#!py while True`, demani a l'usuari: "_Simular connexió (escriu 'ok' si té èxit, o qualsevol altra cosa si falla): _".

1. Si l'usuari escriu "_ok_", mostra "_Connexió establerta a l'intent [X]!_" i surt del bucle amb un break.

1. Si falla, augmenta el número d'intent. Si arriba a l'intent 4, mostra "_ERROR CRÍTIC: Impossible connectar després de 3 intents._" i surt del bucle amb un break.


???example "Possible Solució"

    ```py
    # --- Solució Exercici 3 ---
    intent = 1

    while True:
        estat = input(f"Intent {intent} - Simular connexió ('ok'/falla): ")
        if estat == "ok":
            print(f" Connexió establerta a l'intent {intent}!")
            break
        
        intent += 1
        if intent > 3:
            print(" ERROR CRÍTIC: Impossible connectar després de 3 intents.")
            break
    ```


--8<-- ".acronims.txt"
