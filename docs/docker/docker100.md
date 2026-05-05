# Docker i Mine-craft

Extret de [Instalando Mi Propio SERVER de MINECRAFT !!][]

## Minecraft

Com a client de _Minecraft_ instal·larem el _SKLauncher_ de [https://skmedix.pl/binaries/skl/3.2.18/win-x64/SKlauncher-3.2.18_Setup.exe][]

Hi ha dues versions, _Java_ i _Bedrock_ segons el tipus de client (PC, No PC). Nosaltres instal·larem la Java per utilitzar-la amb PC.

_Minecraft_ és un servidor que escriu dades constantmment. _Mons_, _jugadors_, etc. Cal un disc ràpid.

## Docker

1. Crearem els directoris per preparar l'entorn

    ```bash title="Directori del projecte"
    mkdir C:\asix\docker\minecraft-pc
    cd C:\asix\docker\minecraft-pc
    ```

2. Dins el directori creat, crearem el fitxer `docker-compose.yml` amb els paràmetres necessaris

3.  iniciem el contenidor: `docker compose up`

    * si treballem en mode offline podem assignar-nos com a _OP_ de la consola: `docker exec -u 1000 mc mc-send-to-console op ElMeuNickName`

4. Ja podem connectar-nos amb el joc i dins, una vegada som OPeradors ja podrem executar **T**:
    
    * ☀️ Fer de dia: `/time set day`
        
    * 🛠️ Mode creatiu (per volar i tenir llum infinita): `/gamemode creative`
        
    * 💡 Llum total: `/effect give @s night_vision infinite`

???example "Fitxers"

    === "docker-compose.yml"

        ```yaml title="docker-compose.yml"
        services:
          minecraft: 
            image: itzg/minecraft-server
            container_name: mc
            ports:
            - "25565:25565"
            environment:
            EULA: "TRUE"
            TYPE: "PAPER"
            MEMORY: 4G
            # OPS: "ElMeuNickName"
            # SKIP_OP_ADMIN_CHECK: "true"
            CREATE_CONSOLE_IN_PIPE: "true"
            volumes:
            - ./data:/data
            restart: always

        # duckdns:
        #   image: lscr.io/linuxserver/duckdns
        #   container_name: duckdns
        #   environment:
        #     PUID: 1000
        #     PGID: 1000
        #     TZ: Europe/Madrid
        #     SUBDOMAINS: servidor
        #     TOKEN: token_duck_dns
        #     LOG_FILE: false
        #   restart: always
        ```

## Què hem treballat? Com podem avançar?

1. **El pas cap a la professionalització**: Docker Compose
    
    Hem utilitzat el terminal per a tot, el següent pas natural és analitzar el fitxer `docker-compose.yml`.

    * *Repte*: Aprendre la importància de la indentació (_YAML_) i com aixecar tot l'entorn amb una sola comanda (`docker-compose up -d`).

    * *Concepte*: Infraestructura com a Codi (_IaC_).

2. **Xarxes i Seguretat**: Networking
    
    Actualment, el contenidor està al "_bridge_" per defecte.
    
    * **Repte**: Crear una xarxa personalitzada de Docker (_networks_) i assignar-li una IP estàtica interna al contenidor.
    
    * **Seguretat**:
    
        * Per què és perillós el port _25565_ per defecte? 
        
        * Obrim el port de casa fent _**NAT/Port Forwarding**_ al router.

3. **Gestió i Monitorització**: Observabilitat
    
    Un administrador ha de saber què passa dins el contenidor.

    * **Logs**: Amb la comanda `docker logs -f mc` podem veure qui entra i surt o detectar errors.

    * **Portainer**: Instal·lar _Portainer_ (en un altre contenidor) per gestionar-ho tot des d'una interfície web. És una eina molt usada a l'empresa.

4. **Backup i Persistència**

    Ja que tenim un volum mapejat:
 
    * **Repte**: Fer un script en _Bash_ que aturi el contenidor, faci un `tar.gz` del directori `/data` i torni a aixecar el servei.
    
    * **Concepte**: Disponibilitat i recuperació davant desastres.

5. **Multicontenidor**: Projecte Final

    Minecraft es presta molt bé a arquitectures més complexes:

    * **Proxy BungeeCord**: Configurar un contenidor que faci de "porta d'entrada" (Proxy) i que ens redirigeixi a dos servidors de Minecraft diferents (ex: un de Creatiu i un de Survival) segons el portal que creuem.
    
    * **Dynmap**: Afegir un contenidor que llegeixi els fitxers del món i generi un **mapa web** en temps real (usant un altre port, com el _8123_).


## 🌐 El tancament: Com fem el servidor accessible des d'Internet?

### Què és [Duck DNS][duckdns] i per a què serveix?

La majoria de connexions a Internet domèstiques (com les que tenim a casa) tenen una **IP pública dinàmica**. Això vol dir que cada vegada que el router es reinicia, **la nostra "adreça" a Internet canvia**. 

Si volem que els nostres amics es connectin al servidor de _Minecraft_, no els podem donar una IP que canvia cada dia. Aquí és on entra **[Duck DNS][duckdns]**.

**[Duck DNS][duckdns]** és un servei gratuït de **DNS Dinàmic (DDNS)**. Ens dóna un nom de domini fàcil de recordar (Ex: `asix-montilivi.duckdns.org`) i s'encarrega de saber quina és la nostra IP pública en cada moment.

---

### Com funciona el contenidor de [Duck DNS][duckdns]?

En el fitxer `docker-compose.yml` que hem vist abans, hem afegit un servei anomenat `duckdns`. La seva única funció és:

1. "Despertar-se" cada 5 minuts.

2. Mirar quina és la IP pública de casa nostra.

3. Avisar els servidors de [Duck DNS][duckdns] perquè actualitzin el subdomini.

#### Explicació de les variables de configuració:


* **`SUBDOMAINS`**: El nom que haguem triat (sense el `.duckdns.org`). Podem posar-ne diversos separats per comes.

* **`TOKEN`**: És la nostra "_contrasenya_" única i secreta que ens dóna el web de [Duck DNS][duckdns]. **Mai s'ha de compartir!**

* **`LOG_FILE`**: Si el posem a `false`, el contenidor serà més net i només veurem si l'actualització ha anat bé als logs de Docker.

---

### 🛠️ Configuració Pas a Pas

1. **Registre**: Entrem a [duckdns.org](https://www.duckdns.org) i iniciem sessió amb el compte de Google.

2. **Creem el subdomini**: Escollim un nom que estigui lliure i l'afegim.

3. **Copiem el Token**: El veurem a la part superior de la pantalla (és una cadena llarga de lletres i números).

4. **Actualitzem el Docker Compose**: Posem el subdomini i el token al fitxer.

5. **Aixequem el servei**: `docker-compose up -d`.

---

### ⚠️ L'últim pas: El NAT (Port Forwarding)

Tenir un domini no serveix de res si el router bloqueja les connexions. Perquè el trànsit arribi al nostre contenidor Docker, cal entrar a la configuració del router de casa i afegir una regla de **Port Forwarding**:

* **Servei Minecraft**: Obrim el port `25565` (TCP) cap a la IP local del nostre ordinador.

* **Dynmap**: Obrim el port `8123` (TCP) cap a la IP local del nostre ordinador.

---

### 📝 Repte d'Administració

Comprovem que tot funciona correctament amb la comanda: `#!bash docker logs duckdns`

Si veiem algun dels missatges següents,

* `DuckDNS request at DiaSetmana Mes  Dia HH:MM:SS CEST YYYY successful.`

* `Your IP was updated at DiaSetmana Mes  Dia HH:MM:SS CEST YYYY to IPv4: XXX.YYY.ZZZ.TTT`

ja som visibles des de qualsevol lloc del món!














[Instalando Mi Propio SERVER de MINECRAFT !!]:  https://www.youtube.com/watch?v=Lwvu0qGdSSc
[https://skmedix.pl/binaries/skl/3.2.18/win-x64/SKlauncher-3.2.18_Setup.exe]:   https://skmedix.pl/binaries/skl/3.2.18/win-x64/SKlauncher-3.2.18_Setup.exe
[duckdns]:  https://www.duckdns.org