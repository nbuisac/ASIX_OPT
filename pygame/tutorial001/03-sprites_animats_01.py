# Import dels paquets necessaris
from pygame import sprite       # Per generar i tractar els sprites correctament
from pygame.locals import *     # Necessari per les tecles dels events
import pygame
import sys

# Inicialitzem pygame
pygame.init()
vec = pygame.math.Vector2       # per treballar amb dues dimensions

# Tamany de la finestra del joc
HEIGHT = 450
WIDTH = 400
FPS = 60
ACC = 1                         # acceleració

FramesPerSegon = pygame.time.Clock() ## Permet jugar amb la mateixa velocitat independentment de la velocitat del processador

finestra = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joc Pygame")

## Definim dos tipus de Sprites; el jugador i algun altre objecte
class Personatge(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(pygame.Color("purple"))
        self.pos = vec((10, HEIGHT - 20)) # posició actual
        self.rect = self.surf.get_rect(center = self.pos)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        ## Moviment lateral
        if pressed_keys[K_LEFT]:
            self.pos.x -= ACC
        elif pressed_keys[K_RIGHT]:
            self.pos.x += ACC
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        ## Moviment vertical
        if pressed_keys[K_UP]:
            self.pos.y -= ACC
        elif pressed_keys[K_DOWN]:
            self.pos.y += ACC
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT

        self.rect.midbottom = self.pos

class Plataforma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((220,120,100))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

## Creem els objectes de Joc
jugador = Personatge()
terra = Plataforma()

all_sprites = pygame.sprite.Group()
all_sprites.add(jugador)
all_sprites.add(terra)

# Bucle de "Joc"
while True:
    for event in pygame.event.get():    # Comprovem les events que han succeït
        if event.type == pygame.QUIT:   # Si l'event és tancar la finestra
            pygame.quit()               #    tanquem pygame
            sys.exit()                  #    tanquem el programa

    finestra.fill((0,0,0))              # Cal repintar tota la pantalla
    jugador.move()
    for entity in all_sprites:
            finestra.blit(entity.surf, entity.rect)

    pygame.display.flip()               # Actualitza la finestra
    FramesPerSegon.tick(FPS)