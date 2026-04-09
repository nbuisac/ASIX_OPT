from flask import Flask, request
from datetime import datetime

# Inicialitzem l'aplicació Flask
app = Flask(__name__)

# Definim la ruta '/webhook' i especifiquem que només accepta peticions POST
@app.route('/webhook', methods=['POST'])
def rebre_alerta():
    # Capturem el JSON que ens envia el client (requests ja ho fa fàcil, Flask també)
    dades = request.json
    
    # Comprovem que hi hagi dades i que tinguin la clau 'content' (com vam programar al client)
    if dades and 'content' in dades:
        hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ip_origen = request.remote_addr # Agafem la IP de qui ens envia l'alerta
        
        # Imprimim l'alerta de forma visual per la terminal
        print("\n" + "="*50)
        print(f"[{hora_actual}] ALERTA REBUDA DES DE LA IP: {ip_origen}")
        print("="*50)
        print(dades['content'])
        print("="*50 + "\n")
        
        # Retornem un codi 200 OK al client perquè sàpiga que ho hem rebut bé
        return "Alerta processada correctament", 200
    else:
        # Si algú fa un POST però no envia el format JSON correcte
        return "Format incorrecte. Es requereix un JSON amb la clau 'content'", 400

if __name__ == '__main__':
    # host='0.0.0.0' permet que el servidor escolti peticions de qualsevol IP de la xarxa
    # port=5000 és el port per defecte, però el pots canviar al que vulguis.
    app.run(host='0.0.0.0', port=5000)