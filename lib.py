import pygame

ANCHO =800
ALTO = 600

BLANCO =[255,255,255]
ROJO=[255,0,0]
VERDE=[0,255,0]
AZUL=[0,0,255]

class Cartesiano():
    def __init__(self,pantalla,centro):
        self.c=centro
        self.pan=pantalla

    def Ejes(self):
        pygame.draw.line(self.pan,ROJO,[self.c[0],0],[self.c[0],int(self.c[1]*2)],1)
        pygame.draw.line(self.pan,ROJO,[0,self.c[1]],[int(self.c[0]*2),self.c[1]],1)

    def Transforma(self,p):
        px=int(self.c[0]+p[0])
        py=int(self.c[1]-p[1])
        return [px,py]

    def Punto(self,p):
        pygame.draw.circle(self.pan,ROJO,self.Transforma(p),2)

    def Linea (self,p,q):
        pygame.draw.line(self.pan,AZUL,self.Transforma(p),self.Transforma(q),1)

    def poli(self,l):
        listacartesiana=[]
        for elemento in l:
            p=self.Transforma(elemento)
            listacartesiana.append(p)
        pygame.draw.polygon(self.pan,AZUL,listacartesiana,1)

    def Vector(self,p):
        pygame.draw.line(self.pan,AZUL,self.Transforma([0,0]),self.Transforma(p),1)

    #def SumaVector(self,p,q):
