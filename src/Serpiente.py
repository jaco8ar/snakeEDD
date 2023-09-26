from collections import deque
import pygame


class Serpiente:
    """Representa la serpiente"""
    # Puede contener el temporizador para el movimiento automático de la serpiente

    def __init__(self, cuadricula):
        """Cada pedazo del cuerpo se guarda en un deque"""
        self.cuadricula = cuadricula
        self.cuerpo = deque([[6, 6], [6, 7], [6, 8]])
        self.color = (34, 139, 34)
        self.color_cabeza = (0, 100, 0)
        self.direccion = [0, -1]
        self.haCambiado = False

    def dibujar_serpiente(self, pantalla):
        """Dibujo cada pedazo en la cuadrícula"""
        for index, elemento in enumerate(self.cuerpo):
            elemento_x = elemento[0] * self.cuadricula.tamano_celdas
            elemento_y = elemento[1] * self.cuadricula.tamano_celdas
            ancho = self.cuadricula.tamano_celdas
            largo = self.cuadricula.tamano_celdas

            if index == 0:
                pedazo = pygame.Rect(elemento_x, elemento_y, ancho, largo)
                pygame.draw.rect(pantalla, self.color_cabeza, pedazo)
            else:
                # Dibuja cada elemento en el cuerpo
                pedazo = pygame.Rect(elemento_x, elemento_y, ancho, largo)
                pygame.draw.rect(pantalla, self.color, pedazo)
                self.haCambiado = False

    def mover(self):
        # Esto determina qué estructura de datos debemos usar
        self.cuerpo.appendleft([self.cuerpo[0][0] + self.direccion[0], self.cuerpo[0][1] + self.direccion[1]])
        self.cuerpo.pop()

    def cambiar_direccion(self, neo_direcccion):
        direcciones = {
            "DERECHA": [1, 0],
            "IZQUIERDA": [-1, 0],
            "ARRIBA": [0, -1],
            "ABAJO": [0, 1]
        }
        if direcciones[neo_direcccion][0]+self.direccion[0] != 0 and direcciones[neo_direcccion][1]+self.direccion[1] \
                != 0 and not self.haCambiado:
            self.direccion = direcciones[neo_direcccion]
            self.haCambiado = True

    def colision_bordes(self):
        if self.cuerpo[0][0] < 0 or self.cuerpo[0][0] \
                >= 12 or self.cuerpo[0][1] < 0 or self.cuerpo[0][1] >= 12:
            return True
        return False

    def colision_cuerpo(self):
        # En el bucle principal, después de actualizar la posición de la serpiente
        cabexa = self.cuerpo.popleft()
        if cabexa in self.cuerpo:
            self.cuerpo.appendleft(cabexa)
            return True
        else:
            self.cuerpo.appendleft(cabexa)
            return False
    # La cabeza de la serpiente ha chocado con su propio cuerpo
    # Aquí puedes manejar la colisión, como terminar el juego.

    def crecer(self):
        self.cuerpo.append(self.cuerpo[-1])
