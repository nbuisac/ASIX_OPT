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

3. Iniciem el contenidor: `docker compose up -d`

    Ja tenim el servidor funcionat, podem comprovar que s'està executant amb la comanda `#!bash docker ps`

    ???example "Possible sortida"

        ```bash
        CONTAINER ID IMAGE                       COMMAND                CREATED            STATUS                      PORTS                      NAMES
        1db88f11c7e7 lscr.io/linuxserver/duckdns "/init"                About a minute ago Up About a minute                                      duckdns
        d26b8aa8cad7 itzg/minecraft-server       "/image/scripts/start" About a minute ago Up About a minute (healthy) 0.0.0.0:25565->25565/tcp   mc
        ```

        Podem veure que hi ha un o dos contenidors executant-se. El servidor de _minecraft_ (`mc`) i el `duckdns`.

4. Ja podem connectar-nos amb el joc i dins, una vegada som OPeradors ja podrem executar **T**:

    * Amb SKLauncher, amb la darrera versió de _maig de 2026_ cal configurar la versió _Forge / 26.1.2_

    * si treballem en mode offline podem assignar-nos com a _OP_ de la consola: `docker exec -u 1000 mc mc-send-to-console op ElMeuNickName`
    
    * ☀️ Fer de dia: `/time set day`
        
    * 🛠️ Mode creatiu (per volar i tenir llum infinita): `/gamemode creative`
        
    * 💡 Llum total: `/effect give @s night_vision infinite`

    ???info "Imatges de connexió"

        === "Primera"

            ![mc001][]

        === "Segona"

            ![mc002][]

        === "Tercera"

            ![mc003][]

        === "Quarta"

            ![mc004][]

        === "Cinquena"

            ![mc005][]

        === "Sisena"

            ![mc006][]

        === "Setena"

            ![mc007][]

        === "Vuitena"

            ![mc008][]

        === "Novena"

            ![mc009][]

        === "Desena"

            ![mc010][]

???example "Fitxers"

    === "docker-compose.yml"

        ```yaml title="docker-compose.yml" hl_lines="6 9 10 12"
        services:
          minecraft: 
            image: itzg/minecraft-server:java21
            container_name: mc
            ports:
            - "25565:25565"
            environment:
              VERSION: "1.21"
              EULA: "TRUE"
              TYPE: "PAPER"
              MEMORY: 4G
              # OPS: "ElMeuNickName"
              # SKIP_OP_ADMIN_CHECK: "true"
              CREATE_CONSOLE_IN_PIPE: "true"
              JVM_DD_OPTS: "-Dpaper.playerconnection.keepalive=120"
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

### 🚑 Possibles errors

#### Error de ClassLoader (Java)

Si en mirar els logs (`docker logs mc`) veiem errors tipus `java.lang.ClassLoader` o referències a `Paperclip`, segurament tenim un conflicte de versions de Java.

* **Minecraft < 1.20.5**: Funciona amb Java 17.

* **Minecraft >= 1.20.5 i 1.21**: Requereix Java 21.

**Lliçó d'administrador**: Sempre hem de fer coincidir la versió de la imatge de Docker (el JRE) amb els requeriments de l'aplicació que executem. Si usem `image: itzg/minecraft-server:java21`, ens assegurem compatibilitat amb les versions més modernes.

#### Problemes en connexió

De vegades el WSL ens pot donar problemes a la xarxa. Per solventar-ho podem obrir una _powershell_ en mode administrador i executar

```bash
netsh interface ipv4 set subinterface "vEthernet (WSL (Hyper-V firewall))" mtu=1400 store=persistent
```

_En baixar la MTU a 1400, fem que els paquets siguin una mica més petits i "càpiguen" perfectament per tot el túnel de xarxa de WSL2 sense haver-se de fragmentar._

També podem jugar amb el fitxer `docker-compose.yml` modificant el paràmetre `JVM_DD_OPTS: "-Dpaper.playerconnection.keepalive=120"`. En aquest cas, al posar-li 120, ja l'hem posat prou alt.

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

## Per saber més

Hi ha diferents versions de Servidor:

* 🟩 **Vanilla**:

    És el joc pur, tal com el publica _Mojang_.
    
    * **Avantatges**: El més estable i ràpid d'actualitzar.
    
    * **Desavantatges**: No permet mods (només datapacks). És el més pesat de moure per al servidor si hi ha molts jugadors.

* 🟨 **Forge**: El veterà. Ha estat l'estàndard durant més de 10 anys.

    * **Focus**: Mods de contingut massiu (màquines, màgia, dimensions noves).
    
    * **El millor**: Té la biblioteca de mods històrica més gran.
    
    * **El pitjor**: Triga molt a carregar i consumeix molta memòria RAM.

* 🟦 **Fabric**: El motor modern i lleuger.

    * **Focus**: Rendiment extrem i optimització.
    
    * **El millor**: El joc carrega en segons. És ideal per a servidors tècnics o PCs amb pocs recursos. Molts mods de "millora visual" (com Iris/Sodium) neixen aquí.
    
    * **El pitjor**: No té tants mods de "grans màquines" com Forge (encara que està creixent).
    
* 🟧 **NeoForge**: El "_nou_" Forge.

    * **Què és**: És una escissió (fork) de Forge creada per gairebé tot l'equip original de desenvolupadors després de baralles internes.
    
    * **Estat actual**: A partir de la versió 1.20.1, la majoria de mods grans s'estan mudant aquí. És el futur dels mods pesats.

* 🟪 **Quilt**: L'evolució de Fabric.

    * **Què és**: Creat per ex-desenvolupadors de Fabric. Vol ser més obert a la comunitat i permetre fer coses que Fabric no deixa.
    
    * **Compatibilitat**: Pot executar gairebé tots els mods de Fabric, però no a la inversa.
    
* 🍎 **Paper** (El que tenim configurat).

    * Paper **no** és per a mods (com Forge/Fabric). 
    
    * Paper és per a **Plugins** (comandes com `/spawn`, protecció de terres, economia).
    
    * Està ultra-optimitzat per a servidors amb molta gent perquè no explotin.

Si configurem el _**Docker d'itzg**_, i voleu jugar amb amics i posar-hi "_coses rares_" (màquines, dracs, etc.), haureu de canviar el _TYPE_ a _FORGE_ o _NEOFORGE_. 

Si voleu que el servidor vagi ràpid com un llamp i posar-hi només coses bàsiques, _FABRIC_ seria la millor opció.

Al canviar de _Paper_ a _Fabric/Forge_: Els Plugins (fitxers `.jar` que tinguem a la carpeta `/plugins`) deixaran de funcionar. Els _mods_ de _Fabric_ van a una carpeta anomenada `/mods`.


[Instalando Mi Propio SERVER de MINECRAFT !!]:  https://www.youtube.com/watch?v=Lwvu0qGdSSc
[https://skmedix.pl/binaries/skl/3.2.18/win-x64/SKlauncher-3.2.18_Setup.exe]:   https://skmedix.pl/binaries/skl/3.2.18/win-x64/SKlauncher-3.2.18_Setup.exe
[duckdns]:  https://www.duckdns.org

[mc001]:    ./img/mc001.png
[mc002]:    ./img/mc002.png
[mc003]:    ./img/mc003.png
[mc004]:    ./img/mc004.png
[mc005]:    ./img/mc005.png
[mc006]:    ./img/mc006.png
[mc007]:    ./img/mc007.png
[mc008]:    ./img/mc008.png
[mc009]:    ./img/mc009.png
[mc010]:    ./img/mc010.png