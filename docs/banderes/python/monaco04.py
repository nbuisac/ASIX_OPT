from turtle import Turtle

t = Turtle()
t.clear() # borrem la pantalla
ample = t.screen.window_width()
alt = t.screen.window_height()
## Com que la posició 0,0 és al centre de la pantalla, la posició de dalt a l'esquerra és
## -ample // 2, alt // 2
daltEX = -ample // 2
daltEY = alt // 2
## Primera franja
t.penup()   ## Abans d'anar a dalt a l'esquerra, aixequem el llapis
x = daltEX
y = daltEY
t.goto(x, y)    ## Anem a dalt a l'esquerra
t.pendown()   ## Baixem el llapis
t.color("red")
t.fillcolor("red")
t.begin_fill()
x = x + ample
t.goto(x, y)    ## Anem a dalt a la dreta
y = y - alt // 2 ## y = 0
t.goto(x, y)    ## Anem al mig a la dreta
x = -ample // 2
t.goto(x, y)    ## Anem al mig a l'esquerra
y = alt // 2
t.goto(x, y)    ## Anem a dalt a l'esquerra
t.end_fill()
## Segona franja
## La segona franja comença a  posició 0,0 és al centre de la pantalla, la posició de dalt a l'esquerra és
## -ample / 2, alt / 2
t.penup()   ## Abans d'anar a dalt a l'esquerra, aixequem el llapis
x = daltEX
y = daltEY - alt // 2
t.goto(x, y)    ## Anem al mig a l'esquerra
t.pendown()   ## Baixem el llapis
t.color("yellow")
t.fillcolor("yellow")
t.begin_fill()
x = x + ample
t.goto(x, y)    ## Anem al mig a la dreta
y = y - alt // 2 ## y = 0
t.goto(x, y)    ## Anem a baix a la dreta
x = -ample // 2
t.goto(x, y)    ## Anem a baix a l'esquerra
y = daltEY - alt // 2
t.goto(x, y)    ## Anem a dalt a l'esquerra
t.end_fill()
