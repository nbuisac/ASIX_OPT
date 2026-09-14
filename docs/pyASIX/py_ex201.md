# Iteracions (Bucles `#!py for` amb Llistes i `#!py range`)

Aquí tenim 3 exercicis senzills però directes per consolidar el bucle [`#!py for()`][for] i [`#!py range()`][range]:

## Exercici 1: Detector de Ports Vulnerables

Donada la següent llista de ports oberts trobats en un analitzador de xarxa:

```py
ports_oberts = [22, 80, 21, 443, 23]
```

Fes un script que recorri la llista amb un `#!py for`. Per a cada port:

* Si el port és el 21 (FTP) o el 23 (Telnet), mostrarà: "_ALERTA: El port X no és segur!_".

* Per a qualsevol altre port, mostrarà: "_Port X analitzat i segur._".

## Exercici 2: Generador d'adreces IP de la xarxa local

L'administrador vol generar una llista d'adreces IP per a la xarxa _`192.168.1.X`_, des de la IP _`.1`_ fins a la _`.10`_.

Fes un script utilitzant un bucle `#!py range()` que generi aquestes 10 IPs i les mostri per pantalla amb el format: _Assignant IP: 192.168.1.X_.

## Exercici 3: Informe d'ús de disc de la flota de servidors

Tenim dues llistes paral·leles: una amb els noms dels servidors i una altra amb el % de disc usat.

```py
servidors = ["srv-web", "srv-db", "srv-files"]
us de_disc = [45, 88, 92]
```

Fes un script utilitzant `#!py for i in range(len(servidors))` que mostri l'estat de cada servidor.

Si l'ús de disc és més gran de 80%, afegeix un avís de "_ ESPAI CRÍTIC_".

???example "Possible solució als exercics proposats"

    ```py title="Solució Exercici 1"
    # --- Solució Exercici 1 ---
    ports_oberts = [22, 80, 21, 443, 23]
    for port in ports_oberts:
        if port == 21 or port == 23:
            print(f"ALERTA: El port {port} no és segur!")
        else:
            print(f"Port {port} analitzat i segur.")
    ```

    ```py title="Solució Exercici 2"
    # --- Solució Exercici 2 ---
    for i in range(1, 11):
        print(f"Assignant IP: 192.168.1.{i}")
    ```

    ```py title="Solució Exercici 3"
    # --- Solució Exercici 3 ---
    servidors = ["srv-web", "srv-db", "srv-files"]
    us_de_disc = [45, 88, 92]

    for i in range(len(servidors)):
        nom = servidors[i]
        percentatge = us_de_disc[i]
        if percentatge > 80:
            print(f"Servidor {nom}: {percentatge}% d'ús ->  ESPAI CRÍTIC")
        else:
            print(f"Servidor {nom}: {percentatge}% d'ús -> Normal")
    ```

[for]:      https://docs.python.org/es/3.14/reference/compound_stmts.html#the-for-statement
[range]:    https://docs.python.org/es/3.14/library/stdtypes.html#range

--8<-- ".acronims.txt"
