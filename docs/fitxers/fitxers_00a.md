# DBeaver

Podem instal·lar l'eina [**dBeaver**][dBeaver]{target="_blank"} que ens permet connectar a una base de dades relacional i mantenir a sessió oberta, executant *comandes SQL*, i veure també els objectes de la base de dades.

Per això anirem a la [pàgina de descàrregues de *dBeaver*][dBeaverDownloads]{target="_blank"} i ens descarregarem la **darrera** versió de **dBeaver Community**.

A continuació veureu unes imatges de la instal·lació. Podem dir que el procés és *següent, següent* sense res a tenir en compte. Només cal escollir si voleu que s'instal·li per a tots els usuaris o només pel vostre.

|   |   |   |
|:-:|:-:|:-:|
|[![dBeaver001][]][dBeaver001]{target="_blank"}|[![dBeaver002][]][dBeaver002]{target="_blank"}|[![dBeaver003][]][dBeaver003]{target="_blank"}|
|[![dBeaver004][]][dBeaver004]{target="_blank"}|[![dBeaver005][]][dBeaver005]{target="_blank"}|[![dBeaver006][]][dBeaver006]{target="_blank"}|
|[![dBeaver007][]][dBeaver007]{target="_blank"}|[![dBeaver008][]][dBeaver008]{target="_blank"}|[![dBeaver009][]][dBeaver009]{target="_blank"}|
|[![dBeaver010][]][dBeaver010]{target="_blank"}|[![dBeaver011][]][dBeaver011]{target="_blank"}|[![dBeaver012][]][dBeaver012]{target="_blank"}|

Una vegada instal·lat ja podem iniciar el programa...

* Quan ens pregunti si volem crear una base de dades d'exemple, indicarem **NO**

* Quan volguem escollir una nova connexió, caldrà especificar el tipus: **SQLite**, **MariaDB**

    * En **SQLite**

        * Indicarem un *nom de fitxer* en una *ubicació*. Pot ser que el fitxer ja existeixi o que no. En aquest darrer cas, es crearà quan comencem a crear-hi taules.

        * **descarregar el driver** necessari per la connexió: *JDBC Driver for SQLite*...

    * En **MariaDB**

        * Deixarem les dades per defecte però...

        * Clicarem la opció de **Probar conexión** i aprofitarem per 

            * **descarregar el driver** necessari per la connexió: *JDBC Driver for MariaDB*...
        
* Tot seguit ja podrem accedir a les dades de la nostra base de dades (Compte, depenent de l'usuari amb què ens haguem connectat, tindrem uns o altres permisos)

    Podem treballar sempre amb un **Script SQL**, `F3`, on escriurem les nostres comandes.

    !!!tip "Cal comprovar la base de dades a la que estem connectats."

[![sqliteDbeaver.png][]][sqliteDbeaver.png]{target="_blank"}

## Fixer base SQLite

* Per treballar amb *SQLite*, podem utilitzar el següent fitxer on tenim creades les taules que treballeu al mòdul de bases de dades:

    [empresa.db][]

## Entorn mysql

Per treballar amb *MySql*, podem utilitzar el següent *script* per crear les taules. Compte, cal que ja estiguen en una *base de dades* ja que l'script no la crea:

* Creem un usuari, una base de dades i donem permís total a l'usuari sobre la base de dades creada:

    Per això iniciarem una `shell` amb el botó `Shell` del *xampp-control* i executarem les següents comandes

    ```bash title="Creem l'usuari"
    mysql -u root -e "CREATE USER `usuari`@`localhost` identified by 'usuari';"
    ```

    ```bash title="Creem les bases de dades"
    mysql -u root -e "CREATE DATABASE `empresa`;"
    ```

    ```bash title="Donem permís a l'usuari sobre les bases de dades creades"
    mysql -u root -e "GRANT ALL PRIVILEGES ON `empresa`.* TO `usuari`@`localhost`; FLUSH PRIVILEGES;"
    ```

    Descarregarem el fitxer [empresa.sql][] al directori on tenim el *xampp*, que és el directori on s'obre la shell del xampp.

    Executem la comanda

    ```bash title="Base de dades empresa"
    mysql -u usuari -pusuari empresa -e "source empresaMySQL.sql"
    ```

    Per comprovar les taules creades, executarem

    ```bash title="Base de dades empresa"
    mysql -u usuari -pusuari empresa -e "show tables"
    ```
    ??? "Possible sortida"

        ```doscon
        +-------------------+
        | Tables_in_empresa |
        +-------------------+
        | countries         |
        | departments       |
        | employees         |
        | job_grades        |
        | job_history       |
        | jobs              |
        | locations         |
        | regions           |
        +-------------------+
        ```



[dBeaver]:          https://dbeaver.io/             "dBeaver"
[dBeaverDownloads]: https://dbeaver.io/download/    "dBeaver Downloads"
[dBeaver001]:       ./img/dBeaver001.png           "001"
[dBeaver002]:       ./img/dBeaver002.png           "002"
[dBeaver003]:       ./img/dBeaver003.png           "003"
[dBeaver004]:       ./img/dBeaver004.png           "004"
[dBeaver005]:       ./img/dBeaver005.png           "005"
[dBeaver006]:       ./img/dBeaver006.png           "006"
[dBeaver007]:       ./img/dBeaver007.png           "007"
[dBeaver008]:       ./img/dBeaver008.png           "008"
[dBeaver009]:       ./img/dBeaver009.png           "009"
[dBeaver010]:       ./img/dBeaver010.png           "010"
[dBeaver011]:       ./img/dBeaver011.png           "011"
[dBeaver012]:       ./img/dBeaver012.png           "012"
[empresa.db]:       ./dades/empresa.db             "Base de dades empresa per SQLite"
[sqliteDbeaver.png]:       ./img/sqliteDbeaver.png             "empresa per SQLite al DBeaver"
[empresa.sql]:      ./dades/empresaMySQL.sql        "empresa.sql"
