# Python - Exercicis de fitxers ASIX

Resol aquests exercicis de fitxers amb llenguatge Python

## Exercicis de LECTURA (Anàlisi de dades)

L'objectiu és extreure informació útil d'un fitxer ja existent.

1. **L'analitzador de `/etc/passwd`**:

    Enunciat: Crea un script que llegeixi un fitxer (simulant el format del `/etc/passwd` de Linux: usuari: x :UID:GID:...). El programa ha de mostrar per pantalla només els noms d'usuari i el seu directori "home" (camp 6).

2. **Cercador d'Errors als Logs**:

    Enunciat: Donat un fitxer de log d'un servidor web (per exemple access.log), llegeix-lo i compta quantes línies contenen l'error "404" (pàgina no trobada) i quantes l'error "500" (error de servidor).

## Exercicis d'ESCRIPTURA (Generació de configuracions)

L'objectiu és automatitzar la creació de fitxers de sistema o informes.

1. **Generador de fitxer `/etc/hosts`**:

    Enunciat: Tenim una llista de tuples amb noms de servidors i les seves IPs: `[("web1", "10.0.0.1"), ("db1", "10.0.0.2")]`. Crea un fitxer anomenat `hosts_nou.txt` que tingui el format estàndard: _IP Hostname_.

2. **Còpia de Seguretat de Llista de Paquets**:

    Enunciat: Demana a l'usuari noms de paquets de programari que vulgui instal·lar fins que escrigui *"fi"*. Guarda tots aquests noms en un fitxer anomenat `paquets_a_instal·lar.txt`, un per cada línia.

## Exercicis de LECTURA i ESCRIPTURA (Processament)

Aquests són els més realistes: llegir, modificar i guardar el resultat.

1. **Neteja de comentaris en fitxers `.conf`**:

    Enunciat: Els fitxers de configuració solen estar plens de línies que comencen per **`#`** (_comentaris_). Llegeix un fitxer de configuració (ex: `ssh_config`) i crea un fitxer nou anomenat `ssh_config_clean.txt` que contingui exactament el mateix però sense les línies de comentari ni les línies buides.

2. **Anonimitzador de IPs**:

    Enunciat: Per motius de privacitat (*RGPD*), t'han demanat que llegeixis un fitxer de logs amb adreces IP i en generis un de nou on els últims dos octets de cada IP estiguin ocults (ex: `192.168.1.45 -> 192.168.X.X`).

    En aquest exercici podem obrir els dos fitxers amb un sol `with`.

3. **El Generador de Configuracions (Combinar Correspondència)**

    L'objectiu és crear un script que generi fitxers personalitzats a partir d'una plantilla i un fitxer de dades.

        ```txt title="plantilla 1"
        Hola {nom},
        La teva adreça IP serà {ip} i el teu servidor DNS és {dns}.
        Si us plau, configura el teu equip {equip}.
        ```

        ```txt title="plantilla 2"
        Hola {0},
        La teva adreça IP serà {1} i el teu servidor DNS és {2}.
        Si us plau, configura el teu equip {3}.
        ```

    2. Fitxer `dades.csv`: Un fitxer amb els valors separats per comes (una línia per cada fitxer a generar):

        ```txt
        nom,ip,dns,equip
        Pere,192.168.1.10,8.8.8.8,PC-01
        Marta,192.168.1.11,1.1.1.1,PC-02
        Joan,192.168.1.12,8.8.4.4,PC-03
        ```
    
    3. **Resultat**: El programa ha de crear un fitxer per a cada persona (ex: Pere01.txt, Marta02.txt) amb la informació substituïda.

    ???example "Possible solució"

        ```py
        def generar_correspondencia():
            # 1. Llegim la plantilla i la guardem en una variable
            with open("plantilla.txt", "rt", encoding="utf-8") as f_plantilla:
                contingut_plantilla = f_plantilla.read()

            # 2. Llegim el fitxer de dades
            with open("dades.csv", "rt", encoding="utf-8") as f_dades:
                # Llegim la primera línia per saber quins són els encapçalaments (camps)
                encapçalaments = f_dades.readline().strip().split(",")
                
                # Processem cada línia de dades restant
                for linia in f_dades:
                    valors = linia.strip().split(",")
                    
                    # Creem un diccionari que relacioni el camp amb el seu valor
                    # Ex: {'nom': 'Pere', 'ip': '192.168.1.10', ...}
                    dades_dict = dict(zip(encapçalaments, valors))
                    
                    # Plantilla 1
                    # Substituïm les claus de la plantilla pels valors del diccionari
                    contingut_final = contingut_plantilla.format(**dades_dict)
                    # Una altra solució per la plantilla 1
                    # Assignem cada posició a una variable clara
                    v_nom = valors[0]
                    v_ip = valors[1]
                    v_dns = valors[2]
                    v_equip = valors[3]
                    # Plantilla 2
                    contingut_final = contingut_plantilla.format(valors[0], valors[1], valors[2]) # plantilla 2
                    
                    # Ara sí que podem fer el .format() usant aquests noms
                    contingut_final = contingut_plantilla.format(nom=v_nom, ip=v_ip, dns=v_dns, equip=v_equip)
                    
                    # 3. Escrivim el fitxer de sortida personalitzat
                    nom_fitxer = f"{dades_dict['nom']}{dades_dict['equip[-2:]']}.txt"
                    with open(nom_fitxer, "wt", encoding="utf-8") as f_sortida:
                        f_sortida.write(contingut_final)
                        
                    print(f"Generat el fitxer per a: {dades_dict['nom']}")

        # Executem la funció
        generar_correspondencia()
        ```


--8<-- ".acronims.txt"
