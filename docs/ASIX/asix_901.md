# Gestió amb Python

Entrant en la gestió de xarxes amb *Python*, passem d'administrar el _"ferro"_ local a controlar la infraestructura. Per a un perfil d'ASIX, *Python* és com una _"navalla suïssa"_ per fer _auditories_, _monitoratge_ i _automatització de configuracions_.

Tres pilars fonamentals:

1. Escaneig i Connectivitat (El "ping" intel·ligent)

    En lloc de fer un ping manual, podem usar *Python* per comprovar l'estat de tota una subxarxa i generar un informe (*JSON* o *CSV*) amb els hosts caiguts.

    Eina: Llibreria `subprocess` (que ja hem vist) o llibreries més potents com `scapy`.

2. Automatització de SSH (`Paramiko` / `Netmiko`)

    !!!question "Paramiko / Netmiko"
        
        són llibreries de *python*:
        
        * `Netmiko`: molt usada en xarxes
        * `Paramiko`: més genèrica

    Podem fer un script que es connecti a 50 servidors o routers simultàniament, executi una comanda (com actualitzar el sistema o canviar una regla de firewall) i tanqui la sessió.

    Cas d'ús: "Necessito canviar la contrasenya de l'usuari `admin` a tots els servidors de la planta 2".

3. Consultes de Xarxa i Sockets

    Python tant pot obrir ports com consultar un _DNS_. Podem crear un _"Port Scanner"_ bàsic per veure quins ports tenen oberts els nostres servidors i detectar vulnerabilitats.

    Llibreria: `socket`.

## Un exemple pràctic per començar: Port Scanner Bàsic

Aquest script mira si un port concret està obert en una IP. És molt útil per entendre com funcionen els timeouts i les connexions TCP.

```python
import socket

def check_port(ip, port):
    # Creem un objecte socket (IPv4, TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) # No volem esperar eternament
    
    resultat = s.connect_ex((ip, port)) # Retorna 0 si està obert
    
    if resultat == 0:
        print(f"Port {port}: OBERT")
    else:
        print(f"Port {port}: Tancat")
    s.close()

# Prova-ho amb el teu servidor local o una IP coneguda
check_port("8.8.8.8", 53) # DNS de Google
```
