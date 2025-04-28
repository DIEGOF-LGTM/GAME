import pygame
from personaje import personaje

player = personaje(50,50)

pygame.init()
ancho = 800
alto = 600

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("mi primer juego")


run = True

while run:
    player.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()