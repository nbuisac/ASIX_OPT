import argparse
import psutil
import logging
import requests
import os

def main():
    # ---------------------------------------------------------
    # 1. Configuració dels arguments per comandes (argparse)
    # ---------------------------------------------------------
    parser = argparse.ArgumentParser(description="Agent de monitoratge del sistema (SysMon)")
    parser.add_argument('--ram-limit', type=float, default=80.0, help="Llindar d'ús de RAM en %% (per defecte %(default)s)"
    parser.add_argument('--disk-limit', type=float, default=85.0, help="Llindar d'ús de Disc en %% (per defecte: %(default)s)"
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
    # 3. Recollida de dades del sistema (psutil)
    # ---------------------------------------------------------
    ram_usage = psutil.virtual_memory().percent
    
    # Utilitzem os.path.abspath(os.sep) per obtenir l'arrel de forma multiplataforma ('/' a Linux, 'C:\' a Windows)
    disk_path = os.path.abspath(os.sep) 
    disk_usage = psutil.disk_usage(disk_path).percent

    # Registrem l'estat actual sempre com a INFO
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
    # Només enviem la petició si hi ha alertes i s'ha configurat un webhook
    if alertes and args.webhook:
        # Preparem el format JSON. La clau 'content' és la que utilitza Discord per defecte.
        missatge_final = "🚨 **ALERTA DE SISTEMA** 🚨\n" + "\n".join(alertes)
        payload = {"content": missatge_final}
        print(missatge_final)
        
        try:
            # Fem la petició POST passant el diccionari al paràmetre 'json' (requests ho converteix automàticament)
            resposta = requests.post(args.webhook, json=payload, timeout=10)
            print(resposta)
            
            # Els codis 200 (OK) o 204 (No Content, habitual a Discord) indiquen èxit
            if resposta.status_code in [200, 204]:
                logging.info("Alerta enviada correctament al webhook.")
            else:
                logging.error(f"El webhook ha fallat. Codi d'error HTTP: {resposta.status_code}")
                
        except requests.exceptions.RequestException as e:
            # Captura qualsevol error de xarxa (timeout, no hi ha internet, URL incorrecta...)
            logging.error(f"Error de xarxa intentant connectar amb el webhook: {e}")

if __name__ == '__main__':
    main()
