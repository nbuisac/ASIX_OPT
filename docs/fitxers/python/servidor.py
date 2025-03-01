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

    def post_insert(self, llista):
        camps = unquote(llista.replace("+"," ")).replace("=","&").split("&")[0::2]
        valors = unquote(llista.replace("+"," ")).replace("=","&").split("&")[1::2]
        diccionari = dict(zip(camps, valors))
        on = diccionari["taula"]
        c = self.conn.cursor()
        text = []
        sql = f'INSERT INTO {on} VALUES ({",".join(["?"] * len(camps[1:]))})'
        try:
            c.execute(sql, tuple(valors[1:]))
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

    def do_POST(self):
        directori = 'C:/ASIX/opt/'
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self._set_headers()
        self.end_headers()
        try:
            td = TractaDades(directori)
            contingut = td.post_insert(unquote(post_data).replace("+", " "))
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