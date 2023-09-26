from Boton import Boton
from Cuadricula import Cuadricula
from Comida import Comida
from Serpiente import Serpiente

import pygame
import sys
import os
# Más adelante hacemos import random

# Ejecución del juego
if __name__ == "__main__":
    pygame.init()
    cuadricula = Cuadricula()

    # Crear la pantalla principal del juego
    pantalla = pygame.display.set_mode((cuadricula.ancho, cuadricula.largo))
    reloj = pygame.time.Clock()  # Para limitar los fps

    # Variables del juego
    gameMenu = True
    movible = False
    count = 0
    REFRESH_RATE = 2

    # Obtén el directorio actual
    directorio_actual = os.path.dirname(__file__)

    # Construye la ruta a la imagen dentro de la carpeta "imgs"
    ruta_imagen = os.path.join(directorio_actual, "..", "imgs", "boton-empezar.png")

    # Imagenes de los botones
    btnEmpezarImage = pygame.image.load(ruta_imagen)

    # Definir botones
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

            if event.type == pygame.KEYDOWN and not gameMenu:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    serpiente.cambiar_direccion("IZQUIERDA")
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    serpiente.cambiar_direccion("DERECHA")
                if event.key == pygame.K_UP or event.key == ord('w'):
                    serpiente.cambiar_direccion("ARRIBA")
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    serpiente.cambiar_direccion("ABAJO")
                
            if count == REFRESH_RATE-1 and not gameMenu and movible:
                serpiente.mover()
                movible = False
                
        # Crear una pantalla con el color de cuadricula
        pantalla.fill(cuadricula.color)

        # Control del menu
        if gameMenu:
            if botonInicio.draw(pantalla):
                gameMenu = False  
            pygame.display.update()
            # El menu se actualiza a 60 fps
            reloj.tick(60) 

        # Cada entrada actualizar los elementos
        else:
            count += 1
            if count == REFRESH_RATE:
                fruta.dibujar_comida(pantalla)
                serpiente.dibujar_serpiente(pantalla)
                movible = True
                pygame.display.update()
                count = 0

                # Esto sirve para las colisiones con comida
                if serpiente.cuerpo[0] == fruta.pos:
                    fruta.generar_comida(serpiente.cuerpo)

                    serpiente.crecer()
                    fruta.dibujar_comida(pantalla)
                    pygame.display.update()
            
            reloj.tick(REFRESH_RATE)
