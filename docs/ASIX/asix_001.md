# Eines per Administradors de Sistemes en Python

Un cop dominem la lectura i escriptura de fitxers, el següent pas per a un **administrador de sistemes** és interactuar directament amb el sistema operatiu. Per a això, *Python* ens ofereix dues eines clau: `shutil` per a la gestió de fitxers i directori, i `subprocess` per executar comandes de terminal.

## La llibreria `os` (Interacció amb el Sistema Operatiu)

La llibreria `os` (_Operating System_) és una de les més importants per a un administrador de sistemes. Permet que el nostre script de Python interactuï amb el sistema operatiu per gestionar fitxers, carpetes i rutes de forma independent de si estem a Linux, Windows o macOS.

### Gestió de Directoris i Rutes

Abans de treballar amb un fitxer, sovint hem de saber on som o crear l'estructura de carpetes necessària.

* `os.getcwd()`: (_Get Current Working Directory_) Retorna la ruta d'on s'està executant el script.

* `os.chdir(ruta)`: (_Change Directoy_) Canvia el directori de treball actual.

* `os.listdir(ruta)`: Retorna una llista amb tots els fitxers i carpetes d'una ruta (equivalent a un ls o dir).

* `os.mkdir(nom)`: (_Make Directory_) Crea una carpeta nova.

* `os.makedirs(ruta/completa)`: (_Make Directories_) Crea tota una ruta de carpetes (incloent les subcarpetes intermèdies si no existeixen).

```python
import os

# Veure on som i què hi ha
actual = os.getcwd()
print(f"Estem a: {actual}")
print("Contingut del directori:", os.listdir('.'))

# Crear una estructura per a logs
if not os.path.exists("logs/gener/dia1"):
    os.makedirs("logs/gener/dia1")
    print("Estructura de carpetes creada.")
```

### 2. Manipulació de Fitxers

Operacions bàsiques de manteniment:

* `os.rename(antic, nou)`: Canvia el nom d'un fitxer o carpeta.

* `os.remove(ruta)`: Elimina un fitxer.

* `os.rmdir(ruta)`: Elimina una carpeta (només si està buida).

* `os.path.exists(ruta)`: Comprova si un fitxer o carpeta existeix (retorna `True` o `False`).

* `os.path.isfile(ruta) / os.path.isdir(ruta)`: Comprova si és un fitxer o un directori.

### 3. El submòdul `os.path` (Gestió de rutes)

Com a administradors, sovint hem de _"muntar"_ rutes. Mai ho hem de fer sumant strings (ex: ruta + "/" + fitxer), ja que a Windows s'usa \ i a Linux /. Per això fem servir `os.path.join`.

* `os.path.join(part1, part2)`: Uneix parts d'una ruta usant el separador correcte del sistema.

* `os.path.basename(ruta)`: Retorna només el nom del fitxer d'una ruta completa.

* `os.path.getsize(ruta)`: Retorna la mida del fitxer en bytes.

```python
import os

directori = "/var/log"
fitxer = "auth.log"

# Forma correcta i professional de crear una ruta
ruta_completa = os.path.join(directori, fitxer)

if os.path.exists(ruta_completa):
    mida = os.path.getsize(ruta_completa)
    print(f"El fitxer {ruta_completa} ocupa {mida} bytes.")
```

### 4. Variables d'Entorn

Un _SysAdmin_ sovint necessita consultar variables del sistema (com el _PATH_, l'usuari actual o el _HOME_).

* `os.environ`: Un diccionari que conté totes les variables d'entorn.

* `os.getenv('NOM_VARIABLE')`: Obté el valor d'una variable específica.

```python
import os

usuari = os.getenv('USER') or os.getenv('USERNAME')
home = os.getenv('HOME')

print(f"L'usuari actual és: {usuari}")
print(f"El seu directori personal és: {home}")
```

### Exercici Proposat

**L'Organitzador de Fitxers**: Crea un script que llegeixi el contingut d'una carpeta i:

* Detecti quins elements són _fitxers_ i quins són _carpetes_.

* Per als _fitxers_, n'imprimeixi el _nom_ i la _mida en KB_.

* Si troba algun fitxer amb l'extensió `.old`, l'elimini automàticament.


## La llibreria `shutil` (Operacions de Shell)

Mentre que la llibreria `os` ens permet fer operacions bàsiques, `shutil` (_Shell Utilities_) està dissenyada per a operacions d'alt nivell, com copiar carpetes senceres o comprimir dades.
Funcions principals:

* `shutil.copy(origen, desti)`: Copia un fitxer a una nova ubicació.

* `shutil.move(origen, desti)`: Mou un fitxer o directori (també serveix per canviar el nom).

* `shutil.copytree(origen, desti)`: Copia un directori sencer de forma recursiva (ideal per a backups).

* `shutil.rmtree(directori)`: Elimina un directori sencer, encara que contingui fitxers. Atenció: és irreversible.

* `shutil.make_archive(nom, format, ruta)`: Crea un fitxer comprimit (zip, tar, gztar).

* `shutil.disk_usage(ruta)`: Retorna l'estat de l'espai en disc (total, usat i lliure).

```python title="Creació d'un backup comprimit"
import shutil

origen = "/home/alumne/projecte"
desti_zip = "/home/alumne/backups/backup_projecte"

# Creem un fitxer .zip amb tot el contingut de la carpeta origen
shutil.make_archive(desti_zip, 'zip', origen)

print(f"Còpia de seguretat creada a: {desti_zip}.zip")
```

## La llibreria `subprocess` (Execució de comandes)

Aquesta llibreria permet que *Python* enviï comandes directament al terminal (_Bash_ a _Linux_ o _PowerShell_ a _Windows_) i en recuperi el resultat.

### La funció `subprocess.run()`

És la manera moderna i recomanada d'executar comandes.

* `capture_output=True`: Permet guardar el que la comanda imprimiria per pantalla en una variable.

* `text=True`: Fa que la sortida es tracti com a text (string) i no com a bytes.

* `shell=True`: Permet executar comandes pròpies de la shell per defecte, ja que sinó, només busca fitxers executables. Indica a _Python_ que primer obri la terminal i després executi la comanda dins d'ella.

```python title="Comprovació de connectivitat (Ping)"
import subprocess

# Executem la comanda: ping -c 1 8.8.8.8
resultat = subprocess.run(["ping", "-c", "1", "8.8.8.8"], capture_output=True, text=True)

if resultat.returncode == 0:
    print("Xarxa operativa:")
    print(resultat.stdout)  # Imprimeix la sortida de la comanda
else:
    print("Error de connectivitat.")
```

#### ⚠️ Nota important: Comandes internes vs. Programes externs

Quan utilitzem subprocess.run(), hem de diferenciar entre dos tipus d'ordres:

* **Programes externs**: Són fitxers executables independents que resideixen al disc (ex: `ping.exe`, `python.exe`, `git.exe`, o `ls` i `mkdir` a Linux). Aquests funcionen directament amb `subprocess.run(["ping", "8.8.8.8"])`.

* **Comandes internes del sistema**: Són ordres que no existeixen com a fitxer, sinó que viuen dins de l'intèrpret d'ordres (**cmd.exe** a Windows o **bash** a Linux). Exemples a Windows: `dir`, `cls`, `copy`, `type`.

Si intentem executar una comanda interna sense avisar _Python_, rebrem un error de tipus `FileNotFoundError`.

**L'argument `shell=True`**

Per a les comandes internes, cal afegir l'argument `shell=True`. Això diu a Python que primer invoqui el terminal del sistema i després hi executi la comanda.

```python title="Exemple"
import subprocess

# Això donarà ERROR (FileNotFoundError)
# subprocess.run(["dir"]) 

# Això funcionarà correctament
subprocess.run("dir", shell=True)
```

**Diferències de sintaxi**:

* **Sense `shell=True`**: Passem els arguments com una llista: `["ping", "-n", "1", "8.8.8.8"]`.

* **Amb `shell=True`**: Passem tota la comanda com un únic string: "`dir /w"`.

!!!tip "Consell de seguretat"

    Com a _administradors de sistemes_, cal utilitzar `shell=True` **només quan sigui estrictament necessari**. Si podem fer la tasca amb una llibreria nativa (com `os.listdir()` en comptes de `dir`), l'script serà més ràpid, més segur i funcionarà tant a _Windows_ com a _Linux_ sense canvis.








En _Linux_, comandes com `ls`, `mkdir` o `ping` són realment programes independents (els trobem a `/usr/bin/ls`, etc.), per tant solen funcionar **sense** `shell=True`.

    

    ```python title="Exemple"
    import subprocess

    # Opció A: Si només volem veure-ho per pantalla
    subprocess.run("dir", shell=True)

    # Opció B: Si volem capturar la sortida per processar-la
    resultat = subprocess.run("dir", shell=True, capture_output=True, text=True)
    print(resultat.stdout)
    ```


## Exercici combinat: Manteniment del Sistema

Objectiu: Crear un script que automatitzi la neteja de _logs_ i verifiqui l'estat d'un servei.

Passos del script:

* Comprovar l'espai en disc amb shutil.disk_usage.

* Si l'espai lliure és inferior a un llindar, moure els fitxers de la carpeta `logs_temp` a un fitxer comprimit de backup.

* Reiniciar un servei (simulat o real) amb subprocess per aplicar canvis.

```python
import shutil
import subprocess
import os

# 1. Comprovem l'espai (en GB)
total, usat, lliure = shutil.disk_usage("/")
lliure_gb = lliure // (2**30)

print(f"Espai lliure actual: {lliure_gb} GB")

if lliure_gb < 10:
    print("Espai baix. Iniciant compressió de logs...")
    # 2. Comprimir logs vells
    if os.path.exists("./logs_vells"):
        shutil.make_archive("backup_logs", "zip", "./logs_vells")
        shutil.rmtree("./logs_vells")
        print("Logs comprimits i espai alliberat.")

# 3. Verifiquem l'estat d'un servei (Exemple amb Apache o SSH)
print("Verificant estat del servei...")
subprocess.run(["systemctl", "status", "ssh"], capture_output=False)
```

!!!note "Cal tenir en compte que..."

    Quan usem `subprocess.run()`, la comanda s'ha de passar com una llista de strings, on cada element és una paraula de la comanda original (ex: `["ls", "-l", "/etc"]`).

## 4. Gestió d'errors amb check=True

Per defecte, `subprocess.run()` executa la comanda i continua amb la següent línia del script de Python, encara que la comanda del sistema hagi fallat (per exemple, si intentem fer un `ls` d'una carpeta que no existeix).

Però en administració de sistemes, sovint volem que el script s'aturi i ens avisi si una operació falla. Per fer-ho, utilitzarem l'argument `check=True`.

* **Sense `check=True`**: El script continua malgrat l'error.

* **Amb `check=True`**: Python llançarà una excepció del tipus `CalledProcessError` si la comanda retorna un codi d'error (diferent de 0).

```python title="Intentem crear un directori en una ruta protegida"
import subprocess

try:
    # Intentem crear una carpeta a /root/ sense permisos de sudo
    # L'argument check=True farà que si la comanda falla, salti a l'except
    subprocess.run(["mkdir", "/root/prova_admin"], check=True, capture_output=True, text=True)
    print("Carpeta creada amb èxit.")

except subprocess.CalledProcessError as e:
    print(f"ERROR CRÍTIC: La comanda ha fallat amb el codi {e.returncode}")
    print(f"Detalls de l'error: {e.stderr}")
```

Per què és important el returncode?

En el món _Linux/Unix_, quan una comanda s'executa correctament, retorna el codi 0. Qualsevol altre número (1, 2, 127, etc.) indica un tipus d'error específic.

* 0: OK.

* 1: Error general.

* 127: "Command not found" (la comanda no existeix).

### Exercici proposat

Crea un script que demani el nom d'un paquet (ex: `apache2`, `vim`, `htop`) i utilitzi `subprocess` per saber si està instal·lat al sistema fent servir la comanda `which <nom_paquet>`.

* Si el `returncode` és 0, imprimeix "El programa està instal·lat".

* Si és diferent de 0, imprimeix "El programa NO s'ha trobat".

## 🏆 Reptes final: "Bye-bye Bash"

Escriu un script que realitzi aquesta seqüència completa, que és el dia a dia d'un administrador:

* **Cerca**: Trobar tots els fitxers de la carpeta `/var/log` (o una carpeta de prova) que pesin més de 100 KB (`os.path.getsize`).

* **Còpia**: Copia aquests fitxers a una carpeta anomenada `backup_logs` (`shutil.copy`).

* **Compressió**: Comprimeix la carpeta `backup_logs` en un fitxer `.tar.gz` (`shutil.make_archive`).

* **Verificació**: Executa una comanda del sistema per llistar el contingut del fitxer comprimit i verificar que tot és correcte (`subprocess.run(["tar", "-ztvf", "backup_logs.tar.gz"])`).

[os]:           https://docs.python.org/3/library/os.html   
[shutil]:       https://docs.python.org/3/library/shutil.html
[subprocess]:   https://docs.python.org/3/library/subprocess.html

--8<-- ".acronims.txt"
