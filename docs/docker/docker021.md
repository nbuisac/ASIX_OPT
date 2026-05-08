# Sessió 2: De Nginx a una App Multicapa

Benvinguts a la segona sessió. Avui deixarem de banda els "_contenidors aïllats_" per construir un ecosistema on diferents peces d'un sistema parlen entre elles.

!!!warning "Compte!"

    A _Docker_, cada imatge té la seva pròpia estructura de fitxers. No doneu per fet que les rutes de _Debian/Ubuntu_ funcionen a tot arreu. **Sempre reviseu el Docker Hub** o la configuració per defecte.

## 🎯 Objectius del dia

1. Entendre l'orquestració de xarxa amb el format `compose.yaml`.

2. Implementar persistència real en una base de dades _MariaDB_.

3. Aprendre a crear una imatge des de zero amb `Dockerfile`.

## 🏗️ L'Arquitectura: 3 Capes

En el món real, les aplicacions no són un sol fitxer. Se separen per seguretat i escalabilitat:

* **Capa Web (Nginx)**: Rep l'usuari i gestiona el trànsit (Proxy Invers).

* **Capa d'Aplicació (Python)**: Executa la lògica que nosaltres programem.

* **Capa de Dades (MariaDB)**: On es guarda la informació de forma permanent.

![lamp][]

## 🐋 El Dockerfile: Les 5 comandes clau

El Dockerfile ens permet "congelar" el nostre entorn de programació. Aquestes són les ordres que farem servir:

* **`FROM`**: La base (Ex: una imatge neta de _Python_).

    ???question "Per què slim?"
    
        La versió completa de _Python_ ocupa uns 300-400 MB. La slim n'ocupa uns 40-50 MB.

* **`WORKDIR`**: El **directori de treball _dins del contenidor_**.

    ???question "Quin directori és aquest?"

        Dins del contenidor no estem a "`C:`" ni a la "`$HOME`" de l'usuari, sinó en un _directori que hem definit nosaltres_. Qualsevol fitxer que creï el Python (com un _log_) apareixerà allà dins.

* **`COPY`**: Per moure el nostre codi de la màquina real a la imatge.

* **`RUN`**: Per instal·lar dependències (com llibreries de base de dades).

* **`CMD`**: L'ordre final que arrenca el nostre servidor.

???question "Perquè COPY, RUN i COPY en aquest ordre?"

    Si canviem una línia del codi `main.py` però no afegeix llibreries noves, a l'aturar el contenidor i tornar a crear-lo, Docker no tornarà a instal·lar les llibreries (que és el procés lent), sinó que aprofitarà la capa anterior. Això fa que el `docker compose build` sigui instantani.

## 🛠️ Novetats en les comandes (V2)

A partir d'ara, ja no usarem el guió a la comanda (`docker-compose` està desactualitzat).

* Per aixecar el laboratori: `docker compose up -d`

* Per tornar a fabricar la imatge si canvieu el codi: `docker compose build`

* Per veure què passa dins del backend: `docker compose logs -f backend`

## 💡 Pro-tip d'Administrador: El DNS Intern

Dins d'un fitxer `compose.yaml`, Docker crea una xarxa virtual pròpia. No necessitem saber les IPs dels contenidors!

* Si el servei de base de dades es diu _`db`_, el Python es connectarà al host _db_.

* Si el servei de _backend_ es diu _`app`_, el Nginx enviarà el trànsit a _[http://app][]_.

## 📝 Repte de la sessió

Heu d'aconseguir que el vostre fitxer `main.py` de Python connecti amb la MariaDB usant les credencials que heu definit al fitxer de configuració. Si el log diu "**_Connected to database!_**", la pràctica és un èxit.

???example "Fitxers necessaris"

    === "compose.yaml"

        ```yaml title="compose.yaml"
        services:
          db:
            container_name: asix-db
            image: mariadb:10.11
            environment:
              MARIADB_ROOT_PASSWORD: asix_password
              MARIADB_DATABASE: asix_db
            volumes:
              - ./data/db:/var/lib/mysql

          backend:
            container_name: asix-app
            build: ./backend
            depends_on:
              - db
            environment:
              DB_HOST: db
              DB_USER: root
              DB_PASSWORD: asix_password
              DB_NAME: asix_db

          web:
            container_name: asix-web
            image: nginx:latest
            ports:
              - "80:80"
            volumes:
              - ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
            depends_on:
              - backend
        ```

    === "Dockerfile"

        ```dockerfile title="Dockerfile"
        FROM python:3.11-slim
        WORKDIR /app
        # Instal·lem llibreries necessàries
        COPY requirements.txt .
        RUN pip install --no-cache-dir -r requirements.txt
        # Copiem el nostre codi
        COPY . .
        # Executem l'aplicació
        # CMD ["python", "main.py"]
        CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
        ```

    === "main.py"

        ```py title="main.py"
        import os
        from flask import Flask
        import mysql.connector
        import socket

        app = Flask(__name__)

        @app.route('/')
        def index():
            # LLegim les variables d'entorn que hem definit al compose.yaml
            # Si no existissin, posem un valor per defecte (el segon paràmetre)
            db_config = {
                'host':     os.environ.get('DB_HOST', 'localhost'),
                'user':     os.environ.get('DB_USER', 'root'),
                'password': os.environ.get('DB_PASSWORD', 'asix_password'),
                'database': os.environ.get('DB_NAME', 'asix_db')
            }

            server_ip = socket.gethostbyname(socket.gethostname())

            try:
                conn = mysql.connector.connect(**db_config)
                db_status = "<p style='color:green'>✅ Connexió amb èxit a MariaDB des de Python!</p>"
                conn.close()
            except Exception as e:
                db_status = f"<p style='color:red'>❌ Error de connexió: {e}</p>"

            return f"""
            <h1>Sóc el servidor WEB (Python)</h1>
            <p>IP del contenidor: {server_ip}</p>
            <hr>
            {db_status}
            """

        if __name__ == "__main__":
            # El port 5000 és el que haurem de posar al proxy_pass del Nginx sense gunicorn
            # app.run(host='0.0.0.0', port=5000)
            app.run(host='0.0.0.0')
        ```
    
    === "requirements.txt"

        ```txt title="requirements.txt"
        flask
        mysql-connector-python
        gunicorn
        ```

    === "default.conf"

        ```nginx title="default.conf"
        server {
            listen 80;
            server_name _;

            location / {
                proxy_pass http://backend:5000; # El "pont" cap al servidor python
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            }
        }
        ```

    === ".dockerignore"

        ```plaintext
        __pycache__/
        *.pyc
        *.pyo
        *.db
        ```

        !!!note ".dockerignore?"
        
            Aquest fitxer el podem posar a la carpeta _backend_ per tal que al fer el `#!dockerfile COPY . .` no es copïin aquests fitxers. 🥇

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

>**En resum**
>>
>>Flask no es posa mai "sol" a producció. Sempre va acompanyat d'un servidor WSGI com Gunicorn o uWSGI. Docker no canvia aquesta regla, simplement fa que sigui més fàcil empaquetar-ho tot junt.

[http://app]:   http://app
[lamp]:         ./img/lamp.png
