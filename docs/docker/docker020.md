# Sessió 2: Arquitectura Multicapa i el Dockerfile

!!!warning "Compte!"

    A _Docker_, cada imatge té la seva pròpia estructura de fitxers. No doneu per fet que les rutes de _Debian/Ubuntu_ funcionen a tot arreu. **Sempre reviseu el Docker Hub** o la configuració per defecte.

## 1. OBJECTIU DE LA SESSIÓ

Fins ara hem fet servir imatges oficials (com `Nginx` o `Python`). Avui farem un pas més:

* Crearem la nostra pròpia imatge personalitzada per a un programa en `Python`.

* Connectarem tres serveis perquè treballin junts: un servidor web (`Nginx`), una lògica de negoci (`Python`) i una base de dades (`MariaDB`).

![lamp][]

## 2. L'ESTRUCTURA DE TREBALL
L'ordre és fonamental en l'administració de sistemes. Heu de crear aquesta estructura de carpetes al vostre directori de projecte:

```text
carpeta-projecte/.
                 ├── compose.yaml
                 │
                 ├── backend/
                 │   ├── Dockerfile
                 │   ├── main.py
                 │   └── requirements.txt
                 │   └── [.dockerignore]
                 │
                 └── nginx/
                     └── default.conf
```

## 3. EL DOCKERFILE (La recepta del Backend)

Dins de la carpeta "_`backend`_", el fitxer `Dockerfile` és el que diu a Docker com ha de preparar l'ordinador virtual per al nostre codi. Les instruccions bàsiques són:

* **`FROM`**: Triem el sistema de base (ex: `python:3.11-slim`).

* **`WORKDIR`**: On anirà el nostre codi dins del contenidor (ex: `/app`).

    ???question "Quin directori és aquest?"

        Dins del contenidor no estem a "`C:`" ni a la "`$HOME`" de l'usuari, sinó en un _directori que hem definit nosaltres_. Qualsevol fitxer que creï el Python (com un _log_) apareixerà allà dins.

* **`COPY`**: Passem els fitxers del nostre PC real al contenidor.

* **`RUN`**: Instal·lem les llibreries (ex: `pip install`).

* **`CMD`**: La comanda que arrenca el programa i es queda executant-se.

???question "Perquè COPY, RUN i COPY en aquest ordre?"

    Si canviem una línia del codi `main.py` però no afegeix llibreries noves, a l'aturar el contenidor i tornar a crear-lo, Docker no tornarà a instal·lar les llibreries (que és el procés lent), sinó que aprofitarà la capa anterior. Això fa que el `docker compose build` sigui instantani.

## 4. EL FITXER `compose.yaml`

En lloc de fer molts "`docker run`", farem servir un únic fitxer per aixecar-ho tot. Els punts clau d'avui són:

* **`build: ./backend`**: Docker no busca una imatge a internet, sinó que la "fabrica" usant el fitxer `Dockerfile`.

* **depends_on**: Li diem al backend que s'esperi que la base de dades estigui a punt.

* **networks**: Docker crearà una xarxa interna on els contenidors es veuen entre ells pel seu nom (_DNS intern_).

## 5. CONCEPTES D'ADMINISTRACIÓ (ASIX)

* **Persistència**: MariaDB guardarà les dades en un _volum_. Si esborrem el contenidor, les dades continuen al disc del host.

* **DNS Intern**: Dins de la xarxa de Docker, el _`backend_` pot connectar-se a la base de dades usant simplement el nom del servei (ex: "_`db`_") en lloc d'una IP.

* **Seguretat**: Nginx actua com a "_Proxy Invers_", sent l'únic que té ports oberts cap a l'exterior (el port 80).

## 6. TASQUES A REALITZAR

1. Crear el `Dockerfile` per al _backend_ de Python.

2. Configurar el `docker compose` per aixecar els _3 serveis_.

3. Verificar amb la comanda "`docker compose logs -f`" que el backend es connecta correctament al servidor _MariaDB_.

* Modificar el fitxer de configuració de Nginx perquè redirigeixi les peticions al contenidor de Python.

## Pregunta important.

==En un entorn real utilitzariem Flask sol?==

La resposta és **==NO!==**. Però, quasi...

1. El problema de _**Flask**_ "a seques"

    Quan executem `app.run()`, _Flask_ aixeca un servidor anomenat **Werkzeug**.

    * **A classe**: Pot anar bé perquè si canviem el codi, es reinicia sol i ens dóna missatges d'error molt detallats.

    * **A producció**: _És perillós_. **Werkzeug és monofil** (_single-threaded_). Si un client fa una petició que triga 10 segons a carregar, tota la resta de peticions/clients s'han d'esperar perquè el servidor només pot atendre una petició/client a la vegada. A més, no està preparat per a temes de seguretat ni càrregues massives.

2. En el món real (ja està fet així), posem _**Gunicorn**_ entre el _Nginx_ i el _Flask_.

    * **Què fa?** Gunicorn crea "_treballadors_" (_workers_). Si en configurem 4, el servidor pot atendre 4 peticions simultànies de forma real.

    * Com funciona el "Sandvitx" de producció?

        * **Nginx**: Rep el trànsit, gestiona el SSL/HTTPS i serveix les fotos (estàtics).

        * **Gunicorn**: Rep la petició del Nginx i la gestiona de forma eficient amb Python.

        * **Flask**: És només el codi que diu què cal fer, però no es preocupa de "la xarxa".

3. Com ho fem en Docker per ser "Pro"?

    Si volem que l'entorn sigui 100% professional, només cal posar _gunicorn_ abans de _Flask_:

    1. Al fitxer `requirements.txt`:
        
        Tenim la línia: `gunicorn`

    2. Al fitxer `Dockerfile`:

        En lloc d'executar el fitxer `main.py`, direm a gunicorn que utilitzi `main.py` i la variable `app`:

        ```bash
        CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
        ```

        _On main és el nom del fitxer **.py** i **app** és el nom de la variable **Flask**_.

4. Per què a classe sí ho posem?

    Per a una introducció a `Dockerfile`, potser no caldria, però si algú vol ser més professional, no costa tant.

    Si utilitzem _Gunicorn_, els logs de Python són més difícils de llegir (no surten els errors tan clars a la consola).


[lamp]:     ./img/lamp.png
