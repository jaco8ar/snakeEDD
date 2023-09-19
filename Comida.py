from collections import deque
import pygame
import sys

class Comida:
    """Representa la comida de la serpiente"""

    def __init__(self):
        """Guardar la posición inicial en (8, 2) en un ARDD"""
        self.x = 8
        self.y = 2
        self.pos = [self.x, self.y]
        self.color = (221, 89, 82)

    def dibujar_comida(self):
        """Para el dibujo se hace la escala por el tamaño de celdas"""
        x_pos = self.pos[0] * cuadricula.tamano_celdas
        y_pos = self.pos[1] * cuadricula.tamano_celdas
        ancho = cuadricula.tamano_celdas
        largo = cuadricula.tamano_celdas

        comida = pygame.Rect(x_pos, y_pos, ancho, largo)
        pygame.draw.rect(pantalla, self.color, comida)

    def generar_comida(self):
        pass