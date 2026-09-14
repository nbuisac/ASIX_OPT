# Exercicis d'Ampliació: Entrada de dades i Condicionals

## Bloc 3: Validació i Seguretat Bàsica

!!!tip "Recordatori abans de començar:"

    * Utilitza `#!py input()` si demanes text.

    * Utilitza `#!py int(input())` si demanes números enters (sense decimals, com nombre de fitxers, de carpetes o dies).

    * Utilitza `#!py float(input())` si demanes números amb decimals (como gigabytes, velocitats o el temps que triga a carregar una web).

3.1. _Comprovació de longitud de la contrasenya_

Quan un usuari es crea un compte, hem de comprovar que la contrasenya sigui prou segura.

Fes un script que demani a l'usuari una nova contrasenya. La funció `#!py len(text)` ens diu quantes lletres o caràcters té un text.

* Si la contrasenya té menys de 8 caràcters, mostrarà: "ERROR: La contrasenya és massa curta. Ha de tenir almenys 8 caràcters."

* Si en té 8 o més, mostrarà: "Contrasenya acceptada i guardada correctament."

???example "Possible Solució"

    ```py
    # --- Solució Exercici 3.1 ---
    passw = input("Escriu una nova contrasenya: ")
    if len(passw) < 8:
        print("ERROR: La contrasenya és massa curta. Ha de tenir almenys 8 caràcters.")
    else:
        print("Contrasenya acceptada i guardada correctament.")
    ```

3.2. _El filtre d'usuaris del sistema_

A l'institut tenim tres tipus d'usuaris: `admin`, `professorat` i `alumnat`. Fes un script que demani el nom d'usuari i el seu rol (text).

* Si el rol és "_admin_", imprimirà: "_Accés total: Pots modificar qualsevol paràmetre._"

* Si el rol és "_professat_", imprimirà: "_Accés mitjà: Pots modificar les notes i crear tasques._"

* Si el rol és "_alumnat_", imprimirà: "_Accés bàsic: Només pots consultar continguts._"

* Per a qualsevol altre text, mostrarà: "_Rol no reconegut. Accés denegat._"

???example "Possible Solució"

    ```py
    # --- Solució Exercici 3.2 ---
    usuari = input("Nom d'usuari: ")
    rol = input("Rol (admin/professat/alumnat): ")
    if rol == "admin":
        print("Accés total: Pots modificar qualsevol paràmetre.")
    elif rol == "professat":
        print("Accés mitjà: Pots modificar les notes i crear tasques.")
    elif rol == "alumnat":
        print("Accés bàsic: Només pots consultar continguts.")
    else:
        print("Rol no reconegut. Accés denegat.")
    ```

## Bloc 4: Manteniment de Sistemes i Hardware

4.1. _Alerta de temperatura del servidor (amb #!py float`)_

Els servidors de la sala de màquines tenen sensors de temperatura. Fes un script que demani la temperatura actual de la CPU (número amb decimals, ex: 65.4).

* Si la temperatura és menor que 50.0 ºC: "Estat: Òptim (Fred)"

* Si està entre 50.0 ºC i 75.0 ºC (ambdós inclosos): "_Estat: Normal_"

* Si està entre 75.1 ºC i 85.0 ºC: "_Atenció: Temperatura elevada. Els ventiladors s'activen al 100%._"

* Si és més gran de 85.0 ºC: "_ALERTA CRÍTICA: Sobreescalfament! Apagant el servidor per seguretat..._"

???example "Possible Solució"

    ```py
    # --- Solució Exercici 4.1 ---
    temp = float(input("Introdueix la temperatura de la CPU (ºC): "))
    if temp < 50.0:
        print("Estat: Òptim (Fred)")
    elif temp <= 75.0:
        print("Estat: Normal")
    elif temp <= 85.0:
        print("Atenció: Temperatura elevada. Els ventiladors s'activen al 100%.")
    else:
        print("ALERTA CRÍTICA: Sobreescalfament! Apagant el servidor per seguretat...")
    ```

4.2. _Calculadora de lloguer de disc al núvol_

Una empresa de serveis al núvol cobra segons l'espai en Gigabytes (GB) que utilitza el client.

* El preu base és de 0.15 € per GB.

* Si el client contracta més de 100 GB, se li fa un descompte directe de 5€ sobre el total.

* Si el client contracta més de 500 GB, se li fa un descompte directe del 10% sobre el total.

Fes un script que demani el nom del client i els GB que vol contractar (enter o decimal). El programa ha de calcular el preu final, aplicar el descompte si correspon, i mostrar el pressupost per pantalla.

???example "Possible Solució"

    ```py
    # --- Solució Exercici 4.2 ---
    client = input("Nom del client: ")
    gb = float(input("GB a contractar: "))
    preu = gb * 0.15
    if gb > 100:
        preu = preu - 5
    elif gb > 500:
        preu = preu * 0.95
    print(f"El pressupost final per a {client} és de {preu:.2f} €.")
    ```

## Bloc 5: Lògica Aplicada (Operadors `#!py and` / `#!py or`)

5.1. _Comprovació de manteniment programat_

L'administrador vol saber si pot executar un script de manteniment que esborra fitxers temporals. Aquest script només es pot executar si es compleixen dues condicions a la vegada:

* L'usuari que ho executa ha de ser "_root_".

* L'hora actual de l'ordinador (demana-la com a número enter de 0 a 23) ha de ser més gran o igual a 21 o menor que 8 (fora de l'horari lectiu).

Fes un script que demani l'usuari i l'hora. Utilitza la lògica condicional per mostrar "_Executant manteniment..._" o "_No és segur executar el manteniment en aquest moment._"

???example "Possible Solució"

    ```py
    # --- Solució Exercici 5.1 ---
    usuari = input("Usuari actual: ")
    hora = int(input("Hora actual (0-23): "))
    if usuari == "root" and (hora >= 21 or hora < 8):
        print("Executant manteniment...")
    else:
        print("No és segur executar el manteniment en aquest moment.")
    ```

5.2. _El verificador d'edat per a l'avaluació_

Per matricular-se a 1r d'ASIX cal tenir almenys 16 anys completats durant l'any actual. Fes un script que demani l'any de naixement de l'alumne (ex: 2008) i l'any actual (ex: 2026).

* Calcula l'edat de l'alumne.

* Si té 16 anys o més, mostra: "_Requisit d'edat correcte: Pot matricular-se._"

* Si en té menys de 16, mostra: "_Atenció: Requereix autorització especial del centre._"

???example "Possible Solució"

    ```py
    # --- Solució Exercici 5.2 ---
    any_naixement = int(input("Any de naixement: "))
    any_actual = int(input("Any actual: "))
    edat = any_actual - any_naixement
    if edat >= 16:
        print(f"Edat: {edat} anys. Requisit d'edat correcte: Pot matricular-se.")
    else:
        print(f"Edat: {edat} anys. Atenció: Requereix autorització especial del centre.")
    ```

--8<-- ".acronims.txt"
