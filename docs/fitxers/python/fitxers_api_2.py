import requests

try: 
    dades = {
        'taula' : 'JOBS',
        'job_id' : 'IT_DBAR',
        'job_title' : 'Administrador Bases de Dades Relacionals',
        'min_salary': 1500,
        'max_salary': 2500
    }

    headers = {
        'Content-Type': 'application/json'
    }

    lloc = "http://localhost:8888/"
    reply = requests.post(lloc, data = dades, headers=headers )
    if reply.status_code == requests.codes.ok: 
        print(reply.text)
except requests.exceptions.Timeout: 
    print('Ha passat massa temps per connectar') 
except requests.exceptions.InvalidURL:
    print('Adreça desconeguda!')