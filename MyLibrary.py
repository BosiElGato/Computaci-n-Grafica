import pygame
import math
import sys

ANCHO =800
ALTO = 600

BLANCO =[255,255,255]
ROJO=[255,0,0]
VERDE=[0,255,0]
AZUL=[0,0,255]

ScreenSize=[ANCHO,ALTO]
CENTER=[ANCHO/2,ALTO/2]

class plano():

    def __init__(self, pantalla,centro):
        self.c= centro
        self.screen=pantalla

    def PlanoCartesiano(self):
        pygame.draw.line(self.screen,ROJO,[self.c[0],0],[self.c[0],int(self.c[1]*2)],1)
        pygame.draw.line(self.screen,ROJO,[0,self.c[1]],[int(self.c[0]*2),self.c[1]],1)

    def Transforma(self,p):
        px=int(self.c[0]+p[0])
        py=int(self.c[1]-p[1])
        return [px,py]

    def Punto(self,p):
        pygame.draw.circle(self.screen,ROJO,self.Transforma(p),2)

    def Linea (self,p,q):
        pygame.draw.line(self.screen,AZUL,self.Transforma(p),self.Transforma(q),1)

    def poli(self,l):
        listacartesiana=[]
        for elemento in l:
            p=self.Transforma(elemento)
            listacartesiana.append(p)
        pygame.draw.polygon(self.screen,AZUL,listacartesiana,1)

    def Rota(self,p,grad):
        rad=math.radians(grad)
        self.Transforma(p)
        X1=int((p[0]*(math.cos(rad)))+(p[1]*(math.sin(rad))))
        Y1=int((-(p[0]*(math.sin(rad))))+(p[1]*(math.cos(rad))))
        return [X1,Y1]

    def Escala(self,p,Escala):
        self.Transforma(p)
        X=p[0]*Escala
        Y=p[1]*Escala
        return [X,Y]
