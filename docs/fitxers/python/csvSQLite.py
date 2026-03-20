import csv
import sqlite3

with open("vendes_no_carregades.csv", "wt", encoding="utf8", newline="") as fs:
    escriptor = csv.DictWriter(fs, ["id", "producte", "preu", "quantitat"])
    escriptor.writeheader()
    with open("dades_vendes.csv", encoding="utf8") as f:
        lector = csv.DictReader(f)
        conn = sqlite3.connect("gestio_vendes.db")
        conn.execute('''CREATE TABLE IF NOT EXISTS comanda 
                    (id INTEGER PRIMARY KEY, producte TEXT, total REAL, estat TEXT)''')
        for linia in lector:
            try:
                # Extracció i conversió
                id_comanda = int(linia["id"])
                producte = linia["producte"].strip()
                preu = float(linia["preu"])
                quantitat = int(linia["quantitat"])

                # Lògica de negoci
                total = round(preu * quantitat, 2)
                if total > 500:
                    estat = "PREMIUM"
                else:
                    estat = "STANDARD"
                sql_insert = "INSERT INTO comanda(id, producte, total, estat) VALUES(?,?,?,?)"
                conn.execute(sql_insert, (id_comanda, producte, total, estat))
                
            except Exception as e:
                print(f"Error en carregar les dades: {linia}")
                escriptor.writerow(linia)
        conn.commit()
        sql = "SELECT COUNT(*) q FROM comanda"
        resultat = conn.execute(sql)
        q = resultat.fetchone()
        conn.close()
        print(f"Tenim {q[0]} comandes al a base de dades")
    
