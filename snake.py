from collections import deque
import pygame
import sys
# Más adelante hacemos import random


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
