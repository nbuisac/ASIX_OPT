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

## Programem-ho

Noaltres provarem l'accés a les API a partir de la llibreria `requests`. Aquesta ens dóna mètodes per a fer GET, POST, PUT, DELETE, etc.

Trobareu més informació a: [Llibreria requests a w3chools][].

```py
import requests
```

!!!note "És possible que calgui instal·lar la llibreria `requests`"

    ```bash
    pip install requests
    ```

Provarem l'accés a una API gratuita amb dades de diversos temes: [http://jsonplaceholder.typicode.com/][]

i mirarem el següent codi:

```py
--8<-- "./docs/fitxers/python/fitxers_007_1.py"
```

Si feu la prova, veureu que la resposta la tenim, en format `JSON`, a `reply.json()`. A partir d'aquí ja serem nosaltres els que tractarem les dades com calgui.

També podriem mirar com modificar les dades a partir dels mètodes `PUT`, `POST`, `DELETE`.

!!!tip "Per treballar amb dades `JSON` podem utilitzar la llibreria `json`."

[https://pokeapi.co/api/v2/pokemon/ditto]:  https://pokeapi.co/api/v2/pokemon/ditto
[http://jsonplaceholder.typicode.com/]:    http://jsonplaceholder.typicode.com/
[Llibreria requests a w3chools]:        https://www.w3schools.com/python/module_requests.asp