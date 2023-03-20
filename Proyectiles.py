import pygame
'''Jugador'''
class Proyectil_Jugador:
    def __init__(self,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.scale(pygame.image.load('img/misc/bullet.png').convert_alpha(),(18,34))
        self.speed = 12
        self.pos_x = pos_x + 62
        self.pos_y = pos_y - 32
        self.matar = False
        self.atacar = False
    def mover_bala_jugador(self):
        self.pos_y -= self.speed

    def dibujar_bala_jugador(self, superficie):
        superficie.blit(self.img,(self.pos_x,self.pos_y))

    def matar_enemigo(self):
        self.matar = True

    def detectar_muerte_enemigo(self):
        if self.matar == True:
            self.pos_y = -100

""""ENEMIGO"""
class Proyectil_Enemigo:
    def __init__(self,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.pos_x = pos_x + 40
        self.pos_y = pos_y + 110
        self.trayectoria_y = pos_y
        self.img = pygame.transform.scale(pygame.image.load('img/misc/bullet_enemigo.png').convert_alpha(),(18,34))
    def mover_bala_enemigo(self):
        if self.speed == 10:
            self.trayectoria_y += self.speed
    def dibujar_bala_enemigo(self, superficie):
        superficie.blit(self.img,(self.pos_x,self.trayectoria_y))

