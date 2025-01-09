# Import dels paquets necessaris
from pygame.locals import * # Necessari per les tecles dels events
import pygame
import sys

# Inicialitzem pygame
pygame.init()

# Tamany de la finestra del joc
HEIGHT = 450
WIDTH = 400

FramesPerSegon = pygame.time.Clock() ## Permet jugar amb la mateixa velocitat independentment de la velocitat del processador

finestra = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joc Pygame")

# Bucle de "Joc"
while True:
    for event in pygame.event.get():    # Comprovem les events que han succeït
        if event.type == pygame.KEYDOWN:
            # Mirem la tecla que s'ha premut
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                # Pintem la finestra amb un color de Pygame
                finestra.fill(pygame.Color("blue"))
            if keys[K_a]:
                finestra.fill(pygame.Color("red"))
            if keys[K_d]:
                finestra.fill(pygame.Color("green"))
        if event.type == pygame.QUIT:   # Si l'event és tancar la finestra
            pygame.quit()               #    tanquem pygame
            sys.exit()                  #    tanquem el programa

    pygame.display.flip()               # Actualitza la finestra