# Accés amb APIRest

**REST** en realitat no és una paraula, és un acrònim. Prové de tres paraules d'igual importància:

* Representacional

* Estat

* Transferència

Anem a veure-les per separat

## Representacional

**RE** significa representació. Vol dir que la nostra maquinària emmagatzema, transmet i rep representacions, mentre que el terme representació reflecteix la manera com les dades o estats es conserven dins del sistema i es presenten als usuaris (humans o ordinadors).

**REST** utilitza una manera molt curiosa de representar les seves dades: **sempre és text**. Text pur i senzill.

## Estat
**S** significa *Estat*, de l'anglès *State*. La paraula *estat* és clau per entendre què és **REST** i per a què es podria utilitzar.

Imagineu qualsevol objecte. L'objecte conté un conjunt de propietats. Podem dir que *els valors de totes les propietats de l'objecte constitueixen el seu estat*. Si alguna de les propietats canvia el seu valor, això implica inevitablement l'efecte de canviar l'estat de tot l'objecte. Aquest canvi sovint s'anomena *transició*.

Ara imagineu que **l'objecte s'emmagatzema en un altre lloc**, no al vostre ordinador, sinó en un servidor situat molt lluny. Podeu accedir als recursos del servidor mitjançant la xarxa, però no només l'heu de poder obtenir vosaltres i transferir-lo al vostre ordinador. Per què no? Perquè **ha de ser accessible per a molts** (potser uns quants, potser un milió) usuaris. Ha de romandre al servidor.

Imagineu que cal canviar l'estat de l'objecte a través de la xarxa. Podem fer-ho amb REST. Com? Aviat ho veurem...

## Transferència

**T** significa *Transferència*. La xarxa pot actuar com a portadora que permet transmetre representacions dels estats cap i des del servidor.

!!!note "No l'objecte, sinó els seus estats, o les accions que poden canviar-los, estan subjectes a la transferència."

    Podem dir que transferir els estats ens permet obtenir resultats similars als provocats per les invocacions de mètodes.

**Transferència d'estat de representació.**

## BSD Sockets

Un **socket** és una mena de punt final. Un punt final és un punt on les dades estan disponibles per obtenir-les i on es poden enviar les dades. El vostre programa Python es pot connectar al punt final i utilitzar-lo per intercanviar missatges entre ell mateix i un altre programa que funcioni en algun lloc llunyà a Internet.

La història dels *sockets* va començar l'any 1983 a la *Universitat de Califòrnia a Berkeley*, on es va formular el concepte i on es va dur a terme la primera implementació amb èxit. Berkeley Software Distribution.

## Dominis de socket

Inicialment, els sockets BSD es van dissenyar per organitzar la comunicació en dos dominis diferents. Els dos dominis eren:

* **Domini Unix** (Unix per abreujar): una part dels sockets BSD que s'utilitzen per comunicar programes que funcionen dins d'un sistema operatiu (és a dir, presents simultàniament al mateix sistema informàtic)

* **Domini d'Internet** (INET en resum): una part de l'API de socket BSD que s'utilitza per comunicar programes que funcionen dins de diferents sistemes informàtics, connectats entre si mitjançant una xarxa TCP/IP

## Adreça del socket

Els dos programes que volen intercanviar les seves dades s'han de poder identificar mútuament, per ser precisos, han de tenir la capacitat d'indicar clarament el socket a través del qual es volen connectar.

Els sockets de domini INET s'identifiquen (aborden) per parells de valors:

* *l'adreça IP* del sistema informàtic dins del qual es troba el socket;

* *el número de port*, conegut més sovint com a número de servei.

## Adreça IP

Una adreça IP, més precisament: *adreça IPv4*, és un valor de 32 bits de llarg que s'utilitza per identificar ordinadors connectats a qualsevol xarxa TCP/IP. El valor es presenta normalment com a quatre números de l'interval 0..255 (és a dir, vuit bits de llarg) acoblats amb punts (p. ex., 87.98.239.87).

També hi ha un estàndard IP més recent, anomenat IPv6, que utilitza 128 bits per al mateix propòsit. Nosaltres limitarem les nostres consideracions a IPv4.

## Número de socket/port

El número de socket/port és un nombre sencer de 16 bits que identifica un spcket dins d'un sistema determinat. Com ja heu endevinat, hi ha 65.536 (2 ** 16) possibles números de sòcol/servei.

El terme número de port prové del fet que molts serveis de xarxa estàndard solen utilitzar els mateixos números de port constants, per exemple, el protocol HTTP, un portador de dades utilitzat per REST, sol utilitzar el port 80.

## Protocol

Un protocol és un conjunt estandarditzat de regles que permeten que els processos es comuniquin entre ells.

## Com obtenir un document d'un servidor mitjançant Python

Escriurem el nostre primer programa fent ús de sockets de xarxa.

Els nostres objectius són:

* volem escriure un programa que llegeixi l'adreça d'un lloc WWW utilitzant una funció d'entrada estàndard, `input()`, i, obtingui el document arrel del lloc especificat;
 
* el programa mostra el document a la pantalla;
 
* el programa utilitza TCP per connectar-se al servidor HTTP.

El nostre programa ha de realitzar els següents passos:

1. crear un nou socket capaç de gestionar les transmissions orientades a la connexió basades en TCP;

2. connectar el sòcol al servidor HTTP d'una adreça determinada;

3. enviar una sol·licitud al servidor (el servidor vol saber què volem d'ell)

4. rebre la resposta del servidor (contindrà el document arrel sol·licitat del lloc)

5. tancar el socket (acabar la connexió)

## Programem-ho

Provarem l'accés a una API gratuita amb dades de diversos temes: [http://jsonplaceholder.typicode.com/][]

Utilitzarem la llibreria `socket` per establir les connexions.

```py
import socket 
```

i mirarem el següent codi:

```py
--8<-- "./docs/fitxers/python/fitxers_007.py"
```

Ens hem connectat al port 80, per tant amb el protocol `http`. 



[https://pokeapi.co/api/v2/pokemon/ditto]:  https://pokeapi.co/api/v2/pokemon/ditto
[http://jsonplaceholder.typicode.com/]:    http://jsonplaceholder.typicode.com/