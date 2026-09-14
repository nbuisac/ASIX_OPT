# Exercicis Pràctics: Diccionaris i Inventaris

## Exercici 1: Cercador d'Usuaris del Sistema

Crea un diccionari anomenat usuaris on **les claus siguin noms d'usuari** ("`root`", "`marta`", "`invitat`") i **els valors siguin el seu UID** (un número enter: `0`, `1001`, `1002`).

1. Demana per pantalla un nom d'usuari amb `#!py input()`.

1. Utilitza el mètode `#!py .get()` o l'operador in per comprovar si l'usuari existeix al diccionari.

1. Si existeix, mostra: "`L'usuari [nom] té el UID [uid].`".

1. Si no existeix, mostra: "`ERROR: L'usuari no està registrat al sistema.`".

???example "Posssible Solució"

    ```py
    # --- Solució Exercici 1 ---
    usuaris = {
        "root": 0,
        "marta": 1001,
        "invitat": 1002
    }

    nom = input("Introdueix el nom d'usuari a consultar: ")
    uid = usuaris.get(nom)

    if uid is not None:
        print(f"L'usuari '{nom}' té el UID {uid}.")
    else:
        print(f"ERROR: L'usuari '{nom}' no està registrat al sistema.")
    ```

## Exercici 2: Gestor de Quotes de Disc per Usuari

Tenim el següent diccionari amb el consum de disc en GB de diferents usuaris:

```py
consum_disc = {
    "pere": 12.5,
    "anna": 48.0,
    "marc": 55.2,
    "laura": 8.1
}
```

Fes un script que:

1. Afegeixi un nou usuari "`jordi`" amb un consum de `32.4` GB.

1. Modifiqui el consum de "`anna`" a `51.5` GB.

1. Recorri el diccionari amb `#!py .items()`: per a cada usuari amb un consum superior a 50 GB, ha de mostrar un avís de "_`EXCÉS DE QUOTA: [nom] ({gb} GB)`_".

???example "Posssible Solució"

    ```py
    # --- Solució Exercici 2 ---
    consum_disc = {
        "pere": 12.5,
        "anna": 48.0,
        "marc": 55.2,
        "laura": 8.1
    }

    # 1. Afegim l'usuari
    consum_disc["jordi"] = 32.4

    # 2. Modifiquem un usuari
    consum_disc["anna"] = 51.5

    # 3. Comprovem quotes
    print("=== AUDITORIA DE QUOTES DE DISC ===")
    for nom, gb in consum_disc.items():
        if gb > 50.0:
            print(f"EXCÉS DE QUOTA: {nom} ({gb} GB)")
        else:
            print(f"OK: {nom} ({gb} GB)")
    ```

## Exercici 3: Auditoria d'Inventari de Hardware (Niuat)

Fes servir la llista de diccionaris `inventari` de l'apartat 4 de la teoria:

```py
inventari = [
    {"hostname": "srv-web", "ip": "10.0.0.1", "ram_gb": 16, "estat": "ok"},
    {"hostname": "srv-db", "ip": "10.0.0.2", "ram_gb": 64, "estat": "error"},
    {"hostname": "srv-backup", "ip": "10.0.0.3", "ram_gb": 8, "estat": "ok"}
]
```

Fes un script que:

1. Calculi la RAM total sumada de tots els servidors de la llista fent servir un bucle `#!py for`.

1. Imprimeixi per pantalla la RAM total.

1. Mostri només els nom dels servidors que tinguin més de 10 GB de RAM i el seu estat sigui "_`ok`_".

???example "Posssible Solució"

    ```py
    # --- Solució Exercici 3 ---
    inventari = [
        {"hostname": "srv-web", "ip": "10.0.0.1", "ram_gb": 16, "estat": "ok"},
        {"hostname": "srv-db", "ip": "10.0.0.2", "ram_gb": 64, "estat": "error"},
        {"hostname": "srv-backup", "ip": "10.0.0.3", "ram_gb": 8, "estat": "ok"}
    ]

    ram_total = 0

    for srv in inventari:
        ram_total += srv["ram_gb"]

    print(f"Memòria RAM total instal·lada a la xarxa: {ram_total} GB\n")

    print("Servidors operatius amb més de 10 GB de RAM:")
    for srv in inventari:
        if srv["ram_gb"] > 10 and srv["estat"] == "ok":
            print(f"- {srv['hostname']} ({srv['ip']}): {srv['ram_gb']} GB RAM")
    ```

--8<-- ".acronims.txt"
