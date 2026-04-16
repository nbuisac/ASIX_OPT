import socket
import subprocess

def check_port(ip, port):
    # Creem un objecte socket (IPv4, TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # No volem esperar eternament
    
    resultat = s.connect_ex((ip, port)) # Retorna 0 si està obert
    
    if resultat == 0:
        print(f"Host: {ip:<20} Port {port}: OBERT")
    else:
        pass
        # print(f"Host: {ip:<20} Port {port}: Tancat")
    s.close()

def fes_ping():
    for a in range(1,100):
        subprocess.run([f"ping 192.168.1.{a}", "-n 1", "-w 10"], shell=True, check=False)

fes_ping()