# Excepcions

En aquest apartat esbrinarem com tractar les excepcions en python. Trobareu més informació a:

* [Tractament d'errors  i excepcions][]: tutorial de python

* [Sintaxis del `try`][try]: Sintaxis del `try` a python.

* [Sintaxis del `raise`][raise]: Sintaxis del `raise` a python.


## `#!py try`

En algunes ocasions, dins de qualsevol programa, poden succeir esdeveniments no esperats ni tractats pel programador de manera que z'interromp el programa que s'està executant i aquest deixa d'executar-se.
Un exemple clar que podem prova fàcilment és l'intent de transformar una cadena de caràcters en un número enter, si aquests nos són compatibles:

```py
a = int(input("Entra un número -> "))
```

En aquest cas, si no entrem un valor que pugui transformar-se en nombre, per exemple *"dos"* es donarà una **Excepció**.

```py hl_lines="3"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'dos'
```

!!!tip "Si ens fixem en la tercera línia veurem que l'error que ens dóna és de tipus _`ValueError`_"

Una solució possible seria:

```py hl_lines="3 5"
a = ""
while isinstance(a, str):
    try:
        a = float(input("Entra un número -> "))
    except ValueError:
        pass
print(type(a))
```

En Python, existeix l'estructura 
```py
try:
    ...
except <tipus_d_excepcio>:
    ...
except <tipus_d_excepcio>:
    ...
except <tipus_d_excepcio>:
    ...
else:
    ...
finally:
    ...` 
```

que ens permet capturar els errors i continuar el programa segons ens convingui sense que aquest s'interrompi i segueixi cap on nosaltres vulguem i com vulguem.

Ho veurem en el següent exemple, que inclou totes les parts de l'estructura `#!py try`:

```py
--8<-- "./docs/excepcions/python/excepcions_001.py"
```

En l'exemple anterior podem veure que tenim una **part del codi protegit dins una estructura `#!py try`** on:

* si les dades que entrem no podem passar-se a tipus `float`, es produeix una excepció de tipus `ValueError` i s'executa el primer `except`,

* si el valor de `b` és zero, 0, la divisió produeix l'excepció `ZeroDivisionError` i s'executa el segon `except`,

* els altres `except` són d'exemple. El darrer capturaria qualsevol excepció no esperada, fos del tipus que fos.

* la part del **`else`** s'executa quan **tot ha anat bé**

* la part del **`finally`** s'executa **sempre**. Fins i tot si dins el `try` hiha alguna instrucció `return`, `break` o `continue`. Pot interessanr-nos en *funcions* o *estructures repetitives*

## `#!py raise`

De la mateixa manera que podem **capturar les excepcions**, també podem llançar-ne de creades per nosalters o d'altres existents: Provem el següent codi:

```py
a = input("Entra un número -> ")
if not a.isnumeric():
    raise Exception("ERROR en l'entrada del número")
```

El fet de llançar errors ens pot ser útil quan programem funcions i/o procediments i els paràmetres rebuts siguin incorrectes o succeeixi quelcom que no puguem tractar. Llavors llancem l'excepció i qui cridi la funció caldrà que capturi l'execpció que nosalters hem llançat.



[Tractament d'errors  i excepcions]: https://docs.python.org/tutorial/errors.html#exceptions "Excepcions"

[try]:      https://docs.python.org/reference/compound_stmts.html#try   "try"
[raise]:    https://docs.python.org/3/reference/simple_stmts.html#raise "raise"
