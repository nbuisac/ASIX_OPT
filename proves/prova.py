suma = 0
quants = 0
numero = float(input("Entra un nombre (0 per acabar) -> "))
while numero != 0:
    quants += 1
    suma += numero
    numero = float(input("Entra un nombre (0 per acabar) -> "))
print(f"La mitjana és {suma/quants}")