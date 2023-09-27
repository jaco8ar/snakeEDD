import sys
import os
import pygame
from random import randint
from Boton import Boton
from Cuadricula import Cuadricula
from Comida import Comida
from Serpiente import Serpiente

# Ejecución del juego
if __name__ == "__main__":
    # Inicializar Pygame y crear la cuadrícula del juego
    pygame.init()
    cuadricula = Cuadricula()

    # Crear la pantalla principal del juego y el reloj para limitar los FPS.
    pantalla = pygame.display.set_mode((cuadricula.ancho, cuadricula.largo))
    reloj = pygame.time.Clock()

    # Definir variables del juego
    REFRESH_RATE = 2
    gameMenu = True

    # Definir variable para controlar la generación de frutas
    # Cuando es negativa, se genera una fruta
    mov_para_fruta = -1

    # Obtener el directorio actual
    directorio_actual = os.path.dirname(__file__)

    # Construir la ruta a la imagen dentro de la carpeta "imgs"
    ruta_imagen = os.path.join(directorio_actual, "..", "imgs", "boton-empezar.png")

    # Definir el botón
    btnEmpezarImage = pygame.image.load(ruta_imagen)
    botonInicio = Boton(200, 100, btnEmpezarImage, 0.5)

    # Crear los elementos del juego
    fruta = Comida(cuadricula)
    serpiente = Serpiente(cuadricula)

    # Obtener eventos de usuario cada 150ms
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while True:
        # Ciclo principal del juego
        for event in pygame.event.get():

            # Salir del juego
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Manejar eventos de tecleos
            if event.type == pygame.KEYDOWN and not gameMenu:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    serpiente.cambiar_direccion("IZQUIERDA")
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    serpiente.cambiar_direccion("DERECHA")
                if event.key == pygame.K_UP or event.key == ord('w'):
                    serpiente.cambiar_direccion("ARRIBA")
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    serpiente.cambiar_direccion("ABAJO")

        # Crear una pantalla de fondo
        pantalla.fill(cuadricula.color)

        # Dibujar una cuadrícula encima de la pantalla
        filas, columnas = 13, 13

        for fila in range(filas):
            for columna in range(columnas):
                pygame.draw.rect(pantalla, (0, 139, 139),
                                 pygame.Rect(fila * 50, columna * 50, 50, 50), 3)

        # Control del menu de juego
        if gameMenu:
            # Si se da al botón de empezar, se inicia el juego
            if botonInicio.draw(pantalla):
                gameMenu = False
            pygame.display.update()
            # El menu se actualiza a 60 fps
            reloj.tick(60)

        # Cada entrada actualizar los elementos
        else:
            serpiente.mover()

            # Lógica para generar frutas.
            # Se va restando al entero random hasta que es negativo
            if mov_para_fruta <= 0:
                fruta.dibujar_comida(pantalla)
                mov_para_fruta = -1

            serpiente.dibujar_serpiente(pantalla)
            pygame.display.update()

            # Lógica para colisiones con frutas
            if serpiente.cuerpo[0] == fruta.pos:
                mov_para_fruta = randint(0, 10)
                serpiente.crecer()
                fruta.generar_comida(serpiente.cuerpo)
                pygame.display.update()

            mov_para_fruta -= 1

            # Fin del juego
            if (serpiente.colision_cuerpo()) or (serpiente.colision_bordes()):
                sys.exit()

            reloj.tick(REFRESH_RATE)
