# Python

## Mapejant paquets de Python

Podem instal·lar, actualitzar i eliminar paquets usant un programa anomenat **`pip`**. Per defecte, `pip` instal·larà paquets des de l'[Índex de Paquets de Python] . Podeu navegar per l'índex de paquets de Python anant-hi al vostre navegador web.

!!!tip "Pot resultar complicat trobar el que busquem entre tantes opcions, però..."

**`pip`** té diverses subordres: `install`, `uninstall`, `freeze`, etc. Podem consultar la guia [Instal·lant mòduls de Python] per obtenir la documentació completa de `pip`.

### Ús bàsic

Les eines estàndard d'empaquetatge estan dissenyades perquè es facin servir des de la línia d'ordres.

La següent ordre instal·larà la darrera versió d'un mòdul i les seves dependències des de l'Índex de Paquets de Python:

```bash
python -m pip install AlgunPaquet
```

És possible especificar una versió exacta o mínima directament a la línia d'ordres. Quan s'utilitzi un operand comparador com **>**, **<** o qualsevol altre caràcter especial que pot ser interpretat per l'intèrpret de comandes, el nom del paquet i la versió han d'anar entre cometes dobles:

```bash
python -m pip install AlgunPaquet==1.0.4    # versió específica
python -m pip install "AlgunPaquet>=1.0.4"  # versió mínima
```

Normalment, si ja hi ha instal·lat un mòdul adequat, intentar instal·lar-lo una altra vegada no tindrà cap efecte. **Actualitzar** mòduls existents requereix que se sol·liciti explícitament:

```bash
python -m pip install --upgrade AlgunPaquet
```

### Instal·lant mòduls per l'usuari actual

Si la instal·lació de Python és a nivell de sistema, la instal·lació d'un mòdul per defecte serà efectiva per a tots els usuaris. Passant la opció **`--user`**, instal·larem el paquet únicament per a l'usuari actual, en lloc de fer-ho per a tots els usuaris del sistema.

!!!note "Aquesta opció no està permesa dins un entorn virtual"


[Índex de Paquets de Python]:   https://pypi.org/    "Índex de Paquets de Python"
[Instal·lant mòduls de Python]: https://docs.python.org/3/installing/index.html#installing-index    "Instal·lant mòduls de Python"

--8<-- ".acronims.txt"
