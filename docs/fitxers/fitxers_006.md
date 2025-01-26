# Accés a bases de dades SQL: SQLite

Python inclou moltes llibreries per treballar amb diferents Sistemes Gestors de Bases de Dades. Una de les més utilitzades, per PCs locals, ja que no necessita cap servidor és `SQLite`. Aquesta només genera un fitxer on hi crearem les taules i podrem executar sentències `DDL` i `DML`.

Per això caldrà importar la [llibreria `sqlite3`][sqlite3].

Veurem algun exemple de com treballar contra una base de dades SQLite. Aprendrem a utilitzar-los amb exemples:

## SQLite

Crearem la nostra base de dades amb les següents instruccions, des del mateix Python.

```xml
import sqlite3 
conn = sqlite3.connect('c:/ASIX/tasques.db')
```

Aquesta sentències crearan un fitxer `tasques.db` al directori on executem les instruccions. Treballarem amb aquesta base de dades.

Podem, també, indicar-li un `PATH` absolut per accedir al fitxer 

```py
conn = sqlite3.connect('c:/ASIX/tasques.db')
```

o bé dir-li que treballarem només amm la memòria del PC, sense guardar res a disc.

```py
conn = sqlite3.connect(':memory:') 
```

### DDL - CREATE TABLE

Per crear les taules, utilitzarem sentències `DDL` de la següent forma:

```py
import sqlite3 
conn = sqlite3.connect('c:/ASIX/tasques.db')
c = conn.cursor() 
c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
id INTEGER PRIMARY KEY, 
name TEXT NOT NULL, 
priority INTEGER NOT NULL 
);''') 
```

Hem creat un *cursor* amb la nostra connexió i hem executat una comanda *SQL*.

### DML - INSERT

Anem a afegir informació. Tal i com s'ha creat la taula, si no posem valor a `id`, aquest anirà agafant valors incrementals des de l'1. Per tant, no li posarem valor.

```py
import sqlite3

conn = sqlite3.connect('c:/ASIX/tasques.db')
c = conn.cursor()
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('La primera tasca', 1))
print("Element inserit amb id:", c.lastrowid)
conn.commit()
conn.close()
```

Fixeu-vos com hem introduit els elements, a partir de substituir els `?` de la comanda `#!sql INSERT` pels camps de la tupla passada com a paràmetre. Això és molt millor que concatenar els valors dins la sentència, ja que evitem l'*SQLInjection*.

També hem fet un `#!py conn.commit()` per confirmar els canvis de la transacció.

Al final hem tancat la connexió amb `#!py conn.close()`.

Si tenim vàries files per iserir, podem inserir-les amb una sola comanda si les tenim en una llista de tuples. Vegem-ho:

```py
import sqlite3

conn = sqlite3.connect('c:/ASIX/tasques.db')
c = conn.cursor()
tasks = [
    ('La segona tasca', 2),
    ('La tercera tasca', 5),
    ('La quarta tasca', 10),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
conn.commit()
conn.close()
```

En aquest cas hem executat la comanda `#!py c.executemany(...)` per executar més d'una sentència `#!sql INSERT`.

### DML - SELECT

Per accedir a la informació emmagatzemada utilitzarem la sentència SQL `#!sql SELECT`:

```py
import sqlite3

conn = sqlite3.connect('c:/ASIX/tasques.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM tasks'):
    print(row)
conn.close()
```

Hem llegit **fila a fila del cursor** directament. En aquest cas veiem que escriu:

```txt
(1, 'La primera tasca', 1)
(2, 'La segona tasca', 2)
(3, 'La tercera tasca', 5)
(4, 'La quarta tasca', 10)
```

També podem carregar totes les files a memòria:

```py
import sqlite3

conn = sqlite3.connect('c:/ASIX/tasques.db')
c = conn.cursor()
c.execute('SELECT * FROM tasks')
rows = c.fetchall()
conn.close()
for row in rows:
    print(row)
```

En aquest cas hem utilitzat la comanda `#!py c.fetchall()` per carregar totes les files en una llista. Fins i tot hem tancat la connexió a la base de dades abans de tractar la llista.

Igual que hem utilitzat la comanda `#!py c.fetchall()`, tenim la comanda `#!py c.fetchone()` per llegit les files una a una. Quan ja no queden més dades, retorna None

```py
import sqlite3

conn = sqlite3.connect('c:/ASIX/tasques.db')
c = conn.cursor()
c.execute('SELECT * FROM tasks')
row = c.fetchone()
while not (row is None):
    print(row)
    row = c.fetchone()
conn.close()
```

De manera semblant, podem executar sentències `#!sql UPDATE` i `#!sql DELETE`.

[sqlite3]: https://docs.python.org/library/sqlite3.html





