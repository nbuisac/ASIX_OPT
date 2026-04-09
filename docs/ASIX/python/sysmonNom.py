import argparse
import psutil
import logging
import requests
import os
import socket  # NOVETAT: Ens permetrà agafar el nom de la màquina automàticament

def main():
    # ---------------------------------------------------------
    # 1. Configuració dels arguments per comandes (argparse)
    # ---------------------------------------------------------
    parser = argparse.ArgumentParser(description="Agent de monitoratge del sistema (SysMon)")
    
    # NOVETAT: Afegim un paràmetre obligatori (required=True) pel nom de l'alumne
    parser.add_argument('--nom', type=str, required=True, help="El teu nom o identificador d'alumne")
    
    parser.add_argument('--ram-limit', type=float, default=80.0, help="Llindar d'us de RAM en %% (per defecte: %(default).2f)")
    parser.add_argument('--disk-limit', type=float, default=85.0, help="Llindar d'ús de Disc en %% (per defecte: %(default)s)")
    parser.add_argument('--webhook', type=str, help="URL del Webhook on enviar les alertes (opcional)")
    
    args = parser.parse_args()

    # ---------------------------------------------------------
    # 2. Configuració del sistema de registre (logging)
    # ---------------------------------------------------------
    logging.basicConfig(
        filename='sysmon.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # ---------------------------------------------------------
    # 3. Recollida de dades del sistema (psutil i socket)
    # ---------------------------------------------------------
    ram_usage = psutil.virtual_memory().percent
    
    disk_path = os.path.abspath(os.sep) 
    disk_usage = psutil.disk_usage(disk_path).percent

    # NOVETAT: Agafem el nom de l'ordinador (Hostname)
    nom_ordinador = socket.gethostname()

    logging.info(f"Estat del sistema: RAM {ram_usage}% | Disc {disk_usage}%")

    # ---------------------------------------------------------
    # 4. Avaluació de les alertes
    # ---------------------------------------------------------
    alertes = []
    
    if ram_usage >= args.ram_limit:
        msg_ram = f"Alerta de RAM: Ús al {ram_usage}% (Límit {args.ram_limit}%)"
        logging.warning(msg_ram)
        alertes.append(msg_ram)

    if disk_usage >= args.disk_limit:
        msg_disc = f"Alerta de Disc: Ús al {disk_usage}% (Límit {args.disk_limit}%)"
        logging.warning(msg_disc)
        alertes.append(msg_disc)

    # ---------------------------------------------------------
    # 5. Enviament de l'alerta (requests) si s'escau
    # ---------------------------------------------------------
    if alertes and args.webhook:
        # NOVETAT: Estructurem el missatge perquè mostri qui ens ho envia
        capcalera = (f"🚨 **ALERTA DE SISTEMA** 🚨\n"
                     f"👤 **Alumne:** {args.nom}\n"
                     f"💻 **Equip:** {nom_ordinador}\n"
                     f"-----------------------------------")
                     
        missatge_final = capcalera + "\n" + "\n".join(alertes)
        payload = {"content": missatge_final}
        
        try:
            resposta = requests.post(args.webhook, json=payload, timeout=10)
            
            if resposta.status_code in [200, 204]:
                logging.info("Alerta enviada correctament al webhook.")
            else:
                logging.error(f"El webhook ha fallat. Codi d'error HTTP: {resposta.status_code}")
                
        except requests.exceptions.RequestException as e:
            logging.error(f"Error de xarxa intentant connectar amb el webhook: {e}")

if __name__ == '__main__':
    main()