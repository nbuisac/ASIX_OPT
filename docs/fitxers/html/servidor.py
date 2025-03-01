# Extret de http://www.tugurium.com/python/index.php?C=PYTHON.15_5_4
from http.server import HTTPServer, SimpleHTTPRequestHandler

# crear un manejador propio
class ServiorPeticions(SimpleHTTPRequestHandler):
    def do_GET(self):
        # linies_missatge = []
        # # linies_missatge.append(f'<html>')
        # # linies_missatge.append(f'<head>')
        # # linies_missatge.append(f'<title>Prova</title>')
        # # linies_missatge.append(f'</head>')
        # # linies_missatge.append(f'<body>')
        # linies_missatge.append(f'path={self.path}')
        
        # linies_missatge.append('<b>Hola</b>')
        # for a in self.path.split("/"):
        #     linies_missatge.append(a)
        
        # # linies_missatge.append(f'</body>')
        # # linies_missatge.append(f'</html>')
        # missatge = "<br>".join(linies_missatge)
        # self.send_header('Content-type', 'text/html')
        # self.send_response(200)
        # self.end_headers()
        # self.wfile.write(bytes(missatge, 'utf-8'))

        super().do_GET()

        return


        # linies_missatge = [
        #         '\n___ Client ___\n',
        #         f'client_address={self.client_address} ({self.address_string()})',
        #         f'{self.command=}',
        #         f'path={self.path}',
        #         f'request_version={self.request_version}',
        #         '\n___ Servidor ___\n',
        #         f'server_version={self.server_version}',
        #         f'sys_version={self.sys_version}',
        #         f'protocol_version={self.protocol_version}',
        #         '',
        #         '_ Capçaleres _',
        #         ]
        # for nom, valor in sorted(self.headers.items()):
        #     linies_missatge.append(f'{nom}={valor.rstrip()}')
        # missatge = '\n'.join(linies_missatge)
        # self.send_response(200)
        # self.end_headers()
        # self.wfile.write(bytes(missatge, 'utf-8'))

        # self.wfile.write(b'\n\n_ super().do_GET _\n\n')
        # super().do_GET()
        # return

if __name__ == "__main__":
    # dirección y puerto del servidor
    host = 'localhost'
    puerto = 8888

    # crear una instancia del manejador personalizado
    manejador = ServiorPeticions

    # crear una instancia del servidor
    # con el host, puerto y el manejador propio
    servidor = HTTPServer((host, puerto), manejador)

    # aviso del servidor en funcionamiento
    print(f'Servidor ejecutándose en http://{host}:{puerto}/')

    # iniciar el servidor
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        servidor.shutdown()
        print("Servidor aturat")
