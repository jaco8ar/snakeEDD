import pygame


class Boton:
    def __init__(self, x, y, imagen, escala):
        """
        Crea un botón interactivo en una ventana de Pygame
        con posición inicial (x, y) y redimensionamiento (escala)
        """

        ancho = imagen.get_width()
        altura = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen, (int(ancho * escala), int(altura * escala)))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)

        # Para manejar el evento de un click
        self.presionado = False

    def draw(self, surface):
        """Dibuja el botón en una superficie y maneja eventos de clic."""

        # La variable acción sirve para borrar el botón e iniciar el juego
        accion = False

        # Lógica para manejar clicks sobre el botón
        pos = pygame.mouse.get_pos()

        # Si el botón es presionado dentro de su rectángulo, inicia el juego
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.presionado:
                self.presionado = True
                accion = True

        # Guardar eventos cuando no se presiona el botón
        if pygame.mouse.get_pressed()[0] == 0:
            self.presionado = False

        # Dibujar el botón y comenzar el juego si se cumple la lógica
        surface.blit(self.imagen, (self.rect.x, self.rect.y))
        return accion
