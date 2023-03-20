import pygame
def help_menu():
    pygame.init() #Inicializar Pygame
    screen = pygame.display.set_mode((600, 900)) #Definir la ventana
    clock = pygame.time.Clock() #Definir clock interno
    pygame.display.set_caption("Galaga - v2.0") #Setar nombre
    pygame.mixer.music.load('Sound/music_theme.mp3') #Cargar musica
    pygame.mixer.music.play(3) #Reproducir Musica
    img_help = pygame.image.load('img/misc/menu_ayuda.png')
    img_help_x = 0
    img_help_y = 0
    #Variables
    FPS = 60
    menu_ayuda = 1
    while menu_ayuda == 1:
        #Imprimir en pantalla
        screen.blit(img_help, (img_help_x,img_help_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_ayuda = 0
                    running = 1
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()