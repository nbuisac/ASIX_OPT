# Import dels paquets necessaris
from pygame import sprite       # Per generar i tractar els sprites correctament
from pygame.locals import * # Necessari per les tecles dels events
import pygame
import sys
import random

# Inicialitzem pygame
pygame.init()
vec = pygame.math.Vector2       # per treballar amb dues dimensions

llista_colors = ["white", "pink", "lime", "black", "orange", "yellow"]

# Tamany de la finestra del joc (0, 0) serà FULLSCREEN 
WIDTH = 1920
HEIGHT = 1080
FPS = 60
ACC = 0.5                       # acceleració
FRIC = -0.12                    # fricció que ens fa disminuir la velocitat

FramesPerSegon = pygame.time.Clock() ## Permet jugar amb la mateixa velocitat independentment de la velocitat del processador

flags = pygame.OPENGL
finestra = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)

pygame.display.set_caption("Joc Pygame")

class Personatge(sprite.Sprite):

    def __init__(self):
        #Init de Sprite
        sprite.Sprite.__init__(self)
        self.spriteSheet = pygame.image.load("sprites/camina01.png").convert_alpha()
        AMPLE = 89
        ALT = 208
        x = 20
        y = 152

        self.image  = self.spriteSheet.subsurface((x, y, AMPLE, ALT))
        self.image = pygame.transform.scale(self.image ,(75,100))
        self.image  = pygame.transform.flip(self.image , True, False)   # Fem que miri cap a la dreta
        self.dreta = True                                               # Per saber cap a on mira
        self.rect = self.image.get_rect()
        # Primera posició de la imatge.
        self.pos = vec((finestra.get_width()/2, finestra.get_height()/2)) # posició actual
        self.vel = vec(0,0)       # velocitat x, y
        self.acc = vec(0,0)       # acceleració x, y
        self.rect.center = (self.pos)

    # Mètode heretat de la classe Sprite, que no utilitzarem encara
    def update(self):
        pass

    def move(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()

        ## Moviment lateral
        if pressed_keys[K_LEFT]:
            self.acc.x -= ACC
            if self.dreta:
                self.dreta = False
                self.image  = pygame.transform.flip(self.image , True, False) # Invertim el ninot
        elif pressed_keys[K_RIGHT]:
            self.acc.x += ACC
            if not self.dreta:
                self.dreta = True
                self.image  = pygame.transform.flip(self.image , True, False) # Invertim el ninot

        ## Moviment vertical
        if pressed_keys[K_UP]:
            self.acc.y -= ACC
        elif pressed_keys[K_DOWN]:
            self.acc.y += ACC

        self.acc += self.vel * FRIC
        if abs(self.acc.x) < 0.01:
            self.acc.x = 0
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
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

        self.rect.center = self.pos

class Altres(sprite.Sprite):
    q = 1
    primer_nino = random.randint(1,48)

    def __init__(self):
        # Init de Sprite
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

    # Mètode heretat de la classe Sprite, que no utilitzarem encara
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
            
        if event.type == pygame.QUIT:   # Si l'event és tancar la finestra
            pygame.quit()               #    tanquem pygame
            sys.exit()                  #    tanquem el programa

    jugador.move()
    finestra.fill(pygame.Color(llista_colors[i]))            # Netegem la pantalla
    altres_sprites.draw(finestra)       # Dibuixem els altres
    jugador_sprites.draw(finestra)      # Dibuixem el jugador
    pygame.display.flip()               # Actualitza la finestra
    FramesPerSegon.tick(FPS)