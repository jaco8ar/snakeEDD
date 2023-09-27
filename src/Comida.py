from random import randint
import pygame


class Comida:
    def __init__(self, cuadricula):
        """Guardar la posición inicial en (8, 2) en un ARDD"""
        self.x = 8
        self.y = 2
        self.cuadricula = cuadricula
        self.pos = [self.x, self.y]
        self.color = (221, 89, 82)

    def dibujar_comida(self, pantalla):
        """Para el dibujo se hace la escala por el tamaño de celdas"""
        x_pos = self.pos[0] * self.cuadricula.tamano_celdas
        y_pos = self.pos[1] * self.cuadricula.tamano_celdas
        ancho = self.cuadricula.tamano_celdas
        largo = self.cuadricula.tamano_celdas

        comida = pygame.Rect(x_pos, y_pos, ancho, largo)
        pygame.draw.rect(pantalla, self.color, comida)
        pygame.draw.rect(pantalla, (180, 70, 60), comida, 5)

    def generar_comida(self, cuerpo_serpiente):
        """Se genera un fruto en la cuadrícula"""
        pos = [randint(0, 12), randint(0, 12)]

        # Generar comida por fuera de la serpiente
        while pos in cuerpo_serpiente:
            pos = [randint(0, 12), randint(0, 12)]

        self.pos = pos
