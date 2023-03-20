import pygame
from Misc import *
from Help_menu import *
from Main_game import *

pygame.init() #Inicializar Pygame
screen_x = 600
screen_y = 900
screen = pygame.display.set_mode((screen_x, screen_y)) #Definir la ventana
clock = pygame.time.Clock() #Definir clock interno
clock_2 = pygame.time.Clock() #Definir clock interno
pygame.display.set_caption("Galaga - v2.0") #Setar nombre
pygame.mixer.music.load('Sound/music_theme.mp3') #Cargar musica
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(-1) #Reproducir Musica
#Start Menu
menu_inicio = 1
template = pygame.image.load('img/misc/template.png')
template_x = 0
template_y = 0
boton_img_1 = [pygame.image.load('img/misc/boton_jugar_1.png'),
            pygame.image.load('img/misc/boton_ayuda_1.png'),
            pygame.image.load('img/misc/boton_salir_1.png')]
boton_img_2 = [pygame.image.load('img/misc/boton_jugar_2.png'),
            pygame.image.load('img/misc/boton_ayuda_2.png'),
            pygame.image.load('img/misc/boton_salir_2.png')]
boton_jugar = Boton(boton_img_1[0], boton_img_2[0], 174, 400)
boton_ayuda = Boton(boton_img_1[1], boton_img_2[1], 174, 534)
boton_salir = Boton(boton_img_1[2], boton_img_2[2], 174, 668)
cursor_mouse = Cursor()
FPS_1 = 60
running = 0
menu_ayuda = 0
while menu_inicio == 1:
    screen.blit(template, (template_x, template_y))
    cursor_mouse.update()
    boton_jugar.update(screen,cursor_mouse)
    boton_ayuda.update(screen,cursor_mouse)
    boton_salir.update(screen,cursor_mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                menu_inicio = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor_mouse.colliderect(boton_jugar.rect):
                menu_inicio = 0
                menu_ayuda = 0
                running = 1
            if cursor_mouse.colliderect(boton_ayuda.rect):
                menu_inicio = 0
                menu_ayuda = 1
                running = 0
            if cursor_mouse.colliderect(boton_salir.rect):
                pygame.quit()
                quit()
        clock.tick(FPS_1)
        pygame.display.update()
pygame.quit()
if menu_ayuda == 1:
    help_menu()

main_game()