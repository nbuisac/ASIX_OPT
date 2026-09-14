# Entrada de dades: Interactuant amb l'administrador

Un script d'automatització esdevé realment útil quan és flexible. En lloc de escriure un codi fix per a un sol usuari o una sola adreça IP, necessitem que l'script pugui rebre dades de l'exterior en el moment de l'execució.

En l'administració de sistemes tenim dues maneres principals d'interactuar amb l'usuari: demanant-li dades mentre l'script s'executa (**mode interactiu**) o recollint paràmetres en el mateix moment de cridar l'script (**arguments de línia de comandes**).

## 1. Entrada interactiva amb input()

La funció [`input()`][input()] atura l'execució de l'script i espera que l'administrador escrigui alguna cosa per teclat i premi <kbd>Intro</kbd>.

```python
# Demanem el nom del servei que volem gestionar
servei = input("Introdueix el nom del servei (ex: apache2, ssh, nginx): ")

print("S'està sol·licitant reiniciar el servei: " + servei)
```

### ⚠️ El gran perill de [`input()`][input()]: Tot és un String!

Això és el que més confon al principi. No importa si l'usuari escriu text, un número o un booleà; [`input()`][input()] sempre ho guardarà com un text (String).

Mira aquest exemple d'error de sistemes:

```py
# Volem comprovar l'espai de disc
llindar_alerta = input("A quin % d'ús de disc vols rebre l'alerta?: ")

# Imaginem que l'usuari escriu: 90
# Python realment està fent això: llindar_alerta = "90"

# Si intentem fer una comparació numèrica de seguretat:
# if llindar_alerta > 85:  <-- Això donarà un ERROR (TypeError) perquè no es pot comparar String amb Integer.
```

### La Solució: El canvi de tipus (Casting)

Per poder operar l'entrada com un número, hem d'embolcallar el `input()` amb la funció [`int()`][int()] o [`float()`][float()]:

```py
# Convertim l'entrada directament a un número enter
llindar_alerta = int(input("A quin % d'ús de disc vols rebre l'alerta?: "))

# Ara sí que funcionarà la lògica!
print(f"Alerta configurada correctament al {llindar_alerta}%.")
```

## 2. El nivell SysAdmin: Arguments des de la terminal (sys.argv)

Si responsabilitzem un script de fer còpies de seguretat cada nit a les $3:00$ AM de manera automàtica (`cronjob`), no hi haurà cap humà davant de la pantalla per contestar a un `input()`.

Els administradors de sistemes preferim passar-li la informació a l'script en la mateixa comanda de llançament, tal com fem amb `mkdir carpeta` o `ping 8.8.8.8`.

Per fer això en Python, utilitzem el mòdul `sys` i la seva llista d'arguments `sys.argv`.

### Com funciona `sys.argv`?

`sys.argv` és una llista que conté totes les paraules que hem escrit a la terminal per executar l'script, separades per espais.

* sys.argv[0] sempre és el nom del propi script.

* sys.argv[1] és el primer argument que passem.

* sys.argv[2] és el segon argument, i així successivament.

```py title="gestio_usuaris.py"
import sys

# Mostrem com s'ha executat l'script
print("Nom de l'script executat:", sys.argv[0])

# Recollim el primer paràmetre de la terminal
nom_usuari = sys.argv[1]

print(f"Creant l'usuari del sistema: {nom_usuari}...")
```

Si l'executem a la nostra terminal fent un simple `python3 gestio_usuaris.py`, l'script fallarà (perquè no trobarà la posició [1]). L'hem d'executar passant-li el paràmetre de l'usuari: 

```bash
$ python3 gestio_usuaris.py marta
Nom de l'script executat: gestio_usuaris.py
Creant l'usuari del sistema: marta...
```

!!!tip "De la mateixa manera que passa amb input(),..."

    ... tot el que arriba a través de `sys.argv` arriba com a text (_String_). Si hi passem un port o un ID, cal transformar-lo amb [`int()`][int()].

_Ho veurem més endavant quan haguem treballat amb llistes._

## 🛠️ Pràctica guiada: Script de diagnòstic de xarxa

Anem a crear un script real d'ASIX que _demani una adreça IP_ de la xarxa corporativa _i un port_ de servei, i simuli que fa una connexió d'auditoria.

```py
print("=== AUDITORIA DE CONNECTIVITAT ===")

# Demanem la IP per input interactiu
ip_desti = input("Introdueix la IP del servidor a auditar: ")
# (Imaginem que l'executem com: python3 script.py 172.17.16.12 443)
# ip_desti = int(sys.argv[1])

# Demanem el port passant-lo directament per argument de la terminal
port_desti = int(input("Introdueix el port del servidor a auditar: "))
# (Imaginem que l'executem com: python3 script.py 172.17.16.12 443)
# port_desti = int(sys.argv[2])

print(f"S'està verificant la connexió amb el servidor {ip_desti} pel port {port_desti}...")
print("Estat: PENDENT (Es necessiten estructures condicionals per comprovar-ho!)")
```



[input()]:      https://docs.python.org/library/functions.html#input
[int()]:        https://docs.python.org/library/functions.html#int
[float()]:      https://docs.python.org/library/functions.html#float
[math]:         https://docs.python.org/library/math.html


--8<-- ".acronims.txt"
