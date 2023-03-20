import pygame
class Corazon:
    def __init__(self,cora_x,cora_y):
        pygame.sprite.Sprite.__init__(self)
        #Atributos
        self.img = pygame.image.load("img/misc/vidas_1.png").convert_alpha()
        self.cora_x = 545
        self.cora_y = 5
        self.separacion = 60
    def dibujar_corazon(self,superficie):
        superficie.blit(self.img, (self.cora_x,self.cora_y))

class Texto:
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont('Pixeled', 30)
        self.color = [255,255,255]
        self.sound_win_wave = pygame.mixer.Sound("Sound/win_wave.mp3")
        self.oleada = 1
        self.oleada_diff = 2
    #Textos-puntaje
    def puntaje(self,superficie,score):
        texto_puntaje = self.font.render(("PUNTAJE: "), True, (255, 255, 255))
        texto_score = self.font.render((str(score).zfill(5)), True, (255, 255, 255))
        superficie.blit(texto_puntaje,(10,10))
        superficie.blit(texto_score,(125,10))
    #Textos-enemy-dead-count
    def puntaje_matar_enemigos(self,superficie,score_enemy_dead):
        texto_enemy_dead = self.fon.render(("Enemigos Asesinados: "), True, (255, 255, 255))
        texto_score_enemy_dead = self.fon.render((str(score_enemy_dead).zfill(3)), True, (255, 255, 255))
        superficie.blit(texto_enemy_dead,(10,30))
        superficie.blit(texto_score_enemy_dead,(245,30))
    def agregar_wave(self):
        self.sound_win_wave.play()
        self.oleada += 1

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)
    def update(self):
        self.left, self.top = pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self, img_button_1, img__button_2, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen_boton_normal = img_button_1
        self.imagen_boton_seleccionar = img__button_2
        self.imagen_boton_actual = self.imagen_boton_normal
        self.rect = self.imagen_boton_actual.get_rect()
        self.rect.left, self.rect.top = (x,y)
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_boton_actual = self.imagen_boton_seleccionar
        else:
            self.imagen_boton_actual = self.imagen_boton_normal
        pantalla.blit(self.imagen_boton_actual, self.rect)