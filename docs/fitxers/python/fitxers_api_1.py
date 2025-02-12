## https://jsonplaceholder.typicode.com/
## https://jsonplaceholder.typicode.com/users/3
import requests

try: 
    reply = requests.get("https://jsonplaceholder.typicode.com/users/3", timeout=1)
    if reply.status_code == requests.codes.ok: 
        print(reply.headers)
        print(reply.headers['Content-Type'])
        print(reply.content)
        print(reply.json)
        print(reply.json()["name"])
        print(reply.text)
except requests.exceptions.Timeout: 
    print('Ha passat massa temps per connectar') 
except requests.exceptions.InvalidURL:
    print('Adreça desconeguda!')
else:
    print('Here is your data, my Master!') 

## print(requests.codes.__dict__)