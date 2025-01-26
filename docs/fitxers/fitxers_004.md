# Lectura de fitxers de diferents tipus

Python inclou moltes llibreries per treballar amb fitxers de text de diferents tipus: XML, JSON, CSV, etc.

Veurem alguns exemples de com treballar amb fitxers de diferents tipus. Aprendrem a utilitzar-los amb exemples:

## CSV

El format *CSV* (*"Comma Separated Values"*) és un dels formats de fitxer més populars utilitzats per emmagatzemar i transferir dades entre diferents programes. Actualment, moltes eines de gestió de bases de dades, i el popular Excel, ofereixen la importació i exportació de dades en aquest format.

El fitxer *CSV* és un fitxer de text senzill amb l'extensió `.csv`. Un fitxer típic conté valors separats per comes, però també es permeten altres separadors com el *punt i coma* o la *tabulació*. Cal destacar que només es pot utilitzar un tipus de separador en un fitxer *CSV*.

Cada línia del fitxer representa un conjunt determinat de dades. Opcionalment, a la primera línia podem posar una capçalera que descrigui aquestes dades. Vegem un exemple senzill d'un fitxer anomenat [`contactes.csv`][contactes.csv] que emmagatzema contactes amb un telèfon:

```csv
--8<-- "./docs/fitxers/python/contactes.csv"
```

!!!note "Fixeu-vos que a la primera línia hi ha els noms dels camps"

!!!tip "Nosaltres utilitzarem la llibreria que ve per defecte, però per usos comercials, n'hi ha de millors, com ara la *[Pandas][]*"

## Llegim el fitxer

Per llegir el fitxer utilitzarem la següent estructura:

```py
import csv

with open('contactes.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for fila in reader:
        print(fila)
```

En aquest cas, fila és una llista amb els elements de cadascuna de les files:

```py
['Nom', 'Telefon']
['mare', '666-555-444']
['pare', '678-123-456']
['germana', '654-321-098']
['amic', '675-483-921']
```

Com que tenim la primera línia amb els noms de camp, podem obtenir les dades com un `diccionari`:

```py
import csv

with open('contactes.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        print(row['Nom'], ':', row['Telefon'])
```

Si el fitxer d'entrada, `csv`, no té capçaleres, podem definir-les nosaltres mateixos de la següent forma:

```py hl_lines="4"
import csv

with open('contactes.csv', newline='') as csvfile:
    fieldnames = ['Nom', 'Telefon']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        print(row)
        print(row['Nom'], row['Telefon'])
```

!!!note "A nosaltres, com que la primera fila sí són capçaleres, ens surt una promera fila que no hauria de ser. Caldria treure-la del fitxer de `contactes.csv`"

## Escriptura de dades

Per escriure dades en un fitxer `csv` utilitzarem el següent exemple com a mostra:

```py
import csv

with open('contactes_exportats.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    writer.writerow(['Nom', 'Telefon'])
    writer.writerow(['mare', '666-555-444'])
    writer.writerow(['pare', '678-123-456'])
    writer.writerow(['germana', '654-321-098'])
    writer.writerow(['amic', '675-483-921'])
    writer.writerow(['avi, avia', '612-345-678'])
```

En aquest darrer cas, com que el darrer element conté una coma, hem utilitzat, en el writer, els paràmetres `#py quotechar='"', quoting=csv.QUOTE_MINIMAL` per tal d'escriure'ls entre cometes dobles.

On hem utilitzat `csv.QUOTE_MINIMAL`, podriem haver utilitzat, també:

* **`csv.QUOTE_ALL`**: cita tots els valors

* **`csv.QUOTE_NONNUMERIC`**: només cita valors no numèrics

* **`csv.QUOTE_NONE`**: no cita cap valor. No és una bona idea establir aquest valor si hi ha caràcters especials que requereixen cometes, perquè això generarà un error.

!!!note "Els paràmetres `quotechar` i `quoting` també es poden utilitzar a la funció `read`. Consulteu la documentació per a més informació."

[contactes.csv]: ./python/contactes.csv
[Pandas]:   https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html