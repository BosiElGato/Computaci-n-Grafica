import pygame
import ConfigParser # lee bloques de datos


ANCHO = 800
ALTO = 600

BLANCO = (255,255,255)
VERDE = (0,255,0)
NEGRO = (0,0,0)
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
            
if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO,ALTO])

    seguir=False
    Pagina=1
	fin = False
	reloj=pygame.time.Clock()
	while not fin:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
                    seguir=False
					fin = True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        Pagina+=1
                        if Pagina>2:
                            seguir=False
            pantalla.fill(NEGRO)
    		if pag ==1:
    			texto = fuente.render("HACE MUCHO TIEMPO...", True, BLANCO)
    			pantalla.blit(texto,[100,50])

    		elif pag ==2:
    			texto = fuente.render("Eddie revivio...", True, BLANCO)
    			pantalla.blit(texto,[100,30])
    			imagen = pygame.image.load('jugador.png')
    			imagen = pygame.transform.scale(imagen, (500,280))
    			pantalla.blit(imagen,[50,100])
    			pantalla.blit(texto,[100,100])

		pygame.display.flip()

        reloj = pygame.time.Clock()
    	while not fin:
    		pos = pygame.mouse.get_pos()
    		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
    				fin = True

    		pantalla.fill(NEGRO)
    		todos.draw(pantalla)
    		pantalla.blit(texto,[200,200])
