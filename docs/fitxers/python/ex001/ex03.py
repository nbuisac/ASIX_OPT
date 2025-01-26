f = open("fitxer02.txt", "rt")
quants = 0
suma = 0
numero_str = f.readline()
## Per si el fitxer estigués buit fem el següent en un if
if numero_str != "":
    if numero_str.strip() != "":
        petit = int(numero_str)
        gran = int(numero_str)
        quants = 1
        suma = gran
    while numero_str != "":
        if numero_str.strip() != "":
            numero = int(numero_str)
            quants = quants + 1
            suma = suma + numero
            if numero > gran:
                gran = numero
            elif numero < petit:
                petit = numero
            numero_str = f.readline()
    print(f"El número més petit és {petit}")
    print(f"El número més gran és {gran}")
    print(f"La mitjana és {round(suma / quants, 2)}")
f.close()