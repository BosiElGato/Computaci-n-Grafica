import pygame

ANCHO = 800
ALTO = 600

BLANCO=(255,255,255)
VERDE=(0,255,0)
NEGRO=(0,0,0)

class player(pygame.sprite.Sprite):
    def __init__(self,archivo,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(archivo)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.finx=0

    def update(self):
        pass



if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(NEGRO)
    todos=pygame.sprite.Group()
    fuente = pygame.font.SysFont("monospace", 50)
    cont= 1
    jugador=player('girl.png',[0,0])
    todos.add(jugador)
    #fuente = pygame.font.SysFont("comicsansms", 72)
    #fuente=pygame.font.Font(None,34)

    #texto1=fuente.render(cont,True, BLANCO)

    #pantalla.blit(texto1,[100,200])
    pygame.display.flip()

    reloj= pygame.time.Clock()
    fin = False
    while not fin:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        pantalla.fill(NEGRO)
        todos.draw(pantalla)
        txt = "pos" + str(pos[0])+","+str(pos[1])
        texto=fuente.render(txt,True, BLANCO)
        pantalla.blit(texto,[100,500])
        pygame.display.flip()
        reloj.tick()
