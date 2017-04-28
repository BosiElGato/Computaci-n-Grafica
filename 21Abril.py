import pygame
import random
import sys
import ConfigParser # lee bloques de datos

AnchoImG = 72
AltoImg = 90

ANCHO=800
ALTO=600

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)

def pendiente(x0,x1,y0,y1):
    dy=y1-y0
    dx=x1-x0
    m=int(dy/dx)
    return m
def fun_rect(m,x0,x1,yo,y1):
    m=pendiente(x0,x1,y0,y1)
    y= m*x+y0

class Muro(pygame.sprite.Sprite):

	def __init__(self, img_objeto, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image=img_objeto
		self.rect=self.image.get_rect()
		self.rect.x=pos[0]
		self.rect.y=pos[1]


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
        self.muros=[]

    def update(self):
        if self.fps <7:
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
        '''if self.rect.bottom < 580:
            self.rect.y+=4
        else:
            self.rect.bottom=580'''
        l_col=pygame.sprite.spritecollide(self,self.muros,False)

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


class Misil(pygame.sprite.Sprite):
    def __init__(self, archivoimagen):
        pygame.sprite.Sprite.__init__(self)
        #self.image=pygame.Surface([alto,ancho])
        self.image=pygame.image.load(archivoimagen).convert_alpha()#el convert hace efectiva la transparencia
        #self.image.fill(color)
        self.rect=self.image.get_rect()
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
            else:
                self.x-=1
                self.y-=self.m
                self.rect.x=self.x
                self.rect.y=int(self.y)



class Nivel():

 	def __init__(self, archivo):
		self.interprete=ConfigParser.ConfigParser()
		self.interprete.read(archivo)
		self.origen= self.interprete.get('nivel','origen')
		self.c_ancho=int(self.interprete.get('nivel','cal'))
		self.c_alto=int(self.interprete.get('nivel','can'))
		self.mapa=self.interprete.get('nivel','mapa').split('\n')
		self.lsmuros=self.RetMuros()
		self.m = self.RetImagenes()
		self.infomapa=[]

	def RetMuros(self):
		lm=[]
		j=0
		posy=0
		for l in self.mapa:
			print l
			i=0
			posx=0
			for e in l:
				esm=int(self.interprete.get(e,'muro'))
				if esm ==1:
					imx = int(self.interprete.get(e,'px'))
					imy = int(self.interprete.get(e,'py'))
					posx=i*int(self.c_ancho)
					pos=[posx,posy]
					img=[imx,imy]
					info=[pos,img]
					print '[',posx,',', posy, '] [', imx, ',' ,imy,']'
					lm.append(info)
				i+=1
			j+=1
			posy=j*int(self.c_alto)

		return lm

	def RetImagenes(self):
		imagen = pygame.image.load(self.origen).convert()
		imagen_ancho, imagen_alto = imagen.get_size()
		tabla_fondos=[]
		for i in range(0, imagen_ancho/self.c_ancho):
			linea=[]
			tabla_fondos.append(linea)
			for j in range(0, imagen_alto/self.c_alto):
				cuadro = (i * self.c_ancho, j * self.c_alto, self.c_ancho, self.c_alto)
				linea.append(imagen.subsurface(cuadro))
		return tabla_fondos

if __name__ == '__main__':
    pygame.init()
    pantalla= pygame.display.set_mode([ANCHO,ALTO])
    fondo= pygame.image.load("fondo.jpg")
    goku=pygame.image.load("42x30.png").convert_alpha()
    #broly=pygame.image.load("Broly1.png").convert_alpha()
    todos= pygame.sprite.Group()
    muros=pygame.sprite.Group()
    RecorteAlto=42
    RecorteAncho=30
    #player13=Player1("goku24.png")
    cuadro=goku.subsurface(0,0,RecorteAncho,RecorteAlto)
    gamer=Player1(cuadro)

    info=Nivel('mapa.map')
    for lista in info.lsmuros:
        posm= lista[0]
        pmx = posm[0]
        pmy = posm[1]
        posi=lista[1]
        ix = posi[0]
        iy = posi[1]
        m=Muro(info.m[ix][iy],posm)
        muros.add(m)
        todos.add(m)




    #enemy = Enemigo(broly.subsurface(0,0,200,200))
    gamer.muros=muros
    todos.add(gamer)

    reloj = pygame.time.Clock()
    fin= False

    while not fin:
        #Capturar eventos
        pos=pygame.mouse.get_pos()
        #pygame.mouse.set_visible(False)
        #pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    gamer.dir=0
                    gamer.image=goku.subsurface(gamer.fps*RecorteAncho,RecorteAlto*2,RecorteAncho,RecorteAlto)
                if event.key==pygame.K_LEFT:
                    gamer.dir=1
                    gamer.image=goku.subsurface(0+(RecorteAncho*gamer.fps),RecorteAlto,RecorteAncho,RecorteAlto)
                if event.key==pygame.K_UP:
                    gamer.dir=2
                    gamer.image=goku.subsurface(0+(RecorteAncho*gamer.fps),RecorteAlto*3,RecorteAncho,RecorteAlto)
                if event.key==pygame.K_DOWN:
                    gamer.dir=3
                    gamer.image=goku.subsurface(0+(RecorteAncho*gamer.fps),0,RecorteAncho,RecorteAlto)
                if event.key==pygame.K_SPACE:
                    gamer.dir=4
                    gamer.image=goku.subsurface(gamer.fps*RecorteAncho,RecorteAlto*2,RecorteAncho,RecorteAlto)
                if event.key==pygame.K_b:
                    gamer.image=goku.subsurface(gamer.fps*RecorteAncho,RecorteAlto,RecorteAncho,RecorteAlto)
            if event.type== pygame.MOUSEBUTTONDOWN:
                b=Misil('misil.png')
                b.rect.x=gamer.rect.x+30
                b.rect.y=gamer.rect.y+30
                #b.disparoE=1
                b.Mover(pos)
                todos.add(b)
            pygame.display.flip()



                #print pos
            if event.type== pygame.QUIT:
                fin= True
        pantalla.blit(fondo,[0,0])


        todos.draw(pantalla)
        todos.update()

        reloj.tick(60)
