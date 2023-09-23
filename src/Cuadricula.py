from collections import deque
import pygame
import sys

class Cuadricula:
    """Define el la cuadricula 13 x 13 con celdas de 50 x 50 pixeles"""
    def __init__(self):
        """Guardar tamaños fijos que representan la cuadrícula"""
        self.tamano_celdas = 50
        self.cantidad_celdas = 13
        self.ancho = self.tamano_celdas * self.cantidad_celdas
        self.largo = self.tamano_celdas * self.cantidad_celdas
        self.color = (55, 175, 193)