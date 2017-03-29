import pygame
import random

ANCHO=800
ALTO=600

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)


class Player1(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.y=300
        self.rect.x=400
        self.var_x=5
        self.dir=0#cero para desplazarse a la derecha y uno para la izquierda
        self.muros1=[]

    def update(self):
        #self.rect.x+= self.var_x
        if self.dir==0:
            self.rect.x += self.var_x
            if self.rect.x>(ANCHO -self.rect.width):
                self.rect.x= ANCHO -self.rect.width
                #self.dir=5
        if self.dir==1:
            self.rect.x -= self.var_x
            if self.rect.x<(0):
                self.rect.x= 0
                #self.dir=5
        if self.dir==2:
            self.rect.y -= self.var_x
            if self.rect.y<(0):
                self.rect.y=0
                #self.dir=5
        if self.dir==3:
            self.rect.y += self.var_x
            if self.rect.y>(ALTO - self.rect.height):
                self.rect.y=ALTO - self.rect.height
                #self.dir=5

        l_col=pygame.sprite.spritecollide(self,self.muros1,False)

        for m in l_col:
            if self.dir==0:
                if self.rect.right > m.rect.left:
                    self.rect.right = m.rect.left
            if self.dir==1:
                if self.rect.left < m.rect.right:
                    self.rect.left = m.rect.right
            if self.dir==2:
                if self.rect.top < m.rect.bottom:
                    self.rect.top = m.rect.bottom

            if self.dir==3:
                if self.rect.bottom > m.rect.top:
                    self.rect.bottom = m.rect.top




        #self.dir=5
class Muro(pygame.sprite.Sprite):
    def __init__(self, archivoimagen,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivoimagen).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)

        #self.image=pygame.Surface([alto,ancho])
        self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.y=300
        self.rect.x=400
        self.muros1=[]
        self.dir=0
        self.vel=2
        self.var_x=2
        self.var_y=2

    def update(self):
        #self.rect.x+= self.var_x
        if self.dir==0:
            self.rect.x += self.var_x
            if self.rect.x>(ANCHO -self.rect.width):
                self.rect.x= ANCHO -self.rect.width
                #self.dir=5
        if self.dir==1:
            self.rect.x -= self.var_x
            if self.rect.x<(0):
                self.rect.x= 0
                #self.dir=5
        if self.dir==2:
            self.rect.y -= self.var_x
            if self.rect.y<(0):
                self.rect.y=0
                #self.dir=5
        if self.dir==3:
            self.rect.y += self.var_x
            if self.rect.y>(ALTO - self.rect.height):
                self.rect.y=ALTO - self.rect.height
                #self.dir=5
        l_col=pygame.sprite.spritecollide(self,self.muros1,False)

        for m in l_col:
            if self.dir==0:
                if self.rect.right > m.rect.left:
                    self.rect.right = m.rect.left
            if self.dir==1:
                if self.rect.left < m.rect.right:
                    self.rect.left = m.rect.right
            if self.dir==2:
                if self.rect.top < m.rect.bottom:
                    self.rect.top = m.rect.bottom

            if self.dir==3:
                if self.rect.bottom > m.rect.top:
                    self.rect.bottom = m.rect.top


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    fondo=pygame.image.load("fondo.jpg")

    #Misil1=Misil('misil.png')
    player=Player1('vegeto.png')
    Enemy=Enemigo('vegeta.png')
    muros = pygame.sprite.Group()
    todos=pygame.sprite.Group()



    for i in range(10):
        muro=Muro('muro.png',[0,64*(i)])
        todos.add(muro)
        muros.add(muro)

    for i in range(12):
        muro=Muro('muro.png',[64*(i),0])
        todos.add(muro)
        muros.add(muro)

    for i in range(12):
        muro=Muro('muro.png',[64*(i),534])
        todos.add(muro)
        muros.add(muro)

    for i in range(10):
        muro=Muro('muro.png',[734,64*(i)])
        todos.add(muro)
        muros.add(muro)

    for i in range(3):
        muro=Muro('muro.png',[250,64*(i)])
        todos.add(muro)
        muros.add(muro)

    muro=Muro('muro.png',[540,420])
    todos.add(muro)
    muros.add(muro)

    player.muros1= muros
    Enemy.muros1 = muros
    todos.add(player)
    todos.add(Enemy)
        #todos.add(muro)
#Piske=pagina para crear imagenes.png
#OpenGameArt pagina para descargar imagenes
#Aprender a utilizar a gimp

    fin=False
    reloj=pygame.time.Clock()
    puntos=0
    grito=pygame.mixer.Sound("shot.ogx")

    while not fin:
        #Capturar eventos
        pygame.mouse.set_visible(False)
        #pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    player.dir=0
                if event.key==pygame.K_LEFT:
                    player.dir=1

                if event.key==pygame.K_UP:
                    player.dir=2

                if event.key==pygame.K_DOWN:
                    player.dir=3

                if event.key==pygame.K_SPACE:
                    player.dir=4



            if event.type== pygame.QUIT:
                fin= True

        pantalla.blit(fondo,[0,0])
        todos.draw(pantalla)

        todos.update()
        #pantalla.fill(BLANCO)
        pygame.display.flip()
        reloj.tick(60)
