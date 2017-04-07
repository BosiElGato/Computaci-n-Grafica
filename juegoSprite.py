import pygame

import random

ANCHO=800
ALTO=600

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    fondo=pygame.image.load("fondo.jpg")
    plantilla=pygame.image.load('dbzsprites.png').convert_alpha()
    lista=[]
    reloj=pygame.time.Clock()
    for i in range(12):
        cuadro=plantilla.subsurface(0+(i*66),0,66,85)
        lista.append(cuadro)
    for i  in range(12):
            pantalla.blit(lista[i],[0+(i*66),0])
    #cuadro=plantilla.subsurface(0,0,67,94)
    fin = False
    while not fin:
        #Capturar eventos
        pygame.mouse.set_visible(False)
        #pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                fin= True

            pantalla.fill([0,0,0])
            pantalla.blit(lista[i],[100,100])
            i+=1
            if i== 12:
                i=0

        #todos.draw(pantalla)

        #todos.update()
        #pantalla.fill(BLANCO)
        pygame.display.flip()
        reloj.tick(10)
