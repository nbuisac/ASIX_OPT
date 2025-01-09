# Import dels paquets necessaris
from pygame import sprite       # Per generar i tractar els sprites correctament
from pygame.locals import * # Necessari per les tecles dels events
import pygame
import sys
import random

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

class Personatge(sprite.Sprite):

    def __init__(self):
        #Init de Sprite
        sprite.Sprite.__init__(self)
        self.spriteSheet = pygame.image.load("sprites/ninosGran.png").convert_alpha()
        AMPLE = 150
        ALT = 193
        
        x = 0
        y = 0
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((x, y, AMPLE, ALT)),(75,100))
        self.rect = self.image.get_rect()
        # Primera posició de la imatge.
        self.rect.center = (finestra.get_width()/2, finestra.get_height()/2)

    #Método heredado de la clase Sprite y que no vamos a usar ahora
    def update(self):
        pass

class Altres(sprite.Sprite):
    q = 1
    primer_nino = random.randint(1,48)

    def __init__(self):
        #Init de Sprite
        sprite.Sprite.__init__(self)
        self.spriteSheet = pygame.image.load("sprites/ninosGran.png").convert_alpha()
        AMPLE = 150
        ALT = 193
        
        self.qui_soc = Altres.q

        x = (((Altres.q + Altres.primer_nino) % 49) % 7) * AMPLE
        y = (((Altres.q + Altres.primer_nino) % 49) // 7) * ALT
        print("He creat", self.primer_nino, self.qui_soc, x, y, x + AMPLE, y + ALT)
        self.image = pygame.transform.scale(self.spriteSheet.subsurface((x, y, AMPLE, ALT)),(75,100))
        self.rect = self.image.get_rect()
        # Primera posició de la imatge.
        self.rect.center = (self.q * (AMPLE + 10), 100)
        Altres.q = Altres.q + 1

    #Método heredado de la clase Sprite y que no vamos a usar ahora
    def update(self):
        pass

jugador = Personatge()
jugador_sprites = pygame.sprite.GroupSingle()
jugador_sprites.add(jugador)

altres_sprites = pygame.sprite.Group()
for a in range(10):
    altres_sprites.add(Altres())

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
            
        if event.type == pygame.QUIT:   # Si l'event és tancar la finestra
            pygame.quit()               #    tanquem pygame
            sys.exit()                  #    tanquem el programa

    jugador_sprites.draw(finestra)
    altres_sprites.draw(finestra)
    pygame.display.flip()               # Actualitza la finestra
    FramesPerSegon.tick(FPS)