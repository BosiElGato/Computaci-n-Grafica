import pygame
import random

ANCHO=640
ALTO=480
BLANCO=(255,255,255)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
NEGRO=(0,0,0)

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivo_img):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(archivo_img).convert_alpha()
        self.rect=self.image.get_rect()
        self.der=0
        self.vel=2
        self.temp=random.randint(50,150)
        self.mover=0
        self.x=0
        self.y=0
        self.m=0
        self.xf=0
        self.yf=0

    def Mover(self, pos):
        if self.mover==0:
            self.mover=1
            self.xf=pos[0]
            self.yf=pos[1]
            self.x=self.rect.x
            self.y=self.rect.y
            dx=float(self.xf-self.rect.x)
            dy=float(self.yf-self.rect.y)
            self.m=dy/dx
            print self.m

    def update(self):
        if self.mover==1:
            if self.x < self.xf:
                self.x+=1
                self.y+=self.m
                self.rect.x=self.x
                self.rect.y=int(self.y)

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    fuente=pygame.font.Font(None,32)
    texto=fuente.render('pos:',True,NEGRO)

    todos=pygame.sprite.Group()
    objeto=Enemigo('51x51.png')
    objeto.rect.x=20
    objeto.rect.y=20
    todos.add(objeto)

    fin=False
    reloj=pygame.time.Clock()
    puntos=0

    while not fin:
        #Capturar eventos
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                txt='pos: ' + str(pos[0]) + ',' + str(pos[1])
                texto=fuente.render(txt,True,NEGRO)
                objeto.Mover(pos)


        pantalla.fill(BLANCO)
        todos.update()
        todos.draw(pantalla)
        pantalla.blit(texto,[10,420])
        pygame.display.flip()
        reloj.tick(60)
