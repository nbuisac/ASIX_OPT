# Exercicis de Funcions

## Bloc 1: Funcions bàsiques i `#!py return`

### Exercici 1: Validador d'Adreça IP

Crea una funció anomenada `#!py es_ip_valida(ip)` que rebi una cadena de text amb una adreça IPv4 (ex: `"192.168.1.1"`).

* La funció ha de comprovar que tingui **4 blocs separats per punts** i que cada bloc sigui un número enter entre _0_ i _255_.

* Ha de retornar `#!py True` si és vàlida o `#!py False` si no ho és.

* Prova-la: Utilitza un `#!py if` amb la cridada a la funció per mostrar un missatge verd o vermell per pantalla.

???example "Possible Solució"

    ```py
    # --- Exercici 1 ---
    def es_ip_valida(ip):
        blocs = ip.split(".")
        if len(blocs) != 4:
            return False
        for b in blocs:
            if not b.isdigit():
                return False
            num = int(b)
            if num < 0 or num > 255:
                return False
        return True
    
    # Prova Ex 1
    ip_test = "192.168.1.50"
    if es_ip_valida(ip_test):
        print(f"La IP {ip_test} és vàlida.")
    ```


### Exercici 2: Calculadora de Subxarxa / Mascara

Crea una funció `#!py passar_a_bytes(mida_gb)` que rebi una quantitat de gigabytes (ex: `50`) i retorni el seu equivalent en **Bytes**.

* Recorda: $1 \text{ GB} = 1000 \text{ MB} = 1000 \times 1000 \text{ KB} \dots$

* Utilitza la funció per calcular l'espai en bytes d'un disc de 500 GB i d'un directori de 12 GB.

???example "Possible Solució"

    ```py
    # --- Exercici 2 (Decimal: 1 KB = 1000 Bytes) ---
    def passar_a_bytes(mida_gb):
        # Utilitzem el sistema decimal oficial (1 GB = 1.000 MB = 1.000.000 KB...)
        bytes_totals = mida_gb * 1000 * 1000 * 1000
        return bytes_totals

    print(f"500 GB són {passar_a_bytes(500)} Bytes.")
    ```

## Bloc 2: Valors per defecte i mutabilitat

### Exercici 3: Generador de Comandes Ping

Crea una funció `#!py ping_host(ip, intents=4, timeout=2)` que simuli la preparació d'una comanda de xarxa.

* Si no li passem els intents o el timeout, ha de fer servir els valors per defecte (4 intents i 2 segons).

* La funció ha de retornar la cadena de text formatada de la comanda: `#!py ping -c <intents> -W <timeout> <ip>`.

* Prova de cridar-la:

    1. Només passant-li la IP `"8.8.8.8"`.

    1. Passant-li la IP `"10.0.0.1"` amb `intents=10`.

???example "Possible Solució"

    ```py
    # --- Exercici 3 ---
    def ping_host(ip, intents=4, timeout=2):
        return f"ping -c {intents} -W {timeout} {ip}"

    print(ping_host("8.8.8.8"))
    print(ping_host("10.0.0.1", intents=10))
    ```

### Exercici 4: Afegir Usuari a la Llista (Atenció a la mutabilitat!)

Crea una funció `#!py registrar_usuari(nom_usuari, llista_usuaris=None)` que **afegeixi un usuari en majúscules** a una llista.

* Atenció: Com que les llistes són mutables, recorda inicialitzar `#!py llista_usuaris` a `#!py None` dins dels paràmetres per evitar el problema dels valors per defecte mutables!

* La funció ha de retornar la llista d'usuaris actualitzada.

???example "Possible Solució"

    ```py
    # --- Exercici 4 ---
    def registrar_usuari(nom_usuari, llista_usuaris=None):
        if llista_usuaris is None:
            llista_usuaris = []
        llista_usuaris.append(nom_usuari.upper())
        return llista_usuaris

    usuaris_sys = registrar_usuari("marta")
    registrar_usuari("joan", usuaris_sys)
    print(f"Usuaris registrats: {usuaris_sys}")
    ```


## Bloc 3: Àmbit de variables / Scope

### Exercici 5: Contador de Peticions HTTP

Crea un script amb una variable global `#!py PETICIONS_TOTALS = 0`.

* Defineix una funció `#!py processar_peticio(ip_client, estat_http)`.

* Dins de la funció, incrementa el comptador global `#!py PETICIONS_TOTALS` en 1 cada cop que es crida.

* Si `#!py estat_http` és _500_ o _404_, ha de mostrar una alerta d'error per pantalla.

* Simula 5 crides a la funció i finalment mostra el total de peticions processades.

???example "Possible Solució"

    ```py
    # --- Exercici 5: Contador de Peticions HTTP (Scope / Àmbit de variables) ---

    # Variable global
    PETICIONS_TOTALS = 0

    def processar_peticio(ip_client, estat_http):
        # Indiquem a Python que volem modificar la variable que està fora de la funció
        global PETICIONS_TOTALS
        PETICIONS_TOTALS += 1
        
        # Comprovem si l'estat HTTP indica un error de client (4xx) o de servidor (5xx)
        if estat_http == 404:
            print(f" [ALERTA] Resource Not Found (404) des de la IP: {ip_client}")
        elif estat_http == 500:
            print(f" [CRÍTIC] Internal Server Error (500) des de la IP: {ip_client}")
        else:
            print(f" [OK] Petició processada ({estat_http}) per a {ip_client}")

    # --- Simulem l'arribada de diferents peticions al servidor web ---
    processar_peticio("192.168.1.15", 200)
    processar_peticio("10.0.0.45", 404)
    processar_peticio("172.16.0.8", 200)
    processar_peticio("192.168.1.100", 500)
    processar_peticio("10.0.0.12", 200)

    # Mostrem el total acumulat
    print(f"\n==========================================")
    print(f"Total de peticions HTTP analitzades: {PETICIONS_TOTALS}")
    print(f"==========================================")
    ```

## Bloc 4: Arguments variables *args i **kwargs (correspon a py_023)

### Exercici 6: Calculadora d'Ample de Banda (*args)

Crea una funció `#!py sumar_amplada_banda(*consoms_mbps)` que pugui rebre qualsevol nombre de consums de xarxa en Mbps (ex: 10, 45, 120, 5).

* La funció ha de sumar tots els consums rebuts a `#!py *args` i retornar el total.

* Si el total supera els 1000 Mbps (1 Gbps), ha d'imprimir un avís de saturació de la interfície.

???example "Possible Solució"

    ```py
    # --- Exercici 6 ---
    def sumar_amplada_banda(*consoms_mbps):
        total = sum(consoms_mbps)
        if total > 1000:
            print(f" ALERTA: Consom total de {total} Mbps supera el límit d'1 Gbps!")
        return total

    total_xarxa = sumar_amplada_banda(150, 400, 500, 80)
    print(f"Consom total: {total_xarxa} Mbps")
    ```

### Exercici 7: Constructor de Fitxers de Configuració (**kwargs)

Crea una funció `#!py generar_linies_config(**opcions)` que rebi paràmetres clau-valor variables.

* Exemple de crida: `#!py generar_linies_config(PORT=80, DOCUMENT_ROOT="/var/www/html", MAX_CLIENTS=150)`

* La funció ha de recórrer el diccionari `#!py kwargs` i retornar una llista de cadenes de text amb el format de fitxer de configuració `#!py CLAU = VALOR`.

???example "Possible Solució"

    ```py
    # --- Exercici 7 ---
    def generar_linies_config(**opcions):
        linies = []
        for clau, valor in opcions.items():
            linies.append(f"{clau.upper()} = {valor}")
        return linies

    config_apache = generar_linies_config(port=80, document_root="/var/www/html", max_clients=150)
    for l in config_apache:
        print(l)
    ```




--8<-- ".acronims.txt"
