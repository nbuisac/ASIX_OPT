# Python - Exercici total

Anem a fer un programa, amb diferents opcions, que permeti treballar amb llistes, fitxers i bases de dades. Utilitzarem la base de dades SQLite [empresa.db][]

Farem tot el que puguem mitjançant **funcions**, de manera que el codi del programa quedi el més net possible.

1. Començarem creant un menu amb les opcions que presentarem a l'usuari. Hi haurà una opció per sortir i així *SEMPRE* que haguem finalitzat una opció, tornarem al menú fins que decidim sortir.

2. Farem una opció que ens permeti visualitzar les dades de cadascuna de les taules. El nom de les taules estaran guardats en una *llista de taules* per facilitar-nos la feina. Així, doncs, farem un submenu que presenti cadascuna de les taules. L'usuari escollirà la taula i després tornarem aq aquest submenú. La sortida de les dades, totes, serà per consola.

3. Farem un apartat semblant a l'anterior però fent que la sortida de les dades sigui en un fitxer anomenat `<nom de la taula>.csv`. Serà un fitxer en format `csv`. Podeu fer, si voleu, sortida en foramt *JSON* o *XML*

4. Proposarem afegir camps a la base de dades en algunes de les taules. Caldrà demanar la informació necessària per a cada taula. Recordeu que amb la consulta podeu esbrinar el nom de les columnes de la taula.

[empresa.db]:       ./dades/empresa.db             "Base de dades empresa per SQLite"

--8<-- ".acronims.txt"
