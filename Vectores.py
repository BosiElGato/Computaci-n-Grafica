import pygame

from lib import*


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    plano=Cartesiano(pantalla,[ANCHO/2,ALTO/2])

    print (plano.c)
    plano.Ejes()
    #plano.Linea([10,30],[50,30])
    #plano.Punto([50,30])
    #plano.poli([[10,10],[60,10],[35,35]])
    plano.Vector([50,60])
    pygame.display.flip
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
