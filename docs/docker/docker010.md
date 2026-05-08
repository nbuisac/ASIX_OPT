# Docker Inicial: Imatges, contenidors, volums i ports

## 1. Exploració i descàrrega: Docker Hub

La primera parada de qualsevol administrador és el [Docker Hub][]. Veiem que les imatges no són fitxers màgics, sinó plantilles de sistemes operatius amb aplicacions preinstal·lades.

Per tenir un microservei, el que vulguem, ens descarregarem la imatge que necessitem, per exemple una de _python_:

* **Comanda**: `docker pull python:3.11.15`

* **Concepte**: Descarreguem la "recepta" (_imatge_) al nostre disc local, però encara no hem creat cap "plat" (_contenidor_).

## 2. El servidor Web (Nginx)

Com que crear ràpidament un servei amb python pot ser més complicat, crearem un contenidor amb un servidor web. Utilitzarem la imatge oficial de `Nginx` per entendre com Docker interactua amb el món exterior.

Per això crearem un fitxer `index.html` en un directori determinat: per exemple `C:\ASIX\docker\html`.

Iniciarem un contenidor, servidor web, amb _nginx_, de la següent manera:

```bash
docker run --name ng -v c:/asix/docker/html:/usr/share/nginx/html -p 80:8888 nginx
```

3. Conceptes clau aplicats

En el laboratori pràctic, hem aixecat un contenidor combinant els tres pilars de Docker:

* **El Volum (Persistència)**: Hem mapejat `C:\ASIX\docker\html` a `/usr/share/nginx/html`.

    * **Lliçó**: El contenidor és "_efímer_" (si s'esborra, no passa res), perquè les dades (el fitxer `index.html`) viuen fora d'ell, al nostre ordinador. Hem comprovat que en modificar el fitxer local, els canvis es reflecteixen immediatament a la web.

        Si accedim al servidor [http://localhost:8888][] veurem la web que hem creat. Si modifiquem el fitxer `index.html` i tornem a mirar la pàgina, veurem com canvia.

* **El Port (Comunicació):** Hem mapejat el port local 8888 al port 80 intern del contenidor.

    * **Lliçó**: El contenidor està aïllat. Per poder veure la web des del navegador, hem de "_perforar_" una paret i connectar un port de la nostra màquina real amb el port del contenidor.

* **Imatge vs. Contenidor:**

    * **Imatge**: És el fitxer estàtic (com un fitxer _`.ISO`_).

    * **Contenidor**: És la imatge en execució (com la màquina virtual engegada).

```bash
docker run -d --name el-meu-web -p 8888:80 -v C:/ASIX/docker/html:/usr/share/nginx/html nginx:latest
```

!!!tip "El darrer paràmetre és la imatge"

    Si no posem els dos punts (`:`), darrere el nom de la imatge, sempre se'ns descarregarà la darrera versió `latest`

!!!note "A tenir en compte"

    💡  Recordeu que a Docker la ruta `/usr/share/nginx/html` és sagrada per a _Nginx_. Si intentem posar els fitxers a `/var/www/html` (com fariem a _Debian_), el servidor no trobarà res perquè la seva configuració per defecte apunta a la ruta d'_Alpine Linux_.

    A _Docker_, cada imatge té la seva pròpia estructura de fitxers. No doneu per fet que les rutes de _Debian/Ubuntu_ funcionen a tot arreu. **Sempre reviseu el Docker Hub** o la configuració per defecte.


[Docker Hub]:   http://hub.docker.com
[http://localhost:8888]:    http://localhost:8888