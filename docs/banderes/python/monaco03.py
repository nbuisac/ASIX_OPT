from turtle import Turtle

colors = [ "yellow", "blue", 'orange', 'black']
FILES = len(colors)

t = Turtle()
t.clear() # borrem la pantalla
ample = t.screen.window_width()
alt = t.screen.window_height()
## Com que la posició 0,0 és al centre de la pantalla, la posició de dalt a l'esquerra és
## -ample // FILES, alt // FILES
daltEX = -ample // 2
daltEY = alt // 2
## Primera franja
for i in range(FILES):
    t.penup()   ## Abt.ans d'anar a dalt a l'esquerra, aixequem el llapis
    x = daltEX
    y = daltEY - (alt // FILES) * i
    t.goto(x, y)    ## Anem a dalt a l'esquerra
    t.pendown()   ## Baixem el llapis
    t.color(colors[i])
    t.fillcolor(colors[i])
    t.begin_fill()
    for i in range(2):
        t.forward(ample)
        t.right(90)
        t.forward(alt // FILES)
        t.right(90)
    t.end_fill()

