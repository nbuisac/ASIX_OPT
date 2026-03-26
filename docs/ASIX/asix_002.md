# Eines per Administradors de Sistemes en Python (ii)

Una vegada cobertes les bases de manipulació del sistema (`os`, `shutil`, `subprocess`), podem fer una llista de les llibreries més útils per a un _SysAdmin_, indicant quines venen de sèrie (_**Llibreria Estàndard**_) i quines s'han d'instal·lar via **`pip`** (_**Llibreries de Tercers**_).

## Interacció i Creació d'Eines CLI (Línia de Comandes)

Al fer scripts que s'executen des de la terminal, cal de saber com passar arguments (comandes, flags) als programes.

* [`argparse`][argparse] (Estàndard)

    És la forma nativa de crear interfícies de línia de comandes. Permet definir arguments requerits, opcionals (flags com -h o --verbose) i genera missatges d'ajuda automàticament.

* [`click`][click] (Externa)

    Encara que `argparse` està molt bé, `click` és l'estàndard de facto en la indústria per crear eines CLI complexes gràcies a l'ús de decoradors. És molt més neta i fàcil d'utilitzar per a scripts avançats.

## Monitoratge i Informació del Sistema

* [`psutil`][psutil] (Externa)

    És la llibreria per excel·lència per a la **monitorització del sistema**. Permet obtenir **informació en temps real** sobre l'ús de la CPU, memòria RAM, discos (espai i particions), xarxa i els processos que s'estan executant (com una mena de `top` o `htop` en Python).

* [`platform`][platform] (Estàndard)

    Molt útil per saber on s'està executant l'`script`. Ens indica el sistema operatiu (_Windows_, _Linux_, _macOS_), la versió del kernel, l'arquitectura (_x86_, _ARM_), etc. Perfecte **per fer scripts multiplataforma**.

* [`pathlib`][pathlib] (Estàndard)

    Tot i que ja hem vist `os`, també cal conèixer `pathlib`. És la forma "**_moderna_**" (_Orientada a Objectes_) de treballar amb rutes de fitxers des de Python 3. És molt més neta i fàcil d'entendre que `os.path`.

## Automatització de Xarxes i Connexions Remotes

* [`requests`][requests] (Externa)

    L'eina definitiva per fer **peticions HTTP**. Un SysAdmin interactua constantment amb _APIs REST_ (per exemple, per parlar amb _Proxmox_, _AWS_, _Azure_, _Cloudflare_, un servidor de monitoratge com _Zabbix_, etc.)

* [`paramiko`][paramiko] o [`netmiko`][netmiko] (Externes)

    * [`paramiko`][paramiko]: Implementa el protocol _SSHv2_ de manera nativa. Serveix per connectar-se a servidors Linux remots i executar comandes de forma automatitzada.

        * [`netmiko`][netmiko]: Està construïda sobre _Paramiko_ però està dissenyada específicament per connectar-se a dispositius de xarxa (routers i switches Cisco, MikroTik, Juniper, etc.). Podriem utilitzar-la per configurar els dispositius de xarxa.

## Gestió de Formats i Arxius de Configuració

* [`json`][json] (Estàndard)
    
    Vital per comunicar-se amb APIs o llegir configuracions modernes.

* [`PyYAML`][PyYAML] (Externa)

    YAML és el llenguatge de _Docker Compose_, _Ansible_, _Kubernetes_ i molts altres. Poder llegir, modificar i escriure fitxers `.yml` de forma programàtica és una habilitat clau avui dia.

* [`configparser`][configparser] (Estàndard)

    Perfecte per llegir i escriure els clàssics arxius de configuració d'estil Windows (`.ini`).

## Tractament de Dades i Logs

* [`re`][re] (Estàndard - Expressions Regulars)

    Un SysAdmin passa mitja vida buscant coses dins d'arxius de log _(/var/log/syslog, logs d'Apache/Nginx, etc_.). Saber utilitzar expressions regulars a Python per extreure IPs, dates o codis d'error és una habilitat que ens salvarà moltes hores.

* [`logging`][logging] (Estàndard)

    Cal saber que en producció no s'utilitza `print()`. Hem de fer servir `logging` per generar arxius de registre dels scripts (amb nivells de severitat: _INFO_, _WARNING_, _ERROR_, _CRITICAL_) i incloure dates i formats adequats.

## Gestió del Temps i Tasques

* [`datetime`][datetime] i [`time`][time] (Estàndard)

    Indispensables per crear scripts de còpies de seguretat (crear carpetes amb la data actual) o per mesurar quant de temps triga a executar-se un script.


[argparse]:     https://docs.python.org/3/library/argparse.html
[platform]:     https://docs.python.org/3/library/platform.html
[pathlib]:      https://docs.python.org/3/library/pathlib.html   
[configparser]: https://docs.python.org/3/library/configparser.html
[re]:           https://docs.python.org/3/library/re.html
[logging]:      https://docs.python.org/3/library/logging.html
[datetime]:     https://docs.python.org/3/library/datetime.html
[time]:         https://docs.python.org/3/library/time.html
[json]:         https://docs.python.org/3/library/json.html

[click]:        https://pypi.org/project/click/
[psutil]:       https://pypi.org/project/psutil/
[PyYAML]:       https://pypi.org/project/PyYAML/
[requests]:     https://pypi.org/project/requests/
[paramiko]:     https://pypi.org/project/paramiko/
[netmiko]:      https://pypi.org/project/netmiko/


--8<-- ".acronims.txt"
