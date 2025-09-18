# Python

Quan treballem amb Python, acabarem fent una sèrie de programes que seria bó tenir-los ben emmagatzemats a l'ordinador.

## [GitHub][]

[GitHub][] és una plataforma basada en el núvol on podem emmagatzemar, compartir i treballar juntament amb altres usuaris per **escriure codi**.

Emmagatzemar el nostre codi en un _"repositori"_ a GitHub ens permet:

* Presentar o compartir la feina. 

* Seguir i administrar els canvis al codi al llarg del temps. 

* Deixar que altres usuaris revisin el codi i facin suggeriments per millorar-lo. 

* Col·laborar en un projecte compartit, sense preocupar-nos que els canvis afectin la feina dels col·laboradors abans que estigui llesta per integrar-la.

El treball col·laboratiu, una de les característiques fonamentals de GitHub, és possible gràcies al programari de codi obert [Git][], en què es basa GitHub.

Nosalres utilitzarem GitHub per tenir el codi al núvol i així el professor podrà accedir-hi per veure'l quan li interessi. Per això caldrà:

## Creació del repositori al núvol

1. Crearem, si no el tenim, un compte a [GitHub][]. *No cal que ho feu amb el compte de correu que us ha proporcionat l'institut*.

    ![github001][]

2. Crearem un repositori, a partir d'un enllaç que em proporcionarà el professor: *Trobareu l'enllaç al [moodle del Curs][]*.

    1. Per això accedirem a l'enllaç, abans cal haver fet *login* a [GitHub][].

        ![github002][]

    2. i acceptarem l'**assignment**

    3. Una vegada acceptat l'**assignment**

        ![github003][]

    4. ja se'ns haurà creat un repositori propi.

        ![github004][]

## Treball des de l'ordinador amb el repositori

Ara el que ens caldrà és poder treballar des de l'ordinador amb el repositori. Això implica:

1. Crear un directori al nostre ordinador que serà el *mirall* del repositori. En realitat se'ns crearà un directori, on vulguem, amb el mateix nom del repositori. En l'exemple `opt-alumne`.

2. Treballar en els fitxers locals. Crearem directoris i fitxers i treballarem comhem fet sempre.

3. Pujar el treball al repositori GitHub. Per això utilitzarem les comandes del [git][].

Anem, doncs a fer-ho...

1. Clonem el repositori que tenim al núvol.

    1. Per això accedirem al nostre repositori i desplegarem el botó on diu <span style="background-color:#1f883d; color:white"> &lt;&gt; Code </span> i **copiarem la URL del lloc HTTPS**.

        ![github005][]

    2. Anirem a un directori del nostre ordinador, on vulguem posar aquest repositori (Podem anar-hi en un **cmd** amb la comanda `cd` o bé obrim un **Explorador de carpetes** i ens situem al directori en qüestió)

        ![github006][]

    3. I hi obrirem una terminal, i hiescriurem `git clone `+ *el que hem copiat de la pàgina del nostre repositori*:

        ```doscon
        git clone https://github.com/MontiliviDaw/opt-alumne.git
        ```

        !!!warning "Pot ser que el sitema en demani  com connectar-nos i especificarem amb el browser/navegador."

            ![github007][]

    4. El programa ens respon que clona en un directori que està creant... i ja ho tenim *mig llest*

        ```doscon
        Cloning into 'opt-alumne'...
        remote: Enumerating objects: 4, done.
        remote: Counting objects: 100% (4/4), done.
        remote: Compressing objects: 100% (4/4), done.
        remote: Total 4 (delta 0), reused 2 (delta 0), pack-reused 0 (from 0)
        Receiving objects: 100% (4/4), done.
        ```

        !!!note "Si no us agrada el nom del directori, podeu canviar-lo"

    5. Una vegada tenim el repositori creat i baixat, ens cal configurar dosparàemtres per tal que tot funcioni. Per això ...
    
        1. entrarem al directori des del *cmd*

            ```doscon
            CD opt-alumne
            ```

        2. i executarem les instruccions per afegim les nostres credencials, **nom** i **correu electrònic**

            ```doscon
            git config --local user.email "alumne@institutmontilivi.cat"
            git config --local user.name "Nom Cognom"
            ```

2. Com pujo els fitxers al Repositori? Com treballarem amb el repositori local i el del núvol?

    A partir d’ara, una vegada hagi creat el meu primer, o uns quants, programes, podré pujar-los al repositori. Podem fer-ho, almenys, una vegada per setmana o cada quinze dies. Per això caldrà tenir iniciat un **CMD** al directori principal dels projectes, aquell que se'ns ha creat abans. Tot seguit escriurem la comanda `git status` per comprovar que tenim canvis per pujar...
    
    1. En el meu cas he creat una carpeta anomenada `proves` i dins un programa, dins el directori, anomenat `prova001.py`

        ```doscon hl_lines="1"
        C:\ASIX1\opt-alumne>git status
        On branch main
        Your branch is up to date with 'origin/main'.

        Untracked files:
          (use "git add <file>..." to include in what will be committed)
                proves/

        nothing added to commit but untracked files present (use "git add" to track)
        ```

    2. Cal afegir, al repositori local, els fitxers/directoris que s’han modificat o afegit i per fer-ho fàcil, executarem sempre la comanda `git add *` i tornarem a comprovar amb `git status`

        ```doscon hl_lines="1 3"
        C:\ASIX1\opt-alumne>git add *

        C:\ASIX1\opt-alumne>git status
        On branch main
        Your branch is up to date with 'origin/main'.

        Changes to be committed:
          (use "git restore --staged <file>..." to unstage)
                new file:   proves/prova001.py
        ```

    3. Tot seguit executarem dues comandes, la primera per *validar* el que hem fet i la segona per *pujar-ho al repositori de github*. A la primera comanda **cal posar-hi sempre un comentari** que pot incloure la data i quelcom més.

        ```doscon hl_lines="1 6"
        C:\ASIX1\opt-alumne>git commit -m "aaaammdd primera prova"
        [main 38dc580] aaaammdd primera prova
        1 file changed, 1 insertion(+)
        create mode 100644 proves/prova001.py

        C:\ASIX1\opt-alumne>git push origin main
        Enumerating objects: 5, done.
        Counting objects: 100% (5/5), done.
        Delta compression using up to 12 threads
        Compressing objects: 100% (2/2), done.
        Writing objects: 100% (4/4), 408 bytes | 408.00 KiB/s, done.
        Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
        To https://github.com/MontiliviDaw/opt-alumne.git
          12aa450..38dc580  main -> main
        ```

    4. Si ara comprovem el repositori des de la web, podrem veure que ja presenta més fitxers.

        ![github008][]

    Com  podreu veure ha aparegut un directori `proves\prova001` amb una descripció pel commit i fet en un moment determinat.

    Si entreu dins el directori podreu arribar, fins i tot, a veure el codi del programa que també s’ha pujat al repositori

    ![github009][]

Hi ha eines visuals que em permeten treballar, a partir d'ara amb el repositori. Pel que hem de fer nosaltres no és necessari instal·lar cap programa alternatiu ja que des del mateix **Visual Studio Code** podrem treballar amb el repositori.

De totes maneres, a partir d'ara, si volem pujar el que tenim fet fins un moment determinat, **només cal que executem les tres instruccions següents**

1. `#!doscon git add *`

2. `#!doscon git commit -m "comentari"`

3. `#!doscon git push origin main`

D'aquesta manera ja tindrem el repositori actualitzat amb l'ordinador.

## Treballem des de dos PCs locals amb el mateix repositori

És possible que vulguis treballar a l'institut amb un portàtil i a casa amb un ordinador de sobretaula. 

En aquest cas, repetirem el mateix que hem fet al segon ordinador. Només ens cal tenir en compte que de vegades hauré pujat fitxers des d'un ordinador i quan et posis a treballar en l'altre, aquests fitxers no els tindràs.

Per això és una bona pràctica, **abans de treballar**, executar la comanda **`git pull`**.

!!!danger "En tot cas, sempre, abans de fer el commit i el push, executarem el git pull."

Aquesta comada, `git pull`, es connecta al repositori i descarrega els fitxers i directoris que no tinguem al nostre PC i sí estiguin al repositori, fent que tots dos llocs siguin iguals.

L'ordre de comandes, serà, doncs:

1. **`#!doscon git pull`**

2. Treballem...

3. `#!doscon git add *`

4. `#!doscon git commit -m "comentari"`

5. `#!doscon git push origin main`


!!!warning "En aquest tutorial no hem utilitzat branques"

    En aquest tutorial **no hem utilitzat branques**.

    Si volem utilitzar branques el procés serà un xic diferent, però **no és l'objectiu d'aquest mini tutorial**.


[GitHub]:           https://github.com/
[Git]:              https://git-scm.com/
[moodle del Curs]:  https://moodle.institutmontilivi.cat/course/view.php?id=1491


[github001]:        ./img/github001.png
[github002]:        ./img/github002.png
[github003]:        ./img/github003.png
[github004]:        ./img/github004.png
[github005]:        ./img/github005.png
[github006]:        ./img/github006.png
[github007]:        ./img/github007.png
[github008]:        ./img/github008.png
[github009]:        ./img/github009.png



--8<-- ".acronims.txt"