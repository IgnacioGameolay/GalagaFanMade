import pygame,random
from Proyectiles import Proyectil_Enemigo
pygame.mixer.init()
class Enemigo():
    def __init__(self,select_img,health,enemy_x,enemy_y):
        pygame.sprite.Sprite.__init__(self)
        #Atributos
        self.select_img = select_img
        self.img = [pygame.transform.scale(pygame.image.load('img/enemys/ene1.png').convert_alpha(),(104,80)),
                    pygame.transform.scale(pygame.image.load('img/enemys/ene2.png').convert_alpha(),(104,80)),
                    pygame.transform.scale(pygame.image.load('img/enemys/ene3.png').convert_alpha(),(95,100)),
                    pygame.transform.scale(pygame.image.load('img/enemys/ene4.png').convert_alpha(),(120,128)),
                                ]
        self.health = health
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.speed = 1.25
        self.sound_dead = pygame.mixer.Sound("Sound/enemy_1_dead.mp3")
        self.sound_dead_boss = pygame.mixer.Sound("Sound/kill_boss.mp3")
        self.lista_balas_enemigo = []
        self.puntaje = 150
        self.contador_disparo = 1
        self.aumentar_dificultad = False
        self.num = 0
        if self.aumentar_dificultad == True:
            self.speed += 2
            self.aumentar_dificultad = False
    def mostrar_enemigo(self,superficie):
        superficie.blit(self.img[self.select_img],(self.enemy_x,self.enemy_y))
    def muerte_enemigo(self):
        self.health = 0
        self.sound_dead.play()
        if self.select_img == 3:
            self.sound_dead_boss.play()
    def morir(self,enemigo):
            enemigo.enemigos_lista.remove(enemigo)
    def movimiento_enemigo(self):
        if self.health > 0:
            self.enemy_x += self.speed
        if self.enemy_x >= 550:
            self.speed *= -1
            if self.select_img == 3:
                self.enemy_x = 0
            self.enemy_y += 30
        if self.enemy_x <= 0:
            self.speed *= -1
            self.enemy_y += 30
    def activar_disparo(self):
        if random.randint(0,100) < self.contador_disparo:
            self.disparar_enemigo()
    def disparar_enemigo(self):
        x = self.enemy_x
        y = self.enemy_y
        bala_enemigo = Proyectil_Enemigo(x,y)
        self.lista_balas_enemigo.append(bala_enemigo)
    def agregar_dificultad(self):
        if self.speed < 0:
            self.speed -= 1.5
        elif self.speed > 0:
            self.speed += 1.5
        return self.speed