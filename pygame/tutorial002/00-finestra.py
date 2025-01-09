# Import dels paquets necessaris
import pygame
import sys

# Inicialitzem pygame
pygame.init()

# Tamany de la finestra del joc (0, 0) serà FULLSCREEN 
WIDTH = 1920
HEIGHT = 1080

FramesPerSegon = pygame.time.Clock() ## Permet jugar amb la mateixa velocitat independentment de la velocitat del processador

flags = pygame.OPENGL
finestra = pygame.display.set_mode((WIDTH, HEIGHT), flags, vsync=1)

pygame.display.set_caption("Joc Pygame")

# Bucle de "Joc"
while True:
    for event in pygame.event.get():    # Comprovem les events que han succeït
        if event.type == pygame.QUIT:   # Si l'event és tancar la finestra
            pygame.quit()               #    tanquem pygame
            sys.exit()                  #    tanquem el programa

    pygame.display.flip()               # Actualitza la finestra