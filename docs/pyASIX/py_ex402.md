# Bateria de Reptes Integradors

En aquestes activitats no s'indica quina estructura (`#!py for`, `#!py while`, `#!py list`, `#!py dict`) cal utilitzar. L'objectiu és analitzar el problema, escollir la millor eina i el resoldre'l de la manera més eficient possible.

## Repte 1: L'Auditor de Firewall

A la configuració d'un rúter tenim un registre de les últimes connexions detectades amb l'adreça IP d'origen i el port de destinació:

```python
registres = [
    {"ip": "192.168.1.15", "port": 80},
    {"ip": "10.0.0.45", "port": 22},
    {"ip": "192.168.1.100", "port": 443},
    {"ip": "172.16.0.4", "port": 23},
    {"ip": "192.168.1.15", "port": 3389}
]
```

Crea un script que analitzi aquest registre i mostri una alerta per pantalla si detecta connexions a ports considerats insegurs o crítics (22 per SSH, 23 per Telnet o 3389 per RDP). Per a la resta de ports estàndard (80, 443), ha d'indicar que la connexió és segura.

???tip "Pistes per resoldre'l"

    * Com que tenim una col·lecció d'elements coneguda, quin bucle permet recórrer-la element per element?

    * Cada registre és un conjunt de parelles _clau-valor_. Com s'accedeix al valor del port?

## Repte 2: Validador de Noms d'Usuari del Sistema

Quan un usuari es dóna d'alta al sistema, cal comprovar que el nom d'usuari compleixi dues regles de seguretat fonamentals:

1. Ha de tenir com a mínim 4 caràcters.

1. No pot estar contingut a la llista d'usuaris reservats del sistema: `["root", "admin", "system", "guest"]`.

Fes un script que demani un nom d'usuari per pantalla. Si el nom **no compleix** alguna de les dues regles, l'script ha de mostrar l'error corresponent i tornar a demanar el nom d'usuari **les vegades que calgui** fins que se n'escrigui un de vàlid.

??? tip "Pistes per resoldre'l"

    * Si no sabem vegades s'equivocarà l'usuari, quin tipus de bucle és l'adequat per "capturar-lo" fins que ho faci bé?

    * Recorda la funció `#!py len()` per saber la mida d'un text i l'operador `#!py in` per buscar dins d'una llista.

## Repte 3: Cercador d'Inventari de Servidors

Imagina que un company de feina ens demana les dades d'un servidor concret del centre de dades. Tenim la següent informació organitzada:

```py
servidors = {
    "srv-web": "192.168.1.10",
    "srv-db": "192.168.1.20",
    "srv-mail": "192.168.1.30",
    "srv-proxy": "192.168.1.40"
}
```

Escriu un programa que demani a l'usuari el nom del servidor que vol consultar (ex: `srv-db`).

* Si el servidor existeix, mostra la seva adreça IP.

* Si el servidor no existeix, mostra el missatge: "_`ERROR: Servidor no trobat a l'inventari`_".

??? tip "Pistes per resoldre'l"
    
    * Podem resoldre-ho utilitzant directament mètodes propis de la cerca en diccionaris (com `#!py .get()` o `#!py in`) sense necessitat de fer cap bucle.

## Repte 4: Netejador de Llista d'IPs Duplicades

Després de fer una captura de tràfic a la xarxa, hem obtingut una llista d'adreces IP on moltes d'elles s'han repetit múltiples vegades:

```py
captura_ips = [
    "10.0.0.1",
    "192.168.1.1",
    "10.0.0.1",
    "172.16.0.1",
    "192.168.1.1",
    "10.0.0.1"
]
```

Crea una nova llista buida i utilitza el codi necessari per recórrer la llista original i afegir a la nova llista totes les IPs sense repetir-ne cap. En acabar, mostra la llista neta per pantalla.

??? tip "Pistes per resoldre'l"

    * Podem utilitzar un bucle per anar mirant les IPs una per una.

    * Abans d'afegir una IP a la nova llista (amb `#!py .append()`), com podem comprovar si ja hi és a dins?

## Repte 5: Monitor de Temperatura amb Aturada d'Emergència

Un sensor de la sala de servidors pren lectures de temperatura en graus Celsius de manera continuada:

```py
lectures = [42.1, 45.0, 48.5, 52.3, 71.0, 85.4, 49.0, 41.2]
# lectures = [42.1, 45.0, 48.5, 52.3, 71.0, 75.4, 49.0, 41.2]
```

Fes un script que vagi processant les lectures una per una.

* Si troba una temperatura superior a 80.0 ºC, ha de mostrar un missatge d'emergència ("_`ALERTA CRÍTICA: Sobreescalfament! Aturant el procés d'anàlisi...`_") **i deixar de processar la resta de lectures** immediatament.

* Si la lectura és normal, ha de mostrar "_Lectura [X] ºC: Normal_".

??? tip "Pistes per resoldre'l"

    * Quina instrucció permet tallar o interrompre un bucle en el moment exacte en què es compleix una condició?

## Repte 6: Calculadora d'Ús Mitjà de Memòria RAM

Tenim el registre del percentatge d'ús de RAM de tres servidors durant diferents hores del dia:

```py
us_ram = {
    "srv-app": [45, 50, 55, 60],
    "srv-db": [80, 85, 90, 95],
    "srv-cache": [20, 25, 20, 30]
}
```

Escriu un script que calculi la mitjana d'ús de RAM de cada servidor i la mostri per pantalla. A més, si la mitjana d'un servidor supera el 80%, ha d'afegir l'avís "(_Recomanat ampliar RAM_)".

??? tip "Pistes per resoldre'l"

    * Necessitaràs recórrer el diccionari per obtenir el nom del servidor i la seva llista de valors (el mètode `#!py .items()` serà molt útil).

    * Per calcular la mitjana d'una llista, recorda que pots sumar els seus elements i dividir pel seu total (`#!py len()`).

--8<-- ".acronims.txt"
