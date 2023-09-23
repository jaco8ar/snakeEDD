import pygame
class Boton():
    def __init__(self, x, y, imagen, escala):
        ancho = imagen.get_width()
        altura = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen, (int(ancho*escala), int(altura*escala)))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self, surface):
        accion = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            
            if pygame.mouse.get_pressed()[0]== 1 and self.clicked== False:
                
                self.clicked = True
                accion = True

        if pygame.mouse.get_pressed()[0]== 0:
            
            self.clicked = False

        surface.blit(self.imagen, (self.rect.x, self.rect.y))

        return accion        