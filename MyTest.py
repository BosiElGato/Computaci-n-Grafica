import pygame
from MyLibrary import *


#ScreenSize(ANCHO,ALTO)


if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)

    Plan=plano(pantalla,CENTER)
    Plan.PlanoCartesiano()
    Plan.Punto([30,40])
    Plan.poli([[10,10],[50,10],[50,70]])
    Grados=0
    var_x=0
    Tam=0
    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type ==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    print ('letra a')
                if event.key==pygame.K_SPACE:
                    print ('Tecla espacio')
                if event.key==pygame.K_UP:
                   # print ('Tecla ARRIBA')
                    Grados+=15
                if event.key==pygame.K_DOWN:
                    Grados-=15
                   # print ('Tecla ABAJO')
                if event.key==pygame.K_RIGHT:
                    Tam+=1
                   # print ('Tecla DERECHA')
                if event.key==pygame.K_LEFT:
                   # print ('TeclaIZQUIERDA')
                    Tam-=1

        pygame.display.flip()
        Plan.poli([Plan.Rota([10,10],Grados),Plan.Rota([50,10],Grados),Plan.Rota([50,70],Grados)])
        Plan.poli([Plan.Escala([10,10],Tam),Plan.Escala([50,10],Tam),Plan.Escala([50,70],Tam)])
