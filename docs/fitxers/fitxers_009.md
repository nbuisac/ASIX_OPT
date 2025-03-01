# Accés a URL amb GET
Podem accedir, amb *Python*, a diferents URL i tractar-ne el resultat.

## Programem-ho

Accedirem a la URL a partir de la llibreria `requests`. Aquesta ens dóna mètodes per a fer GET, POST, PUT, DELETE, etc.

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
--8<-- "./docs/fitxers/python/fitxers_api_1.py"
```

Fixeu-vos ue per accedir a les dades, passem la informació necessària amb una URL amigable. Semblant al que hemm programat a l'apartat del servidor, on llegim els paràmetres pel `path` de la URL.

Si feu la prova, veureu que la resposta la tenim, en format `JSON`, a `reply.json()`. A partir d'aquí ja serem nosaltres els que tractarem les dades com calgui.

També podriem mirar com modificar les dades a partir dels mètodes `PUT`, `POST`, `DELETE`.

!!!tip "Per treballar amb dades `JSON` podem utilitzar la llibreria `json`."

[https://pokeapi.co/api/v2/pokemon/ditto]:  https://pokeapi.co/api/v2/pokemon/ditto
[http://jsonplaceholder.typicode.com/]:    http://jsonplaceholder.typicode.com/
[Llibreria requests a w3chools]:        https://www.w3schools.com/python/module_requests.asp