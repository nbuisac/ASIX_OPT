# Python - Exercicis d'iteracions per ASIX - 2

Resol aquests exercicis d'iteracions amb [`for`][for] i/o [`while`][while].

1. **Verifiquem l'estat dels servidors**. Tenim una llista de servidors i el seu estat (online/offline). Mostra només els que estan offline.

    ```python
    # Creem les llistes
    servidors = ["srv-web-01", "srv-db-01", "srv-app-01", "srv-backup-01", "srv-dns-01"]
    estats = ["online", "offline", "online", "offline", "online"]
    ```

    ```txt title="Possible sortida"
    Servidors offline:
    ⚠️  srv-db-01 està offline
    ⚠️  srv-backup-01 està offline
    ```

    ???example "Possible solució"
    
        ```py
        # Creem les llistes
        servidors = ["srv-web-01", "srv-db-01", "srv-app-01", "srv-backup-01", "srv-dns-01"]
        estats = ["online", "offline", "online", "offline", "online"]
        print("Servidors offline:")
        for i in range(len(servidors)):
            if estats[i] == "offline":
                print(f"  ⚠️  {servidors[i]} està {estats[i]}")
        ```

2. **Calculem l'ús mitjà de CPU**. Tenim els percentatges d'ús de CPU de diversos servidors. Calcula la mitjana.

    ```py
    # Creem la llista
    us_cpu = [45.2, 78.5, 23.0, 91.3, 56.7, 34.2, 88.9]  # Percentatges
    ```

    ```txt title="Possible sortida"
    Ús mitjà de CPU: 59.69%
    ```

    ???example "Possible solució"

        ```py
        # Creem la llista
        us_cpu = [45.2, 78.5, 23.0, 91.3, 56.7, 34.2, 88.9]  # Percentatges

        # Solució
        suma = 0
        for us in us_cpu:
            suma += us

        mitjana = suma / len(us_cpu)
        print(f"Ús mitjà de CPU: {mitjana:.2f}%")
        ```

3. **Filtrem IPs d'una xarxa**. Tenim una llista d'adreces IP i volem trobar només les de la xarxa `192.168.1.x`.

    ```py
    # Creem la llista
    ips = ["192.168.1.10", "10.0.0.5", "192.168.1.25", "172.16.0.1", 
        "192.168.1.100", "8.8.8.8", "192.168.2.5"]
    ```

    ```txt title="Possible sortida"
    IPs de la xarxa 192.168.1.x:
    ✓ 192.168.1.10
    ✓ 192.168.1.25
    ✓ 192.168.1.100
    ```

    ???example "Possible solució"

        ```py
        # Creem la llista
        ips = ["192.168.1.10", "10.0.0.5", "192.168.1.25", "172.16.0.1", 
            "192.168.1.100", "8.8.8.8", "192.168.2.5"]

        # Solució
        print("IPs de la xarxa 192.168.1.x:")
        for ip in ips:
            if ip[:10] == "192.168.1.":
                print(f"  ✓ {ip}")
        ```

4. **Comptem intents d'accés fallits**. Registre d'intents de login. Compta quants han estat fallits (més de 3 intents).

    ```py
    # Creem la llista (usuari, intents_fallits)
    intents_login = [
        ["admin", 1],
        ["root", 5],
        ["usuari1", 0],
        ["guest", 7],
        ["admin", 2],
        ["test", 4]
    ]
    ```

    ```txt title="Possible sortida"
    ⚠️  Usuari root té 5 intents fallits
    ⚠️  Usuari guest té 7 intents fallits
    ⚠️  Usuari test té 4 intents fallits

    Total d'usuaris sospitosos: 3
    ```

    ???example "Possible solució"

        ```py
        # Creem la llista (usuari, intents_fallits)
        intents_login = [
            ["admin", 1],
            ["root", 5],
            ["usuari1", 0],
            ["guest", 7],
            ["admin", 2],
            ["test", 4]
        ]

        # Solució
        sospitosos = 0
        for registre in intents_login:
            usuari = registre[0]
            intents = registre[1]
            if intents > 3:
                print(f"⚠️  Usuari {usuari} té {intents} intents fallits")
                sospitosos += 1

        print(f"\nTotal d'usuaris sospitosos: {sospitosos}")
        ```

5. **Verifiquem ports oberts**. Tenim una llista de ports i volem saber **quins** estan entre els perillosos (1-1024).

    ```py
    # Creem la llista
    ports_oberts = [22, 80, 443, 3306, 8080, 21, 23, 25]
    ```

    ```txt title="Possible sortida"
    Ports oberts perillosos (<=1024): [22, 80, 443, 21, 23, 25]
    Total de ports perillosos oberts: 6
    ```

    ???example "Possible solució"

        ```py
        # Creem la llista
        ports_oberts = [22, 80, 443, 3306, 8080, 21, 23, 25]

        # Solució
        ports_perillosos = []
        for port in ports_oberts:
            if port <= 1024:
                ports_perillosos.append(port)

        print(f"Ports oberts perillosos (<=1024): {ports_perillosos}")
        print(f"Total de ports perillosos oberts: {len(ports_perillosos)}")
        ```

6. **Generem la configuració de VLANs**. Genera la configuració de VLANs per a un switch donada una llista de IDs.

    ```py
    # Creem la llista
    vlan_ids = [10, 20, 30, 40, 50]
    vlan_noms = ["VLAN_VENDES", "VLAN_MARQUETING", "VLAN_IT", "VLAN_RRHH", "VLAN_INVITATS"]
    ```

    La sortida que s'espera de cada VLAN és la següent:

    ```txt title="Exemple de configuració de la primera VLAN"
    vlan 10
        name VLAN_VENDES
    !
    ```

    ```txt title="Possible sortida"
    Configuració de VLANs:
    ==============================
    vlan 10
            name VLAN_VENDES
    !
    vlan 20
            name VLAN_MARQUETING
    !
    vlan 30
            name VLAN_IT
    !
    vlan 40
            name VLAN_RRHH
    !
    vlan 50
            name VLAN_INVITATS
    !
    ```

    ???example "Possible solució"

        ```py
        # Creem la llista
        vlan_ids = [10, 20, 30, 40, 50]
        vlan_noms = ["VLAN_VENDES", "VLAN_MARQUETING", "VLAN_IT", "VLAN_RRHH", "VLAN_INVITATS"]

        # Solució
        print("Configuració de VLANs:")
        print("=" * 30)
        for i in range(len(vlan_ids)):
            print(f"vlan {vlan_ids[i]}")
            print(f"\tname {vlan_noms[i]}")
            print("!")
        ```

7. **Monitoritzem la temperatura dels racks**. Crea una alerta si alguna temperatura de rack supera el llindar de 30°C.

    ```py
    # Creem la llista (rack_id, temperatura)
    temperatures = [
        ["RACK-A1", 28.5],
        ["RACK-A2", 31.2],
        ["RACK-B1", 26.0],
        ["RACK-B2", 33.5],
        ["RACK-C1", 29.8]
    ]
    ```

    ```txt title="Possible sortida"
    🔥 ALERTA: RACK-A2 a 31.2°C (supera 30.0°C)
    🔥 ALERTA: RACK-B2 a 33.5°C (supera 30.0°C)

    Total d'alertes: 2
    ```

    ???example "Possible solució"

        ```py
        # Creem la llista (rack_id, temperatura)
        temperatures = [
            ["RACK-A1", 28.5],
            ["RACK-A2", 31.2],
            ["RACK-B1", 26.0],
            ["RACK-B2", 33.5],
            ["RACK-C1", 29.8]
        ]

        # Solució
        LLINDAR = 30.0
        alertes = 0

        for rack in temperatures:
            nom = rack[0]
            temp = rack[1]
            if temp > LLINDAR:
                print(f"🔥 ALERTA: {nom} a {temp}°C (supera {LLINDAR}°C)")
                alertes += 1

        if alertes == 0:
            print("✓ Totes les temperatures són normals")
        else:
            print(f"\nTotal d'alertes: {alertes}")
        ```

8. **Processem logs de firewall**. Compta quantes vegades apareix cada tipus d'acció (_ALLOW_/_DENY_) en els logs. Indica el nombre de _ALLOW_, el nombre de _DENY_ i el _% de DENY_ respecte del total.

    ```py
    # Creem la llista
    logs_firewall = [
        "ALLOW 192.168.1.10 -> 8.8.8.8:53",
        "DENY 10.0.0.5 -> 192.168.1.1:22",
        "ALLOW 192.168.1.25 -> 172.217.0.46:443",
        "DENY 172.16.0.1 -> 192.168.1.10:3389",
        "ALLOW 192.168.1.100 -> 13.107.42.14:443",
        "DENY 192.168.1.50 -> 192.168.1.1:23"
    ]
    ```

    ```txt title="Possible sortida"
    Connexions permeses (ALLOW): 3
    Connexions denegades (DENY): 3
    Ratio de bloqueig: 50.0%
    ```

    ???example "Possible solució"
    
        ```py
        # Creem la llista
        logs_firewall = [
            "ALLOW 192.168.1.10 -> 8.8.8.8:53",
            "DENY 10.0.0.5 -> 192.168.1.1:22",
            "ALLOW 192.168.1.25 -> 172.217.0.46:443",
            "DENY 172.16.0.1 -> 192.168.1.10:3389",
            "ALLOW 192.168.1.100 -> 13.107.42.14:443",
            "DENY 192.168.1.50 -> 192.168.1.1:23"
        ]

        # Solució
        allow_count = 0
        deny_count = 0

        for log in logs_firewall:
            paraula = log.split()[0]
            if paraula == "ALLOW":
                allow_count += 1
            elif paraula == "DENY":
                deny_count += 1

        print(f"Connexions permeses (ALLOW): {allow_count}")
        print(f"Connexions denegades (DENY): {deny_count}")
        print(f"Ratio de bloqueig: {deny_count/(allow_count+deny_count)*100:.1f}%")
        ```

9. **Assignem IPs estàtiques a dispositius**: Assigna IPs d'un rang a una llista de dispositius de xarxa. Les adreces que anirem assignant seran de la xarxa `192.168.1.0/24`, a partir de la _10_. Mostra una llista amb el nom del dispositiu i la IP assignada.

    ```py
    # Creem les llistes
    dispositius = ["router-principal", "switch-core", "ap-wifi-01", "ap-wifi-02", "nas-backup"]
    ```

    ```txt title="Possible sortida"
    Assignacions d'IP:
    ------------------------------
    router-principal     -> 192.168.1.10
    switch-core          -> 192.168.1.11
    ap-wifi-01           -> 192.168.1.12
    ap-wifi-02           -> 192.168.1.13
    nas-backup           -> 192.168.1.14
    ```

    ???example "Possible solució"

        ```py
        # Creem les llistes
        dispositius = ["router-principal", "switch-core", "ap-wifi-01", "ap-wifi-02", "nas-backup"]
        ip_base = "192.168.1."
        ip_inicial = 10

        # Solució
        assignacions = []
        for i in range(len(dispositius)):
            ip_completa = ip_base + str(ip_inicial + i)
            assignacions.append([dispositius[i], ip_completa])

        print("Assignacions d'IP:")
        print("-" * 30)
        for assignacio in assignacions:
            print(f"{assignacio[0]:20} -> {assignacio[1]}")
        ```

10. **Backup de configuracions**. Verifica quins equips tenen backup actualitzat (< 7 dies) i quins no. Ves mostrant una llista de l'estat de cada equip: _OK_ o _PENDENT_ i al final la llista de tots els PENDENTs.

    ```py
    # Creem la llista (equip, dies_desde_ultim_backup)
    backups = [
        ["router-cisco-01", 2],
        ["switch-hp-core", 5],
        ["firewall-paloalto", 12],
        ["switch-acces-01", 1],
        ["router-cisco-02", 8],
        ["wifi-controller", 3]
    ]
    ```

    ```txt title="Possible sortida"
    ✓ router-cisco-01: backup fa 2 dies [OK]
    ✓ switch-hp-core: backup fa 5 dies [OK]
    ✗ firewall-paloalto: backup fa 12 dies [PENDENT]
    ✓ switch-acces-01: backup fa 1 dies [OK]
    ✗ router-cisco-02: backup fa 8 dies [PENDENT]
    ✓ wifi-controller: backup fa 3 dies [OK]

    Resum:
        Equips actualitzats: 4
        Equips pendents: 2
        Llista pendents: firewall-paloalto, router-cisco-02
    ```

    ???example "Possible solució"

        ```py
        # Creem la llista (equip, dies_desde_ultim_backup)
        backups = [
            ["router-cisco-01", 2],
            ["switch-hp-core", 5],
            ["firewall-paloalto", 12],
            ["switch-acces-01", 1],
            ["router-cisco-02", 8],
            ["wifi-controller", 3]
        ]

        # Solució
        DIES_MAXIMS = 7
        actualitzats = []
        pendents = []
        algun_pendent = False

        for equip in backups:
            nom = equip[0]
            dies = equip[1]
            if dies <= DIES_MAXIMS:
                actualitzats.append(nom)
                print(f"✓ {nom}: backup fa {dies} dies [OK]")
            else:
                algun_pendent = True
                pendents.append(nom)
                print(f"✗ {nom}: backup fa {dies} dies [PENDENT]")

        print(f"\nResum:")
        print(f"\tEquips actualitzats: {len(actualitzats)}")
        print(f"\tEquips pendents: {len(pendents)}")
        if algun_pendent:
            print(f"\tLlista pendents: {', '.join(pendents)}")
        ```

11. **Monitoratge de serveis amb reconnexió automàtica**: Ets l'administrador d'un data center. Tens una llista de serveis crítics que cal monitoritzar. El sistema ha de:

    * Inicialment assignarem de forma aleatòria l'estat `offline` a alguns processos. `#!py if random.random() < 0.4:`

    * Després anirem iterant mentre hi hagi algun servei `offline`. Ens aturarem quan hagem trobat TOTS els serveis `online`

        * Comprovarem l'estat de cada servei
    
        * Si està caigut, intentarem reiniciar-lo (màxim 3 intents). Amb una probabilitat del 70% el posarem a estat `online`
    
        * Si esgotem els intents (3), passem a mode degradat i alertem
    
        * Continuem monitoritzant fins que tots els serveis estiguin estables o en mode degradat

    !!!note "Simulem el nou estat, després de reiniciar el sistema amb un valor aleatori."

    ```py
    # ============================================================
    # CREEM LES DADES INICIALS
    # ============================================================

    serveis = [
        {"nom": "Apache Web Server", "port": 80, "estat": "online", "intents_reinici": 0},
        {"nom": "MySQL Database", "port": 3306, "estat": "online", "intents_reinici": 0},
        {"nom": "DNS Bind", "port": 53, "estat": "online", "intents_reinici": 0},
        {"nom": "Correu Postfix", "port": 25, "estat": "online", "intents_reinici": 0},
        {"nom": "Monitor Zabbix", "port": 10050, "estat": "online", "intents_reinici": 0}
    ]
    ```

    ```txt title="Possible sortida"
    ============================================================
    SISTEMA DE MONITORATGE DE SERVEIS - DATA CENTER
    ============================================================
    Serveis a monitoritzar: 5
    Estat inicial: 3 online, 2 offline
    ============================================================

    --- CICLE DE MONITORATGE #1 ---
    ✓ Apache Web Server (port 80): OPERATIU
    ✓ MySQL Database (port 3306): OPERATIU
    ✓ DNS Bind (port 53): OPERATIU
    ⚠️  Correu Postfix (port 25): CAIGUT!
        Intent de reinici #1/3...
        ✗ Reinici fallit. Esperant 2s...
    ⚠️  Monitor Zabbix (port 10050): CAIGUT!
        Intent de reinici #1/3...
        ✗ Reinici fallit. Esperant 2s...

    Resum cicle: 3 online | 2 offline | 0 degradats

    --- CICLE DE MONITORATGE #2 ---
    ✓ Apache Web Server (port 80): OPERATIU
    ✓ MySQL Database (port 3306): OPERATIU
    ✓ DNS Bind (port 53): OPERATIU
    ⚠️  Correu Postfix (port 25): CAIGUT!
        Intent de reinici #2/3...
        ✗ Reinici fallit. Esperant 2s...
    ⚠️  Monitor Zabbix (port 10050): CAIGUT!
        Intent de reinici #2/3...
        ✗ Reinici fallit. Esperant 2s...

    Resum cicle: 3 online | 2 offline | 0 degradats

    --- CICLE DE MONITORATGE #3 ---
    ✓ Apache Web Server (port 80): OPERATIU
    ✓ MySQL Database (port 3306): OPERATIU
    ✓ DNS Bind (port 53): OPERATIU
    ⚠️  Correu Postfix (port 25): CAIGUT!
        Intent de reinici #3/3...
        ✗ Reinici fallit. Esperant 2s...
    ⚠️  Monitor Zabbix (port 10050): CAIGUT!
        Intent de reinici #3/3...
        ✗ Reinici fallit. Esperant 2s...

    Resum cicle: 3 online | 2 offline | 0 degradats

    --- CICLE DE MONITORATGE #4 ---
    ✓ Apache Web Server (port 80): OPERATIU
    ✓ MySQL Database (port 3306): OPERATIU
    ✓ DNS Bind (port 53): OPERATIU
    🔴 Correu Postfix: MODE DEGRADAT (intents esgotats)
        → ALERTA: Necessita intervenció manual urgent!
    🔴 Monitor Zabbix: MODE DEGRADAT (intents esgotats)
        → ALERTA: Necessita intervenció manual urgent!

    Resum cicle: 3 online | 0 offline | 2 degradats

    ============================================================
    MONITORATGE FINALITZAT: Sistema en mode degradat parcial
    ============================================================

    📊 INFORME D'INCIDENT (Total cicles: 4)
    ------------------------------------------------------------
    🟢 Apache Web Server         Port: 80     Estat: ONLINE     Intents: 0
    🟢 MySQL Database            Port: 3306   Estat: ONLINE     Intents: 0
    🟢 DNS Bind                  Port: 53     Estat: ONLINE     Intents: 0
    🔴 Correu Postfix            Port: 25     Estat: DEGRADAT   Intents: 3
    🔴 Monitor Zabbix            Port: 10050  Estat: DEGRADAT   Intents: 3
    ------------------------------------------------------------
    Accions pendents:
    → Intervenció manual requerida: Correu Postfix
    → Intervenció manual requerida: Monitor Zabbix
    ```

    ???example "Possible solució"
    
        ```py
        import random  # Per simular comportament real

        # ============================================================
        # CREEM LES DADES INICIALS
        # ============================================================

        serveis = [
            {"nom": "Apache Web Server", "port": 80, "estat": "online", "intents_reinici": 0},
            {"nom": "MySQL Database", "port": 3306, "estat": "online", "intents_reinici": 0},
            {"nom": "DNS Bind", "port": 53, "estat": "online", "intents_reinici": 0},
            {"nom": "Correu Postfix", "port": 25, "estat": "online", "intents_reinici": 0},
            {"nom": "Monitor Zabbix", "port": 10050, "estat": "online", "intents_reinici": 0}
        ]

        # Simulem que alguns serveis fallen aleatòriament per fer l'exercici realista
        random.seed(42)  # Per resultats reproduïbles
        for servei in serveis:
            if random.random() < 0.4:  # 40% probabilitat de fallada
                servei["estat"] = "offline"

        print("=" * 60)
        print("SISTEMA DE MONITORATGE DE SERVEIS - DATA CENTER")
        print("=" * 60)
        print(f"Serveis a monitoritzar: {len(serveis)}")
        print(f"Estat inicial: {sum(1 for s in serveis if s['estat'] == 'online')} online, "
            f"{sum(1 for s in serveis if s['estat'] == 'offline')} offline")
        print("=" * 60)

        # ============================================================
        # VARIABLES DE CONTROL DEL WHILE
        # ============================================================

        MAX_INTENTS = 3           # Intents màxims de reinici per servei
        TEMPS_ESPERA = 2          # Segons simulats entre intents
        cicles_monitoratge = 0    # Comptador de voltes del while
        serveis_estables = False  # Condició de sortida

        # ============================================================
        # BUCLE WHILE PRINCIPAL - Monitoratge continu
        # ============================================================

        while not serveis_estables:
            
            cicles_monitoratge += 1
            print(f"\n--- CICLE DE MONITORATGE #{cicles_monitoratge} ---")
            
            serveis_estables = True  # Assumim que està tot bé fins que provem el contrari
            tots_degradats = True    # Per detectar si tot està en mode degradat
            
            # Iterem amb índex per poder modificar la llista mentre iterem
            i = 0
            while i < len(serveis):
                servei = serveis[i]
                
                # =========================================================
                # CAS 1: Servei ONLINE - només verifiquem
                # =========================================================
                if servei["estat"] == "online":
                    print(f"  ✓ {servei['nom']} (port {servei['port']}): OPERATIU")
                    tots_degradats = False
                    
                # =========================================================
                # CAS 2: Servei OFFLINE - intentem reiniciar
                # =========================================================
                elif servei["estat"] == "offline":
                    serveis_estables = False  # Encara tenim feina a fer
                    
                    if servei["intents_reinici"] < MAX_INTENTS:
                        # Intent de reinici
                        servei["intents_reinici"] += 1
                        print(f"  ⚠️  {servei['nom']} (port {servei['port']}): CAIGUT!")
                        print(f"      Intent de reinici #{servei['intents_reinici']}/{MAX_INTENTS}...")
                        
                        # Simulem el resultat del reinici (70% èxit)
                        exit_reinici = random.random() < 0.7
                        if exit_reinici:
                            servei["estat"] = "online"
                            print(f"      ✓ REINICI EXITÓS! Servei restaurat.")
                            tots_degradats = False
                        else:
                            print(f"      ✗ Reinici fallit. Esperant {TEMPS_ESPERA}s...")
                            # En un entorn real: time.sleep(TEMPS_ESPERA)
                            
                    else:
                        # Esgotats els intents -> Mode degradat
                        servei["estat"] = "degradat"
                        print(f"  🔴 {servei['nom']}: MODE DEGRADAT (intents esgotats)")
                        print(f"      → ALERTA: Necessita intervenció manual urgent!")
                
                # =========================================================
                # CAS 3: Servei DEGRADAT - ja no intentem res
                # =========================================================
                elif servei["estat"] == "degradat":
                    print(f"  🔴 {servei['nom']}: EN MODE DEGRADAT (esperant tècnic)")
                    # Els serveis degradats no impedeixen sortir del while
                    # però tampoc són "estables" del tot
                
                i += 1  # IMPORTANT: Incrementar índex del while intern
            
            # =========================================================
            # CONDICIÓ DE SORTIDA DEL WHILE PRINCIPAL
            # =========================================================
            
            # Comptem estats
            online_count = sum(1 for s in serveis if s["estat"] == "online")
            offline_count = sum(1 for s in serveis if s["estat"] == "offline")
            degradat_count = sum(1 for s in serveis if s["estat"] == "degradat")
            
            print(f"\n  Resum cicle: {online_count} online | {offline_count} offline | {degradat_count} degradats")
            
            # Sortim si no queden serveis offline (només online o degradats)
            if offline_count == 0:
                serveis_estables = True
                print("\n" + "=" * 60)
                if degradat_count > 0:
                    print("MONITORATGE FINALITZAT: Sistema en mode degradat parcial")
                else:
                    print("MONITORATGE FINALITZAT: Tots els serveis operatius")
                print("=" * 60)

        # ============================================================
        # INFORME FINAL
        # ============================================================

        print(f"\n📊 INFORME D'INCIDENT (Total cicles: {cicles_monitoratge})")
        print("-" * 60)

        for servei in serveis:
            estat_icon = "🟢" if servei["estat"] == "online" else "🔴"
            print(f"{estat_icon} {servei['nom']:<25} Port: {servei['port']:<6} "
                f"Estat: {servei['estat'].upper():<10} Intents: {servei['intents_reinici']}")

        print("-" * 60)
        print("Accions pendents:")
        pendents = [s["nom"] for s in serveis if s["estat"] == "degradat"]
        if pendents:
            for p in pendents:
                print(f"  → Intervenció manual requerida: {p}")
        else:
            print("  Cap. Sistema estable.")
        ```


[while]:                https://docs.python.org/reference/compound_stmts.html#the-while-statement       "while"
[for]:                  https://docs.python.org/reference/compound_stmts.html#the-for-statement         "for"

--8<-- ".acronims.txt"
