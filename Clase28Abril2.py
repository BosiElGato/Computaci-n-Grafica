import pygame
#Mostrar texto en pantalla
ALTO = 480
ANCHO = 640

BLANCO=(255,255,255)
VERDE=(0,255,0)
NEGRO=(0,0,0)

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pantalla.fill(NEGRO)
    fondo= pygame.image.load("BackGround.jpg")
    todos=pygame.sprite.Group()
    #jp=Jugador(50,30)
    #todos.add(jp)
    fx=0
    fy=0
    fin =False
    reloj=pygame.time.Clock()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print 'salto'
                    #jp.Salto()

        pantalla.blit(fondo,[fx,-1200])
        fx-=2
        #pantalla.fill(NEGRO)
        #todos.update()
        #todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
