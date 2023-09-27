from collections import deque
import pygame


class Serpiente:
    """Representa la serpiente"""

    def __init__(self, cuadricula):
        """Cada pedazo del cuerpo se guarda en un deque"""
        self.cuadricula = cuadricula
        self.cuerpo = deque([[6, 6], [6, 7], [6, 8]])
        self.color = (34, 139, 34)
        self.color_cabeza = (0, 100, 0)
        self.direccion = [0, -1]

        # Variable para manejar el caso en el que la serpiente se devuelve
        # Al dar dos veces al botón contrario a su dirección actual
        self.cambio_direccion = False

    def dibujar_serpiente(self, pantalla):
        """Dibujar cada pedazo en la cuadrícula"""
        for index, elemento in enumerate(self.cuerpo):
            elemento_x = elemento[0] * self.cuadricula.tamano_celdas
            elemento_y = elemento[1] * self.cuadricula.tamano_celdas
            ancho = self.cuadricula.tamano_celdas
            largo = self.cuadricula.tamano_celdas

            if index == 0:
                # Si el pedazo es la cabeza, lo dibujo de otro color
                pedazo = pygame.Rect(elemento_x, elemento_y, ancho, largo)
                pygame.draw.rect(pantalla, self.color_cabeza, pedazo)
            else:
                pedazo = pygame.Rect(elemento_x, elemento_y, ancho, largo)
                pygame.draw.rect(pantalla, self.color, pedazo)
                self.cambio_direccion = False

    def mover(self):
        """Acceder a los elementos del cuerpo y sumar la dirección"""
        self.cuerpo.appendleft([self.cuerpo[0][0] + self.direccion[0],
                                self.cuerpo[0][1] + self.direccion[1]])
        self.cuerpo.pop()

    def cambiar_direccion(self, nueva_direccion):
        """Manejar el evento de las teclas para cambiar dirección"""
        direcciones = {
            "DERECHA": [1, 0],
            "IZQUIERDA": [-1, 0],
            "ARRIBA": [0, -1],
            "ABAJO": [0, 1]
        }

        # Verificar si la nueva dirección es válida y no es un cambio de dirección repetido
        cambio_valido = (
                (direcciones[nueva_direccion][0] + self.direccion[0] != 0)
                and (direcciones[nueva_direccion][1] + self.direccion[1] != 0)
                and not self.cambio_direccion
        )

        if cambio_valido:
            self.direccion = direcciones[nueva_direccion]
            self.cambio_direccion = True

    def colision_bordes(self):
        """Lógica por si la cabeza se sale de los bordes"""
        cabeza_afuera = (12 < self.cuerpo[0][0] < 0) or (12 < self.cuerpo[0][1] < 0)

        return cabeza_afuera

    def colision_cuerpo(self):
        """Lógica para colisiones con el propio cuerpo"""

        # Se saca la cabeza temporalmente y se verifica si está en el cuerpo
        cabeza_temp = self.cuerpo.popleft()

        if cabeza_temp in self.cuerpo:
            self.cuerpo.appendleft(cabeza_temp)
            return True
        else:
            self.cuerpo.appendleft(cabeza_temp)
            return False

    def crecer(self):
        """Se define para crecer por la cola,
        aunque da la ilusión de crecer por la cabeza"""
        self.cuerpo.append(self.cuerpo[-1])
