import pygame
import random
import sys

AnchoImG = 72
AltoImg = 90

ANCHO=800
ALTO=600

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        #self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.image=archivoimagen
        self.rect=self.image.get_rect()
        self.rect.x=600
        self.rect.y=400
        self.der=0
        self.vel=2
        #self.temporizador=100
        self.temporizador=random.randint(50,150)
        self.disparo=0
        self.fps=0
        self.pos=[0,0]

    def update(self):
        if self.fps <2:
            self.fps+=1
        else:
            self.fps=0
        self.temporizador-=1
        if self.temporizador==0:
            self.disparo=1
            self.temporizador=random.randint(50,150)
        else:
            self.disparo=0
        if self.rect.x>self.pos[0]+70:
            self.rect.x-=2
        else:
            self.rect.x=self.pos[0]+70
        if self.rect.y>self.pos[1]:
            self.rect.y-=2
        else:
            self.rect.y=self.pos[1]
            #self.temporizador=random.randint(50,150)


class Player1(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        #self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.image=archivoimagen
        self.rect=self.image.get_rect()
        self.rect.y=300
        self.rect.x=400
        self.var_x=10
        self.var_y=10
        self.dir=0#cero para desplazarse a la derecha y uno para la izquierda
        self.fps=0
        self.gravity=0

    def update(self):
        if self.fps <2:
            self.fps+=1
        else:
            self.fps=0
        if self.dir==0:
            self.rect.x += self.var_x
        if self.dir==1:
            self.rect.x -= self.var_x
        if self.dir==2:
            self.rect.y -= self.var_y*4
        if self.dir==3:
            self.rect.y += self.var_y
        self.dir=5
        if self.rect.bottom < 600:
            self.rect.y+=4
        else:
            self.rect.bottom=600
class Misil(pygame.sprite.Sprite):
    def __init__(self, archivoimagen,pos):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.disparoE=0

    def update(self):
        if self.disparoE == 0:
            self.rect.x-=5
        else:
            self.rect.x+=5





if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO,ALTO])
    fondo= pygame.image.load("fondo.jpg")
    goku=pygame.image.load("grande.png").convert_alpha()
    broly=pygame.image.load("Broly1.png").convert_alpha()
    todos= pygame.sprite.Group()
    #player13=Player1("goku24.png")

    cuadro=goku.subsurface(0,0,200,200,)
    gamer=Player1(cuadro)
    enemy = Enemigo(broly.subsurface(0,0,200,200))




    todos.add(gamer,enemy)

    reloj = pygame.time.Clock()
    fin= False
    while not fin:
        #Capturar eventos
        pygame.mouse.set_visible(False)
        #pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    gamer.dir=0
                    gamer.image=goku.subsurface(gamer.fps*200,0,200,200)
                if event.key==pygame.K_LEFT:
                    gamer.dir=1
                    gamer.image=goku.subsurface(0,0,200,200)
                if event.key==pygame.K_UP:
                    gamer.dir=2

                if event.key==pygame.K_DOWN:
                    gamer.dir=3

                if event.key==pygame.K_SPACE:
                    gamer.dir=4
                    b=Misil('misil.png',[gamer.rect.x+120,gamer.rect.y+120])
                    #grito.play()
                    b.disparoE=1
                    todos.add(b)
                    #balas.add(b)
                    gamer.image=goku.subsurface(gamer.fps*200,400,200,200)
                if event.key==pygame.K_b:
                    gamer.image=goku.subsurface(gamer.fps*200,200,200,200)
            if event.type== pygame.QUIT:
                fin= True
            enemy.image=broly.subsurface(enemy.fps*200,200,200,200)
            enemy.pos=[gamer.rect.x,gamer.rect.y]
            if enemy.disparo==1:
                b=Misil('misil.png',[gamer.rect.x+120,gamer.rect.y+120])
                #grito.play()
                b.disparoE=0
                todos.add(b)
        pantalla.blit(fondo,[0,0])
        #if gamer.rect.bottom != pantalla.get_height():
        #    gamer.gravity()


        todos.draw(pantalla)

        todos.update()
        #pantalla.fill(BLANCO)
        pygame.display.flip()
        reloj.tick(30)
