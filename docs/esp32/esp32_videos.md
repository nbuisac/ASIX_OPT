Video interrupcions en comptes de treballar en forma **POLL**

* [https://www.youtube.com/watch?v=crVZC4YcakQ][]{target="_blank"}
    Tenim interrupcions externes i internes
    Tots els Pins GPIO poden utilitzar-se per Interrupcions

    Cal una funció que es cridarà quan un pin canvii d'estat

    * attachInterrupt(GPIO, ISR, MODE)
    
        * GPIO Pin que cal escoltar

        * ISR Funció a executar: La funció es pot declarar **IRAM_ATTR** que posa la funció a la *RAM interna* i no a la *flash*

        * MODE és quan cal que s'executi: LOW, HIGH, CHANGE, FALLING, RISING

    * attachInterrupt(GPIO)

[https://www.youtube.com/watch?v=crVZC4YcakQ]:      https://www.youtube.com/watch?v=crVZC4YcakQ     "Interripcions"
    
