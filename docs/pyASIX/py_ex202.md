# Bateria d'Exercicis: Bucle FOR i Recorregut de Llistes


## Bloc A: Recorregut Directe (`#!py for element in llista`)

En aquest bloc no necessitem índexs; només volem agafar cada dada una per una, processar-la o fer-hi comprovacions.

### Exercici 1: Cercador d'usuaris inactius

En una auditoria de seguretat tenim una llista d'usuaris del sistema:

```py
usuaris = ["marta", "invitat", "pau", "test", "laura", "admin_vell"]
```

Fes un script que recorri la llista.

Si l'usuari conté la paraula "_invitat_", "_test_" o "_vell_", ha de mostrar: "_USUARI SOSPETÓS O INACTIU: [nom] -> Cal revisar el compte_".

Per als altres, mostrarà: "_Usuari actiu: [nom]_".

!!!tip "Utilitza in en strings de la mateixa manera que l'hem explicat per a llistes"

### Exercici 2: Filtre de pings fallits

Un script de monitorització recull la latència en mil·lisegons (ms) d'una sèrie de servidors. Si un servidor no respon, es registra un -1.

```py
latencies = [12, 15, -1, 24, -1, 18, 9]
```

Fes un script que recorri la llista de latències i:

1. Compti quants servidors han caigut (quants -1 hi ha) fent servir una variable comptador (caiguts = 0).

1. Per a cada -1, mostri un missatge d'error.

1. En acabar el bucle, mostri el total de servidors caiguts.

### Exercici 3: Calculadora de suma total de tràfic de xarxa

Tenim un registre amb els Megabytes (MB) descarregats per diferents equips de l'aula al llarg del dia:

```py
consums_mb = [120.5, 450.0, 89.2, 1200.8, 310.4]
```

Fes un script que:

1. Utilitzi un bucle `#!py for` i una variable acumuladora (`#!py total = 0.0`) per sumar el consum de tots els equips.

1. Imprimeixi el total de Megabytes consumits a l'aula.

1. Si el total supera els 2000 MB (2 GB), mostri un avís: "Alerta de consum elevat a la xarxa!".

## Bloc B: Generació i Seqüències (for i in range(...))

Aquest bloc serveix per practicar la creació de seqüències de números o la repetició d'accions un número controlat de vegades.

### Exercici 4: Generador de la taula de direccionament d'un Switch

Un switch te 24 ports Ethernet configurables. Fes un script utilitzant `#!py range()` que generi la configuració inicial de tots els ports del 1 al 24 de la següent manera:

* Del port 1 al 20: "_Port FastEthernet 0/[num] -> Mode ACCÉS (Clients)_"

* Del port 21 al 24: "_Port FastEthernet 0/[num] -> Mode TRUNK (Lligam amb servidors/routers)_"

### Exercici 5: Noms d'equips automatitzats

Hem de nombrar 15 ordinadors nous per a un aula d'informàtica (des de pc-01 fins a pc-15).

Fes un script utilitzant `#!py range()` que generi els noms.

!!!tip "Repte de format"

    Si el número és menor de 10, afegeix-li un zero a l'esquerra (ex: _pc-01_, _pc-02_... _pc-10_). Utilitza un `#!py if` per controlar-ho.


## Bloc C: Llistes Paral·leles i Posicions (`#!py for i in range(len(...))`)

Quan tenim dues o més llistes relacionades per la seva posició (índex), necessitem iterar amb `#!py range(len(llista)`).

### Exercici 6: Validació de contrasenyes per defecte

Tenim una llista amb noms d'usuaris i una llista paral·lela amb les seves contrasenyes actuals:

```py
usuaris = ["root", "admin", "maria", "jordi"]
contrasenyes = ["root123", "admin", "M@ria2024", "1234"]
```

Fes un script que recorri les posicions de les llistes i comprovi les contrasenyes:

* Si la contrasenya és "_1234_", "_admin_" o "_root123_", ha de mostrar: "_DANGER: L'usuari [nom] utilitza una contrasenya molt feble ([pass])!_".

* Si no, mostrarà: "_OK: L'usuari [nom] té una contrasenya acceptable._"

### Exercici 7: Comparativa de rendiment de dos servidors

Tenim les lectures de temps de resposta (en ms) de dos servidors (_srv-A_ i _srv-B_) fent la mateixa tasca durant 5 proves:

```py
proves_srv_A = [120, 140, 110, 150, 130]
proves_srv_B = [115, 160, 105, 155, 125]
```

Fes un script que compari prova a prova (posició a posició) quin dels dos servidors ha estat el més ràpid:

* Mostra per a cada prova: "_Prova [num]: Servidor A ([ms]ms) vs Servidor B ([ms]ms) -> Més ràpid: [A/B]_" 

    _La primera prova se suposa que pels umans és la 1._

### Exercici 8: Comprovació de quotes de disc (Amb modificació de text)

Tenim una llista d'usuaris i una llista amb l'espai utilitzat en GB:

```py
usuaris = ["pere", "anna", "marc", "laura"]
espai_gb = [12, 48, 52, 5]
```

**La quota màxima de disc permesa és de 50 GB.**

Fes un script que recorri les llistes i:

* Si un usuari supera els 50 GB, mostri: "_EXCÉS DE QUOTA: [nom] ocupa [GB] GB. Enviant correu d'avís..."_.

* Si està a punt de superar-la (entre 40 i 50 GB inclosos), mostri: "_ALERTA: [nom] ocupa [GB] GB (Prop del límit)"_.

* Si ocupa menys de 40 GB: "_Dins de límit: [nom] ([GB] GB)"_.

[for]:      https://docs.python.org/es/3.14/reference/compound_stmts.html#the-for-statement
[range]:    https://docs.python.org/es/3.14/library/stdtypes.html#range

--8<-- ".acronims.txt"
