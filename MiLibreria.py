import pygame
import math
ANCHO=800
ALTO=600


ROJO=[255,0,0]
VERDE=[0,255,0]
AZUL=[0,0,255]
BLANCO=[255,255,255]
NEGRO=[0,0,0]
C=(400,300)
#Funciones para la transformacion lineal de la pantalla al palno cartesiano

def Xprima(Cx):
    return(C[0]+Cx)


def Yprima(Cy):
    return(C[1]-Cy)
#===============================================0========
#Funcion que cambia el tamano de las figuras
escala=3
def EscalamientoX(x,Sx):
    r=x*Sx
    return r

def EscalamientoY(y,Sy):
    s=y*Sy
    return s

#Funcion que rota las figuras
rot = math.radians(90)
def Xrotacion(X1,Y1,Grados):
    rad=math.radians(Grados)
    re1=int((X1*(math.cos(rad)))+(Y1*(math.sin(rad))))
    return re1

def Yrotacion(X2,Y2,Grados):
    rad=math.radians(Grados)
    re2=int((-(X2*(math.sin(rad))))+(Y2*(math.cos(rad))))
    return re2

#Funcion para poner un punto en la pantalla, esta recibe un punto
def Punto(pantalla,punto,r=10):
    punto[0]=Xprima(punto[0])
    punto[1]=Yprima(punto[1])
    pygame.draw.circle(pantalla,AZUL,punto,r)

#Funcion para dibujar un plano cartesiano en una pantalla
def Plano(pantalla):
    pygame.draw.line(pantalla,AZUL,[C[0],0],[C[0],C[0]*2],1)
    pygame.draw.line(pantalla,AZUL,[0,C[1]],[ANCHO,C[1]],1)
    
#Funcion para dibujar un triangulo en un plano cartesiano 
def Triangulo(pantalla,Punto1,Punto2,Punto3):
    Punto1[0]=Xprima(Punto1[0])
    Punto2[0]=Xprima(Punto2[0])
    Punto3[0]=Xprima(Punto3[0])
    Punto1[1]=Yprima(Punto1[1])
    Punto2[1]=Yprima(Punto2[1])
    Punto3[1]=Yprima(Punto3[1])
    pygame.draw.polygon(pantalla,VERDE,[Punto1,Punto2,Punto3],2)
#Funcion que cambia el tamaño de un triangulo en el plano cartesiano 
def TrianguloEscalado(pantalla,pun1,pun2,pun3,NivelEscalado):
        pun1=[EscalamientoX(pun1[0],NivelEscalado),EscalamientoY(pun1[1],NivelEscalado)]
        pun2=[EscalamientoX(pun2[0],NivelEscalado),EscalamientoY(pun2[1],NivelEscalado)]
        pun3=[EscalamientoX(pun3[0],NivelEscalado),EscalamientoY(pun3[1],NivelEscalado)]
        Triangulo(pantalla,pun1,pun2,pun3)
        
def TrianguloRotador(pantalla,punt1,punt2,punt3,Rotacion):
    punt1=[Xrotacion(punt1[0],punt1[1],Rotacion),Yrotacion(punt1[0],punt1[1],Rotacion)]
    punt2=[Xrotacion(punt2[0],punt2[1],Rotacion),Yrotacion(punt2[0],punt2[1],Rotacion)]
    punt3=[Xrotacion(punt3[0],punt3[1],Rotacion),Yrotacion(punt3[0],punt3[1],Rotacion)]
    Triangulo(pantalla,punt1,punt2,punt3)

reloj=pygame.time.Clock()
#Funciion para di
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    Plano(pantalla)
    var_y=0
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
                            var_y+=15
                           # print ('Tecla ABAJO')
                        if event.key==pygame.K_RIGHT:
                            var_x+=15
                           # print ('Tecla DERECHA')
                        if event.key==pygame.K_LEFT:
                           # print ('TeclaIZQUIERDA')
                            var_x-=15
                 
        pygame.display.flip()
        #Triangulo(pantalla,[0,0],[50,0],[25,25])
        #Punto(pantalla,[26,26])
        #TrianguloEscalado(pantalla,[0,0],[50,0],[25,25],5)
        TrianguloRotador(pantalla,[0,0],[50,0],[25,25],var_y)
        reloj.tick(30)
        
        
        

    
