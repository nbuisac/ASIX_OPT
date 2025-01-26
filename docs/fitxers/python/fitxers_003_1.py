## Amb write
com = "Amb writelines"
print(com.upper())
print(len(com) * "=")
llista = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge"]
f = open("exemple_wl.txt", "wt", encoding="cp850")
f.writelines(llista)
f.close()