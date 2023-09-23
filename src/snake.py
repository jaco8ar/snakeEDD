from collections import deque
from Boton import Boton
from Cuadricula import Cuadricula
from Comida import Comida
from Serpiente import Serpiente

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

    #variables del juego
    gameMenu = True

    #imagenes de los botones
    btnEmpezarImage = pygame.image.load("imgs/boton-empezar.png")

    #def botones 
    botonInicio = Boton(200, 100, btnEmpezarImage, 0.5)


    # Crear los elementos del juego
    fruta = Comida(cuadricula)
    serpiente = Serpiente(cuadricula)

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

        #Control del menu
        if gameMenu == True:
            if botonInicio.draw(pantalla):
                gameMenu = False  
            pygame.display.update()
            # Máximo 60 FPS
            reloj.tick(60) 


        # Cada entrada actualizar los elementos
        else:
            fruta.dibujar_comida(pantalla)
            serpiente.dibujar_serpiente(pantalla)
        
            pygame.display.update()

            # Máximo 60 FPS
            reloj.tick(1)
    
