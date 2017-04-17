import pygame
import ConfigParser # lee bloques de datos
'''
$$$$$$$$$$$$$$$$$$$$$$$$$
		  $.......................$
		  $.......................$
		  $.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$.......................$
			$$$$$$$$$$$$$$$$$$$$$$$$$'''

ANCHO = 800
ALTO = 600

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
class Muro(pygame.sprite.Sprite):

	def __init__(self, img_objeto, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image=img_objeto
		self.rect=self.image.get_rect()
		self.rect.x=pos[0]
		self.rect.y=pos[1]

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
	pantalla = pygame.display.set_mode([ANCHO,ALTO])
    goku=pygame.image.load("grande.png").convert_alpha()
	todos=pygame.sprite.Group()
	muros=pygame.sprite.Group()

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

	todos.draw(pantalla)
	pygame.display.flip()





	fin = False
	reloj=pygame.time.Clock()
	while not fin:
			pygame.mouse.set_visible(False)
            #pos=pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        gamer.dir=0
                        gamer.image=goku.subsurface(gamer.fps*128,128,128,128)
                    if event.key==pygame.K_LEFT:
                        gamer.dir=1
                        gamer.image=goku.subsurface(0,0,128,128)
                    if event.key==pygame.K_UP:
                        gamer.dir=2

                    if event.key==pygame.K_DOWN:
                        gamer.dir=3

                    if event.key==pygame.K_SPACE:
                        gamer.dir=4
                        b=Misil('misil.png',[gamer.rect.x+128,gamer.rect.y+128])
                        #grito.play()
                        b.disparoE=1
                        todos.add(b)
                        #balas.add(b)
                        gamer.image=goku.subsurface(gamer.fps*128,256,128,128)
                    if event.key==pygame.K_b:
                        gamer.image=goku.subsurface(gamer.fps*128,128,128,128)
				if event.type == pygame.QUIT:
					fin = True
