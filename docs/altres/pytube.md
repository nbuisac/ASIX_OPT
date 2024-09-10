# Python

## Descarreguem un vídeo de Youtube amb Python i pytube

Per veure la simplicitat de treballar amb mòduls de python, executarem un exemple que ens permetrà crear un entorn virtual on instal·larem el mòdul `pytube` i ens descarregarem un vídeo.

### Creem un entorn i l'activem

```bash
python -m venv .pytube
.pytube\Scripts\Activate
```

### Instal·lem el paquet `pytube`

```bash
pip install pytube
```

!!!tip "Pots trobar la documentació de [pytube prement aquest enllaç][pytube]{target="_blank"}."

### Executem comandes dins l'intèrpret de python

```bash 
python
```

```py
from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=pdgFqPbw64g")
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
exit()
```

### El resultat és ...

```bash hl_lines="1-3 10 13-15 17 19"
C:\asix>python -m venv .pytube
C:\asix>.pytube\Scripts\Activate
(.pytube) C:\asix>pip install pytube
Collecting pytube
  Using cached pytube-15.0.0-py3-none-any.whl.metadata (5.0 kB)
Using cached pytube-15.0.0-py3-none-any.whl (57 kB)
Installing collected packages: pytube
Successfully installed pytube-15.0.0

(.pytube) C:\asix>python
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from pytube import YouTube
>>> yt = YouTube("https://www.youtube.com/watch?v=pdgFqPbw64g")
>>> yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
'C:\\asix\\🔴 Qué es el ESP32 y porque deberías tener esta placa.mp4'
>>> exit()

(.pytube) C:\asix>dir
 El volumen de la unidad C no tiene etiqueta.
 El número de serie del volumen es: DEF8-1976

 Directorio de C:\asix

05/07/2024  11:30    <DIR>          .
05/07/2024  11:27    <DIR>          .pytube
05/07/2024  11:30        14.474.970 🔴 Qué es el ESP32 y porque deberías tener esta placa.mp4
               1 archivos     14.474.970 bytes
               2 dirs  138.858.414.080 bytes libres

(.pytube) C:\asix>
```

[![pytube001.png][]][pytube001.png]{target="_blank"}

[Índex de Paquets de Python]:   https://pypi.org/    "Índex de Paquets de Python"
[Instal·lant mòduls de Python]: https://docs.python.org/3/installing/index.html#installing-index    "Instal·lant mòduls de Python"
[pytube]:                       https://pypi.org/project/pytube/    "pytube"
[pytube001.png]:                ./img/pytube001.png     "Vídeo descarregat"

--8<-- ".acronims.txt"
