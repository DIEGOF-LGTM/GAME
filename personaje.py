import pygame
import costantes

class Personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, costantes.ANCHO_PERSONAJE, costantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, costantes.COLOR_PERSONAJE, self.forma)

    def movimiento(self, delta_x, delta_y):
        self.forma.x += delta_x
        self.forma.y += delta_y