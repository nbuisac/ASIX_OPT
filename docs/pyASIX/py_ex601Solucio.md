# Exercicis Pràctics: Fitxers i CSV

## Exercici 1: Filtre i Anàlisi de Log d'Errors

Descarrega o crea un fitxer fictici anomenat `app.log` amb el contingut següent:

```txt
[2026-03-10 08:00:12] INFO - Inici de la connexió
[2026-03-10 08:01:45] WARNING - Temps de resposta alt
[2026-03-10 08:03:10] ERROR - Fallada en la connexió a la BD
[2026-03-10 08:05:00] INFO - Petició rebuda
[2026-03-10 08:06:22] ERROR - Espai en disc insuficient
```

Fes un script que:

1. Llegeixi el fitxer `app.log` línia per línia.

1. Compti quantes línies contenen la paraula "_`ERROR`_".

1. Guardi només les línies d'error en un nou fitxer anomenat `errors_critics.txt`.

1. Mostri per pantalla: "_`S'han trobat [X] errors i s'han guardat a 'errors_critics.txt'.`_"

???example "Possible Solució"

    ```py
    # --- Solució Exercici 1 ---
    comptador_errors = 0

    with open("app.log", "r", encoding="utf-8") as f_entrada:
        with open("errors_critics.txt", "w", encoding="utf-8") as f_sortida:
            for linia in f_entrada:
                if "ERROR" in linia:
                    comptador_errors += 1
                    f_sortida.write(linia)

    print(f"S'han trobat {comptador_errors} errors i s'han guardat a 'errors_critics.txt'.")
    ```

## Exercici 2: Generador de Comptes d'Usuari des de CSV

Imagina que l'equip de Recursos Humans et proporciona el fitxer `nous_empleats.csv` (separat per comes) amb el nom i el departament dels nous treballadors:

```txt
nom,cognom,departament
Marta,Rovira,Sistemes
Joan,García,Xarxes
Laia,Font,Desenvolupament
```

Fes un script que:

1. Llegeixi el fitxer `nous_empleats.csv` fent servir `#!py csv.DictReader`.

1. Generi un nom d'usuari per a cada empleat seguint la regla: **primera lletra del nom en minúscula + cognom en minúscula** (Ex: _`mrovira`_).

1. Generi un nou fitxer `usuaris_creats.csv` (separat per punt i coma ;) amb les columnes: `username`, `departament`.

???example "Possible Solució"

    ```py
    # --- Solució Exercici 2 ---
    import csv

    usuaris_finals = []

    # 1. Llegir el fitxer original
    with open("nous_empleats.csv", "r", encoding="utf-8") as f_in:
        lector = csv.DictReader(f_in, delimiter=",")
        for fila in lector:
            # Generar username: 1a lletra nom + cognom en minúscules
            nom_lletra = fila["nom"][0].lower()
            cognom_clean = fila["cognom"].lower()
            username = f"{nom_lletra}{cognom_clean}"
            
            usuaris_finals.append({
                "username": username,
                "departament": fila["departament"]
            })

    # 2. Escriure el nou fitxer CSV
    camps = ["username", "departament"]

    with open("usuaris_creats.csv", "w", newline="", encoding="utf-8") as f_out:
        escriptor = csv.DictWriter(f_out, fieldnames=camps, delimiter=";")
        escriptor.writeheader()
        escriptor.writerows(usuaris_finals)

    print("Fitxer 'usuaris_creats.csv' generat amb èxit.")
    ```


--8<-- ".acronims.txt"
