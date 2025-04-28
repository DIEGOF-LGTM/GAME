import pygame
from personaje import personaje
import costantes


player = personaje(50,50)

pygame.init()
ancho = costantes.ANCHO_VENTANA
alto = costantes.ALTO_VENTANA

ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("mi primer juego")
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

reloj = player.timer.clock()






run = True

while run:

    reloj.tick(costantes.FPS)
    ventana.fill(costantes.COLOR_FONDO)

    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
       delta_x = costantes.velocidad
    if mover_izquierda == True:
       delta_y = -costantes.velocidad
    if mover_abajo == True:
       delta_x = costantes.velocidad
    if mover_arriba == True:
       delta_y = -costantes.velocidad

    player.movimeiento(delta_x, delta_y)

    player.dibujar(ventana)
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        run = False
     elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            mover_izquierda = True 
        if event.key == pygame.K_d:
            mover_derecha = True
        if event.key == pygame.K_w:
            mover_arriba = True
        if event.key == pygame.K_s:
            mover_abajo = True
     elif event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            mover_izquierda = False
        if event.key == pygame.K_d:
            mover_derecha = False
        if event.key == pygame.K_w:
            mover_arriba = False
        if event.key == pygame.K_s:
            mover_abajo = False



    pygame.display.update()
pygame.quit()