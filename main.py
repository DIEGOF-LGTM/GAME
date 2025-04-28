import pygame
from personaje import personaje
import costantes


player = personaje(50,50)

pygame.init()
ancho = costantes.ANCHO_VENTANA
alto = costantes.ALTO_VENTANA

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("mi primer juego")


run = True

while run:
    player.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.k_a:
                print("izquierda")
            if event.key == pygame.k_d:
                print("derecha ")
            if event.key == pygame.k_w:
                print("arriba")
            if event.key == pygame.k_s:
                print("abajo")
                


    pygame.display.update()
pygame.quit()