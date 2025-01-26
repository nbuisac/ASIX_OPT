## Amb write
com = "Amb writelines i map"
print(com.upper())
print(len(com) * "=")
llista = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge"]
f = open("exemple_wl2.txt", "wt", encoding="cp850")
f.writelines(map(lambda a: a + "\n", llista))
f.close()