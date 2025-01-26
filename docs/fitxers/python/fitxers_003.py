## Amb write
com = "Amb write"
print(com.upper())
print(len(com) * "=")
f = open("exemple_w.txt", "wt", encoding="cp850")
for a in ["primera", "segona", "tercera", "quarta", "cinquena"]:
    q = f.write(a + " línia" + "\n")
    print(f"Escrits {q} caràcters, inclós el salt de línia")
f.close()
