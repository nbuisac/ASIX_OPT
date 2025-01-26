# Accés extern

Sovint, la informació que necessitem per treballar, l'anem a buscar automàticamentsense necessitar d'interactuar amb el programa donant-li la informació.

Aquesta informació la podem tenir:

* emmagatzemada en fitxers

* accessible en una base de dades local o externa

* accessible mitjançant protocols de xarxa tipus `http` o `https`

Ara ens centrarem en l'accés a informació que tinguem en fitxers de text.

Cal diferenciar entre fitxers de text i fitxers binaris, tot i que nosaltres ens centrearem en els fitxers de text. 

* **Fitxers de text**: són aquells en què emmagatzemem dades en codi ascii, i que, si en
mostrem el contingut (`type` en *Windows* o `cat` en *linux*) podem veure el que s'hi  emmagatzema. Guarda totes les dades com a caràcter imprimible.

    ![ascii.png][]

* **Fitxers binaris**: són aquells fitxers en què emmagatzemem les dades en bits o Bytes. Si en mostrem el contingut (`type`/`cat`) solem veure caràcters estranys. Solen ser executables, fitxers multimèdia, comprimits, etc.

    ![binari.png][]

Les accions que solem fer en un **fitxer de text** són:

* lectura: llegim el contingut del fitxer:

    * tot de cop

    * línia a línia

    * caràcter a caràcter

* escriptura: escrivim en el fitxer

    * creant-lo prèviament si no existeix

    * sobrescrivint el contingut que tingui el fitxer existent

    * afegint al final del fitxer existent

    hi ha diverses consideracions segons l'existència prèvia o no del fitxer.

Una vegada hem llegit el fitxer o l'estem llegint línia a línia o caràcter a caràcter, caldrà tractar-ne les dades per la qual cosa utilitzarem sempre estructures iteratives.

[ascii.png]:    ./img/ascii.png     "cat/type de fitxer ascii"
[binari.png]:    ./img/binari.png     "cat/type de fitxer binari"