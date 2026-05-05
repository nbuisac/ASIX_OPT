# Dynmap (Visualització Web)

## Instal·lació de Docker

El procés d'instal·lació és molt senzill: el descarreguem de [pàgina de descàrrega de Docker amb explicacions][] i prémer el botó de *Get Docker Desktop*. (En el  moment de fer aquest tutorial m'he trobat la versió 3.5.2 per a windows).

Iniciem el fitxer d'instal·lació i ...

![Docker002.png][]
![Docker003.png][]
![Docker004.png][]

i una vegada reiniciat l'ordinador ja tenim Docker instal·lat. ![Docker005.png][]

??? Danger "I si falla?"
    És possible que ens falti instal·lar el *kernel de Linux* al nostre windows. En aquest cas ens sortirà una imatge semblant a
    
    ![Docker006.png][]
    
    El que cal fer és seguir [l'enllaç][] que ens proposa i fer la instal·lació del kernel de Linux al nostre sistema Windows.
    
    ![NucliLinux001.png][] ![NucliLinux002.png][

??? Danger "En Windows Home potser ..."

    És possible que ens falti instal·lar el *kernel de Linux* al nostre windows. En aquest cas podem anar a la consola i executar les següents comandes:
    
        wsl -l -o
        wsl --install -d Ubuntu
        wsl  --set-version Ubuntu 2
        wsl --update (aquesta com administrador)
        
    La primera ens mostra les distribucions de Linux per instal·lar al nostre PC i la segona instal·la el kernel del Linux.
    Com que segurament haurem instal·lat la versió 1 de wsl cal actualitzar a wsl2; això ho fan les dues darreres línies.

[pàgina de descàrrega de Docker amb explicacions]:  https://hub.docker.com/editions/community/docker-ce-desktop-windows "Docker"
[l'enllaç]: https://aka.ms/wsl2kernel "Instal·lació del kernel Linux a Windows 10"

[Docker002.png]:        ./img/Docker002.png
[Docker003.png]:        ./img/Docker003.png
[Docker004.png]:        ./img/Docker004.png
[Docker005.png]:        ./img/Docker005.png
[Docker006.png]:        ./img/Docker006.png
[NucliLinux001.png]:    ./img/NucliLinux001.png
[NucliLinux002.png]:    ./img/NucliLinux002.png
