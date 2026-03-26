# Eines per Administradors de Sistemes en Python

## 🚀 Projecte: "L'Alerta del SysAdmin"

L'objectiu és crear un script que monitoritzi el servidor i generi un fitxer de log si el disc o la RAM superen un llindar crític.

```python
import psutil
import datetime

# Configurem els llindars (thresholds)
MAX_DISC = 90.0  # %
MAX_RAM  = 80.0  # %

# 1. Obtenim les dades del sistema
percentatge_disc = psutil.disk_usage('/').percent
percentatge_ram = psutil.virtual_memory().percent
data_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2. Lògica de control
if percentatge_disc > MAX_DISC or percentatge_ram > MAX_RAM:
    missatge = f"[{data_actual}] ALERTA: Disc al {percentatge_disc}% | RAM al {percentatge_ram}%\n"
    
    # 3. Guardem l'alerta en un fitxer de log
    with open("alertes_sistema.log", "a", encoding="utf8") as f:
        f.write(missatge)
    print("⚠️ S'ha registrat una alerta de sistema!")
else:
    print(f"✅ Sistema estable: Disc {percentatge_disc}% - RAM {percentatge_ram}%")
```

## "El Servidor Central d'Alertes"

Podem muntar un servidor molt senzill a un ordinador que rebi les alertes de sistema. Això seria el Servidor del concepte Client-Servidor.

### 1. El Servidor (un de sol)

Només cal la llibreria nativa [flask][] (molt lleugera) per rebre les alertes per HTTP:

```py
from flask import Flask, request
app = Flask(__name__)

@app.route('/alerta', methods=['POST'])
def rebre_alerta():
    dades = request.json
    print(f"🚨 Alerta de {request.remote_addr}: {dades['missatge']}")
    return "Rebut", 200

app.run(host='0.0.0.0', port=5000)
```


[os]:           https://docs.python.org/3/library/os.html   
[shutil]:       https://docs.python.org/3/library/shutil.html
[subprocess]:   https://docs.python.org/3/library/subprocess.html

[flask]:        https://pypi.org/project/Flask/

--8<-- ".acronims.txt"
