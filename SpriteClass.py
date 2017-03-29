import pygame
import random

ANCHO=800
ALTO=600

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
#jug=pygame.image.load("player.png")
#ene=pygame.image.load("enemy.png")
class Misil(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.rect=self.image.get_rect()


class Bloque(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.rect=self.image.get_rect()



class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.rect=self.image.get_rect()
        self.der=0
        self.vel=2

    def update(self):
        if self.rect.x==(ANCHO-self.rect.width):
            self.der=1

        if self.rect.x==0:
            self.der=0

        if self.der==0:
            self.rect.x+=self.vel
        else:
            self.rect.x-=self.vel

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)

    Misil1=Misil('misil.png')
    player=Bloque('vegeto.png')
    todos=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    todos.add(Misil1)
    todos.add(player)

    for i in range(5):
        b1=Enemigo('vegeta.png')
        b1.rect.x=random.randint(10,(ANCHO-b1.rect.width))
        b1.rect.y=random.randint(10,(ALTO-b1.rect.height))
        bloques.add(b1)
        todos.add(player)
        todos.add(b1)

#Piske=pagina para crear imagenes.png
#OpenGameArt pagina para descargar imagenes


    fin=False
    reloj=pygame.time.Clock()
    puntos=0
    while not fin:
        pygame.mouse.set_visible(False)
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                fin= True

        player.rect.x=pos[0]
        player.rect.y=pos[1]
        Misil1.rect.x=pos[0]
        Misil1.rect.y=pos[1]
        #Lista de cuadros golpeados si el tercer argumento esta en false no se desaparecen los obstaculos
        lg=pygame.sprite.spritecollide(player,bloques,True)

        for b in lg:
            puntos+=1
            print (puntos)

        pantalla.fill(BLANCO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
