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
DRETA = 0
ESQUERRA = 1

FramesPerSegon = pygame.time.Clock() ## Permet jugar amb la mateixa velocitat independentment de la velocitat del processador

flags = pygame.OPENGL
finestra = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)

pygame.display.set_caption("Joc Pygame")

class Personatge(sprite.Sprite):

    def __init__(self):
        # Definició de les imatges. De l'esquerra caminant (a - les 9 del rellotge) i en sentit horari
        # a) (10, 152) - (109, 360)
        # b) (109, 56) - (208, 267)
        # c) (223, 20) - (298, 227)
        # d) (324, 14) - (415, 229)
        # e) (437, 68) - (532, 283)
        # f) (529, 148) - (660, 363)
        # g) (430, 284) - (546, 507)
        # h) (324, 340) - (415, 555)
        # i) (221, 336) - (300, 543)
        # j) (113, 284) - (204, 499)
        posicions = []
        posicions.append([(10, 152), (109, 360)])
        posicions.append([(109, 56), (208, 267)])
        posicions.append([(223, 20), (298, 227)])
        posicions.append([(324, 14), (415, 229)])
        posicions.append([(437, 68), (532, 283)])
        posicions.append([(529, 148), (660, 363)])
        posicions.append([(430, 284), (546, 507)])
        posicions.append([(324, 340), (415, 555)])
        posicions.append([(221, 336), (300, 543)])
        posicions.append([(113, 284), (204, 499)])

        #Init de Sprite
        sprite.Sprite.__init__(self)
        llista_sps = []
        for quin in range(8):
            spriteSheet = pygame.image.load("sprites/camina0" + str(quin + 1) + ".png").convert_alpha()
            llista_sps.append(spriteSheet)


        self.imatges = []
        for estat in range(len(posicions)):
            llista_imatges_dreta = []
            llista_imatges_esquerra = []
            for quin in range(len(llista_sps)):
                spriteSheet = llista_sps[quin]
                x = posicions[estat][0][0]
                y = posicions[estat][0][1]
                AMPLE = posicions[estat][1][0] - posicions[estat][0][0] + 1
                ALT =  posicions[estat][1][1] - posicions[estat][0][1] + 1
                imatge  = spriteSheet.subsurface((x, y, AMPLE, ALT))
                imatge = pygame.transform.scale(imatge ,(75,100))
                if estat >= 3 and estat <= 7:
                    llista_imatges_dreta.append(imatge)
                    imatge = pygame.transform.flip(imatge, True, False)     # totes les imatges miraran cap a l'esquerra, per defecte
                    llista_imatges_esquerra.append(imatge)
                else:
                    llista_imatges_esquerra.append(imatge)
                    imatge = pygame.transform.flip(imatge, True, False)     # totes les imatges miraran cap a l'esquerra, per defecte
                    llista_imatges_dreta.append(imatge)

            self.imatges.append([llista_imatges_dreta, llista_imatges_esquerra])

        self.corrent = False
        self.p1 = 0
        self.p2 = 0
        self.costat = DRETA
        self.image  = self.imatges[self.p1][self.costat][self.p2]
        self.rect = self.image.get_rect()
        # Primera posició de la imatge.
        self.pos = vec((finestra.get_width()/2, finestra.get_height()/2)) # posició actual
        self.vel = vec(0,0)       # velocitat x, y
        self.acc = vec(0,0)       # acceleració x, y
        self.rect.center = (self.pos)
        self.fps = 0

    # Mètode heretat de la classe Sprite, que no utilitzarem encara
    def update(self):
        if self.vel.x == 0 and self.vel.y == 0:
            self.p1 = 8
            self.p2 = 1
            self.costat = ESQUERRA
        else:
            if self.vel.x != 0 and self.vel.y == 0:
                if self.corrent:
                    self.p1 = 5
                else:
                    self.p1 = 0
            elif self.vel.x == 0 and self.vel.y > 0:
                if self.corrent:
                    self.p1 = 7
                else:
                    self.p1 = 8
            elif self.vel.x == 0 and self.vel.y < 0:
                if self.corrent:
                    self.p1 = 3
                else:
                    self.p1 = 2
            elif self.vel.x > 0 and self.vel.y > 0:
                if self.corrent:
                    self.p1 = 6
                else:
                    self.p1 = 9
            elif self.vel.x < 0 and self.vel.y < 0:
                if self.corrent:
                    self.p1 = 4
                else:
                    self.p1 = 1
            elif self.vel.x < 0 and self.vel.y > 0:
                dreta = False
                if self.corrent:
                    self.p1 = 6
                else:
                    self.p1 = 9
            if self.vel.x > 0:
                self.costat = DRETA
            else:
                self.costat = ESQUERRA

            self.fps += 1
            if self.fps > 10:
                self.fps = 0
                self.p2 = self.p2 + 1
                if self.p2 >= len(self.imatges[self.p1][self.costat]):
                    self.p2 = 0


    def move(self):
        self.image  = self.imatges[self.p1][self.costat][self.p2]
        self.rect = self.image.get_rect()
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
        if abs(self.vel.x) < 0.5:
            self.vel.x = 0
            if abs(self.acc.x) < 0.5:
                self.acc.x = 0
        if abs(self.vel.y) < 0.5:
            self.vel.y = 0
            if abs(self.acc.y) < 0.5:
                self.acc.y = 0
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
    jugador_sprites.update()            # Actualitzem el jugador
    altres_sprites.draw(finestra)       # Dibuixem els altres
    jugador_sprites.draw(finestra)      # Dibuixem el jugador
    pygame.display.flip()               # Actualitza la finestra
    FramesPerSegon.tick(FPS)