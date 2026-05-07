---
title: Reserva de Ports
---
# Reserva de Ports

Informació extreta de [Windows 10 forbidden port bind](https://pomeroy.me/2020/09/solved-windows-10-forbidden-port-bind/ "Windows 10 forbidden port bind"){target="_blank"}.

## Contextualització

Al configurar serveis, configurem alguns ports per escoltar-los.De vegades els registrats i d'altres vegades, altres ports que necessitem.
Sovint creiem que Windows ens deixa utilitzar qualsevol port que no tinguem utilitzat, però en algunes ocasions i segons el que tinguem instal·lat, windows es reserva uns ports, de forma aleatòria, i ningú ens asssegura que el port que podem obrir avui el podrem obrir també demà.

Sol solventar-se reiniciant l'ordinador, ja que aquest reserva aleatòriament altres ports, però la millor opció és tenir ja reservats els ports amb els que sovint treballem.

Si executem la següent comanda, en Windows, `netsh interface ipv4 show excludedportrange protocol=tcp` podrem veure els ports que no podrem utilitzar en la sessió.

``` doscon hl_lines="1"
C:\MVD>netsh interface ipv4 show excludedportrange protocol=tcp

Protocolo tcp Intervalos de exclusión de puertos

Puerto de inicio    Puerto final
----------          --------
      1898        1997
      1998        2097
      2180        2279
     50000       50059     *

* - Exclusiones de puertos administrados.
```

Aquests rangs de ports que ara són del 1898 al 1997, del 1998 al 2097 i del 2180 al 2279 aniran variant cada vegada que reiniem l'ordinador. En algun cas, poden incloure algun port que necessitem utilitzar i llavors ens sortirà un error semblant a

``` doscon
Error: Unable to start container: Error response from daemon: Ports are not available: listen tcp 0.0.0.0:8000: bind: An attempt was made to access a socket in a way forbidden by its access permissions.
```

## Solució

Per evitar-ho el que farem serà reservar els rangs de ports que utilitzarem per tal que Windows **mai els inclogui en aquesta llista**. El que farem serà afegir-los de la mateixa manera que estan els ports de la darrera línia de l'execució de la darrera comanda hl_lines="1-2"
``` apacheconf 
     50000       50059     *
* - Exclusiones de puertos administrados.
```

Per això utilitzarem la comanda `netsh interface ipv4 add excludedportrange ...`

``` doscon
C:\MVD>netsh interface ipv4 add excludedportrange ?

Uso: add excludedportrange [protocol=]tcp|udp
             [startport=]<entero> [numberofports=]<entero>
             [[store=]active|persistent]

Parámetros:

      Etiqueta           Valor
      protocol       - Uno de los valores siguientes:
                       tcp: agrega una exclusión para TCP.
                       udp: agrega una exclusión para UDP.
      startport      - El número de puerto inicial para una exclusión.
      numberofports  - El número de puertos comenzando desde startport
                       para una exclusión.
      store          - Uno de los valores siguientes:
                       active:     configuración solo dura hasta
                                   siguiente arranque.
                       persistent: el cambio es permanente.
                                   Este es el valor predeterminado.

Notas: agrega una exclusión para un bloque consecutivo de puertos.

Ejemplo:

      add excludedportrange protocol=tcp startport=50000 numberofports=20
```

excloent tots aquells ports i/o rang de ports a utilitzar.

!!! Note "Com a administrador"
	Per executar la comanda `netsh interface ipv4 add excludedportrange ...` caldrà haver iniciat la sessió del `cmd` com **Administrador**.

En el nostre cas si volem reservar els ports 8000, 8080, 8888, i del 40000 al 4010. Podem fer-ho amb les següents comandes:


``` doscon
netsh interface ipv4 add excludedportrange protocol=tcp startport=8000 numberofports=1 store=persistent
netsh interface ipv4 add excludedportrange protocol=tcp startport=8080 numberofports=1 store=persistent
netsh interface ipv4 add excludedportrange protocol=tcp startport=8888 numberofports=1 store=persistent
netsh interface ipv4 add excludedportrange protocol=tcp startport=40000 numberofports=11 store=persistent
```

Al posar la opció `persistent` aquesta reserva quedarà per sempre en el nostre PC i per tant no tindrem problemes per a utilitzar aquests ports.

!!! Note "i els ports per defecte dels serveis?"
      Els ports per defecte dels serveis http (80), https (443), ssh (22), ftp (20, 21), etc estan dins el rang dels primers 1024 i no crec que Windows *s'atreveixi* a utilitzar-los. Podem afegir els ports del *mysql (3306)*, *postgreSQL (5432)*, etc.

Amb les següents comandes reservarem els ports *reservats* (20-22, 80 i 443)i els de BD (3306 i 5432).
``` doscon
netsh interface ipv4 add excludedportrange protocol=tcp startport=20 numberofports=3 store=persistent
netsh interface ipv4 add excludedportrange protocol=tcp startport=80 numberofports=1 store=persistent
netsh interface ipv4 add excludedportrange protocol=tcp startport=443 numberofports=1 store=persistent
netsh interface ipv4 add excludedportrange protocol=tcp startport=3306 numberofports=1 store=persistent
netsh interface ipv4 add excludedportrange protocol=tcp startport=5432 numberofports=1 store=persistent
```

I ens assegurem que tenim reservats els ports que voldrem utilitzar algun dia

``` doscon hl_lines="7-9 16-21"
C:\MVD>netsh interface ipv4 show excludedportrange protocol=tcp

Protocolo tcp Intervalos de exclusión de puertos

Puerto de inicio    Puerto final
----------          --------
        20          22     *
        80          80     *
       443         443     *
      1898        1997
      1998        2097
      2180        2279
      2764        2863
      2864        2963
      2964        3063
      3306        3306     *
      5432        5432     *
      8000        8000     *
      8080        8080     *
      8888        8888     *
     40000       40010     *
     50000       50059     *

* - Exclusiones de puertos administrados.
```
## i si vull eliminar alguna exclusió?

De la mateixa manera que es poden afegir rangs d'exclusió de ports, aquests també poden eliminar-se amb la comanda `netsh interface ipv4 delete excludedportrange ...`. En aquest cas **cal eliminar el mateix rang que hem afegit**, i si cal, després podràs afegir ports d'un en un o en altres intervals.

``` doscon
C:\MVD>netsh interface ipv4 delete excludedportrange ?

Uso: delete excludedportrange [protocol=]tcp|udp
             [startport=]<entero> [numberofports=]<entero>
             [[store=]active|persistent]

Parámetros:

      Etiqueta           Valor
      protocol       - Uno de los valores siguientes:
                       tcp: elimina una exclusión para TCP.
                       udp: elimina una exclusión para UDP.
      startport      - El número de puerto de inicio de una exclusión
                       creada anteriormente.
      numberofports  - El número de puertos comenzando desde startport
                       de una exclusión creada anteriormente.
      store          - Uno de los valores siguientes:
                       active:     la eliminación solo dura hasta
                                   siguiente arranque.
                       persistent: la eliminación es permanente.
                                   Este es el valor predeterminado.

Notas: elimina una exclusión de bloques consecutivos de puertos.
         Los valores de startport y numberofports deben ser
         exactamente los mismos que en la exclusión creada previamente.

Ejemplo:

      delete excludedportrange protocol=tcp startport=50000 numberofports=20
```

Per exemple, en aquest cas ho escriurem de forma més abreujada...

``` doscon
netsh int ipv4 del ex tcp 40000 11
```

--8<-- ".acronims.txt"
