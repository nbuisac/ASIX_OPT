# Exercicis Pràctics: Fitxers i CSV

## Exercici 1: Filtre i Anàlisi de Log d'Errors

Descarrega o crea un fitxer fictici anomenat `app.log` amb el contingut següent:

```txt
[2026-03-10 08:00:12] INFO - Inici de la connexió
[2026-03-10 08:01:45] WARNING - Temps de resposta alt
[2026-03-10 08:03:10] ERROR - Fallada en la connexió a la BD
[2026-03-10 08:05:00] INFO - Petició rebuda
[2026-03-10 08:06:22] ERROR - Espai en disc insuficient
```

Fes un script que:

1. Llegeixi el fitxer `app.log` línia per línia.

1. Compti quantes línies contenen la paraula "_`ERROR`_".

1. Guardi només les línies d'error en un nou fitxer anomenat `errors_critics.txt`.

1. Mostri per pantalla: "_`S'han trobat [X] errors i s'han guardat a 'errors_critics.txt'.`_"

## Exercici 2: Generador de Comptes d'Usuari des de CSV

Imagina que l'equip de Recursos Humans et proporciona el fitxer `nous_empleats.csv` (separat per comes) amb el nom i el departament dels nous treballadors:

```txt
nom,cognom,departament
Marta,Rovira,Sistemes
Joan,García,Xarxes
Laia,Font,Desenvolupament
```

Fes un script que:

1. Llegeixi el fitxer `nous_empleats.csv` fent servir `#!py csv.DictReader`.

1. Generi un nom d'usuari per a cada empleat seguint la regla: **primera lletra del nom en minúscula + cognom en minúscula** (Ex: _`mrovira`_).

1. Generi un nou fitxer `usuaris_creats.csv` (separat per punt i coma ;) amb les columnes: `username`, `departament`.



--8<-- ".acronims.txt"
