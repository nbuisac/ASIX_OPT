# Eines per Administradors de Sistemes en Python

Aquest exercici combina les quatre llibreries següents: `argparse`, `psutil`, `logging` i `requests`.

## 🚀 Projecte: "Creació d'un Agent de Monitoratge (SysMon) amb Alertes Webhook"

Ets l'administrador de sistemes d'una petita empresa. Teniu diversos servidors crítics i necessiteu un script lleuger (un _agent_) que comprovi periòdicament si els servidors s'estan quedant sense memòria RAM o espai al disc. Si algun recurs supera el llindar de perill, l'script ha de deixar constància en un fitxer de registre (_log_) i enviar una alerta al canal de l'equip d'IT (mitjançant un _Webhook_).

### Objectius de l'script (_sysmon.py_)

Cal crear un script en Python que compleixi els següents requisits:

1. Interfície per Comandes (argparse)

    L'_script_ no pot tenir valors fixats dins el codi (hardcoded). Ha d'acceptar els següents arguments des de la terminal:

    * `--ram-limit`: Llindar d'ús de la RAM en percentatge (per defecte: 80).

    * `--disk-limit`: Llindar d'ús del disc principal en percentatge (per defecte: 85).

    * `--webhook`: URL opcional on enviar l'alerta. Si no s'indica, només guardarà l'alerta al fitxer de log.

2. Monitoratge del Sistema (`psutil`)

    * L'script ha d'obtenir el percentatge d'ús de la memòria RAM actual.

    * L'script ha d'obtenir el percentatge d'ús de la partició principal (`/` a _Linux_ o `C:\` a _Windows_).

3. Registre d'Activitats (`logging`)

    Tota l'execució s'ha de registrar en un arxiu anomenat _`sysmon.log`_.

    Ha de registrar un missatge d'_INFO_ cada cop que l'script s'executi, indicant els valors actuals (Ex: **_INFO** - Comprovació: RAM 45% | Disc 60%_).

    Si un valor supera el llindar indicat, ha de registrar un missatge de WARNING (Ex: **_WARNING** - Alerta de RAM: Ús al 88% (Límit 80%)_).

4. Alertes Externes (`requests` i `json`)

    Si hi ha un _WARNING_ i l'usuari ha passat una _URL de webhook_, l'script ha de fer una petició _POST_ enviant un diccionari en format _JSON_ cap a aquesta URL amb el missatge d'alerta.

## Exemples d'execució esperats:

* Cas 1: Execució normal sense superar els límits
    
    ```bash
    $ python sysmon.py --ram-limit 90 --disk-limit 90
    ```

    (No surt res per pantalla, però al fitxer sysmon.log s'hi afegeix: AAAA-MM-DD HH:MI:SS - INFO - Estat del sistema: RAM 45%, Disc 72%_)

* Cas 2: Execució forçant l'alerta amb Webhook (límit al 10%)

    ```bash
    $ python sysmon.py --ram-limit 10 --webhook https://webhook.site/el-seu-codi-aqui
    ```

    (Al fitxer `sysmon.log` hi queda el registre del _WARNING_ i, a més, a la web _webhook.site_ rep el missatge _POST_ amb l'alerta en _JSON_).

!!!note "En comptes d'un servidor webhook podriem enviar un missatge a Discord o telegram"

???example "Possible solució"

    La solució està pensada perquè veiem algunes bones pràctiques (com utilitzar `if __name__ == '__main__':`, separar la lògica en blocs i capturar errors de xarxa).

    === "Client"
    
        ```py
        --8<-- "./docs/ASIX/python/sysmon.py"
        ```

    === "Servidor"

        ```py
        --8<-- "./docs/ASIX/python/server.py"
        ```

[os]:           https://docs.python.org/3/library/os.html   
[shutil]:       https://docs.python.org/3/library/shutil.html
[subprocess]:   https://docs.python.org/3/library/subprocess.html

[flask]:        https://pypi.org/project/Flask/

[argparse]:     https://docs.python.org/3/library/argparse.html
[platform]:     https://docs.python.org/3/library/platform.html
[pathlib]:      https://docs.python.org/3/library/pathlib.html   
[configparser]: https://docs.python.org/3/library/json.html
[configparser]: https://docs.python.org/3/library/configparser.html
[re]:           https://docs.python.org/3/library/re.html
[logging]:      https://docs.python.org/3/library/logging.html
[datetime]:     https://docs.python.org/3/library/datetime.html
[time]:         https://docs.python.org/3/library/time.html
[json]:         https://docs.python.org/3/library/json.html

[psutil]:       https://pypi.org/project/psutil/
[PyYAML]:       https://pypi.org/project/PyYAML/
[requests]:     https://pypi.org/project/requests/
[paramiko]:     https://pypi.org/project/paramiko/
[netmiko]:      https://pypi.org/project/netmiko/

--8<-- ".acronims.txt"
