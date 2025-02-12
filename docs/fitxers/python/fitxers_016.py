import random
import time
MAXIM = 100
MINIM = 1
def demana_numero(des_de = 1, fins_a = 10):
    n = input(f"Entra un Numero ({des_de}..{fins_a} -> ")
    while not n.isdigit() or int(n) < des_de or int(n) > fins_a:
        n = input(f"ERROR: Entra un Numero ({des_de}..{fins_a} -> ")
    return int(n)

nom = input("Entra el teu nom -> ")
numero_a_encertar = random.randint(MINIM, MAXIM)
temps_inicial = time.time()
numero = demana_numero(MINIM, MAXIM)
intents = 1
while numero != numero_a_encertar:
    print("Noooooooooo!!!!", end=" ")
    if  numero_a_encertar < numero:
        print("és més petit")
    else:
        print("és més gran")
    numero = demana_numero(MINIM, MAXIM)
    intents += 1
temps_final = time.time()
segons = temps_final - temps_inicial
print(f"Correcte, l'has encertat en {intents} intents i en {segons} segons")

try:
    nom_fitxer = "puntuacions.txt"
    fi = open(nom_fitxer, "a")
    fi.write(f"{nom}:{MINIM}:{MAXIM}:{numero_a_encertar}:{intents}:{segons}\n")
    fi.close()
except FileNotFoundError as e:
    print(f"ERROR: Fitxer {nom_fitxer} no trobat. ({e})")
except Exception as e:
    print(f"ERROR: Error no tractat. ({e})")
