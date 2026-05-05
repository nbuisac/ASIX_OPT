# Dynmap (Visualització Web)

Ara afegirem el plugin _Dynmap_ és el "**wow factor**".

Permet veure el món de _Minecraft_ des d'una web estil Google Maps. Com que fas utilitzem la imatge d'*itzg*, només cal:

* afegir una variable d'entorn:

    ```yaml
        SPIGET_RESOURCES: "273" (Això descarrega el plugin automàticament).
    ```

* i obrir el port `8123`.

Així, amb un sol "servei" (_Minecraft_), podem exposar dues aplicacions diferents (el joc i una web de mapes).

Passarem de tenir un "_procés a la consola_" a tenir una a**rquitectura de serveis real**:

* un servidor de jocs i

* un servidor web funcionant en paral·lel.

```yaml title="Docker Compose amb Dynmap i Portainer"
services:
  minecraft: 
    image: itzg/minecraft-server
    container_name: mc
    tty: true
    stdin_open: true
    ports:
      - "25565:25565" # Port del joc
      - "8123:8123"   # Port de la interfície web de Dynmap
    environment:
      EULA: "TRUE"
      TYPE: "PAPER"
      MEMORY: 4G
      ONLINE_MODE: "false"
      CREATE_CONSOLE_IN_PIPE: "true"
      # Descarrega automàticament el plugin Dynmap de Spigot
      SPIGET_RESOURCES: "273" 
    volumes:
      - ./data:/data
    restart: always

  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    ports:
      - "9443:9443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data
    restart: always

volumes:
  portainer_data:
```

## 🛠️ Passos a fer

* **Actualitzar el stack**: Cal executar `docker-compose up -d`. Docker detectarà els canvis, crearà el contenidor de _Portainer_ i actualitzarà el de _Minecraft_.
    
* **Esperar la descàrrega**: El servidor trigarà una mica més a arrencar perquè ha de descarregar el fitxer `.jar` del plugin i instal·lar-lo.

* **Accedir a la web**:

    * Cal obrir el navegador i anar a: [http://localhost:8123][]

        ???danger "Si no funciona"

            O encara no s'ha iniciat o bé el plugin no s'ha descarregat correctament.

            En el segon cas:

            * el descarreguem de [https://dynmap.us/builds/dynmap/][] la versió **v3.7-SNAPSHOT** més nova.
            
                Podriem haver trobat versions a: [https://modrinth.com/plugin/dynmap/versions][] (versió paper) [https://modrinth.com/plugin/dynmap/version/3.7-beta-8][] però no n'ha funcionat cap

            * el copiem a `./data/plugins`

            * reiniciem el contenidor del _mein-craft`: `docker restart mc`
    
    * Al principi es veurà negre. Cal entrar al joc i moure'ns una mica per "renderitzar" el mapa.
    
* **Comanda de renderitzat**: Des de la consola (o des de _Portainer_), podem forçar el dibuixat del mapa amb:
    
    `docker exec -u 1000 mc mc-send-to-console dmap fullrender world`

## 🎓 Conceptes d'ASIX per treballar

* **Microserveis**: Una sola màquina (o contenidor) pot oferir diferents tipus de serveis (TCP pel joc, HTTP per la web).

* **Manteniment**: Si entrem a _Portainer_, veurem que el volum de dades de _Minecraft_ ara té una carpeta nova: `/data/plugins/dynmap`. Poden veure com el plugin genera milers de petites imatges .png (les tiles del mapa).
    Networking: Per què 8123 i no 80? Poden provar de canviar el port extern a 80:8123 i veure com ara hi accedeixen sense posar el port al navegador (només http://localhost).


[https://modrinth.com/plugin/dynmap/versions]:              https://modrinth.com/plugin/dynmap/versions
[https://modrinth.com/plugin/dynmap/version/3.7-beta-8]:    https://modrinth.com/plugin/dynmap/version/3.7-beta-8
[http://localhost:8123]:                                    http://localhost:8123
[https://dynmap.us/builds/dynmap/]:                         https://dynmap.us/builds/dynmap/