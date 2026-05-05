# Portainer

*Portainer* ens ajudarà a visualitzar conceptes abstractes (com les capes de les imatges o les xarxes virtuals) abans de barallar-nos amb la consola. ës possible que moltes coses les puguem fer amb _Docker Desktop_ ja que treballem en un entorn Windows.

## 1. Instal·lació de Portainer (El mètode "_Docker-way_")

El millor és que el despleguem com un contenidor més. També podem afegir-lo al mateix `docker-compose.yml` que ja tenim, o crear-ne un de nou, en un nou directori.

```yml
services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    restart: always
    ports:
      - "9443:9443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data

volumes:
  portainer_data:
```

## 2. Conceptes clau per explicar a classe

Mentre explorem la interfície (entrant a [https://localhost:9443][]), destacarem aquests punts:

* **El Socket de Docker** (`docker.sock`): És el "cor" de Docker; permet que el contenidor de _Portainer_ doni ordres al motor Docker de l'amfitrió. És un concepte de sistemes pur.

* **Stacks vs. Compose**: _Portainer_ anomena "**_Stacks_**" als projectes de _Docker Compose_. Podem desplegar el servidor de _Minecraft_ directament des de la interfície web copiant i enganxant el codi _YAML_.
    
* **Explorador de fitxers**: Des de _Portainer_ podem entrar als volums i veure els fitxers de configuració del _Minecraft_ sense sortir del navegador.

## 3. Exercici pràctic

Repte d'investigació dins de _Portainer_:

* **Monitorització**: Trobeu la gràfica de consum de _CPU_ i _RAM_ del servidor de _Minecraft_ mentre algú corre pel món generant mapa.

* **Consola Interactiva**: Utilitzant la funció "Console" de _Portainer_, entra dins del contenidor i executar la comanda `df -h` per veure l'espai en disc.

* **Logs en viu**: Filtra els _logs_ per buscar el moment exacte en què un usuari determinat s'ha connectat.



[https://localhost:9443]: https://localhost:9443