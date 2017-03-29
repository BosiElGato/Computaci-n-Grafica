import pygame

ANCHO=800
ALTO=600


ROJO=[255,0,0]
VERDE=[0,255,0]
AZUL=[0,0,255]
BLANCO=[255,255,255]
NEGRO=[0,0,0]
C=(400,300)
var_y=10;
var_x=10;
reloj=pygame.time.Clock()
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    pygame.draw.line(pantalla,AZUL,[50,0],[50,200],3)
    fin= False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    print ('letra a')
                if event.key==pygame.K_SPACE:
                    print ('Tecla espacio')
                if event.key==pygame.K_UP:
                   # print ('Tecla ARRIBA')
                    var_y-=15
                if event.key==pygame.K_DOWN:
                    pygame.draw.line(pantalla,AZUL,[50+var_y,50],[50+var_y,0],3)
                    var_y+=15
                   # print ('Tecla ABAJO')
                if event.key==pygame.K_RIGHT:
                    var_x+=15
                   # print ('Tecla DERECHA')
                if event.key==pygame.K_LEFT:
                   # print ('TeclaIZQUIERDA')
                    var_x-=15
        pantalla.fill(BLANCO)
        pygame.draw.circle(pantalla,ROJO,[var_x,var_y],20,20)
        pygame.draw.rect(pantalla,AZUL,[40,0,400,40],40)
        pygame.draw.rect(pantalla,VERDE,[0,200,100,200],50)
        pygame.draw.rect(pantalla,NEGRO,[250,100,70,100],100)
        pygame.display.flip()
        reloj.tick(30)
