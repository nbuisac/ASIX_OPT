# Exercicis Pràctics: Diccionaris i Inventaris

## Exercici 1: Cercador d'Usuaris del Sistema

Crea un diccionari anomenat usuaris on **les claus siguin noms d'usuari** ("`root`", "`marta`", "`invitat`") i **els valors siguin el seu UID** (un número enter: `0`, `1001`, `1002`).

1. Demana per pantalla un nom d'usuari amb `#!py input()`.

1. Utilitza el mètode `#!py .get()` o l'operador in per comprovar si l'usuari existeix al diccionari.

1. Si existeix, mostra: "`L'usuari [nom] té el UID [uid].`".

1. Si no existeix, mostra: "`ERROR: L'usuari no està registrat al sistema.`".

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


--8<-- ".acronims.txt"
