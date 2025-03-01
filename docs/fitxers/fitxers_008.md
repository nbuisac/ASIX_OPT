# Servidor web amb python

Python ens permet crear un servidor que escolti peticions web per un port determinat, aquest pot ser el `80`, predeterminat per `http` o qualsevol altre, per exemple `8888`, i per una IP determinada del nostre *servidor*/*ordinador*.

Per això podem utilitzar la llibreria [http.server][]

!!!warning "`http.server` no es recomana per producció ja que només implementa [comprovacions de seguretat bàsiques]."

!!!note "Aquest mòdul només suporta HTTP/1.0 i HTTP/1.1"

## Fitxers per proves

* [index.html][]{download="index.html"}

* [favicon.ico][]{download="favicon.ico"}

* [montilivi.png][]{download="montilivi.png"}

* [layout.html][]{download="layout.html"}

* [empresa.db][]{download="empresa.db"}

## Servidor amb la comanda `python`

Podem iniciar un servidor web des de la mateixa linia de comandes de la següent forma

```py title="executat des de cmd"
python -m http.server 8888 -b 127.0.0.1 -d C:\ASIX\opt
```

Això iniciarà un servidor web per la IP `127.0.0.1` i pel port `8888` que servirà les pàgines que trobi al directori `C:\ASIX\opt`

D'aquest manera, però, no tenim el control de res.

## Servidors programats

Podem crear el nostre propi servidor i fer unes accions o unes altres depenent de diferents paràmetres: URL demanada, ip orígen, etc. Per això ens caldrà definir una **Classe**, que definirà el servidor, on hi programarem allò necessari i després l'instanciarem i l'iniciarem.

Les peticions es tractebn amb un manipulador, *handler*. El mòdul `http.server` proveeix diferents tipus de *handler*

* **`BaseHTTPRequestHandler`**: Tracta les peticions HTTP entrants.

    Proporciona mètodes per analitzar sol·licituds, enviar respostes i gestionar errors.

    Podem sobbreeescriure mètodes per a personalitzar el comportament del servidor HTTP.

* **`SimpleHTTPRequestHandler`**: És una subclasse de `BaseHTTPRequestHandler` que proporciona una implementació bàsica per servir fitxers des de directori on corre el servidor i de qualsevol dels seus subdirectoris.

    Suporta els mètodes GET i HEAD, i genera automàticament llistats de directoris.

    Si troba un fitxer `index.html` mostrarà el seu contingut en lloc de la llista de fitxers del directori.

* **`ThreadingHTTPServer`**: Estén la classe `HTTPServer` proporcionant un servidor HTTP multifil.

    Crea un nou fil per a cada petició entrant, cosa que pot millorar el rendiment quan es manegen múltiples connexions simultànies.

* **`CGIHTTPRequestHandler`**: És una subclasse de `BaseHTTPRequestHandler` que proporciona suport per servir scripts CGI. Executa l'script i torna la sortida com a resposta HTTP. *Aquest mètode s'eliminarà a partir de la versió 3.15 de python*

Anirem creant diferents tipus de servidor, de manera que, cada vegada en tinguem més control.

### Sense control

```py title="servidor.py"
from http.server import HTTPServer, SimpleHTTPRequestHandler

# adreça i port del servidor
host = 'localhost'
port = 8888

# creem una instància del manipualdor por defecte
manipulador = SimpleHTTPRequestHandler

# creem una instància del servidor
# amb el host, port i manipulador preestablerts
servidor = HTTPServer((host, port), manipulador)

# avis del servidor en funcionamient
print(f'Servidor executant-se a http://{host}:{port}/')

# iniciem el servidor
servidor.serve_forever()
```

Aquest servidor serveix els fitxers que es demanen sense cap mena de manipulació nostre. El manipulador `SimpleHTTPRequestHandler` permet servidor fitxers estàtics, que es troben al servidor, siguin de la naturalesa que siguin.

!!!warning "Els fitxers han d'estar al directori on s'executa el servidor."

### Indicant el directori de treball

Per decidir a quin directori tenim la pàgina que volem servir começarem definint una *Classe* que extengui `SimpleHTTPRequestHandler` i d'aquesta manera, al crear el *manipulador*, podem passar-li altres paràmetres.

```py title="servidor.py"
from http.server import HTTPServer, SimpleHTTPRequestHandler

# directori de treball
directori = r'C:\ASIX\opt'

# creem un manipulador propi
class ManipuladorPersonal(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # establim el directori de treball
        super().__init__(*args, directory=directori, **kwargs)

# adreça i port del servidor
host = 'localhost'
port = 8888

# creem una instància del manipualdor por defecte
manipulador = ManipuladorPersonal

# creem una instància del servidor
# amb el host, port i manipulador preestablerts
servidor = HTTPServer((host, port), manipulador)

# avis del servidor en funcionamient
print(f'Servidor executant-se a http://{host}:{port}/')

# iniciem el servidor
servidor.serve_forever()
```

!!!note "És important afegir els paràmeters `self, *args, **kwargs`, ja que sense ells, no funcionaria"

Només hem sobreescrit el mètode `__init__`. Aquí li hem pogut establir el directori de treball.

Per personalitzar la resposta donada, cal sobreescriure el mètode `do_GET()`.

### Personalitzem la resposta

En el següent exemple, sobreescriurem el mètode `do_GET()` per definir un comportament personalitzat pel maneig de peticions `GET`, on podem mostrar els atributs de la petició. Acabarem cridant `super().do_GET()`, per tal que el servidor envïi el fitxer sol·licitat inicialment.

```py title="servidor.py"
from http.server import HTTPServer, SimpleHTTPRequestHandler

# directori de treball
directori = r'C:\ASIX\opt'

# creem un manipulador propi
class ManipuladorPersonal(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # establim el directori de treball
        super().__init__(*args, directory=directori, **kwargs)
    def do_GET(self):
        ## Posem les diferents linies en una llista de strings
        linies_missatge = [
                '\n___ Client ___\n',
                f'client_address={self.client_address} ({self.address_string()})',
                f'self.command={self.command}',
                f'path={self.path}',
                f'request_version={self.request_version}',
                '\n___ Servidor ___\n',
                f'server_version={self.server_version}',
                f'sys_version={self.sys_version}',
                f'protocol_version={self.protocol_version}',
                '',
                '_ Capçaleres _',
                ]
        ## Afegim les capçaleres
        for nom, valor in sorted(self.headers.items()):
            linies_missatge.append(f'{nom}={valor.rstrip()}')
        missatge = '\n'.join(linies_missatge)
        self.send_response(200)
        self.end_headers()
        ## Fi de les caçaleres i afegim el missatge
        self.wfile.write(bytes(missatge, 'utf-8'))
        ## Acabem afegint el fitxer que se'ns ha demanat cridant el mètode do_GET del pare
        self.wfile.write(b'\n\n_ super().do_GET _\n\n')
        super().do_GET()
        return


# adreça i port del servidor
host = 'localhost'
port = 8888

# creem una instància del manipualdor por defecte
manipulador = ManipuladorPersonal

# creem una instància del servidor
# amb el host, port i manipulador preestablerts
servidor = HTTPServer((host, port), manipulador)

# avis del servidor en funcionamient
print(f'Servidor executant-se a http://{host}:{port}/')

# iniciem el servidor
servidor.serve_forever()
```

Fixeu-vos en les variables que podem consultar per tal de saber diferents paràmetres:

* `self.client_address`: ('127.0.0.1', 51692) (127.0.0.1) l'adreça i el port del cient que fa la petició

* `self.command`: petició que realitza el client, en aquest cas `GET`

* `self.path`: el que vé a la URL després del protocol, el servidor  i el port

Amb aquesta darrera variable, `path`, i possiblement el `command`, podem decidir què fer en un servidor, per exemple agafar els paràmeters i enviar unes dades o fer alguna acció, per exemple, en una base de dades.

A la vegada, fixeu-vos que podem canviar algunes capçaleres de les que enviem de resposta. Ho hem fet amb la línia

* `self.send_response(200)`

Al final hem afegit el fitxer que es demana, però podriem haver tornat les dades que nosaltres volguéssim.

### Ho fem tot manualment

Podem extendre la classe `BaseHTTPRequestHandler`, on no podem **sobreescriure** el mètode `do_GET` **però sí implementar-lo**. Farem varis exemples, un primer on tornarem el fitxers que se'ns demani o 404 en cas de not trobar-lo.

```py title="servidor.py"
from http.server import HTTPServer, BaseHTTPRequestHandler

# directori de treball
directori = 'C:/ASIX/opt'

# creem un manipulador propi
class ManipuladorPersonal(BaseHTTPRequestHandler):
    def do_GET(self):
        ## Servim el fitxer que se'ns demani fins on hi ha el nom
        if "?" in self.path:
            path = self.path[:self.path.index("?")]
            parametres = self.path[self.path.index("?") + 1:]
            if parametres == "":
                parametes = ""
        else:
            path = self.path
            parametres = []
        if path == "/":
            path = "/index.html"
        try:
            fitxer = open(directori + path, 'rb')
            contingut = fitxer.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contingut)
        except FileNotFoundError:
            self.send_error(404, f'Fitxer no trobat: {format(path)}')
        return

# adreça i port del servidor
host = 'localhost'
port = 8888

# creem una instància del manipualdor por defecte
manipulador = ManipuladorPersonal

# creem una instància del servidor
# amb el host, port i manipulador preestablerts
servidor = HTTPServer((host, port), manipulador)

# avis del servidor en funcionamient
print(f'Servidor executant-se a http://{host}:{port}/')

try:
    # iniciem el servidor
    servidor.serve_forever()
except KeyboardInterrupt:
    servidor.shutdown()
    print("Aturada del servidor")
```

En aquest cas hem obert el fitxer que se'ns demana en format binari i l'hem retornat sense cap canvi. També hem aprofitat per posar la crida del servidor `#!py servidor.serve_forever()` protegida per quan finalitem el servidor amb `Control + C`. Si ho mireu bé, hem tractat el `self.path` per tal de servir per defecte el fitxer `index.html` quan no ens diguin cap fitxer i per treure els possibles paràmetes que passem en crides `GET`.

### Amb URL amigables

Darrerament les URL son de tipus amigable. Això implica que tenim un fitxer que és el que serveix **totes** les peticions i la resposta depen del *Path* que porta la URL. Aquest és com si tingués direrents opcions separades per `/`. Així el que fariem seria determinar quina opció cal fer segons aquests paràmetes. Anem a fer-ne un exemple:

```py title="servidor.py"
from http.server import HTTPServer, BaseHTTPRequestHandler

# directori de treball

def empleats(llista):
    text = []
    text.append("<h1>Llista dels empleats</h1>")
    text.append("<ul>")
    text.append("<li>King, Steven: 24000</li>")
    text.append("<li>Kochhar, Neena: 17000</li>")
    text.append("<li>De Haan, Lex: 17000</li>")
    text.append("<li>Hunold, Alexander: 9000</li>")
    text.append("<li>Ernst, Bruce: 6000</li>")
    text.append("</ul>")
    return ("\n").join(text)

def departaments(llista):
    text = []
    text.append("<h1>Llista dels departaments</h1>")
    text.append("<ul>")
    text.append("<li>Administration</li>")
    text.append("<li>Marketing</li>")
    text.append("<li>Shipping</li>")
    text.append("<li>IT</li>")
    text.append("<li>Sales</li>")
    text.append("<li>Executive</li>")
    text.append("<li>Accounting</li>")
    text.append("<li>Contracting</li>")
    text.append("</ul>")
    return ("\n").join(text)

def altres(llista):
    text = []
    text.append("<h1>Llista de paràmetres</h1>")
    text.append("<ul>")
    for parametre in llista:
        text.append(f"<li>{parametre}</li>")
    text.append("</ul>")
    return ("\n").join(text)

# creem un manipulador propi
class ManipuladorPersonal(BaseHTTPRequestHandler):
    def do_GET(self):
        directori = 'C:/ASIX/opt/'
        plantilla = "layout.html"

        ## Separem les part de la URL definida
        llista_parametres = self.path.split("/")
        print(llista_parametres)
        ## Ja tenim els paràmetres i ara els tractarem segons les opcions
        if llista_parametres[1] == 'empleats':
            contingut = empleats(llista_parametres[2:])
        elif llista_parametres[1] == 'departaments':
            contingut = departaments(llista_parametres[2:])
        else :
            contingut = altres(llista_parametres[1:])
        try:
            self.send_response(200)
            self.end_headers()
            fplantilla = open(directori + plantilla, 'r', encoding="utf8")
            plantilla = fplantilla.read()
            fplantilla.close()
            self.wfile.write(bytes(plantilla.replace("{{COS_DEL_CODI}}", contingut), "utf8"))
        except FileNotFoundError:
            self.send_error(404, f'Imposible tornar la resposta')
        return

# adreça i port del servidor
host = 'localhost'
port = 8888

# creem una instància del manipualdor por defecte
manipulador = ManipuladorPersonal

# creem una instància del servidor
# amb el host, port i manipulador preestablerts
servidor = HTTPServer((host, port), manipulador)

# avis del servidor en funcionamient
print(f'Servidor executant-se a http://{host}:{port}/')

try:
    # iniciem el servidor
    servidor.serve_forever()
except KeyboardInterrupt:
    servidor.shutdown()
    print("Aturada del servidor")
```

Aquesta vegada hem definit tres funcions `empleats()`, `departaments()` i `altres()` que ens retornen el text que cal afegir a la nostra resposta: Per fer-ho hem agafat un fitxer `index.html` i li hem afegit el text dins el cos. Aquestes tres funcions podrien estar en un mòdul a part.

El problema és que ara no ens retorna els fitxers d'imatges, etc. Podem, però, modificar el programa per tal que primer comprovi si estem demanant un fitxer o bé no. En cas que no trobem el fitxer, tractarem la petició com una URL amiga.

```py title="servidor.py"
from http.server import HTTPServer, BaseHTTPRequestHandler

# directori de treball

def empleats(llista):
    text = []
    text.append("<h1>Llista dels empleats</h1>")
    text.append("<ul>")
    text.append("<li>King, Steven: 24000</li>")
    text.append("<li>Kochhar, Neena: 17000</li>")
    text.append("<li>De Haan, Lex: 17000</li>")
    text.append("<li>Hunold, Alexander: 9000</li>")
    text.append("<li>Ernst, Bruce: 6000</li>")
    text.append("</ul>")
    return ("\n").join(text)

def departaments(llista):
    text = []
    text.append("<h1>Llista dels departaments</h1>")
    text.append("<ul>")
    text.append("<li>Administration</li>")
    text.append("<li>Marketing</li>")
    text.append("<li>Shipping</li>")
    text.append("<li>IT</li>")
    text.append("<li>Sales</li>")
    text.append("<li>Executive</li>")
    text.append("<li>Accounting</li>")
    text.append("<li>Contracting</li>")
    text.append("</ul>")
    return ("\n").join(text)

def altres(llista):
    text = []
    text.append("<h1>Llista de paràmetres</h1>")
    text.append("<ul>")
    for parametre in llista:
        text.append(f"<li>{parametre}</li>")
    text.append("</ul>")
    return ("\n").join(text)

# creem un manipulador propi
class ManipuladorPersonal(BaseHTTPRequestHandler):
    def do_GET(self):
        directori = 'C:/ASIX/opt/'
        fitxer_demanat = ""
        ## Busquem possibles paràmetres GET
        if "?" in self.path:
            fitxer_demanat = self.path[:self.path.index("?")]
            parametres = self.path[self.path.index("?") + 1:]
            if parametres == "":
                parametes = ""
        else:
            fitxer_demanat = self.path
            parametres = []
        try:
            fitxer = open(directori + fitxer_demanat, 'rb')
            contingut = fitxer.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contingut)
            return
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        ## Si no era un fitxer del sistema, tratarem les dades com una URL amiga
        plantilla = "layout.html"
        ## Separem les part de la URL definida
        llista_parametres = self.path.split("/")
        ## Ja tenim els paràmetres i ara els tractarem segons les opcions
        if llista_parametres[1] == 'empleats':
            contingut = empleats(llista_parametres[2:])
        elif llista_parametres[1] == 'departaments':
            contingut = departaments(llista_parametres[2:])
        else :
            contingut = altres(llista_parametres[1:])
        try:
            self.send_response(200)
            self.end_headers()
            fplantilla = open(directori + plantilla, 'rt', encoding = "utf8")
            plantilla = fplantilla.read()
            fplantilla.close()
            self.wfile.write(bytes(plantilla.replace("{{COS_DEL_CODI}}", contingut), "utf8"))
        except FileNotFoundError:
            self.send_error(404, f'Imposible tornar la resposta')
        return

# adreça i port del servidor
host = 'localhost'
port = 8888

# creem una instància del manipualdor por defecte
manipulador = ManipuladorPersonal

# creem una instància del servidor
# amb el host, port i manipulador preestablerts
servidor = HTTPServer((host, port), manipulador)

# avis del servidor en funcionamient
print(f'Servidor executant-se a http://{host}:{port}/')

try:
    # iniciem el servidor
    servidor.serve_forever()
except KeyboardInterrupt:
    servidor.shutdown()
    print("Aturada del servidor")
```

A partir d'aquest codi, podem modificar-lo per tal de tractar dades que ens puguin arribar através de la URL i així afegir informació en una base de dades Relacional, etc.

Podem implementar un servidor web que rebi peticions d'un client web i vagi afegint files en una base de dades.
També podem utilitzar el mateix servidor per servir resultats en diferents formats.

!!!tip "De la mateixa maner que hem implemetat el mètode `do_GET()`, podem implementar: `do_POST()`, `do_PUT()`, `do_DELETE()`, `do_PATCH()`, `do_OPTIONS()`, `do_HEAD()`"

## Exemple d'accés a BD

En aquest exemple canviarant **moltes** coses ja que els mètodes es treballaran com si fos una APIRest, de manera que retornarem les dades en format `json`.

En aquest cas també permetrem fer `#!sql INSERT` i `#!sql DELETE` de la següent forma:

* [http://127.0.0.1:8888/departments/][]: Selecionem tots els **departaments**

* [http://127.0.0.1:8888/departments/80][]: Selecionem el **departament** 80

* [http://127.0.0.1:8888/departments/department_id/80/department_id/50/department_id/90/][]: Selecionem els **departaments** 80, 50 i 90

* [http://127.0.0.1:8888/employees/department_id/80/department_id/50/][]: Seleccionem els **empleats** del departament 50

* [http://127.0.0.1:8888/employees/department_id/80/department_id/50/department_id/90/][]: Selecionem els **empleats** dels departaments 80, 50 i 90

* [http://127.0.0.1:8888/regions/region_id/2][]: seleccionem la **regió** 2

* [http://127.0.0.1:8888/regions/region_name/Europe][]: seleccionem la **regió** de nom `Europe`

* [http://127.0.0.1:8888/jobs/min_salary/3000/][]: seleccionem la **tasca** amb sou mínim de 3000

* [http://127.0.0.1:8888/put/jobs/IT_DBA/Administrador%20de%20bases%20de%20dades/1000/2000][]: **afegim la tasca** `IT_DBA` amb descripció `Administrador de bases de dades`, sou mínim 1000 i sou màxim 2000

* [http://127.0.0.1:8888/delete/jobs/IT_DBA][]: **eliminem la tasca** `IT_DBA`


```py
import sqlite3
import json
from urllib.parse import unquote
from http.server import HTTPServer, BaseHTTPRequestHandler

# directori de treball

class TractaDades:
    def __init__(self, directori):
        self.conn = sqlite3.connect(directori + "empresa.db")

    def do_GET(self, llista_parametres):
        # Implementem un INSERT a la taula JOBS i rebem tots els paràmetres
        if len(llista_parametres) > 3 and \
           llista_parametres[1] == "put" and \
           llista_parametres[2].upper() == "JOBS":
            contingut = self.put_que(llista_parametres[2], llista_parametres[3:])
        elif len(llista_parametres) > 2 and \
           llista_parametres[1] == "delete":
            contingut = self.delete_que(llista_parametres[2], llista_parametres[3:])
        else:
            contingut = self.llista_que(llista_parametres[1], llista_parametres[2:])
        return contingut

    def do_PUT(self, llista_parametres):
        contingut = self.llista_que(llista_parametres[1], llista_parametres[2:])
        return contingut

    def do_DELETE(self, llista_parametres):
        contingut = self.llista_que(llista_parametres[1], llista_parametres[2:])
        return contingut


    def llista_que(self, que, llista):
        c = self.conn.cursor()
        text = []
        sql = f'SELECT * FROM {que}'
        ## Treiem un possible element buit al final
        while len(llista) > 0 and llista[-1] == "":
            llista = llista[:-1]
        ## Si tenim un segon paràmete és el ID que es vol trobar
        ## si hi ha més paràmetres suposarem que van per parelles i són camp/valor
        if len(llista) > 1 and llista[1] != "":
            sql = sql + " WHERE " + " OR ".join(a + " = ?" for a in llista[::2])
            print("sql -> ", sql)
            print("llista -> ", llista)
            files = c.execute(sql, tuple(llista[1::2]))
        elif len(llista) >= 1 and llista[0] != "":
            if que[-3:].upper() == "IES":
                camp = que[:-3] + "Y_ID"
            else:
                camp = que[:-1] + "_ID"
            sql += f" WHERE {camp} = ?"
            files = c.execute(sql, (llista[0], ))
        else:
            files = c.execute(sql)
        # Aconseguim el nom de totes les columnes
        columnes = [a[0] for a in c.description]
        for fila in files:
            text.append(dict(zip(columnes, fila)))
        return json.dumps(text)

    def put_que(self, que, llista):
        if que.upper() == "JOBS":
            c = self.conn.cursor()
            text = []
            sql = f'INSERT INTO {que} VALUES ({",".join(["?"] * len(llista))})'
            try:
                c.execute(sql, tuple(llista))
                self.conn.commit()
                a = self.conn.total_changes
            except Exception as e:
                self.conn.rollback()
                return '{"resultat" : 1, "message": "' + str(e) + '"}'
            
        return '{"resultat" : 0, "afegits": ' + str(a) + '}'

    def delete_que(self, que, llista):
        c = self.conn.cursor()
        text = []
        sql = f'DELETE FROM {que} WHERE '
        ## Si tenim un segon paràmete és el ID que es vol trobar
        if que[-3:].upper() == "IES":
            camp = que[:-3] + "Y_ID"
        else:
            camp = que[:-1] + "_ID"
        sql += f"{camp} = ?"
        try:
            c.execute(sql, (llista[0], ))
            self.conn.commit()
            a = self.conn.total_changes
        except Exception as e:
            self.conn.rollback()
            return '{"resultat" : 1, "message": "' + str(e) + '"}'        
        return '{"resultat" : 0, "eliminats": ' + str(a) + '}'

# creem un manipulador propi
class ManipuladorPersonal(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        directori = 'C:/ASIX/opt/'
        fitxer_demanat = ""
        ## Transformem els caràcters estranys que venen per la URL -> %20, etc
        cami = unquote(self.path)
        ## Busquem possibles paràmetres GET
        if "?" in cami:
            fitxer_demanat = cami[:cami.index("?")]
            parametres = cami[cami.index("?") + 1:]
            if parametres == "":
                parametes = ""
        else:
            fitxer_demanat = cami
            parametres = []
        try:
            fitxer = open(directori + fitxer_demanat, 'rb')
            contingut = fitxer.read()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(contingut)
            return
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        ## Si no era un fitxer del sistema, tratarem les dades com una URL amiga
        ## Separem les part de la URL definida
        llista_parametres = cami.split("/")
        ## Ja tenim els paràmetres i ara els tractarem segons les opcions
        try:
            td = TractaDades(directori)
            contingut = td.do_GET(llista_parametres)
            if contingut == "[]":
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
            else:
                self._set_headers()
            self.wfile.write(bytes(contingut, "utf8"))
        except FileNotFoundError:
            self.send_error(404, f'Imposible tornar la resposta')
        return

# adreça i port del servidor
host = 'localhost'
port = 8888

# creem una instància del manipualdor por defecte
manipulador = ManipuladorPersonal

# creem una instància del servidor
# amb el host, port i manipulador preestablerts
servidor = HTTPServer((host, port), manipulador)

# avis del servidor en funcionamient
print(f'Servidor executant-se a http://{host}:{port}/')

try:
    # iniciem el servidor
    servidor.serve_forever()
except KeyboardInterrupt:
    servidor.shutdown()
    print("Aturada del servidor")
```

!!!info "Material extret de [http://www.tugurium.com/python/index.php?C=PYTHON.15_5_4][]"

[http.server]: https://docs.python.org/es/3.13/library/http.server.html
[comprovacions de seguretat bàsiques]:  https://docs.python.org/es/3.13/library/http.server.html#http-server-security

[index.html]:   ./html/index.html
[montilivi.png]:    ./html/montilivi.png
[favicon.ico]:  ./html/favicon.ico
[layout.html]:  ./html/layout.html
[empresa.db]:  ./dades/empresa.db
[http://www.tugurium.com/python/index.php?C=PYTHON.15_5_4]: http://www.tugurium.com/python/index.php?C=PYTHON.15_5_4

[http://127.0.0.1:8888/departments/]: http://127.0.0.1:8888/departments/
[http://127.0.0.1:8888/departments/80]: http://127.0.0.1:8888/departments/80
[http://127.0.0.1:8888/departments/department_id/80/department_id/50/department_id/90/]: http://127.0.0.1:8888/departments/department_id/80/department_id/50/department_id/90/
[http://127.0.0.1:8888/employees/department_id/80/department_id/50/]: http://127.0.0.1:8888/employees/department_id/80/department_id/50/
[http://127.0.0.1:8888/employees/department_id/80/department_id/50/department_id/90/]: http://127.0.0.1:8888/employees/department_id/80/department_id/50/department_id/90/
[http://127.0.0.1:8888/regions/region_id/2]: http://127.0.0.1:8888/regions/region_id/2
[http://127.0.0.1:8888/regions/region_name/Europe]: http://127.0.0.1:8888/regions/region_name/Europe
[http://127.0.0.1:8888/jobs/min_salary/3000/]: http://127.0.0.1:8888/jobs/min_salary/3000/
[http://127.0.0.1:8888/put/jobs/IT_DBA/Administrador%20de%20bases%20de%20dades/1000/2000]: http://127.0.0.1:8888/put/jobs/IT_DBA/Administrador%20de%20bases%20de%20dades/1000/2000
[http://127.0.0.1:8888/delete/jobs/IT_DBA]: http://127.0.0.1:8888/delete/jobs/IT_DBA
