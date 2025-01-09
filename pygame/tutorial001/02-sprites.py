# Import dels paquets necessaris
from pygame import sprite       # Per generar i tractar els sprites correctament
from pygame.locals import *     # Necessari per les tecles dels events
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

## Definim dos tipus de Sprites; el jugador i algun altre objecte
class Personatge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(pygame.Color("purple"))
        self.pos = ((15, HEIGHT - 35)) # posició actual
        self.rect = self.surf.get_rect( center = self.pos)

class Plataforma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((220,120,100))
        self.rect = self.surf.get_rect(bottomleft = (0, HEIGHT))

## Creem els objectes de Joc
jugador = Personatge()
terra = Plataforma()

all_sprites = pygame.sprite.Group()
all_sprites.add(jugador)
all_sprites.add(terra)

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

    for entity in all_sprites:
            finestra.blit(entity.surf, entity.rect)

    pygame.display.flip()               # Actualitza la finestra