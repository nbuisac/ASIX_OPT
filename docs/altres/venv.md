# Python

## Entorns virtuals de Python

Les aplicacions a Python usualment fan ús de *paquets* i *mòduls* que no formen part de la *llibreria estàndard*. Les aplicacions de vegades necessiten una *versió específica d'una llibreria*, ja que aquesta aplicació requereix que un bug particular hagi estat solucionat o bé l'aplicació ha estat escrita usant una versió obsoleta de la interfície de la llibreria.

Això vol dir que potser no és possible per a una instal·lació de Python complir els requeriments de totes les aplicacions. *Si l'aplicació A necessita la versió 1.0 d'un mòdul particular i l'aplicació B necessita la versió 2.0, els requeriments entren en conflicte* i instal·lar la versió 1.0 o 2.0 deixarà una de les aplicacions sense funcionar.

La solució a aquest problema és crear un [entorn virtual][]{target="_blank"} , un **directori** que conté una *instal·lació de Python* d'una versió en particular, a més d'*uns quants paquets addicionals*.

### Creant entorns virtuals

El mòdul utilitzat per crear entorns virtuals és el **`venv`**. **`venv`** instal·larà la versió de Python que estiguem utilitzant Podem veure-la executant `python --version`.

Per crear un entorn virtual, decidim a quina carpeta volem crear-lo i executem el mòdul `venv` com a script amb la ruta a la carpeta:

```bash
python -m venv entorn001
```

Això crearà el directori **entorn001** si no existeix, i també crearà directoris que contenen una còpia de l'intèrpret de Python i diversos fitxers de suport.

Una ruta comuna per al directori d'un entorn virtual és `.venv`. Aquest nom manté el directori típicament amagat a la consola i fora de vista mentre li dóna un nom que explica quin és el motiu de la seva existència. També permet que no hi hagi conflicte amb els fitxers de definició de variables dentorn `.env` que algunes eines suporten.

Un cop creat l'entorn virtual, podrem activar-lo.

=== "Windows"

    ```cmd
    entorn001\Scripts\activate
    ```

=== "Unix o MacOS"

    ```bash
    source entorn001 /bin/activate
    ```

    !!!note "Aquest script està escrit per a la consola bash. Si utilitzeu les consoles *csh* or *fish* , hi ha scripts alternatius `activate.cshi` `activate.fishque` haureu d'usar al seu lloc."

A l'activar l'entorn virtual canvia el prompt de la  consola per mostrar quin entorn virtual està usant, i modifica l'entorn perquè en executar *python* sigui amb aquesta versió i instal·lació en particular. Per exemple:

```bash hl_lines="2"
$ source ~/envs/entorn001/bin/activate
(entorn001) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/entorn001/lib/python3.5/site-packages']
```

Per desactivar l'entorn virtual, cal executar:

```bash
deactivate
```


[entorn virtual]:   https://docs.python.org/3/tutorial/venv.html    "Entorn virtual"


--8<-- ".acronims.txt"
