# Exercicis de Funcions

## Bloc 1: Funcions bàsiques i `#!py return`

### Exercici 1: Validador d'Adreça IP

Crea una funció anomenada `#!py es_ip_valida(ip)` que rebi una cadena de text amb una adreça IPv4 (ex: `"192.168.1.1"`).

* La funció ha de comprovar que tingui **4 blocs separats per punts** i que cada bloc sigui un número enter entre _0_ i _255_.

* Ha de retornar `#!py True` si és vàlida o `#!py False` si no ho és.

* Prova-la: Utilitza un `#!py if` amb la cridada a la funció per mostrar un missatge verd o vermell per pantalla.

### Exercici 2: Calculadora de Subxarxa / Mascara

Crea una funció `#!py passar_a_bytes(mida_gb)` que rebi una quantitat de gigabytes (ex: `50`) i retorni el seu equivalent en **Bytes**.

* Recorda: $1 \text{ GB} = 1000 \text{ MB} = 1000 \times 1000 \text{ KB} \dots$

* Utilitza la funció per calcular l'espai en bytes d'un disc de 500 GB i d'un directori de 12 GB.

## Bloc 2: Valors per defecte i mutabilitat

### Exercici 3: Generador de Comandes Ping

Crea una funció `#!py ping_host(ip, intents=4, timeout=2)` que simuli la preparació d'una comanda de xarxa.

* Si no li passem els intents o el timeout, ha de fer servir els valors per defecte (4 intents i 2 segons).

* La funció ha de retornar la cadena de text formatada de la comanda: `#!py ping -c <intents> -W <timeout> <ip>`.

* Prova de cridar-la:

    1. Només passant-li la IP `"8.8.8.8"`.

    1. Passant-li la IP `"10.0.0.1"` amb `intents=10`.


### Exercici 4: Afegir Usuari a la Llista (Atenció a la mutabilitat!)

Crea una funció `#!py registrar_usuari(nom_usuari, llista_usuaris=None)` que **afegeixi un usuari en majúscules** a una llista.

* Atenció: Com que les llistes són mutables, recorda inicialitzar `#!py llista_usuaris` a `#!py None` dins dels paràmetres per evitar el problema dels valors per defecte mutables!

* La funció ha de retornar la llista d'usuaris actualitzada.

## Bloc 3: Àmbit de variables / Scope

### Exercici 5: Contador de Peticions HTTP

Crea un script amb una variable global `#!py PETICIONS_TOTALS = 0`.

* Defineix una funció `#!py processar_peticio(ip_client, estat_http)`.

* Dins de la funció, incrementa el comptador global `#!py PETICIONS_TOTALS` en 1 cada cop que es crida.

* Si `#!py estat_http` és _500_ o _404_, ha de mostrar una alerta d'error per pantalla.

* Simula 5 crides a la funció i finalment mostra el total de peticions processades.

## Bloc 4: Arguments variables *args i **kwargs (correspon a py_023)

### Exercici 6: Calculadora d'Ample de Banda (*args)

Crea una funció `#!py sumar_amplada_banda(*consoms_mbps)` que pugui rebre qualsevol nombre de consums de xarxa en Mbps (ex: 10, 45, 120, 5).

* La funció ha de sumar tots els consums rebuts a `#!py *args` i retornar el total.

* Si el total supera els 1000 Mbps (1 Gbps), ha d'imprimir un avís de saturació de la interfície.

### Exercici 7: Constructor de Fitxers de Configuració (**kwargs)

Crea una funció `#!py generar_linies_config(**opcions)` que rebi paràmetres clau-valor variables.

* Exemple de crida: `#!py generar_linies_config(PORT=80, DOCUMENT_ROOT="/var/www/html", MAX_CLIENTS=150)`

* La funció ha de recórrer el diccionari `#!py kwargs` i retornar una llista de cadenes de text amb el format de fitxer de configuració `#!py CLAU = VALOR`.

--8<-- ".acronims.txt"
