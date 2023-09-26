from collections import deque
import pygame
import sys

class Serpiente:
    """Representa la serpiente"""
    # Puede contener el temporizador para el movimiento automático de la serpiente

    def __init__(self, cuadricula):
        """Cada pedazo del cuerpo se guarda en un deque"""
        self.cuadricula = cuadricula
        self.cuerpo = deque([[4, 2], [3, 2], [2, 2]])
        self.color = (153, 7, 82)
        self.direccion = [1, 0]
        self.haCambiado = False

    def dibujar_serpiente(self, pantalla):
        """Dibujo cada pedazo en la cuadrícula"""
        for elemento in self.cuerpo:
            # Dibuja cada elemento en el cuerpo
            elemento_x = elemento[0] * self.cuadricula.tamano_celdas
            elemento_y = elemento[1] * self.cuadricula.tamano_celdas
            ancho = self.cuadricula.tamano_celdas
            largo = self.cuadricula.tamano_celdas

            pedazo = pygame.Rect(elemento_x, elemento_y, ancho, largo)
            pygame.draw.rect(pantalla, self.color, pedazo)
            self.haCambiado = False

    def mover(self):
        # Esto determina qué estructura de datos debemos usar
        self.cuerpo.appendleft([self.cuerpo[0][0] + self.direccion[0], self.cuerpo[0][1] + self.direccion[1]])
        self.cuerpo.pop()

    def cambiarDireccion(self, neoDirecccion):
        direcciones = {
            "DERECHA": [1,0],
            "IZQUIERDA": [-1,0],
            "ARRIBA": [0,-1],
            "ABAJO": [0,1]
        }
        if direcciones[neoDirecccion][0]+self.direccion[0] != 0 and direcciones[neoDirecccion][1]+self.direccion[1] != 0 and not self.haCambiado:
            self.direccion = direcciones[neoDirecccion]
            self.haCambiado = True
        
    def colision_comida(self):
        pass

    def colision_bordes(self):
        pass

    def colision_cuerpo(self):
        pass

    def crecer(self):
        self.cuerpo.append(self.cuerpo[-1])
