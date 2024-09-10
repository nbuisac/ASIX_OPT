# Python - Exercicis

## Treball de classe

En aquest exercici estàs ajudant a la teva germana petita a fer els deures per a l'escola. El professor busca la puntuació correcta, la gramàtica i una excel·lent selecció de paraules.

### 1. Posa en majúscula el títol del treball

Qualsevol bon paper necessita un títol amb el format adequat. Implementeu la funció `#!py capitalize_title(<title>)` que pren un títol `str` com a paràmetre i posa en majúscula la primera lletra de cada paraula. Aquesta funció hauria de retornar un `str` amb el primer caràcter de cada paraula en majúscula i la resta en minúscula.

!!!question "Possible execució"

    ```py
    titol_majuscules("les meves aficions") # Retorna 'Les Meves Aficions'
    titol_majuscules("LES MEVES AFICIONS") # Retorna 'Les Meves Aficions'
    ```

### 2. Comprova si cada frase acaba amb un punt

Volem assegurar-nos que la puntuació del treball sigui perfecta. Implementa la funció `#!py comprova_final_de_frase()`que pren com a paràmetre una frase. Aquesta funció hauria de retornar un valor `bool` `True` si la frase acaba en punt `.` o `False` en cas contrari.

!!!question "Possible execució"

    ```py
    comprova_final_de_frase("M'agrada anar al cinema, jugar a la play i passejar pel parc.") # Retorna True
    comprova_final_de_frase("M'agrada anar al cinema, jugar a la play i passejar pel parc")  # Retorna False
    comprova_final_de_frase("M'agrada anar al cinema, jugar a la play i passejar pel parc. ")  # Retorna False
    ```

### 3. Netegeu espais sobrants

Perquè el treball sembli professional, cal eliminar els espais innecessaris. Implementa la funció `#!py neteja_espais()` que pren una frase com a paràmetre. La funció ha d'eliminar espais en blanc addicionals tant al principi com al final de la frase, retornant una frase nova i actualitzada `str`.

!!!question "Possible execució"

    ```py
    neteja_espais("   M'agrada passejar el gos.  ") # Retorna "M'agrada passejar el gos."
    ```

### 4. Substitueix paraules per un sinònim

Per millorar encara més el treball, podem substituir alguns dels adjectius pels seus sinònims. Escriu la funció `#!py canvia_paraula()` que pren tres paràmetres, *frase inicial*, *paraula a canviar*, *nova paraula a posar*. Aquesta funció ha de reemplaçar totes les instàncies de la *paraula a canviar* la *nova paraula a posar* i tornar-ne una nova `str` amb la frase actualitzada.

!!!question "Possible execució"

    ```py
    canvia_paraula("Faig magdalenes bones", "bones", "increïbles") # Ha de retornar "Faig magdalenes increïbles"
    ```

## Deures d'anglès

En aquest altre exercici, ajudaràs a la teva germana petita amb els deures de *vocabulari en anglès*, que li sembla molt tediosa. La seva classe està aprenent a crear paraules noves afegint *prefixos* i *sufixos* . Donat un conjunt de paraules, el professor busca paraules transformades correctament amb l'ortografia correcta afegint el prefix al principi o el sufix al final.

Hi ha quatre activitats a la tasca, cadascuna amb un conjunt de text o paraules per treballar.

### 1. Afegiu un prefix a una paraula

Un dels prefixos més comuns en anglès és ***un***, que significa ***no***. En aquesta activitat, la teva germana ha de fer paraules negatives afegint-hi el prefix ***un***.

Implementa la funció `#!py afegeix_prefix_un(<paraula>)` que pren `paraula` com a paràmetre i retorna una paraula nova amb prefix `un`:

!!!question "Possible execució"

    ```py
    afegeix_prefix_un("happy") # Ha de retornar 'unhappy'
    afegeix_prefix_un("manageable") # Ha de retornar 'unmanageable'
    ```

### 2. Afegiu prefixos als grups de paraules

Hi ha quatre prefixos més comuns que està estudiant la classe de la teva germana: `en` (que significa "posar a" o "cobrir amb"), `pre` (que significa "abans" o "endavant"), `auto` (que significa "un mateix" o "el mateix") i `inter` (que significa 'entre' o 'entre').

En aquest exercici, la classe està creant grups de paraules de vocabulari utilitzant aquests prefixos, perquè es puguin estudiar junts. Cada prefix ve en una llista amb les paraules habituals amb les quals s'utilitza. Els estudiants han d'aplicar el prefix i produir una cadena que mostri el prefix aplicat a totes les paraules.

Implementa la funció `#!py fes_grups_de_paraules(<paraules>)` que pren a `paraules` com a paràmetre de la forma següent: [<prefix>, <paraula_1>, <paraula_2> .... <paraula_n>], i retorna una cadena amb el prefix aplicat a cada paraula que s'assembla a: '<prefix> :: <prefix><paraula_1> :: <prefix><paraula_2> :: <prefix><paraula_n>'.

!!!question "Possible execució"

    ```py
    fes_grups_de_paraules(['en', 'close', 'joy', 'lighten']) # Retorna 'en :: enclose :: enjoy :: enlighten'
    fes_grups_de_paraules(['pre', 'serve', 'dispose', 'position'])  # Retorna 'pre :: preserve :: predispose :: preposition'
    fes_grups_de_paraules(['auto', 'didactic', 'graph', 'mate'])  # Retorna 'auto :: autodidactic :: autograph :: automate'
    fes_grups_de_paraules(['inter', 'twine', 'connected', 'dependent'])  # Retorna 'inter :: intertwine :: interconnected :: interdependent'
    ```

### 3. Elimina un sufix d'una paraula

`ness` és un sufix comú que significa "estat de ser" . En aquesta activitat, la teva germana ha de trobar la paraula *arrel original* eliminant el sufix `ness`. Però, per descomptat, hi ha regles d'ortografia molestes: si la paraula arrel originalment acabava en una consonant seguida d'una "y", aleshores la "y" es va canviar per "i". L'eliminació de "ness" ha de restaurar la "y" en aquestes paraules arrel. ex. ***happiness--> happi--> happy***.

Implementa la funció `#!py elimina_sufix_ness(<word>)` que pren una *paraula* com a paràmetre, i retorna la *paraula arrel* sense el *sufix* `ness`.

!!!question "Possible execució"

    ```py
    elimina_sufix_ness("heaviness") # Retorna  'heavy'
    elimina_sufix_ness("sadness")   # Retorna 'sad'
    ```

### Extreu i transforma una paraula

Sovint s'utilitzen sufixos per canviar la part del discurs a la qual s'assigna una paraula. Una pràctica habitual en anglès és **verbing** o **verbifying**, on un adjectiu es converteix en verb afegint un sufix `en`.

En aquesta tasca, la teva germana practicarà paraules **verbing** extraient un adjectiu d'una frase i convertint-la en verb. Afortunadament, totes les paraules que s'han de transformar aquí són *normals*: no necessiten canvis ortogràfics per afegir el *sufix*.

Implementa la funció `#!py adjectiu_a_verb(<frase>, <index>)` que pren dos paràmetres. una `frase` on aplicarem la funció, i l'`<index>` que indica on tenim la raualua a modificar dins la frase. La funció ha de retornar l'adjectiu extret com a verb.

!!!question "Possible execució"

    ```py
    adjectiu_a_verb('I need to make that bright.', -1 ) # Ha de retornar 'brighten'
    adjectiu_a_verb('It got dark as the sun set.', 2) # Ha de retornar 'darken'
    ```


* [Extret de ...][]{target="_blank}
* i [de ...][]{target="_blank}



[Extret de ...]:        https://exercism.org/tracks/python/exercises/little-sisters-essay       "Extret de ..."
[de ...]:               https://exercism.org/tracks/python/exercises/little-sisters-vocab       "Extret de ..."

--8<-- ".acronims.txt"
