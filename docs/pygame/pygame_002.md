# pygame amb un tutorial

Per aprendre a programar en *Python* fent un joc, intentarem crear un petit joc on un *personatge* ha de sobreviude enmig d'un munt de personatges o objectes que es mouran per la pantalla de forma aleatòria.

Crearem un objecte que serà el nostre *personatge* i que podrem moure per tota la pantalla i, aniran sortint objectes que es mouran sols des de dalt de la pantalla. Es tractarà d'anar esquivant els diferents objectes que puguin anar sorgint, amb moviments cap "amunt", "avall", a dreta o a esquerra.

A partir d'aquí, la imaginació de cadascú pot fer que el joc estigui al mar, al cel, sigui un peix, un avió, o qualsevol altre cosa que creieu. 

També es pot canviar la rutina i fer que calgui tocar els objectes o fins i tot, aquestes podrien portar un número que seria el resultat d'una operació o ...

Podem aprendre el més bàsic de *pygame* [amb tutorial][] d'on ha sortit part de la idea d'aquest **tutorial propi**.

## La finestra principal

Per saber més sobre les **finestres** podem visitar [https://www.pygame.org/docs/ref/display.html][]

Tot joc necessita una finestra on es desenvoluparà el joc. Aquesta tindrà un tamany determinat, que podem calcular a partir de la pantalla de l'ordinador i la resolució. o bé establir-lo de forma fixa. També posarem un títol a la barra de la finestra del  joc i farem que quan premem la creu o `X` de la finestra, aquesta es tanqui. Per això tenim el següent codi;

```py title="Joc amb finestra bàsica"
--8<-- "./pygame/tutorial001/00-finestra.py"
```

En aquest cas, hem posat el codi de sortir del programa, dins el mateix `while`, quan detectem l'esdeveniment de tancar la finestra.

???note "I si vols més"

    ```py title="Joc amb finestra avançada" hl_lines="9 10 14 15"
    --8<-- "./pygame/tutorial002/00-finestra.py"
    ```



## Events

Per saber més sobre els **events** podem visitar [https://www.pygame.org/docs/ref/event.html][]

En tot programa basat en finestres li poden succeir una sèrie d'*"esdeveniments"* que podem capturar i així programar què fer en cada cas. En el programa anterior, hem capturat l'*esdeveniment* *Tancar la finestra*, `pygame.QUIT`. Alguns d'aquests *esdeveniments*, a més, porten algun paràmetre per saber més sobre ell. En *pygame* tenim els següents:

| Esdeveniment | Atributs |
|:-------------|:---------|
| QUIT              | none |
| ACTIVEEVENT       | gain, state |
| KEYDOWN           | key, mod, unicode, scancode |
| KEYUP             | key, mod, unicode, scancode |
| MOUSEMOTION       | pos, rel, buttons, touch |
| MOUSEBUTTONUP     | pos, button, touch |
| MOUSEBUTTONDOWN   | pos, button, touch |
| JOYAXISMOTION     | joy (deprecated), instance_id, axis, value |
| JOYBALLMOTION     | joy (deprecated), instance_id, ball, rel |
| JOYHATMOTION      | joy (deprecated), instance_id, hat, value |
| JOYBUTTONUP       | joy (deprecated), instance_id, button |
| JOYBUTTONDOWN     | joy (deprecated), instance_id, button |
| VIDEORESIZE       | size, w, h |
| VIDEOEXPOSE       | none |
| USEREVENT         | code |

Anem a capturar el fet de prémer una tecla i canviar el color de fons del nostre joc:

```py title="Joc amb captura d'events bàsica" hl_lines="2 21-30"
    --8<-- "./pygame/tutorial001/01-events.py"
```

Tot això ho controlem a cada iteració del buble principal. Encara no estem controlant quantes vegades per segon s'executa el bucle.

???question "Prova de capturar el click del Mouse, per posar la pantalla en negre, altra vegada."

    ```py
    if event.type == pygame.MOUSEBUTTONDOWN:
        finestra.fill(pygame.Color("black"))
    ```


???note "I si vols més"

    ```py title="Joc amb captura d'events avançada" hl_lines="2 9 14 38-50 57"
    --8<-- "./pygame/tutorial002/01-events.py"
    ```

    !!!note "La línia `#!py FramesPerSegon.tick(FPS)` controla que la iteració es realitzi FPS vegades per segon i no més"

        Depenent de la velocitat del nostre processador, podria ser que el joc anés més o menys ràpid. Aquí no ho apreciem però en jocs amb moviment sí que ho podrem comprovar.

## Sprites

_**"Sprite"**_ és una paraula anglesa que significa _**"follet"**_. En la programació de videojocs, aquest terme es va començar a utilitzar de manera habitual després que el dissenyador de xips *Jay Miner* els popularitzés.

Els *sprite* són una **classe de mapes de bits**. Aquests mapes es creen a la pantalla d'un ordinador a partir d'un dibuix inicial utilitzant un maquinari gràfic especial (sense necessitat de càlculs addicionals de la CPU de l'ordinador).

En l'àmbit dels videojocs, els *sprites* són un **conjunt d'imatges** que representa un personatge o objecte (o una part d'ells) de manera gràfica i que s'utilitza per poder crear qualsevol efecte de moviment o per canviar el seu estat o posició a l'escena.

Normalment els **sprites** estan formats per una imatge i un [objecte Rect][]. Aquest objecte de la classe *`Rect`* representa el rectangle on tenim la nostra animació i ens serà útil per les col·lisions.

Per crear un objecte a partir d'un *Sprite*, cal **"redefinir" la classe `pygame.sprite.Sprite`**, afegint codi en alguns del seus *mètodes*. Començarem per implementar un jugador, que no serà res més que un rectangle de color `purple`, i un terra, de color marró.

Caldrà doncs:

1. Definir una *classe*, que *hereti de la classe `pygame.sprite.Sprite`, per cada tipus de objecte.

2. Crear cadascun dels objectes.

3. Pintar-los a cada iteració.

Sovint es crea una agrupació d'objectes per tal de no deixar-nos de tractar-ne cap. Podem crear doferents grups d'objectes, segons el seu tractament.

```py title="Joc amb sprites bàsic" hl_lines="2 19-33 35-41 60 61"
--8<-- "./pygame/tutorial001/02-sprites.py"
```

La posició dels nostres objectes la definim en base *al seu centre* o *a baix a l'esquerra*. Tenim diverses opcions: `center`, `topleft`, `bottomleft`, `topright`, `bottomright`, `midtop`, `midleft`, `midbottom`, `midright`.

???note "I si vols més"

    ```py title="Joc amb sprites avançats" hl_lines="2 6 25-43 45-69 71-73 75-77 111 112"
    --8<-- "./pygame/tutorial002/02-sprites.py"
    ```

    !!!note "Hem utilitzat els personatges a partir d'un sol document, amb tots ells dibuixats en el mateix fitxer"

        Podem tenir diferents imatges, només cal definir bé quin requadre cal agafar per cadascun d'ells.

## Animació

Podem moure els personatges per la pantalla, per això, caldrà capturar algun event, per exemple la pulsació d'una tecla determinada, i així calcular la nova posició pel personatge. També pot moure's, a cada iteració, sense necessitat de cap event. Per això caldrà tenir definides unes variables que indicaran la posició actual i l'increment de `x` i/o de `y` que seria la direcció del moviment.

Pel moviment necessitem algunes variables com ara: la posició actual del personatge, la direcció cap a on anem i si volem, també podem tenir una acceleració o desacceleració.

Com que treballem en un espai bidimensional, aquestes variables les podem definir com un vestor de dos elements, la part de la `x` i l apart de la `y`.

També podem fer que el nostre personatge només avanci quan premem una tecla, o bé, que avanci sempre en la direcció que indica la darrera tecla premuda.

Anem a veure un exemple senzill i l'anirem ampliant.

```py title="Joc amb moviment bàsic" hl_lines="9 14 15 31-53 77 78 83"
--8<-- "./pygame/tutorial001/03-sprites_animats_01.py"
```

Com a amplicació, el que farem , és que el *jugador* es mogui d'una forma més semblant a la realitat. Cada vegada que premem la tecla cap alguna direcció, semblarà com si li donéssim un impuls que s'anirà reduint amb el temps. Per això necessitarem la posició, la velocitat i l'acceleració.
Treballarem amb el que anomenem acceleració i quan no apretem cap tecla, aquesta s'anirà reduint fins a 0.

```py title="Joc amb moviment bàsic" hl_lines="16 30 31 49-51"
--8<-- "./pygame/tutorial001/03-sprites_animats_02.py"
```

Ampliarem més, afegint altres elements que es mouran de forma aleatòria per la pantalla.

```py title="Joc amb moviment de diversos objectes" hl_lines="72-100 109-111 123-124"
--8<-- "./pygame/tutorial001/03-sprites_animats_03.py"
```

## Col·lisions

Quan tenim diversos elements mostrant-se en pantalla, necessitem, sovint, detectar algunes col·lisions entre diferents elements. Sovint tractarem les col·lisions del personatge amb altes elements, alguns seran *"enemics"*, altes podran ser part del paissatge.

Cada *Sprite* de pygame té (hauria de tenir) un objecte rectangular o *"`Rect`"* assignat. Aquest objecte rectangular té la mateixa amplada i alçada que el propi *Sprite* i representa els seus límits.

Aquest *"rectangle"* al voltant del jugador està, òbviament, ocult (no visible) i s'utilitza per a escenaris com la detecció de col·lisions. *Pygame* inclou diverses funcions que poden detectar si dos o més objectes `Rect` s'estan creuant entre si, també conegut com a "col·lisió".

Mitjançant el mètode següent en un objecte `Rect`, podrem determinar si està en contacte amb l'altre objecte `Rect` que s'ha passat als seus paràmetres. En paraules més senzilles, podem determinar si *`Sprite A`* està en contacte amb *`Sprite B`*.

```py
self.rect.colliderect(sprite.rect)
```

També trobem mètodes que treballen amb un grup de *Sprites*

```py
pygame.sprite.spritecollideany(sprite, group)
```

L'avantatge d'aquesta funció és que, per molt gran que sigui el grup, detectarà si l'*Sprite* està en col·lisió o no amb algun dels *sprites* del grup. Tornarà `True` si es detecta una col·lisió, en cas contrari `False`. Si no s'ha produït cap col·lisió, None es retornarà el valor .

Encara trobem algun altre mètode per detectar col·lisions entre elements d'un grup i elements d'un altre grup:

```py
pygame.sprite.groupcollide(group1, group2)
```

El valor de retorn d'aquesta funció té la forma d'un *diccionari* on els sprites en col·lisió del grup1 són claus i el valor és la llista d'*sprites* del grup2 que es tallen.

Treballem les col·lisions amb el següent exemple:

```py title="Joc amb moviment i control de col·lisions" hl_lines="114-123 125-129"
--8<-- "./pygame/tutorial001/04-collisions_01.py"
```


Altres enllaços interessants:

* Accés al rellotge intern: [https://www.pygame.org/docs/ref/time.html][]

[pygame]:   https://www.pygame.org/ "pygame"
[primer tutorial]: https://coderslegacy.com/python/pygame-platformer-game-development/?utm_content=cmp-true
[amb tutorial]: https://github.com/Patataman/PythonBasic/blob/master/frameworks/pygame/

[https://www.pygame.org/docs/ref/display.html]: https://www.pygame.org/docs/ref/display.html
[https://www.pygame.org/docs/ref/event.html]:   https://www.pygame.org/docs/ref/event.html
[objecte Rect]:                                 https://www.pygame.org/docs/ref/rect.html
[http://caca.zoy.org/wiki/libcaca]:             http://caca.zoy.org/wiki/libcaca
[https://www.pygame.org/docs/ref/time.html]:    https://www.pygame.org/docs/ref/time.html
