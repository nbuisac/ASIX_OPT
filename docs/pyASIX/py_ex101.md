# Exercicis: Llistes, Conversió de Tipus i Condicionals

Aquí tenim 4 exercicis més que connecten tot el que s'ha vist fins ara:

* lectura de dades,

* conversions,

* operacions amb llistes i

* presa de decisions amb if/else.

## 1. **Control d'accés a IP permesa (_Whitelist_)**

A la configuració d'un tallafocs (firewall) tenim una llista fixa d'adreces IP de confiança (_whitelist_):

```py
ips_permeses = ["192.168.1.10", "192.168.1.15", "10.0.0.5"]
```

Fes un script que:

1. Demani a l'usuari que introdueixi la seva adreça IP.

1. Comprovi si aquesta IP està dins de la llista _ips_permeses_.

1. Si hi és, mostrarà el missatge: "_Accés concedit. La teva IP ocupa la posició X de la llista de confiança._" (Utilitza el mètode `#!py .index()` per trobar la posició X).

1. Si no hi és, mostrarà: "_ALERTA: IP bloquejada pel tallafocs._"

## 2. **Monitorització de disc i desglossament de gigabytes**

Imagina que estem fent un inventari de discs durs de servidors. Tenim la següent llista amb les capacitats en Gigabytes (GB) de 3 servidors:

```py
capacitats_gb = [250, 500, 1000]
```

Fes un script que:

1. Demani a l'administrador la capacitat en GB d'un nou servidor (converteix l'entrada a enter) i l'afegeixi a la llista amb `#!py .append()`.

1. Mostri per pantalla quants servidors tenim en total registrats (fent servir `#!py len()`).

1. Comprovi si el primer servidor de la llista (`#!py capacitats_gb[0]`) té menys de 300 GB.

    1. Si en té menys de 300, mostrarà: "Atenció: El primer servidor té poc espai (X GB). Es recomana substituir-lo."

    1. Si en té 300 o més, mostrarà: "Tots els servidors principals tenen capacitat suficient."

## 3. **Generador de Ports i Assignació Aleatòria**

Per configurar un servei provisional, un administrador vol assignar un port de comunicació dinàmic entre el 1024 i el 49151.

Fes un script que:

1. Importi el mòdul `#!py random`.

1. Generi un port aleatori en aquest rang utilitzant `#!py random.randint()`.

1. Tingui una llista de ports reservats: `#!py ports_ocupats = [8080, 3306, 5432, 27017]`.

1. Comprovi si el port generat a l'atzar està dins la llista ports_ocupats:

    1. Si ja està ocupat, mostrarà: "_ERROR: El port X generat està ocupat. Torna a intentar-ho._"

    1. Si està lliure, mostrarà: "_EXIT: Port X assignat correctament al nou servei._"

## 4. **Calculadora de Mètrica de Xarxa (amb `#!py round` i `#!py math.sqrt`)**

En instal·lar un enllaç de fibra, es fan tres proves de latència (en mil·lisonons, ms).

Fes un script que:

1. Demani a l'usuari el resultat de 3 proves de ping (números decimals, `#!py float`).
    
    Desa els 3 valors en una llista anomenada proves.

2. Calcula la mitjana de les tres proves: $\text{mitjana} = \frac{\text{prova}_1 + \text{prova}_2 + \text{prova}_3}{3}$.

3. Arrodoneix el resultat a 2 decimals fent servir `#!py round()`.

4. Si la mitjana és menor o igual a 20.0 ms: "_Connexió d'alta velocitat (Excel·lent)_".

5. Si la mitjana és més gran de 20.0 ms: "_Latència elevada. Revisa l'enllaç de xarxa_".

--8<-- ".acronims.txt"
