# Import dels paquets necessaris
from pygame import sprite       # Per generar i tractar els sprites correctament
from pygame.locals import *     # Necessari per les tecles dels events
import pygame
import sys
import random

# Inicialitzem pygame
pygame.init()
vec = pygame.math.Vector2       # per treballar amb dues dimensions

# Tamany de la finestra del joc
HEIGHT = 450
WIDTH = 400
FPS = 60
ACC = 0.5                       # acceleració
FRIC = -0.12                    # fricció que ens fa disminuir la velocitat

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
        self.vel = vec(0,0)       # velocitat x, y
        self.acc = vec(0,0)       # acceleració x, y
        self.rect = self.surf.get_rect(center = self.pos)

    def move(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()
        ## Moviment lateral
        if pressed_keys[K_LEFT]:
            self.acc.x -= ACC
        elif pressed_keys[K_RIGHT]:
            self.acc.x += ACC

        ## Moviment vertical
        if pressed_keys[K_UP]:
            self.acc.y -= ACC
        elif pressed_keys[K_DOWN]:
            self.acc.y += ACC

        self.acc += self.vel * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
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

class Altres(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        # self.surf.fill(pygame.Color(random.random()*255, random.random()*255, random.random()*255))
        self.surf.fill(pygame.Color("white"))
        self.pos = vec((50, 100)) # posició actual
        self.vel = vec(random.randint(-2,2), random.randint(-2,2))       # velocitat x, y
        self.rect = self.surf.get_rect(center = self.pos)
        self.fps = 0

    def update(self):
        self.fps += 1
        if self.fps >= 300:
            self.fps = 0
            self.vel = vec(random.randint(-2,2), random.randint(-2,2))
                               
        self.pos += self.vel

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT

        self.rect.midbottom = self.pos

## Creem els objectes de Joc
jugador = Personatge()
terra = Plataforma()

all_sprites = pygame.sprite.Group()
all_sprites.add(jugador)

for a in range(3):
    all_sprites.add(Altres())
all_sprites.add(terra)

# Bucle de "Joc"
while True:
    for event in pygame.event.get():    # Comprovem les events que han succeït
        if event.type == pygame.QUIT:   # Si l'event és tancar la finestra
            pygame.quit()               #    tanquem pygame
            sys.exit()                  #    tanquem el programa

    finestra.fill((0,0,0))              # Cal repintar tota la pantalla
    jugador.move()
    all_sprites.update()
    for entity in all_sprites:
        finestra.blit(entity.surf, entity.rect)

    pygame.display.flip()               # Actualitza la finestra
    FramesPerSegon.tick(FPS)