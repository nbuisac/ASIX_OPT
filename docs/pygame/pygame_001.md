# pygame

[pygame][] és una llibreria per a Python preparada per fer jocs. Ens permet crear jocs d'una forma més fàcil ja que incorpora una  sèrie de *Classes* que podem *entendre* per crear, després, els objectes del joc.

Per instal·lar la darrera versió, podem excecutar la comanda

```bash
python -m pip install pygame
```

També podem crear un entorn virtual i afegir-li, per no posar mòduls o llibreries de python per defecte en el nostre entorn.

``` bash
mkdir pygame
cd pygame
python -m venv pygame
.\pygame\Scripts\activate
python -m pip install pygame
```

Ara ja podrem treballar en aquest entorn i utilitzar pygame, només en aquest entorn.

```bash
code .
```


Per sortir de l'entorn executarem:

```bash
.\pygame\Scripts\deactivate
```

Provarem el que podem fer, d'una manera pràctica, aprenent a través d'exemples:

Intentarem seguir algun tutorial partint del [primer tutorial][].

La llibreria [pygame][] ens ajudarà en :

1. Detecció de col·lisions

1. Moviment del jugador (moviment lateral realista)

1. Mecànica de salt

1. Gravetat i fricció

1. Desplaçament per la pantalla (creant una alçada infinita)

El primer que cal, però, és definir algunes de les característiques del joc:

```py
import pygame
from pygame.locals import *
 
pygame.init()

HEIGHT = 450
WIDTH = 400
FPS = 60

FramePerSec = pygame.time.Clock() ## Permet jugar amb la mateixa velocitat independentment de la velocitat del processador
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joc Pygame")
```

## Codi senzill i bàsic

Abans de veure l'estreuctura d'un joc amb els seus elements mòbils, veurem l'estructura bàsica amb un exemple senzill:

```py linenums="1" hl_lines="1 7-9 11-13 15-16 20 21-23 25 28 30-31 33 35 37-38"
--8<-- "./pygame/tutorial001/000-inici.py"
```

En aquest codi podem veure el següent:

* **línia 1**: Importem la llibreria `pygame` per a poder treballar amb ella

* **línies 7 a 9**: Definim el tamany de la pantalla i el refresc que farem de la mateixa `fps`, frames per segon.

* **línia 11**: Generem la pantalla amb el tamany definit prèviament.

* **línia 12**: Posem títol a la patalla de joc.

* **línia 13**: Inicialitzem el *"rellotge"* que comptarà els *"frames per segon"*.

* **línies 15 i 16**: Definim una *"font"* per escriure text en el joc

* **línia 20**: *"Bucle"* del joc fins la línia `35`

* **línies 21 a 23**: Controlem quan es vulgui tancar la finestra.

* **línia 25**: Pintem TOTA la finestra (com reiniciar-la), d'un sol color. És el fons de la pantalla

* **línia 28**: Dibuixem una circumferència

* **línies 30 i 31**: Definim un text, amb un color, i el posem dins de la *`pantalla`*

* **línia 33**: Actualitzem la pantalla. Si no es fes tot de cop, no es veuria del tot bé. La llibreria `pygame` ja està preparada per aquest funcionament.

* **línia 35**: Espera el temps necessari per no fer més *iteracions per segon* (*frames per segon*) dels que definim.

* **línies 37 i 38**: Tanquem la finestra i el programa.

[pygame]:   https://www.pygame.org/ "pygame"
<!-- [primer tutorial]: https://coderslegacy.com/python/pygame-platformer-game-development/?utm_content=cmp-true -->
[primer tutorial]: https://coderslegacy.com/python/python-pygame-tutorial/

