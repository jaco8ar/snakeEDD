from collections import deque
import pygame
import sys
# Más adelante hacemos import random


class Cuadricula:
    """Define el la cuadricula 13 x 13 con celdas de 50 x 50 pixeles"""
    def __init__(self):
        """Guardar tamaños fijos que representan la cuadrícula"""
        self.tamano_celdas = 50
        self.cantidad_celdas = 13
        self.ancho = self.tamano_celdas * self.cantidad_celdas
        self.largo = self.tamano_celdas * self.cantidad_celdas
        self.color = (55, 175, 193)


class Serpiente:
    """Representa la serpiente"""
    # Puede contener el temporizador para el movimiento automático de la serpiente

    def __init__(self):
        """Cada pedazo del cuerpo se guarda en un deque"""
        self.cuerpo = deque([[4, 2], [3, 2], [2, 2]])
        self.color = (153, 7, 82)
        self.direccion = [1, 0]

    def dibujar_serpiente(self):
        """Dibujo cada pedazo en la cuadrícula"""

        for elemento in self.cuerpo:
            # Dibuja cada elemento en el cuerpo
            elemento_x = elemento[0] * cuadricula.tamano_celdas
            elemento_y = elemento[1] * cuadricula.tamano_celdas
            ancho = cuadricula.tamano_celdas
            largo = cuadricula.tamano_celdas

            pedazo = pygame.Rect(elemento_x, elemento_y, ancho, largo)
            pygame.draw.rect(pantalla, self.color, pedazo)

    def mover(self):
        # Esto determina qué estructura de datos debemos usar
        self.cuerpo.appendleft([self.cuerpo[0][0] + self.direccion[0], self.cuerpo[0][1] + self.direccion[1]])
        self.cuerpo.pop()

    def colision_comida(self):
        pass

    def colision_bordes(self):
        pass

    def colision_cuerpo(self):
        pass


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


# Ejecución del juego
if __name__ == "__main__":
    pygame.init()
    cuadricula = Cuadricula()

    # Crear la pantalla principal del juego
    pantalla = pygame.display.set_mode((cuadricula.ancho, cuadricula.largo))
    reloj = pygame.time.Clock()  # Para limitar los fps

    # Crear los elementos del juego
    fruta = Comida()
    serpiente = Serpiente()

    # Cada 150 ms actualizo la pantalla con el evento
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
        # Verificar la validez de los comandos entrados

        for event in pygame.event.get():
            # Salir del juego
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                serpiente.mover()

        # Crear una pantalla con el color de cuadricula
        pantalla.fill(cuadricula.color)

        # Cada entrada actualizar los elementos
        fruta.dibujar_comida()
        serpiente.dibujar_serpiente()
        pygame.display.update()

        # Máximo 60 FPS
        reloj.tick(60)
