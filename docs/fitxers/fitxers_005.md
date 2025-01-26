# Lectura de fitxers de diferents tipus

Python inclou moltes llibreries per treballar amb fitxers de text de diferents tipus: XML, JSON, CSV, etc.

Veurem alguns exemples de com treballar amb fitxers de diferents tipus. Aprendrem a utilitzar-los amb exemples:

## XML

Treballarem a partir del fitxer [books.xml][] que desarem al mateix directori on tinguem els programes que provem.

```xml
--8<-- "./docs/fitxers/python/books.xml"
```

El processament de fitxers **XML** a *Python* és molt fàcil gràcies a la classe [`#!py ElementTree`][ElementTree] proporcionada pel mòdul [`#!py xml.etree.ElementTree`][xml.etree.ElementTree]. L'objecte [`#!py ElementTree`][ElementTree] s'encarrega de presentar el document *XML* en forma d'arbre sobre el qual ens podem moure cap amunt o cap avall. També tenim l'objecte [`#!py Element`][Element] que representa un sol node de l'arbre.

En primer lloc, hem d'importar el mòdul adequat i definir-ne un àlies. És habitual utilitzar l'àlies `#!py ET`, però per descomptat podem posar-li el nom que vulguem. Per crear un arbre (un objecte `#!py ElementTree`) a partir d'un document *XML* existent, el passarem al mètode d'anàlisi de la manera següent:

```py
import xml.etree.ElementTree as ET 
tree = ET.parse('books.xml') 
root = tree.getroot() 
```

El mètode `#!py getroot` retorna l'element arrel. Amb accés a l'element arrel, podem arribar a qualsevol element del document. Cadascun d'aquests elements està representat per una classe anomenada `#!py Element`.

A més del mètode d'anàlisi, podem utilitzar el mètode anomenat `fromstring`, que, com a argument, pren XML com a cadena:

```py
import xml.etree.ElementTree as ET

f = open("books.xml")
root = ET.fromstring(f.read())
```

!!!note "El mètode `#!py fromstring` no retorna un objecte `#!py ElementTree` sinó que retorna l'element `#!py root` representat per la classe `#!py Element`."

```py
import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
print('The root tag is:', root.tag)
print('The root has the following children:')
for child in root:
    print(child.tag, child.attrib)
```

!!!note "podem accedir a les dades internes a través d'uns índexos"
    
    Per exemple: 
    
    * **`root[0][0].text`**: retorna el primer element *llibre*, `[0]`, i mostra el **text** del seu primer fill, [0][0]. 
    
        ```py
        print(root[0][0].text) ## mostra -> Antoine de Saint-Exupéry
        print(root[0][1].text) ## mostra -> 1943
        ```

Per mostrar tots els autors podem utilitzar el mètode `#!py iter()`que busca per tot l'arbre i a qualsevol nivell, de la següent forma:

```py
import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for author in root.iter('author'):
    print(author.text)
```

També tenim el màtode `#!py findall()` però aquest, a diferència del que sembla, només busca en el primer nivell des d'on estem:

```py
import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for author in root.findall('author'):
    print(author.text)
```

!!!note "No mostra res ja que `autor` no està al primer nivell"

```py
import xml.etree.ElementTree as ET 
tree = ET.parse('books.xml') 
root = tree.getroot() 
for book in root.findall('book'): 
    print(book.get('title')) 
```

!!!note "En aquest cas, els `book` sí que estan al primer nivell"

### Modificacions

Podem modificar un fitxer *XML* afegint, modificant i eliminant elements i/o etiquetes. Per això utilitzarem mels mètodes `#!py append`, `#!py set`, `#!py remove` que no tractarem aquí.

Per desar el document XML caldrà utilitzar el mètode `#!py write` a partir d'un objecte de tipus `#!py ElementTree`.

```py
tree = ET.ElementTree(root) 
```


[books.xml]:                ./python/books.xml
[xml.etree.ElementTree]:    https://docs.python.org/library/xml.etree.elementtree.html
[ElementTree]:              https://docs.python.org/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree
[Element]:                  https://docs.python.org/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element