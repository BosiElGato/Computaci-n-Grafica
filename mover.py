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
            self.rect.y+=5
        else:
            self.rect.y-=5

class Player1(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.y=ALTO-self.rect.height
        self.rect.x=50
        self.var_x=2
        self.dir=0#cero para desplazarse a la derecha y uno para la izquierda

    def update(self):
        #self.rect.x+= self.var_x
        if self.dir==0:
            self.rect.x += self.var_x
        if self.dir==1:
            self.rect.x -= self.var_x



class Enemigo(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.rect=self.image.get_rect()
        self.der=0
        self.vel=2
        #self.temporizador=100
        self.temporizador=random.randint(50,150)
        self.disparo=0

    def update(self):
        self.temporizador-=1
        if self.temporizador==0:
            self.disparo=1
            self.temporizador=random.randint(50,150)
        else:
            self.disparo=0
            #self.temporizador=random.randint(50,150)

        if self.rect.x > (ANCHO-self.rect.width):
            #if self.rect.x%10==0:
                #self.disparo==1
            #else:
            #    self.disparo==0
            self.der=1
            self.vel+=1
        if self.rect.x < 2:
            self.der=0
        if self.der==0:
            self.rect.x+=self.vel
        else:
            self.rect.x-=self.vel

        '''if self.rect.x%10 ==0:
            self.disparo=1
        else:
            self.disparo=0'''



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    fondo=pygame.image.load("fondo.jpg")

    #Misil1=Misil('misil.png')
    player=Player1('vegeto.png')
    todos=pygame.sprite.Group()
    Enemigos=pygame.sprite.Group()
    balas =pygame.sprite.Group()
    balasEnemigas=pygame.sprite.Group()
    Players=pygame.sprite.Group()
    #todos.add(Misil1)
    Players.add(player)
    todos.add(player)

    for i in range(5):
        b1=Enemigo('vegeta.png')
        b1.rect.x=random.randint(10,(ANCHO-b1.rect.width))
        b1.rect.y=random.randint(10,(ALTO-100))
        #bloques.add(b1)
        Enemigos.add(b1)
        todos.add(player)
        todos.add(b1)

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
                if event.key == pygame.K_SPACE:
                    b=Misil('misil.png',[player.rect.x,player.rect.y])
                    grito.play()
                    b.disparoE=1
                    todos.add(b)
                    balas.add(b)

            if event.type== pygame.QUIT:
                fin= True
        #Logica de interaccion del juego

        #player.rect.x=pos[0]
        #player.rect.y=pos[1]
        #Misil1.rect.x=pos[0]
        #Misil1.rect.y=pos[1]
        #Lista de cuadros golpeados si el tercer argumento esta en false no se desaparecen los obstaculos
        lg=pygame.sprite.spritecollide(player,Enemigos,True)
        #ListaColision=pygame.sprite.spritecollide(balas,Enemigos,True)
        for e in Enemigos:
            if e.disparo==1:
                b=Misil('misil.png',[e.rect.x,e.rect.y])
                grito.play()
                b.disparoE=0
                todos.add(b)
                balasEnemigas.add(b)

            # l_Impactosenemigos=pygame.sprite.spritecollide(b,Players,True)
        for s in balasEnemigas:
            l_Impactosenemigos=pygame.sprite.spritecollide(s,Players,True)
            for r in l_Impactosenemigos:
                balasEnemigas.remove(r)
                todos.remove(r)

        for b in balas:
            l_impactos=pygame.sprite.spritecollide(b,Enemigos,True)
            for e in l_impactos:
                balas.remove(b)
                todos.remove(b)
                puntos+=1
        pantalla.blit(fondo,[0,0])
        #pantalla.fill(BLANCO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
