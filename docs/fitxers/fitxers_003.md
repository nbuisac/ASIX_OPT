# Escriptura en fitxers de text

Per a més informació podem accedir a la documentació oficial de python: [lectura i escriptura de fitxers]

Els passos que farem seran els següents:

* obrirem el fitxer

* escriurem la informació

* tancarem el fitxer

És important, a l'hora d'obrir el fitxer, tractar els possibles errors: fitxer inexistent, sense permís de lectura, fitxer ja obert, etc...

Veurem les instruccions necessàries, pas a pas:

## [open][]

Per obrir el fitxer utilitzarem la funció [`open`][open] de la següent forma:

```py
fitxer = open('exemple_w.txt', 'wt')
```

!!!tip "Per defecte, el fitxer s'obriria en mode lectura `r` i com fiter de text `t`, per tant `rt`, per això li hem posat el mode `w`"

D'aquesta manera ja tenim una variable, `fitxer`, que ens permet escriure contingut al fitxer.

Els modes d'obertura d'un fitxer són:

* **`'r'`**: obert per a la lectura *(per defecte)*

* **`'w'`**: obert per escriure, truncant primer el fitxer

* **`'x'`**: obert per a la creació exclusiva, fallant si el fitxer ja existeix

* **`'a'`**: obert per escriure, afegint-lo al final del fitxer si existeix

* **`'b'`**: mode binari

* **`'t'`**: mode de text *(per defecte)*

* **`'+'`**: obert per actualitzar (lectura i escriptura) 

En el moment d'obrir el fitxer, podem especificar-li la codificació del mateix: `utf-8`, `cp850`, etc.

## write

Per escriure en un fitxer, utilitzarem la funció `#!py f.write(<text>)`, que escriu el text en el fitxer i ens **retorna el nombre de caràcters escrits** (en mode text) o nombre de bytes (en mode binari).

Vegem-ne un exemple:

```py
--8<-- "./docs/fitxers/python/fitxers_003.py"
```

## writelines

La funció `#!py writeline()` ens permet escriure el que tinguem emmagatzemat en una llista, afegint tots els elements de la llista però sense escriure al final cap alt de línia. Per exemple:

```py
--8<-- "./docs/fitxers/python/fitxers_003_1.py"
```

Escriurà al fitxer `dillunsdimartsdimecresdijousdivendresdissabtediumenge` sense cap alt de línia.

Per solventar-ho podem utilitzar una funció *lambda*, que no hem explicat, dins la funció *map* que tampoc hem explicat. Però aquí ho deixo:

```py
--8<-- "./docs/fitxers/python/fitxers_003_2.py"
```

També podem utilitzar `#!py with` per esciure al fitxer:

```py
--8<-- "./docs/fitxers/python/fitxers_003_3.py"
```

## close

Després d'haver escrit en un fitxer, **cal tancar-lo** ja que així provoquem l'escriptura de les dades a disc. Si no tanquem el fitxer i el programa finalitza inesperadament, podrien no haver-se escrit algunes dades a disc.

```py
close(<variable_del_fitxer>)
```

Al treballar amb fitxers, podem tenir algun error. Per tal de no deixar-lo obert podem utilitzar un codi semblant a:

```py
f = open('exemple.txt', "wt")
try:
    # Utilitzem el fitxer
    pass
finally:
    # Aquesta part SEMPRE s'executarà
    f.close()
```

## [with][]

Fins ara hem vist que quan obrim un fitxer amb `open()`, és obligatori tancar-lo amb `close()` per assegurar que les dades s'escriuen correctament i no es malbaraten recursos del sistema.

*Python* ofereix una forma molt més neta i segura de gestionar els fitxers: la sentència `with`. Aquesta estructura actua com un "gestor de context" (_Context Manager_).

Avantatges d'utilitzar with:

* _**Tancament automàtic**_: El fitxer es tanca sol quan finalitza el bloc de codi indentat, fins i tot si el programa peta o hi ha una excepció a mig procés.

* _**Codi més net**_: Ens estalviem d'haver d'escriure el `try...finally` i el `f.close()`.

* _**Seguretat**_: Evitem l'error típic de l'administrador d'oblidar-se de tancar un descriptor de fitxer, cosa que podria bloquejar el fitxer en el sistema operatiu.

```py
## Escriure fitxers amb la sentència with
com = "Escriptura amb with"
print(com.upper())

llista = ["Linux", "Windows", "macOS", "FreeBSD"]

# Obrim el fitxer fent servir 'with'
# Al final del bloc indentat, el fitxer es tancarà automàticament
with open("sistemes.txt", "wt", encoding="utf-8") as f:
    for so in llista:
        f.write(so + "\n")

# Aquí el fitxer ja està tancat i és segur continuar
print("Fitxer guardat i tancat correctament.")
```

Tot i que no no hem parlat massa del `try`, obrir els fitxers amb o sense `with`, fent que sigui segur el tractament de fitxers i que el sistema no es quedi bloquejant un fitxer, tenim les dues opcions:

```python title="Opció sense with"
f = open('logs.txt', 'w')
try:
    f.write("Dada important")
finally:
    f.close() # Cals recordar d'escriure-ho sempre
```

```python title="Opció amb with"
with open('logs.txt', 'w') as f:
    f.write("Dada important")
# Aquí el fitxer JA està tancat, sense fer res més.
```

Això darrer és l'**estandard actual**. El with fa el codi més llegible i menys propens a errors humans.

| Aspecte | Mètode Clàssic (open + close) | Mètode Recomanat (with) |
|:--------|:--------|:--------|
| **Codi** | Requereix f.close() explícit. | El tancament és automàtic. |
| **Seguretat** | "Si el programa peta abans del close, el fitxer queda obert." | "El fitxer es tanca sempre, encara que hi hagi un error." |
| **Llegibilitat** | Més línies de codi (necessita try/finally). | Codi més net i fàcil de llegir. |
| **Gestió d'errors** | Cal gestionar-lo manualment. | El gestor de context ho gestiona de forma nativa. |

```python title="Exemple dels dos casos"
# MÈTODE TRADICIONAL (Més perillós)
f = open("config.txt", "w")
f.write("Nova configuració")
# Si aquí el sistema s'atura, el fitxer podria quedar bloquejat o corrupte
f.close() 

# MÈTODE AMB 'WITH' (Segur i professional)
with open("config.txt", "w") as f:
    f.write("Nova configuració")
# En sortir de l'intentació, Python fa el close() per nosaltres automàticament.
```


[lectura i escriptura de fitxers]:  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files   "lectura i escriptura de fitxers"
[open]: https://docs.python.org/3/library/functions.html#open   "open"
[with]: https://docs.python.org/3/reference/compound_stmts.html#the-with-statement