##
## Caràcter a caràcter
##
com = "Caràcter a caràcter"
print(com.upper())
print(len(com) * "=")
f = open("exemple.txt", encoding="cp850")
caracter = f.read(1)
while caracter != '':
    print(caracter, end = "")
    caracter = f.read(1)
print()
# f.close()
##
## Línia a línia
##
com = "Línia a línia"
print(com.upper())
print(len(com) * "=")
f = open("exemple.txt", encoding="cp850")
linia = f.readline()
while linia != '':
    print(linia, end = "")
    linia = f.readline()
print()
# f.close()
##
## Tot de cop
##
com = "Tot de cop"
print(com.upper())
print(len(com) * "=")
f = open("exemple.txt", encoding="cp850")
tot = f.read()
print(tot, end = "")
print()
# f.close()
##
## Tot de cop en una llista
##
com = "Tot de cop en una llista"
print(com.upper())
print(len(com) * "=")
f = open("exemple.txt", encoding="cp850")
linies = list(f.read())
for linia in linies:
    print(linia, end = "")
print()
# f.close()
##
## Totes les línies en una llista
##
com = "Totes les línies en una llista"
print(com.upper())
print(len(com) * "=")
f = open("exemple.txt", encoding="cp850")
linies = f.readlines()
for linia in linies:
    print(linia, end = "")
print()
# f.close()
##
## Línia a línia amb un for
##
com = "Línia a línia amb un for"
print(com.upper())
print(len(com) * "=")
f = open("exemple.txt", encoding="cp850")
for linia in f:
    print(linia, end = "")
print()
# f.close()
##
## Amb with
##
com = "Amb with"
print(com.upper())
print(len(com) * "=")
with open("exemple.txt", encoding="cp850") as f:
    for linia in f:
        print(linia, end = "")
    print()