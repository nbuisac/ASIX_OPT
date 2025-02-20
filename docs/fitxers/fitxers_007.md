# Accés a bases de dades SQL: MariaDB

Python inclou moltes llibreries per treballar amb diferents Sistemes Gestors de Bases de Dades. Una de les més utilitzades és `MariaDB`/`Mysql`.

Per això caldrà importar la llibreria `mariadb`. Trobareu informació sobre el seu ús a:

* [How to connect Python programs to MariaDB][mariadb].

* [MariaDB Connector/Python][mariadb git hub]

Veurem algun exemple de com treballar contra una base de dades SQLite. Aprendrem a utilitzar-los amb exemples:

## MariaDB

Crearem la nostra base de dades amb les següents instruccions, des del mateix Python.

```py
import mariadb 

connc = mariadb.connect(
    host="localhost",
    user="usuari",
    password="password",
    database="base_de_dades"
)
```

Aquesta sentències es connecten a la base de dades determinada amb les credencials que li passem.

### DDL - CREATE TABLE

Per crear les taules, utilitzarem sentències `DDL` de la següent forma:

```py
c = connc.cursor() 
c.execute('''CREATE TABLE IF NOT EXISTS tasks ( 
id INTEGER PRIMARY KEY AUTO_INCREMENT, 
name VARCHAR(100) NOT NULL, 
priority INTEGER NOT NULL 
);''') 
```

Hem creat un *cursor* amb la nostra connexió i hem executat una comanda *SQL*.

### DML - INSERT

Anem a afegir informació. Tal i com s'ha creat la taula, si no posem valor a `id`, aquest anirà agafant valors incrementals des de l'1. Per tant, no li posarem valor.

```py
c = connc.cursor()
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('La primera tasca', 1))
print("Element inserit amb id:", c.lastrowid)
print("Files inserides ", c.rowcount)
connc.commit()
connc.close()
```

Fixeu-vos com hem introduit els elements, a partir de substituir els `?` de la comanda `#!sql INSERT` pels camps de la tupla passada com a paràmetre. Això és molt millor que concatenar els valors dins la sentència, ja que evitem l'*SQLInjection*.

També hem fet un `#!py connc.commit()` per confirmar els canvis de la transacció. Si no es confirmen, no quedaran desats a la base de dades ja que es farà un `#!sql ROLLBACK`.

Al final hem tancat la connexió amb `#!py connc.close()`.

Si tenim vàries files per inserir, podem inserir-les amb una sola comanda si les tenim en una llista de tuples. Vegem-ho:

```py
c = connc.cursor()
tasks = [
    ('La segona tasca', 2),
    ('La tercera tasca', 5),
    ('La quarta tasca', 10),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
print("Files inserides ", c.rowcount)
connc.commit()
connc.close()
```

En aquest cas hem executat la comanda `#!py c.executemany(...)` per executar més d'una sentència `#!sql INSERT`.

### DML - SELECT

Per accedir a la informació emmagatzemada utilitzarem la sentència SQL `#!sql SELECT`:

```py
c.execute('SELECT * FROM tasks')
print("Mostrem", c.rowcount, "files")
for row in c:
    print(row)
connc.close()
```

Hem llegit **fila a fila del cursor** directament. En aquest cas veiem que escriu:

```txt
Mostrem 4 files
(1, 'La primera tasca', 1)
(2, 'La segona tasca', 2)
(3, 'La tercera tasca', 5)
(4, 'La quarta tasca', 10)
```

També podem carregar totes les files a memòria:

```py
c.execute('SELECT * FROM tasks')
rows = c.fetchall()
print("Mostrem", c.rowcount, "files carregades ja a memòria")
for row in rows:
    print(row)
```

En aquest cas hem utilitzat la comanda `#!py c.fetchall()` per carregar totes les files en una llista. Fins i tot podem tancar la connexió a la base de dades abans de tractar la llista.

Igual que hem utilitzat la comanda `#!py c.fetchall()`, tenim la comanda `#!py c.fetchone()` per llegit les files una a una. Quan ja no queden més dades, retorna `None`

```py
c = connc.cursor()
c.execute('SELECT * FROM tasks')
row = c.fetchone()
while not (row is None):
    print(row)
    row = c.fetchone()
    print("Hem mostrat ", c.rowcount, "files")

connc.close()
```

De manera semblant, podem executar sentències `#!sql UPDATE` i `#!sql DELETE`.

[mariadb]: https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/

[mariadb git hub]:  https://mariadb-corporation.github.io/mariadb-connector-python/





