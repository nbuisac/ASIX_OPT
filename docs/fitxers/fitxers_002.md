# Lectura de fitxers de text

Per a més informació podem accedir a la documentació oficial de python: [lectura i escriptura de fitxers]

Els passos que farem seran els següents:

* obrirem el fitxer

* llegirem la informació

* tancarem el fitxer

És important, a l'hora d'obrir el fitxer, tractar els possibles errors: fitxer inexistent, sense permís de lectura, fitxer ja obert, etc...

Veurem les instruccions necessàries, pas a pas:

## [open][]

Per obrir el fitxer utilitzarem la funció [`open`][open] de la següent forma:

```py
fitxer = open('exemple.txt')
```

!!!tip "Per defecte, el fitxer s'obre en mode lectura `r` i com fiter de text `t`, per tant `rt`"

D'aquesta manera ja tenim una variable, `fitxer`, que ens permet accedir al contingut del fitxer.

Els modes d'obertura d'un fitxer són:

* **`'r'`**: obert per a la lectura *(per defecte)*

* **`'w'`**: obert per escriure, truncant primer el fitxer

* **`'x'`**: obert per a la creació exclusiva, fallant si el fitxer ja existeix

* **`'a'`**: obert per escriure, afegint-lo al final del fitxer si existeix

* **`'b'`**: mode binari

* **`'t'`**: mode de text *(per defecte)*

* **`'+'`**: obert per actualitzar (lectura i escriptura) 

En el moment d'obrir el fitxer, podem especificar-li la codificació del mateix: `utf-8`, `cp850`, etc.

## read

Per llegir el contingut d'un fitxer, utilitzarem la funció `#!py f.read(<mida>)`, que llegeix una quantitat de dades i **les retorna com a cadena** (en mode text) o objecte bytes (en mode binari). `mida` és un *argument numèric opcional*. Quan s'omet la mida o és negativa, es llegirà i es retornarà **tot** el contingut del fitxer. **Compte** si el fitxer és el doble de gran que la memòria de la vostra màquina. En cas contrari, es llegeixen i es retornen **com a màxim** caràcters de `mida` (en mode text) o bytes de `mida` (en mode binari). Si s'ha arribat al final del fitxer, f.read() retornarà una cadena buida (`''`).

## readline

També podem llegir un fitxer de text línia a línia, utilitzarem la funció `#!py f.readline()`. 

`#!py f.readline()` llegeix una única línia del fitxer; **el caràcter de nova línia (`\n`) es deixa al final de la cadena** i només s'omet a l'última línia del fitxer si el fitxer no acaba en una nova línia. Això fa que el valor de retorn sigui inequívoc; quan `#!py f.readline()` retorna una cadena buida, significa que s'ha arribat al final del fitxer, mentre que una línia en blanc es representa amb '\n', una cadena que conté només un salt de línia.

Per llegir línies d'un fitxer, podem utilitzar un bucle sobre l'objecte fitxer. Això és més eficient de memòria, ràpid i condueix a un codi senzill:

```py 
fitxer = open('exemple.txt')
for linia in fitxer:
    print(linia, end="")
```

Si volem llegir totes les línies d'un fitxer, i carregar-les en una llista, podem utilitzar `#!py list(f)` o `#!py f.readlines()`.

Anem a provar aquest programa, que llegirà el fitxer i en mostrarà el contingut de diferents formes:

```py
--8<-- "./docs/fitxers/python/fitxers_002.py"
```

## close

Una bona pràctica és, després d'haver llegit el fitxer, **tancar-lo**. Segurament aquest acabarà tancan-se sautomàticament si arribem al final, però sempre és millor assegurar-nos-en.

```py
close(<variable_del_fitxer>)
```

Al treballar amb fitxers, podem tenir algun error. Per tal de no deixar-lo obert podem utilitzar un codi semblant a:

```py
f = open('exemple.txt')
try:
    # Utilitzem el fitxer
    pass
finally:
    # Aquesta part SEMPRE s'executarà
    f.close()
```

També podem llegir un fitxer i tancar-lo automàticament al final amb la sentència `with`:

```py
with open('exemple.txt') as f:
    # Utilitzar el fichero. Es tancarà automàticament
    pass
```

Aquesta darrera opció ens estalvia algunes línies de codi.


[lectura i escriptura de fitxers]:  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files   "lectura i escriptura de fitxers"
[open]: https://docs.python.org/3/library/functions.html#open   "open"