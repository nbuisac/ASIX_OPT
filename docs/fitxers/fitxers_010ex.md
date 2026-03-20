# Python - Migració Crítica de Vendes (CSV a SQLite)

**Context**

L'empresa "ASIX-Tech" ha comprat una botiga antiga que gestionava les vendes en un fitxer de text. La teva missió com a administrador de sistemes és **crear un script de Python** que **netegi** aquestes dades i les **munti** en una base de dades **SQLite3** per a la nova aplicació web.

**Tasques a realitzar**

* **Creació de la DB**: Crea una base de dades anomenada **_gestio_vendes.db_** amb una taula 

    | comandes |
    |-----------------|
    | id INT **CLAU PRIMÀRIA**|
    | producte TEXT |
    | total REAL |
    | estat TEXT |

    ```sql title="Comanda CREATE TABLE"
    CREATE TABLE comanda (
	    id INT PRIMARY KEY,
	    producte TEXT,
	    total REAL,
	    estat TEXT
    );
    ```

    
* **Lectura i Filtre**: Llegeix el fitxer [**_dades_vendes.csv_**][dades_vendes].

    ???info "Contingut del fitxer dades_vendes.csv"

        ```txt
        --8<-- "docs/fitxers/dades/dades_vendes.csv"
        ```

* **Lògica de Negoci**:
        
    * Si el preu o la quantitat **no són números vàlids**, descarta la fila i **mostra un avís per pantalla**.

    * **Calcula el total** multiplicant _preu * quantitat_.
        
        * Si el total és superior a 500€, marca l'estat com a 'PREMIUM', si no, 'ESTANDARD'.

* **Inserció Segura**: Insereix les dades vàlides utilitzant consultes parametritzades (?) per evitar injecció SQL.

* **Verificació**: Fes un **SELECT** final que mostri per consola quants registres s'han inserit correctament.

* **Fitxer de log**: Les dades de les files que no hem inserit les poden desar en un altre fitxer de log (amb format _csv_), anomenat `vendes_no_carregades.csv`


???example "Possible solució: Sense llistes"

    ```py
    --8<-- "docs/fitxers/python/csvSQLite.py"
    ```

???example "Possible solució: Amb llistes"

    ```py
    --8<-- "docs/fitxers/python/csvSQLiteLlistes.py"
    ```

[dades_vendes]:       ./dades/dades_vendes.csv             "dades_vendes.csv"

--8<-- ".acronims.txt"
