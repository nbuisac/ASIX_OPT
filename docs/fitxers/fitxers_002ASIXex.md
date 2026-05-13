# Python - Exercicis de fitxers ASIX

Resol aquests exercicis de fitxers amb llenguatge Python

## 1. Lectura: L'Auditoria de Seguretat

**Objectiu**: Utilitzar _`csv.reader`_ per filtrar dades d'un fitxer existent.

**L'escenari**: Tenim un fitxer anomenat `accessos.csv` amb les columnes: `data`, `usuari`, `ip`, `estat` (on estat pot ser "_èxit_" o "_fallida_").

**L'exercici**: Crea un programa que llegeixi el fitxer i mostri per pantalla només els intents de connexió que han estat una "fallida". Al final, el programa ha de dir el número total d'intents fallits detectats.

!!!tip "Consell pedagògic"
    
    Així aprenem a processar logs, una tasca típica de l'administrador de sistemes.

???example "Exemple de equips.csv"

    ```txt
    data,usuari,ip,estat
    2024-05-10,admin,192.168.1.5,èxit
    2024-05-10,user1,10.0.0.50,fallida
    2024-05-11,convidat,172.16.0.5,fallida
    2024-05-11,admin,192.168.1.5,èxit
    ```

## 2. Escriptura: Generador de Configuracions

**Objectiu**: Crear un fitxer de text pla (`.txt` o `.conf`) a partir d'inputs de l'usuari.

**L'escenari**: L'administrador necessita generar fitxers de configuració ràpids per a nous servidors.

**L'exercici**: Fes un script que demani a l'usuari:

* _Nom del servidor_.

* _IP local_.

* _Port de servei_ (ex: 8080).

El programa ha de crear un fitxer anomenat `config_[nom_servidor].txt` amb el següent format intern:

```ini
[SERVER_CONFIG]
HOST_NAME = "servidor1"
IP_ADDRESS = "192.168.1.10"
PORT = 8080
STATUS = "active"
```

## 3. Lectura i Escriptura (Mix): Actualització d'Inventari

**Objectiu**: Llegir un _CSV_, modificar les dades en memòria i guardar el resultat en un **fitxer nou**.

**L'escenari**: Tenim un inventari de màquines `equips.csv` amb: `id`, `nom`, `ram_gb`. L'empresa ha decidit ampliar la memòria de tots els equips.

L'exercici:

* Llegeix el fitxer `equips.csv`.

* Crea un nou fitxer anomenat `equips_actualitzats.csv`.

* Per a cada fila, duplica la quantitat de _RAM_ (per exemple, si un equip tenia 8GB, ara en tindrà 16GB).

* Guarda les noves dades al fitxer nou mantenint l'estructura _CSV_.

???example "Exemple de fitxer d'equips"

    ```csv
    id,nom,ram_gb,os,ubicacio
    1,SRV-WEB-01,16,Ubuntu 22.04,Sala A
    2,SRV-DB-02,32,Debian 12,Sala B
    3,SRV-PROXMOX,64,Proxmox VE,Sala A
    4,WS-ADMIN-01,8,Windows 11,Oficina 1
    5,SRV-FILE-03,16,TrueNAS Core,Sala B
    6,WS-DESENV-02,16,Linux Mint,Oficina 2
    7,SRV-DNS-01,4,CentOS Stream,Sala A
    8,WS-SUPORT-04,12,Windows 10,Oficina 1
    9,SRV-BACKUP,32,Ubuntu 22.04,Magatzem
    10,WS-LAB-05,4,Kali Linux,Laboratori
    ```

--8<-- ".acronims.txt"
