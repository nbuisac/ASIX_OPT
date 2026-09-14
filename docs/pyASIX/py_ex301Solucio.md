# Exercicis Pràctics: Bucle WHILE i Validació

## Exercici 1: Reintent de contrasenya (Límit d'intents)

En un sistema d'autenticació, un usuari té un màxim de 3 intents per encertar la contrasenya correcta ("_superSecret123_").

Fes un script que:

1. Utilitzi una variable comptador `#!py intents = 0`.

1. Demani la contrasenya a l'usuari en un bucle [`#!py while`][while].

1. Si la contrasenya és correcta, mostri "_Accés concedit!_" i surti del bucle.

1. Si falla, augmenti el comptador d'intents.

1. Si arriba a 3 intents fallits, el bucle s'ha de aturar i mostrar: "_COMPTE BLOCAT: Has superat el màxim d'intents._"

???example "Possible Solució"

    ```py
    # --- Solució Exercici 1 ---
    intents = 0
    correcta = False

    while intents < 3 and not correcta:
        passw = input("Introdueix la contrasenya: ")
        if passw == "superSecret123":
            correcta = True
            print("Accés concedit!")
        else:
            intents += 1
            print(f"Contrasenya incorrecta. Intents restants: {3 - intents}")

    if not correcta:
        print("COMPTE BLOCAT: Has superat el màxim d'intents.")
    ```

## Exercici 2: Validació d'entrada de la memòria RAM

Un script de configuració de màquines virtuals exigeix assignar una quantitat de RAM en Megabytes (MB) que sigui com a mínim de 1024 MB (1 GB) i com a màxim de 32768 MB (32 GB).

Fes un script que demani la memòria RAM en un bucle [`#!py while`][while] fins que l'usuari introdueixi un valor compres dins d'aquest rang. Quan sigui vàlid, mostra: _"Màquina virtual configurada amb [X] MB de RAM._"

???example "Possible Solució"

    ```py
    # --- Solució Exercici 2 ---
    ram = int(input("Introdueix la RAM per a la VM (entre 1024 i 32768 MB): "))

    while ram < 1024 or ram > 32768:
        print("ERROR: Quantitat de RAM fora de rang (Mínim 1024 MB, Màxim 32768 MB).")
        ram = int(input("Introdueix una quantitat vàlida de RAM: "))

    print(f"Màquina virtual configurada amb {ram} MB de RAM.")
    ```

## Exercici 3: Confirmació d'acció crítica (_S/N_)

Quan un SysAdmin vol reiniciar un servidor de producció, l'script ha de demanar confirmació. Només s'accepten com a respostes vàlides "_S_" (_Sí_) o "_N_" (_No_).

Fes un script que:

1. Demani a l'usuari: "_Estàs segur que vols reiniciar el servidor? (S/N): _".

1. Si escriu qualsevol cosa diferent de "_S_" o "_N_" (nota: pot ser en majúscula o minúscula), l'script ha d'insistir dient: "_Resposta no vàlida. Escriu 'S' o 'N'._".

1. En sortir del bucle:

    * Si ha escollit "S", mostra: "_Reiniciant el servidor..._".

    * Si ha escollit "N", mostra: "_Operació cancel·lada per l'usuari._".

???example "Possible Solució"

    ```py
    # --- Solució Exercici 3 ---
    resposta = input("Estàs segur que vols reiniciar el servidor? (S/N): ").upper()

    while resposta != "S" and resposta != "N":
        print("Resposta no vàlida. Escriu 'S' o 'N'.")
        resposta = input("Estàs segur que vols reiniciar el servidor? (S/N): ").upper()

    if resposta == "S":
        print("Reiniciant el servidor...")
    else:
        print("Operació cancel·lada per l'usuari.")
    ```

## Exercici 4: Calculadora acumulativa de despeses de llicències

L'administrador vol anar introduint el preu de diferents llicències de software una per una fins que escrigui el número 0 per acabar.

Fes un script que:

1. Demani el preu d'una llicència (_decimal_, _float_).

1. Vagi sumant el preu a una variable _total_.

1. El bucle s'executarà mentre el preu introduït no sigui 0.

1. En acabar (quan l'usuari escrigui 0), mostri el cost total acumulat de les llicències.

**NOTA**: Pots afegir els preus en una llista i després tractar les dades de la llista

???example "Possible Solució"

    ```py
    # --- Solució Exercici 4 ---
    total = 0.0
    preu = float(input("Introdueix el preu de la llicència (€) [Escriu 0 per acabar]: "))

    while preu != 0:
        total += preu
        preu = float(input("Introdueix el preu de la següent llicència (€) [Escriu 0 per acabar]: "))

    print(f"Cost total acumulat de les llicències: {total:.2f} €")
    ```

    o bé

    ```py
    # --- Solució Exercici 4 ---
    llista_preus = []
    preu = float(input("Introdueix el preu de la llicència (€) [Escriu 0 per acabar]: "))

    while preu != 0:
        llista_preus.append(preu)
        preu = float(input("Introdueix el preu de la següent llicència (€) [Escriu 0 per acabar]: "))

    print(f"Cost total acumulat de les llicències: {sum(llista_preus):.2f} €")
    ```

[while]:      https://docs.python.org/es/3.14/reference/compound_stmts.html#while

--8<-- ".acronims.txt"


