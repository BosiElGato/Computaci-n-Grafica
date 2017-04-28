import pygame
import ConfigParser # lee bloques de datos


ANCHO = 800
ALTO = 600
  
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
		self.origen= self.interprete.get('nivel3','origen')
		self.c_ancho=int(self.interprete.get('nivel3','cal'))
		self.c_alto=int(self.interprete.get('nivel3','can'))
		self.mapa=self.interprete.get('nivel3','mapa').split('\n')
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

	todos=pygame.sprite.Group()
	muros=pygame.sprite.Group()

	info=Nivel('mapa3.map')
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
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					fin = True