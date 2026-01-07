# Python - Exercicis d'iteracions per ASIX

Resol aquests exercicis d'iteracions amb [`for`][for] i/o [`while`][while].

1. _Escaneig de subxarxa (Simulat)_: Demanem a l'usuari que introdueixi els tres primers octets d'una xarxa (_ex: 192.168.1_). El programa generarà i imprimirà totes les adreces IP possibles de la _.1_ a la _.254_.

2. _Comprovació de ports_: Donada una llista de ports comuns (80, 443, 22, 3306, 8080), i una altra amb el nom dels serveis, cal recórrer una de les llistes i "_simular_" una connexió. De forma aleatòria determinarem si el port és OBERT o TANCAT i mostrarem un missatge com ara "Servei nom_del_servei OBERT" o bé "Servei nom_del_servei TANCAT", 

    ```python
    PORTS = [20, 21, 22, 23, 25, 67, 68, 69, 80, 110, 443, 3306, 8000, 8080, 8888]
    SERVEIS = ["FTP-DATA", "FTP", "SSH", "TELNET", "smtp", "dhcpS", "dhcpC", "TFTP", "HTTP", "POP3", "HTTPS", "mySQL", "HTTP", "HTTP", "HTTP"]
    ```

3. _Monitoratge amb while_: Crea un bucle que simuli fer "`ping`" a un servidor cada 5 segons. El bucle només s'aturarà si el servidor "cau" (utilitzarem una probabilitat aleatòria amb el _mòdul random_). Demana la IP a l'usuari.

4. _Generador de noms d'usuari_: Donada una llista amb noms i cognoms reals (ex: ["Pere Pi", "Marta Mas"]), utilitza un bucle per generar noms d'usuari en format _lowercase_ i _sense espais_ (ex: _ppi_, _mmas_ o _pere.pi_, _marta.mas_).

    !!!tip "Com eliminem caràcters estranys?"

        ```python
        # Elimina accents i lletres especials (com la ç o la ñ)
        # Ex: "Eulàlia" -> "Eulalia", "Cañellas" -> "Canellas"
        import unicodedata
        text_normalitzat = unicodedata.normalize('NFKD', "Eulàlia").encode('ascii', 'ignore').decode('ascii')
        ```

    Reptes segons la llista que tinguem:

    1. Format simple: Primera lletra del nom + primer cognom (en minúscules).

        Exemple: _`jpuigvert`_
    
    2. Repte de neteja de dades: Com que hi ha espais i caràcters especials (com la "ç", l'accent o la "ny"), busca com substituir-los o ignorar-los.

        Exemple: _`mribabosch`_ (juntant els dos cognoms sense la "_**i**_").
    
    3. Filtratge: Generar un correu electrònic corporatiu tipus _`nom.cognom@empresa.cat`_ per a tots els usuaris.

    4. Repetits: Posa els usuaris creats en una llista i si algun es repeteix, afegeix-li un número al final, 1 pel primer, 2, pel segon, etc. 
    
        Per exemple: _"Joan Puig"_ i _"Júlia Puig"_ serien _"jpuig"_ i _"jpuig1"_
    
    5. Generador de Comandes Bash: En comptes de crear només els noms, podem crear la comanda per crear l'usuari en _Linux_.

        ```bash
        useradd -m -s /bin/bash nom_usuari
        ```

    ???example "Exemple de noms"
    
        ```python title="Noms que ens compliquen la vida"
        usuaris_nous = [
            ("Jordi", "Puigvert i Casals"),
            ("Montserrat", "Vila i Rovira"),
            ("Arnau", "Serra i Martí"),
            ("Laia", "Font i Capdevila"),
            ("Oriol", "Soler i Gual"),
            ("Meritxell", "Riba i Bosch"),
            ("Marc", "Prats i Roca"),
            ("Eulàlia", "Ventura i Grau"),
            ("Pol", "Sabaté i Solé"),
            ("Aina", "Garriga i Cañellas")
        ]
        ```

5. _Validador de robustesa de contrasenyes_: L'usuari introdueix una contrasenya i el programa la recorre caràcter a caràcter per comprovar si té almenys una majúscula, un número i un símbol. Al final ens ha de dir si compleix o no aquest requeriment.

6. _Bloqueig per intents (Login)_: El programa ha de tenir un bucle `while` que demani una contrasenya. L'usuari té 3 intents per encertar-lo. Si falla els 3, el programa imprimeix "Compte bloquejat per seguretat". Posa el password a encertar en una variable, no cal demanar-lo.

7. _Analitzador de Logs d'Apache_: En una llista de frases donada que simulen un log (amb IPs i codis d'error com 200, 404, 500). Recorre les línies i compta quants errors "404" hi ha.

    ???example "Exemple de línies de log"
    
        ```python
        LINIES_A_ANALITZAR = [
        '172.17.1.4 - - [07/Jan/2026:00:02:34 +0100] "GET /0487-DAM-DAW-Entorns/assets/javascripts/workers/search.973d3a69.min.js HTTP/1.1" 200 16450 "https://apunts.institutmontilivi.cat/0487-DAM-DAW-Entorns/proves/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"',
        '172.17.1.4 - - [07/Jan/2026:00:02:34 +0100] "GET /0487-DAM-DAW-Entorns/img/favicon.ico HTTP/1.1" 200 19051 "https://apunts.institutmontilivi.cat/0487-DAM-DAW-Entorns/proves/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"',
        '172.17.1.4 - - [07/Jan/2026:00:03:48 +0100] "GET /DAW-MP06/arquitectures.html HTTP/1.1" 200 12637 "-" "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)"',
        '127.0.0.1 - - [07/Jan/2026:00:05:10 +0100] "GET / HTTP/1.1" 403 228 "-" "Mozilla/5.0 (ISPConfig monitor)"',
        '127.0.0.1 - - [07/Jan/2026:00:10:11 +0100] "GET / HTTP/1.1" 200 228 "-" "Mozilla/5.0 (ISPConfig monitor)"',
        '127.0.0.1 - - [07/Jan/2026:00:15:08 +0100] "GET / HTTP/1.1" 200 228 "-" "Mozilla/5.0 (ISPConfig monitor)"',
        '127.0.0.1 - - [07/Jan/2026:00:20:08 +0100] "GET / HTTP/1.1" 200 228 "-" "Mozilla/5.0 (ISPConfig monitor)"',
        '172.17.1.4 - - [07/Jan/2026:00:21:45 +0100] "GET /robots.txt HTTP/1.1" 404 4173 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot"',
        '172.17.1.4 - - [07/Jan/2026:00:21:45 +0100] "GET /robots.txt HTTP/1.1" 404 418 "-" "Mozilla/5.0 (Macintosh; Intel MacOS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot"',
        '127.0.0.1 - - [07/Jan/2026:00:25:09 +0100] "GET / HTTP/1.1" 200 228 "-" "Mozilla/5.0 (ISPConfig monitor)"',
        '127.0.0.1 - - [07/Jan/2026:00:30:07 +0100] "GET / HTTP/1.1" 404 228 "-" "Mozilla/5.0 (ISPConfig monitor)"',
        '127.0.0.1 - - [07/Jan/2026:00:35:05 +0100] "GET / HTTP/1.1" 200 228 "-" "Mozilla/5.0 (ISPConfig monitor)"',
        '172.17.1.4 - - [07/Jan/2026:00:35:31 +0100] "GET /usuari1/CIBER-M5023.git/info/refs?service=git-upload-pack HTTP/1.1" 401 4367 "-" "git/2.34.1 (#174-Ubuntu SMP Fri Nov 14 20:25:16 UTC 2025 5.15.0-164-generic; linux x64) vscode/1.107.1 (Visual Studio Code)"',
        '172.17.1.4 - - [07/Jan/2026:00:35:31 +0100] "GET /usuari1/CIBER-M5023.git/info/refs?service=git-upload-pack HTTP/1.1" 200 709 "-" "git/2.34.1 (#174-Ubuntu SMP Fri Nov 14 20:25:16 UTC 2025 5.15.0-164-generic; linux x64) vscode/1.107.1(Visual Studio Code)"',
        '172.17.1.4 - - [07/Jan/2026:00:35:31 +0100] "POST /usuari1/CIBER-M5023.git/git-upload-pack HTTP/1.1" 200 674 "-" "git/2.34.1 (#174-Ubuntu SMP Fri Nov 14 20:25:16 UTC 2025 5.15.0-164-generic; linux x64) vscode/1.107.1 (Visual Studio Code)"',
        '172.17.1.4 - - [07/Jan/2026:00:37:41 +0100] "GET /robots.txt HTTP/1.1" 404 4173 "-" "-"',
        '172.17.1.4 - - [07/Jan/2026:01:21:12 +0100] "GET /DAW-M0612/exemples/api/inventari?id=10 HTTP/1.1" 200 589 "http://localhost:5174/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"',
        '172.17.1.4 - - [07/Jan/2026:01:22:52 +0100] "GET /usuari1/CIBER-M5023.git/info/refs?service=git-upload-pack HTTP/1.1" 401 4367 "-" "git/2.34.1 (#174-Ubuntu SMP Fri Nov 14 20:25:16 UTC 2025 5.15.0-164-generic; linux x64) vscode/1.107.1 (Visual Studio Code)"',
        '172.17.1.4 - - [07/Jan/2026:01:22:52 +0100] "GET /usuari1/CIBER-M5023.git/info/refs?service=git-upload-pack HTTP/1.1" 200 709 "-" "git/2.34.1 (#174-Ubuntu SMP Fri Nov 14 20:25:16 UTC 2025 5.15.0-164-generic; linux x64) vscode/1.107.1(Visual Studio Code)"',
        '172.17.1.4 - - [07/Jan/2026:01:22:52 +0100] "POST /usuari1/CIBER-M5023.git/git-upload-pack HTTP/1.1" 200 674 "-" "git/2.34.1 (#174-Ubuntu SMP Fri Nov 14 20:25:16 UTC 2025 5.15.0-164-generic; linux x64) vscode/1.107.1 (Visual Studio Code)"',
        '127.0.0.1 - - [07/Jan/2026:01:25:05 +0100] "GET / HTTP/1.1" 200 228 "-" "Mozilla/5.0 (ISPConfig monitor)"',
        '172.17.1.4 - - [07/Jan/2026:01:25:52 +0100] "GET /usuari1/CIBER-M5023.git/info/refs?service=git-upload-pack HTTP/1.1" 401 4367 "-" "git/2.34.1 (#174-Ubuntu SMP Fri Nov 14 20:25:16 UTC 2025 5.15.0-164-generic; linux x64) vscode/1.107.1 (Visual Studio Code)"',
        '172.17.1.4 - - [07/Jan/2026:01:29:26 +0100] "GET /MOD-OPT/html/exemples/style.css HTTP/1.1" 404 418 "https://apunts.institutmontilivi.cat/MOD-OPT/html/exemples/p1-s3-ex2.html" "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:146.0) Gecko/20100101 Firefox/146.0"'
        ]
        ```

8. Neteja de fitxers temporals: Donada una llista de noms de fitxers, recórrer-la i "esborrar" (imprimir per pantalla) només aquells que acabin en _`.tmp`_ o _`.log`_.

    ???example "Exemple de fitxers"
    
        ```python
        FITXERS = [
            '/var/log/dpkg.log.10.gz',
            '/var/log/dbconfig-common',
            '/var/log/dbconfig-common/dbc.log.1',
            '/var/log/dbconfig-common/dbc.log',
            '/var/log/alternatives.log',
            '/var/log/dpkg.log.3.gz',
            '/var/log/auth.log',
            '/var/log/dpkg.log',
            '/var/log/syslog.1',
            '/var/log/alternatives.log.6.gz',
            '/var/log/apport.log',
            '/var/log/btmp.1',
            '/var/log/btmp',
            '/var/log/alternatives.log.2.gz',
            '/var/log/auth.log.2.gz',
            '/var/log/dmesg.3.tmp',
            '/var/log/dpkg.log.2.gz',
            '/tmp/.XIM-unix.log',
            '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-systemd-resolved.service-Ser41h',
            '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-systemd-resolved.service-Ser41h/tmp',
            '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-upower.service-9OWUxh.tmp',
            '/tmp/.X11-unix.tmp',
            '/tmp/.ICE-unix.log',
            '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-ntp.service-erKexg',
            '/tmp/systemd-private-e23089bbb5df4291ab877f7cdb88ebdd-ntp.service-erKexg.tmp',
            '/tmp/snap-private.tmp',
            '/tmp/snap-private-tmp/snap.lxd',
            '/tmp/snap-private-tmp/snap.tmp',
            '/tmp/.font-unix',
            '/tmp/.Test-unix'
        ]
        ```

4. _Alertes de disc_: Donada una _llista_ o una _tupla_ de tuples amb el nom del servidor i el percentatge de disc ocupat, l'alumne ha de recórrer la llista i mostrar un missatge d'alerta ("CRITICAL") només per a aquells que superin el 90%.
    A més pots fer:
    
    * Calcula la mitjana d'ocupació.

    * Crea una _llista negra_ amb els servidors que estan en alerta.

    ???example "Exemple de tuples"
    
        ```python title="Llista de tuples"
        LLISTA_TUPLES = [
            ("WEB-PROD-01", 45.2),
            ("DB-SQL-PRIMARY", 92.8),
            ("MAIL-SERVER", 15.0),
            ("BACKUP-NAS", 98.1),
            ("DEV-SANDBOX", 60.5)
        ]
        ```

        ```python title="Tupla de tuples, amb IP"
        TUPLA_TUPLES = (
            (1, "SVR-WEB", "192.168.1.10", 30),
            (2, "SVR-DB", "192.168.1.20", 95),
            (3, "SVR-APP", "192.168.1.30", 88)
        )
        ```

5. _Càlcul de consum mitjà_: Un bucle que demani a l'usuari el consum de RAM de diversos processos fins que s'escrigui **"`fi`"**. Al final, ha de mostrar la mitjana de consum.

11. _Monitoratge de Consum i Seguretat de Processos_: Tenim una llista dels processos que s'estan executant actualment en un servidor Linux. Cada procés està representat per una tupla amb la següent informació: (PID, Nom_Procés, Usuari, %_CPU, Estat).

    ```python
    processos = [
        (101, "systemd", "root", 0.5, "running"),
        (102, "apache2", "www-data", 12.5, "running"),
        (103, "mysql", "mysql", 45.8, "running"),
        (104, "python3", "alumne", 85.2, "running"),
        (105, "bash", "alumne", 1.2, "sleeping"),
        (106, "apache2", "www-data", 14.1, "running"),
        (107, "cryptominer", "alumne", 98.5, "running"),
        (108, "nginx", "www-data", 2.1, "running")
    ]
    ```

    **Objectius**

    1. _Filtratge de Processos Crítics_: Utilitza un bucle per identificar quins processos consumeixen més del 80% de la CPU. El programa ha d'imprimir una alerta indicant el nom del procés i l'usuari que el va llançar.

    2. _Càlcul de Càrrega per Usuari_: Cal recórrer la llista i sumar el consum de CPU total d'un usuari concret (per exemple, `www-data`). Fem-ho demanant el nom de l'usuari que volem analitzar.

    3. _Simulació de "`kill`" de Processos_: Si un procés té el nom "_`cryptominer`_", el programa ha d'imprimir: "`[SEGURETAT] Aturant PID {pid} per alt consum no autoritzat`".

    4. _Resum de l'Estat_: Compta quants processos estan en estat "_running_" i quants en "_sleeping_".


[while]:                https://docs.python.org/reference/compound_stmts.html#the-while-statement       "while"
[for]:                  https://docs.python.org/reference/compound_stmts.html#the-for-statement         "for"

--8<-- ".acronims.txt"
