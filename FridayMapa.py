import pygame
import ConfigParser

ANCHO = 800
ALTO = 600

class Muro(pygame.sprite.Sprite):
	def __init__(self,im_obj,pos):
		pygame.sprite.Sprite.__init__(self)
		self.image=im_obj
		self.rect=self.image.get_rect()
		self.rect.x=pos[0]
		self.rect.y=pos[1]

class nivel():
	def __init__(self,archivo):
		self.interprete=ConfigParser.ConfigParser()
		#print interprete.get('nivel','origen')
		self.interprete.read(archivo)
		self.origen=self.interprete.get('nivel','origen')
		self.c_ancho=int(self.interprete.get('nivel','c_x'))
		self.c_alto=int(self.interprete.get('nivel','c_y'))
		self.mapa=self.interprete.get('nivel','mapa').split('\n')
		self.lsmuros=self.RetMuros()
		self.infomapa=[]

	def RetMuros(self):
		lm=[]
		j=0
		i=0
		posy=0
		for l in self.mapa:
			print l
			for e in l:
				posx=0
				esm=int(self.interprete.get(e,'muro'))
				if esm==1:
					imx=int(self.interprete.get(e,'px'))
					imy=int(self.interprete.get(e,'py'))
					posx=i * int(self.c_ancho)
					print posx
				i+=1
			j+=1
			posy=j * int(self.c_alto)
		return lm
	def retimagen(self):
		imagen = pygame.image.load(self.origen).convert()
		imagen_ancho,imagen_alto=imagen.get.size()
		tabla_fondos=[]
		for fondo_x in range(0,imagen_ancho/self.c_alto):
			linea=[]
			tabla_fondos.append(linea)
			for fondo_y in range(0,imagen_alto/self.c_alto):
				cuadro=(fondo_x *ancho,fondo_y*alto, ancho,alto)
				linea.append(imagen.subsurface(cuadro))

			return tabla_fondos





def Recortar(archivo, cx, cy):
	imagen = pygame.image.load(archivo)

	ancho_img, alto_img = imagen.get_size()#devuelve tamanio de la imagen
	lon_x = ancho_img /cx # es igual a 16
	lon_y = alto_img/cy
	m=[] # lista de filas de varios cuadros
	y=[]
	for i in range(lon_x):
		fila=[]
		for j in range(lon_y): # range sera de 0 a 16
			cuadro = imagen.subsurface(0+(i*cx),0 + (j*cy),cx,cy)
			fila.append(cuadro)
		m.append(fila)
	return m


if __name__ == '__main__':
	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO,ALTO])
	imagen=pygame.image.load('Imagen2.png')
	cx=64
	cy=64
	img_ancho,img_alto = imagen.get_size()
	print img_ancho,img_alto
	m=[]
	lim_an=img_ancho/cx
	lim_al=img_alto/cy
	for j in range(lim_al):
		ls=[]
		for i  in range(lim_an):
			cuadro=imagen.subsurface(0 +(i*cx),0+(j*cy),cx,cy)
			ls.append(cuadro)
			#pantalla.blit(ls[i],[0+(i*cx),0+(j*cy)])
		m.append(ls)
	#pantalla.blit(m[0][0],[0,0])
	todos=pygame.sprite.Group()
	muros=pygame.sprite.Group()
	info=nivel('mapa.bosi')
	for lista in info.lsmuros:
		posm=lista[0]
		pmx=posm[0]
		pmy=posm[1]
		ix=posi[0]
		iy=posi[1]
		posi=lista[0]
		print posm, posi
		m=Muro(m[ix][iy],posm)
		muros.add(m)
		todos.add(m)

	todos.draw(pantalla)
	pygame.display.flip()


	#infomapa = ConfigParser.ConfigParser()
	#infomapa.read('mapa.bosi')

	#archivo= infomapa.get('nivel','origen')


	#mapa = infomapa.get('nivel','mapa').split('\n')

	pygame.display.flip()
	fin = False

	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True
