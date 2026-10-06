# Bloc 1: Exercicis d'Input i Conversió de Tipus (Typecasting)

!!!tip "Recordatori abans de començar:"

    * Utilitza `#!py input()` si demanes text.

    * Utilitza `#!py int(input())` si demanes números enters (sense decimals, com nombre de fitxers, de carpetes o dies).

    * Utilitza `#!py float(input())` si demanes números amb decimals (como gigabytes, velocitats o el temps que triga a carregar una web).

1.1. _El calculador d'espai per a còpies (Backups)_

Quan fem còpies de seguretat dels ordinadors de l'institut, l'espai es mesura, amb decimals, en Gigabytes. Fes un script que demani a l'administrador:

* El nom del servidor del qual fem la còpia.

* Quants GB ocupa la còpia de seguretat actual (pot tenir decimals, ex: 4.5).

El programa ha de calcular quant espai necessitarem si volem guardar tres còpies exactes d'aquell servidor i mostrar el resultat final per pantalla amb un missatge clar.

**Per fer més**: Podem donar les dades en GB i també en MB. Recorda que 1GB = 1000MB

???example "Possible solució"

    ```py
    # --- Solució Exercici 1.1. ---
    nom_servidor = input("Nom del servidor: ")
    mida_backup = float(input("Mida de la còpia en GB (ex: 4.5): "))
    espai_total = mida_backup * 3
    print("Per guardar 3 còpies de", nom_servidor, " necessitarem ", espai_total, " GB.")
    ```

    o millor 

    ```py title="Solució amb constants"
    # --- Solució Exercici 1.1. ---
    COPIES = 3
    nom_servidor = input("Nom del servidor: ")
    mida_backup = float(input("Mida de la còpia en GB (ex: 4.5): "))
    espai_total = mida_backup * COPIES
    print("Per guardar", COPIES, "còpies de", nom_servidor, "necessitarem", espai_total, "GB.")
    ```

1.2. _Repartiment de memòria RAM_

Imagina que tenim un ordinador central a l'aula amb una quantitat de memòria RAM, en un valor enter (ex: 16 o 32 Gigabytes). Fes un script que demani de forma interactiva:

* Quants GB de memòria RAM té el servidor en total (número enter).

* Entre quantes màquines virtuals d'alumnes s'ha de repartir de manera equivalent.

El programa ha de calcular i mostrar quants GB de RAM li tocaran a la màquina de cada alumne.

**Compte**: Tot i que la RAM total sigui entera, el resultat de la divisió pot donar decimals!

???example "Possible solució"

    ```py
    # --- Solució Exercici 1.2. ---
    ram_total = int(input("Total de RAM del servidor (GB): "))
    num_maquines = int(input("Número de màquines virtuals: "))
    ram_per_maquina = ram_total / num_maquines
    print("Cada màquina virtual disposarà de: " + str(ram_per_maquina) + " GB de RAM.")
    ```

## Bloc 2: Exercicis amb Condicionals (`#!py if`, `#!py elif`, `#!py else`)

2.1: _El detector de webs lentes_

Com a administradors, hem de controlar que les pàgines web de la nostra empresa carreguin ràpidament. Fes un script que demani a l'usuari el temps de càrrega d'una web en segons (utilitza `#!py float` perquè pot trigar 1.5 segons, 0.8 segons, etc.).

El programa ha de prendre una decisió segons el temps introduït:

* Si triga menys de 1.0 segon, ha de mostrar: "_La web va genial! Rendiment òptim._"

* Si triga entre 1.0 i 3.0 segons (ambdós inclosos), ha de mostrar: "_Rendiment acceptable, demana una ullada, però funciona._"

* Si triga més de 3.0 segons, ha de mostrar: "_ALERTA: La web va massa lenta! Cal revisar el servidor._"

???example "Possible solució"

    ```py
    # --- Solució Exercici 2.1 ---
    temps = float(input("Temps de càrrega de la web (segons): "))
    if temps < 1.0:
        print("La web va genial! Rendiment òptim.")
    elif temps <= 3.0:
        print("Rendiment acceptable, demana una ullada, però funciona.")
    else:
        print("ALERTA: La web va massa lenta! Cal revisar el servidor.")
    ```

    o millor

    ```py
    # --- Solució Exercici 2.1 ---
    # 2.1: El detector de webs lentes
    TEMPS_1 = 1.0
    TEMPS_2 = 3.0

    temps_carrega = float(input("Quant triga a carregar la pàgina? "))

    if temps_carrega < TEMPS_1:
        missatge = "La web va genial! Rendiment òptim."
    elif temps_carrega <= TEMPS_2:
        missatge = "Rendiment acceptable, demana una ullada, però funciona."
    else:
        missatge = "ALERTA: La web va massa lenta! Cal revisar el servidor."

    print(missatge)
    ```

2.2. _Control de bateries als portàtils de l'aula_

Volem fer un script que s'executi als portàtils dels alumnes de 1r d'ASIX per comprovar si han de connectar el carregador. El programa demanarà el percentatge actual de la bateria (un número enter del 0 al 100).

La lògica del programa ha de ser:

* Si la bateria és igual a 100, mostrarà: "_Bateria completament carregada._"

* Si la bateria és menor o igual que 15, mostrarà: "_ALERTA CRÍTICA: Connecta el carregador immediatament!_"

* Si la bateria és menor o igual que 30 (però més gran de 15), mostrarà: "_Bateria baixa. Guarda la teva feina._"

* En qualsevol altre cas (bateria correcta), mostrarà: "_Nivell de bateria correcte per treballar._"

???example "Possible solució"

    ```py
    # --- Solució Exercici 2.2 ---
    bateria = int(input("Introdueix el % de bateria actual: "))
    if bateria == 100:
        print("Bateria completament carregada.")
    elif bateria <= 15:
        print("ALERTA CRÍTICA: Connecta el carregador immediatament!")
    elif bateria <= 30:
        print("Bateria baixa. Guarda la teva feina.")
    else:
        print("Nivell de bateria correcte per treballar.")
    ```

[print()]:              https://docs.python.org/3/library/functions.html#print  "print()"
[input()]:              https://docs.python.org/3/library/functions.html#input  "input()"


--8<-- ".acronims.txt"
