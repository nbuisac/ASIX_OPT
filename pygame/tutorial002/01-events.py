# Import dels paquets necessaris
from pygame.locals import * # Necessari per les tecles dels events
import pygame
import sys

# Inicialitzem pygame
pygame.init()

llista_colors = ["white", "pink", "lime", "black", "orange", "yellow"]

# Tamany de la finestra del joc (0, 0) serà FULLSCREEN 
WIDTH = 1920
HEIGHT = 1080
FPS = 60

FramesPerSegon = pygame.time.Clock() ## Permet jugar amb la mateixa velocitat independentment de la velocitat del processador

flags = pygame.OPENGL
finestra = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)

pygame.display.set_caption("Joc Pygame")

# Bucle de "Joc"
i = -1
while True:
    for event in pygame.event.get():    # Comprovem les events que han succeït
        if event.type == pygame.KEYDOWN:        # Si l'event és premuda una tecla
            # Mirem la tecla que s'ha premut
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                # Pintem la finestra amb un color de Pygame
                finestra.fill(pygame.Color("blue"))
            elif keys[K_a]:
                finestra.fill(pygame.Color("red"))
            elif keys[K_d]:
                finestra.fill(pygame.Color("green"))

        if event.type == pygame.MOUSEBUTTONDOWN: # Si l'event és prémer un botó del ratolí
            botons = list(pygame.mouse.get_pressed(num_buttons=3))
            if botons[0]:               # botó esquerre
                i = (i + 1) % len(llista_colors)
            elif botons[2]:             # botó dret
                i -= 1
                if i < 0:
                    i = len(llista_colors) - 1
            elif botons[1]:             # botó mig
                i = 0
            finestra.fill(pygame.Color(llista_colors[i]))
            posicio = pygame.mouse.get_pos()
            print(posicio, botons, llista_colors[i], i, end= " ")
            
        if event.type == pygame.QUIT:   # Si l'event és tancar la finestra
            pygame.quit()               #    tanquem pygame
            sys.exit()                  #    tanquem el programa

    pygame.display.flip()               # Actualitza la finestra
    FramesPerSegon.tick(FPS)