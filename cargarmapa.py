import pygame
import ConfigParser # lee bloques de datos


ANCHO = 800
ALTO = 600
  

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


	infomapa = ConfigParser.ConfigParser()
	infomapa.read('mapa.map')

	print infomapa.sections()
	archivo= infomapa.get('nivel','origen')

	c_x = int(infomapa.get('nivel', 'c_x'))
	c_y = int(infomapa.get('nivel', 'c_x'))
	#CARGAR INFO DE FONDO
	mattriz_img = Recortar(archivo, c_x, c_y)#devuelve arreglo de imagenes recortadas
	#pantalla.blit(mattriz_img[0][0],[0,0])
	#pygame.display.flip()

	mapa = infomapa.get('nivel','mapa').split('\n')# esto le quita el \n
	j=0
	y=0
	for l in mapa:
		#print l
		i=0
		for e in l:
			x=0+(i*c_x)
			gx = int(infomapa.get(e,'px'))
			gy = int(infomapa.get(e,'py'))
			pantalla.blit(mattriz_img[gx][gy], [x,y])
			i+=1
		j+=1
		y=0+(j*c_y)

	pygame.display.flip()
	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True