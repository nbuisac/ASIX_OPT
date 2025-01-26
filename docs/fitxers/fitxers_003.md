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


[lectura i escriptura de fitxers]:  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files   "lectura i escriptura de fitxers"
[open]: https://docs.python.org/3/library/functions.html#open   "open"