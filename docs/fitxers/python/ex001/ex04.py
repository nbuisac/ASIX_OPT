import random
QUANTIAT = 1000000
def genera_combinacio():
    combi = []
    while len(combi) < 6:
        n = random.randint(1, 49)
        if n in combi:
            continue
        combi.append(n)
    return combi

f = open("fitxer04.txt", "wt")
q = 0
while q < QUANTIAT:
    combinacio = genera_combinacio()
    combinacio.sort()
    for n in combinacio:
        f.write(str(n) + " ")
    f.write("\n")
    q = q + 1

f.close()