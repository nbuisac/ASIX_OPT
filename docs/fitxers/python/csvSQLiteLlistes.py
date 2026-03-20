import csv
import sqlite3

llista_inserts = []
llista_descartades = []
with open("dades_vendes.csv", encoding="utf8") as f:
    lector = csv.DictReader(f)
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

            # Afegim les dades a la llista
            llista_inserts.append((id_comanda, producte, total, estat))

        except Exception as e:
            # Afegim les dades no carregades
            llista_descartades.append(linia)

columnes_log = ["id", "producte", "preu", "quantitat"]
with open("vendes_no_carregades.csv", "wt", encoding="utf8", newline="") as fs:
    escriptor = csv.DictWriter(fs, columnes_log, extrasaction='ignore')
    escriptor.writeheader()
    # Escrivim les dades no carregades amb un writerows
    escriptor.writerows(llista_descartades)

try:
    conn = sqlite3.connect("gestio_vendes.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS comanda 
                (id INTEGER PRIMARY KEY, producte TEXT, total REAL, estat TEXT)''')
    if len(llista_inserts) > 0:
        sql_insert = "INSERT OR IGNORE INTO comanda(id, producte, total, estat) VALUES(?,?,?,?)"
        # executemany permet executar molts INSERT en una sola comanda
        conn.executemany(sql_insert, llista_inserts)
        conn.commit()

    sql = "SELECT COUNT(*) q FROM comanda"
    resultat = conn.execute(sql)
    # Recollim una sola fila
    q = resultat.fetchone()
    conn.close()
    print(f"Tenim {q[0]} comandes a la base de dades")
except sqlite3.Error as e:
    print(f"Error de base de dades: {e}")
