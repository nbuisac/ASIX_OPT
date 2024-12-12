n1 = int(input("Entra un número -> "))
n2 = int(input("Entra un altre número -> "))
nn1, nn2 = n1, n2
while nn1 != nn2:
    if nn1 > nn2:
        nn1 = nn1 - nn2
    else:
        nn2 = nn2 - nn1
print(f"mcd({n1}, {n2}) = {nn1}")
