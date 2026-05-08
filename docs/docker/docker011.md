# Docker Avançat: Dockerfile i Multicapa

## 🏗️ L'arquitectura Multicapa

L'esquema de funcionament serà:

<kbd>Usuari</kbd> -> <kbd>Nginx (Port 80)</kbd> -> <kbd>Python (Backend)</kbd> -> <kbd>MariaDB (Dades)</kbd>

Comandes clau per a la classe:

* `docker compose build`: Construeix la imatge del backend llegint el `Dockerfile`.

* `docker compose up -d`: Aixeca tot el laboratori.

* `docker compose logs -f backend`: Per depurar errors de connexió amb la base de dades.

## 📝 Repte

Heu d'aconseguir que el servidor Nginx faci de "Proxy" cap al vostre backend de Python. Reviseu la configuració de `default.conf` i useu `proxy_pass http://backend:5000;`.

1. **Guia per als Alumnes (PDF)**: Document llest per imprimir o compartir, amb tota l'explicació visual del Dockerfile i l'estructura de 3 capes.
[file-tag: code-generated-file-0-1778257928845267603]

2. **Apunts per al teu MkDocs (Markdown)**: El codi font que pots copiar i enganxar directament a la teva documentació de classe.
[file-tag: code-generated-file-1-1778257928845273073]
