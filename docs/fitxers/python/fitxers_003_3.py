## Amb write
com = "Amb writelines map i with"
print(com.upper())
print(len(com) * "=")
llista = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge"]
with open("exemple_wl3.txt", "wt", encoding="cp850") as f:
    f.writelines(map(lambda a: a + "\n", llista[:5]))