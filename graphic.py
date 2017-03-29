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
escala = 2
def escalamientoX(x,Sx):
    r=x*Sx
    return Xprima(r)

def escalamientoY(y,Sy):
    s=y*Sy
    return Yprima(s)
#Funcion que rota las figuras
rot = math.radians(90)
def Xrotacion(X1,Y1,Grados):
    re1=int((X1*(math.cos(Grados)))+(Y1*(math.sin(Grados))))
    retrx=Xprima(re1)
    return retrx

def Yrotacion(X2,Y2,Grados):
    re2=int((-(X2*(math.sin(Grados))))+(Y2*(math.cos(Grados))))
    retry=Yprima(re2)
    return retry

#Funcion para poner un punto en la pantalla, esta recibe un punto
def Punto(p,r=1):
    pygame.draw.circle(pantalla,AZUL,p,r)

#Funcion para dibujar un plano cartesiano en una pantalla
def Plano():
    pygame.draw.line(pantalla,AZUL,[C[0],0],[C[0],C[0]*2],1)
    pygame.draw.line(pantalla,AZUL,[0,C[1]],[ANCHO,C[1]],1)

def poligono(Punto1,Punto2,Punto3):
    pygame.draw.polygon(pantalla,AZUL,[Punto1,Punto2,Punto3],3)


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    #pygame.draw.line(pantalla,VERDE,[Xprima(20),Yprima(10)],[Xprima(60),Yprima(10)],15)
    #pygame.draw.line(pantalla,VERDE,[Xrotacion(20,10,rot ),Yrotacion(20,10,rot )],[Xrotacion(60,10,rot ),Yrotacion(60,10,rot )],15)
    #pygame.draw.circle(pantalla,AZUL,[10,10],2)
    #Llamado a las funciones de transformacion lineal
    Xtrans=Xprima(-50)
    Ytrans=Yprima(-50)
    Punto([Xtrans,Ytrans])
    #==========================================
    #Funcion para hacer un triangulo en la pnatalla
    Xtransp1=Xprima(20)
    Ytransp1=Yprima(10)
    Xtransp2=Xprima(60)
    Ytransp2=Yprima(10)
    Xtransp3=Xprima(60)
    Ytransp3=Yprima(30)

    PuntoPol1=([Xtransp1,Ytransp1])
    PuntoPol2=([Xtransp2,Ytransp2])
    PuntoPol3=([Xtransp3,Ytransp3])
    poligono(PuntoPol1,PuntoPol2,PuntoPol3)
    #=========================================
    #Funciones de escalamiento para el triangulo

    X1=escalamientoX(20,escala)
    Y1=escalamientoY(10,escala)
    X2=escalamientoX(60,escala)
    Y2=escalamientoY(10,escala)
    X3=escalamientoX(60,escala)
    Y3=escalamientoY(30,escala)

    Punto1=([X1,Y1])
    Punto2=([X2,Y2])
    Punto3=([X3,Y3])
    poligono(Punto1,Punto2,Punto3)
    #Funcion para rotar una figura en un plano
    X6=Xrotacion(20,10,rot)
    Y6=Yrotacion(20,10,rot)
    X4=Xrotacion(60,10,rot)
    Y4=Yrotacion(60,10,rot)
    X5=Xrotacion(60,30,rot)
    Y5=Yrotacion(60,30,rot)
    Punto6=([X6,Y6])
    Punto4=([X4,Y4])
    Punto5=([X5,Y5])
    poligono(Punto6,Punto4,Punto5)


    Plano()
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
