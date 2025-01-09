import pygame
import sys

colors = ["black", "yellow", "pink", "violet", "red", "green", "blue", "orange"]
pygame.init()

WIDTH = 600
HEIGHT = 700
FPS = 8

pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Primera pantalla")
FramesPerSegon = pygame.time.Clock() ## Permet jugar amb la mateixa velocitat independentment de la velocitat del processador

pygame.font.init() # per poder escriure text a la pantalla
my_font = pygame.font.SysFont('Serif', 30, True)

no_fi = True
color = 0
while no_fi:
    for event in pygame.event.get():    # Comprovem les events que han succeït
        if event.type == pygame.QUIT:   # Si l'event és tancar la finestra
            no_fi = False

    pantalla.fill(pygame.Color(colors[color]))
    color = (color + 1) % len(colors)

    pygame.draw.circle(pantalla, colors[color], (WIDTH // 2, HEIGHT // 2 ), min(WIDTH, HEIGHT) // 2)

    text_surface = my_font.render('Game Over', True, colors[color])
    pantalla.blit(text_surface, (100, 0))

    pygame.display.flip()

    FramesPerSegon.tick(FPS)

pygame.quit()               #    tanquem pygame
sys.exit()                  #    tanquem el programa