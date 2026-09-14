# Exercicis Pràctics: Bucle WHILE i Validació

## Exercici 1: Reintent de contrasenya (Límit d'intents)

En un sistema d'autenticació, un usuari té un màxim de 3 intents per encertar la contrasenya correcta ("_superSecret123_").

Fes un script que:

1. Utilitzi una variable comptador `#!py intents = 0`.

1. Demani la contrasenya a l'usuari en un bucle [`#!py while`][while].

1. Si la contrasenya és correcta, mostri "_Accés concedit!_" i surti del bucle.

1. Si falla, augmenti el comptador d'intents.

1. Si arriba a 3 intents fallits, el bucle s'ha de aturar i mostrar: "_COMPTE BLOCAT: Has superat el màxim d'intents._"

## Exercici 2: Validació d'entrada de la memòria RAM

Un script de configuració de màquines virtuals exigeix assignar una quantitat de RAM en Megabytes (MB) que sigui com a mínim de 1024 MB (1 GB) i com a màxim de 32768 MB (32 GB).

Fes un script que demani la memòria RAM en un bucle [`#!py while`][while] fins que l'usuari introdueixi un valor compres dins d'aquest rang. Quan sigui vàlid, mostra: _"Màquina virtual configurada amb [X] MB de RAM._"

## Exercici 3: Confirmació d'acció crítica (_S/N_)

Quan un SysAdmin vol reiniciar un servidor de producció, l'script ha de demanar confirmació. Només s'accepten com a respostes vàlides "_S_" (_Sí_) o "_N_" (_No_).

Fes un script que:

1. Demani a l'usuari: "_Estàs segur que vols reiniciar el servidor? (S/N): _".

1. Si escriu qualsevol cosa diferent de "_S_" o "_N_" (nota: pot ser en majúscula o minúscula), l'script ha d'insistir dient: "_Resposta no vàlida. Escriu 'S' o 'N'._".

1. En sortir del bucle:

    * Si ha escollit "S", mostra: "_Reiniciant el servidor..._".

    * Si ha escollit "N", mostra: "_Operació cancel·lada per l'usuari._".

## Exercici 4: Calculadora acumulativa de despeses de llicències

L'administrador vol anar introduint el preu de diferents llicències de software una per una fins que escrigui el número 0 per acabar.

Fes un script que:

1. Demani el preu d'una llicència (_decimal_, _float_).

1. Vagi sumant el preu a una variable _total_.

1. El bucle s'executarà mentre el preu introduït no sigui 0.

1. En acabar (quan l'usuari escrigui 0), mostri el cost total acumulat de les llicències.

**NOTA**: Pots afegir els preus en una llista i després tractar les dades de la llista

[while]:      https://docs.python.org/es/3.14/reference/compound_stmts.html#while

--8<-- ".acronims.txt"
