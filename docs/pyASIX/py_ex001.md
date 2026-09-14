# Exercicis: Entrada de dades, conversió de tipus i Condicionals

## Bloc 1: Exercicis d'Input i Conversió de Tipus (Typecasting)

!!!tip "Recordatori abans de començar:"

    * Utilitza `#!py input()` si demanes text.

    * Utilitza `#!py int(input())` si demanes números enters (sense decimals, com nombre de fitxers, de carpetes o dies).

    * Utilitza `#!py float(input())` si demanes números amb decimals (como gigabytes, velocitats o el temps que triga a carregar una web).

1.1. _El calculador d'espai per a còpies (Backups)_

Quan fem còpies de seguretat dels ordinadors de l'institut, l'espai es mesura, amb decimals, en Gigabytes. Fes un script que demani a l'administrador:

* El nom del servidor del qual fem la còpia.

* Quants GB ocupa la còpia de seguretat actual (pot tenir decimals, ex: 4.5).

El programa ha de calcular quant espai necessitarem si volem guardar tres còpies exactes d'aquell servidor i mostrar el resultat final per pantalla amb un missatge clar.

**Per fer més**: Podem donar les dades en GB i també en MB. Recorda que 1GB = 1000MB

1.2. _Repartiment de memòria RAM_

Imagina que tenim un ordinador central a l'aula amb una quantitat de memòria RAM, en un valor enter (ex: 16 o 32 Gigabytes). Fes un script que demani de forma interactiva:

* Quants GB de memòria RAM té el servidor en total (número enter).

* Entre quantes màquines virtuals d'alumnes s'ha de repartir de manera equivalent.

El programa ha de calcular i mostrar quants GB de RAM li tocaran a la màquina de cada alumne.

**Compte**: Tot i que la RAM total sigui entera, el resultat de la divisió pot donar decimals!

## Bloc 2: Exercicis amb Condicionals (`#!py if`, `#!py elif`, `#!py else`)

2.1: _El detector de webs lentes_

Com a administradors, hem de controlar que les pàgines web de la nostra empresa carreguin ràpidament. Fes un script que demani a l'usuari el temps de càrrega d'una web en segons (utilitza `#!py float` perquè pot trigar 1.5 segons, 0.8 segons, etc.).

El programa ha de prendre una decisió segons el temps introduït:

* Si triga menys de 1.0 segon, ha de mostrar: "_La web va genial! Rendiment òptim._"

* Si triga entre 1.0 i 3.0 segons (ambdós inclosos), ha de mostrar: "_Rendiment acceptable, demana una ullada, però funciona._"

* Si triga més de 3.0 segons, ha de mostrar: "_ALERTA: La web va massa lenta! Cal revisar el servidor._"

2.2. _Control de bateries als portàtils de l'aula_

Volem fer un script que s'executi als portàtils dels alumnes de 1r d'ASIX per comprovar si han de connectar el carregador. El programa demanarà el percentatge actual de la bateria (un número enter del 0 al 100).

La lògica del programa ha de ser:

* Si la bateria és igual a 100, mostrarà: "_Bateria completament carregada._"

* Si la bateria és menor o igual que 15, mostrarà: "_ALERTA CRÍTICA: Connecta el carregador immediatament!_"

* Si la bateria és menor o igual que 30 (però més gran de 15), mostrarà: "_Bateria baixa. Guarda la teva feina._"

* En qualsevol altre cas (bateria correcta), mostrarà: "_Nivell de bateria correcte per treballar._"



[print()]:              https://docs.python.org/3/library/functions.html#print  "print()"
[input()]:              https://docs.python.org/3/library/functions.html#input  "input()"


--8<-- ".acronims.txt"
