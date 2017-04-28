import pygame
#Mostrar texto en pantalla
ALTO = 480
ANCHO = 640

BLANCO=(255,255,255)
VERDE=(0,255,0)
NEGRO=(0,0,0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, al,an):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.velocidad=2
        self.vary=0
        self.saltar=0
        self.dir=0

    def Salto(self):
        print 'salto'
        self.vary=-10


    def gravedad(self):
        if self.vary ==0:
            self.vary=1
        else:
            self.vary += 0.35

        piso=ALTO- self.rect.height
        if self.rect.y >= piso and self.vary>=0:
            self.vary=0
            self.rect.y=piso


    def update(self):
        self.gravedad()
        #self.rect.x+=self.velocidad
        self.rect.y+=self.vary
        if self.dir==0:
            self.rect.x += 2
            if self.rect.x >(ANCHO-self.rect.width):
                self.rect.x = ANCHO-30
            else:
                self.rect.x+=self.velocidad
        elif self.dir==1:
            self.rect.x -= 2
            if self.rect < 2:
                self.rect.x=0
            else:
                self.rect.x+=self.vary

                        #if self.dir==2:
        #    self.rect.y -= 2
        #if self.dir==3:
        #    self.rect.y += 2
        #self.dir=5

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pantalla.fill(NEGRO)
    fondo= pygame.image.load("BackGround.jpg")
    t_alto,t_ancho=fondo.get_size()
    todos=pygame.sprite.Group()
    jp=Jugador(50,30)
    todos.add(jp)
    fx=0
    fin =False
    reloj=pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        jp.dir=0
                    if event.key==pygame.K_LEFT:
                        jp.dir=1
                    if event.key==pygame.K_UP:
                        jp.dir=2
                    if event.key==pygame.K_DOWN:
                        jp.dir=3
                if event.key == pygame.K_SPACE:
                    print 'salto'
                    jp.Salto()

        if jp.rect.right > 500 and jp.dir==0:
            #fx-=2
            jp.rect.right=500
            if fx > ANCHO-t_ancho:
                fx-=2
            else:
                fx=ANCHO-t_ancho
        if jp.rect.right <100 and jp.dir==1:
            #fx+=2
            jp.rect.right=100
            print fx
            if fx < 0 :
                fx+=2
            else:
                fx=0




        pantalla.blit(fondo,[fx,-900])

        #pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
