import pygame,time
from Proyectiles import Proyectil_Jugador
from Misc import Corazon
pygame.mixer.init()
class Nave():
    def __init__(self,health):
        pygame.sprite.Sprite.__init__(self)
        #Atributos
        self.img = pygame.transform.scale(pygame.image.load("img/spaceship/spaceship1.png").convert_alpha(),(140,140))
        self.img_1 = pygame.transform.scale(pygame.image.load("img/spaceship/spaceship1_1.png").convert_alpha(),(140,140))
        self.img_propulsor_1 = pygame.transform.scale(pygame.image.load("img/spaceship/spaceship2.png").convert_alpha(),(144,138))
        self.img_propulsor_2 = pygame.transform.scale(pygame.image.load("img/spaceship/spaceship3.png").convert_alpha(),(144,138))
        self.img_propulsor_3 = pygame.transform.scale(pygame.image.load("img/spaceship/spaceship4.png").convert_alpha(),(144,138))
        self.img_propulsor_4 = pygame.transform.scale(pygame.image.load("img/spaceship/spaceship5.png").convert_alpha(),(144,138))
        self.img_exp_1 = pygame.transform.scale(pygame.image.load("img/explosion/exp0.png").convert_alpha(),(144,138))
        self.img_exp_2 = pygame.transform.scale(pygame.image.load("img/explosion/exp1.png").convert_alpha(),(144,138))
        self.img_exp_3 = pygame.transform.scale(pygame.image.load("img/explosion/exp2.png").convert_alpha(),(144,138))
        self.img_exp_4 = pygame.transform.scale(pygame.image.load("img/explosion/exp3.png").convert_alpha(),(144,138))
        self.img_exp_5 = pygame.transform.scale(pygame.image.load("img/explosion/exp4.png").convert_alpha(),(144,138))

        self.lista_img = [self.img, self.img_1]
        self.lista_img_propulsores = [self.img_propulsor_1, self.img_propulsor_2, self.img_propulsor_3, self.img_propulsor_4]
        self.lista_img_explosiones = [self.img_exp_1,self.img_exp_2,self.img_exp_3,self.img_exp_4,self.img_exp_5]

        self.select_img_nave = 0
        self.select_img_propulsores = 0
        self.select_img_exp = 0

        self.animacion_img = self.lista_img[self.select_img_nave]
        self.animacion_img_propulsores = self.lista_img_propulsores[self.select_img_propulsores]
        self.animacion_img_explosiones = self.lista_img_explosiones[self.select_img_exp]

        self.contador_cambio_animacion = 1
        self.contador_cambio_animacion_2 = 1
        self.contador_cambio_animacion_3 = 1

        self.health = health
        self.spaceship_x = 235  #screen_x = 600
        self.spaceship_y = 750  #screen_y = 900
        self.speed = 40
        self.vivir = True

        self.balas = []
        self.vidas = []

        self.sonido_disparo = pygame.mixer.Sound('Sound/shoot_theme.mp3')
        self.sonido_muerte_nave = pygame.mixer.Sound('Sound/spaceship_dead_theme.mp3')
        self.sonido_perder_vida_nave = pygame.mixer.Sound('Sound/3.mp3')
        self.poder_disparar = True

    #Metodos
    def dibujar_nave(self,superficie):
        if self.health > 0:
            self.animacion_img = self.lista_img[self.select_img_nave]
            self.animacion_img_propulsores = self.lista_img_propulsores[self.select_img_propulsores]
            superficie.blit(self.animacion_img_propulsores,(self.spaceship_x-2,self.spaceship_y+2))
            superficie.blit(self.animacion_img,(self.spaceship_x,self.spaceship_y))
        if self.health <= 0:
            self.animacion_img_explosiones = self.lista_img_explosiones[self.select_img_exp]
            superficie.blit(self.animacion_img_explosiones,(self.spaceship_x,self.spaceship_y))
            self.health -= 1

    def animacion_nave(self,tiempo):
        if self.contador_cambio_animacion == tiempo:
            self.select_img_nave += 1
            self.contador_cambio_animacion += 1
            if self.select_img_nave > len(self.lista_img) - 1:
                self.select_img_nave = 0

    def animacion_propulsores(self,tiempo_2):
        #print('prop')
        if self.contador_cambio_animacion_2 == tiempo_2:
            self.select_img_propulsores += 1
            self.contador_cambio_animacion_2 += 1
            if self.select_img_propulsores > len(self.lista_img_propulsores) - 1:
                self.select_img_propulsores = 0

    def animacion_explosiones(self,tiempo_3):
        if self.contador_cambio_animacion_3 == tiempo_3:
            self.select_img_exp += 1
            self.contador_cambio_animacion_3 += 1
            if self.select_img_exp > len(self.lista_img_explosiones)-1:
                self.select_img_exp = 0



    def disparar(self,x,y):
        bala_jugador = Proyectil_Jugador(x,y)
        self.balas.append(bala_jugador)
        self.sonido_disparo.play()
    def perder_vida_nave(self):
        self.sonido_perder_vida_nave.play()
        self.health = self.health - 1
    def muerte_nave(self):
        if self.health == 0:
            self.sonido_perder_vida_nave.stop()
            self.sonido_muerte_nave.set_volume(4)
            self.sonido_muerte_nave.play()