def demana_numero():
    while True:
        try:
            n = int(input("Entra un número enter -> "))
            if n == -1 or n > 0:
                return n
        except Exception:
            pass

f = open("fitxer02.txt", "wt")
n = demana_numero()
while n != -1:
    f.write(str(n) + "\n")
    n = demana_numero()
f.close()