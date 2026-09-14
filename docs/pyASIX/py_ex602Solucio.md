# Exercicis Pràctics: JSON i XML

## Exercici 1: Gestor de Configuració JSON

Imagina que tenim un fitxer `network_settings.json` amb la següent informació de xarxa:

```json
{
    "interficie": "eth0",
    "dhcp": false,
    "ip": "192.168.1.100",
    "dns_servers": ["8.8.8.8", "1.1.1.1"]
}
```

Fes un script en Python que:

1. Llegeixi el fitxer `network_settings.json`.

1. Canviï el valor de "_dhcp_" a `#!py True`.

1. Afegeixi un nou servidor DNS _`"9.9.9.9"`_ a la llista "_`dns_servers`_".

1. Guardi les modificacions en un nou fitxer anomenat `network_settings_updated.json` ben formatat (`#!py indent=4`).

???example "Possible Solució"

    ```py
    import json

    # 1. Llegir el fitxer JSON
    with open("network_settings.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    # 2. Modificar dades
    config["dhcp"] = True

    # 3. Afegir nou DNS a la llista
    config["dns_servers"].append("9.9.9.9")

    # 4. Guardar en un nou fitxer
    with open("network_settings_updated.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

    print("Configuració actualitzada guardada correctament.")
    ```

## Exercici 2: Parser de Fitxer de Serveis XML

Crea un fitxer fictici anomenat `services.xml` amb la llista de serveis del sistema:

```xml
<services>
    <service name="apache2">
        <port>80</port>
        <status>active</status>
    </service>
    <service name="ssh">
        <port>22</port>
        <status>active</status>
    </service>
    <service name="ftp">
        <port>21</port>
        <status>inactive</status>
    </service>
</services>
```

Fes un script en Python que:

1. Llegeixi i analitzi el fitxer `services.xml` utilitzant `ElementTree`.

1. Recorri tots els serveis i mostri només els nom dels serveis que estiguin actius (`<status>active</status>`) juntament amb el seu port.

???example "Possible Solució"

    ```py
    import xml.etree.ElementTree as ET

    # 1. Carregar el fitxer XML
    tree = ET.parse("services.xml")
    root = tree.getroot()

    print("=== SERVEIS ACTIUS AL SISTEMA ===")

    # 2. Recórrer cada servei
    for servei in root.findall("service"):
        nom = servei.attrib.get("name")
        port = servei.find("port").text
        estat = servei.find("status").text
        
        # Comprovar si està actiu
        if estat == "active":
            print(f" Servei '{nom}' actiu escoltant al port {port}.")
    ```


--8<-- ".acronims.txt"
