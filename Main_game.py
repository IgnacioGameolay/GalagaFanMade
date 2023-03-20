import pygame
import random,time
from Misc import Texto
from Jugador import *
from Enemigos import *
def main_game():
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
    #Wallpaper
    wallpaper_x = 0
    wallpaper_y = 0
    wallpaper = pygame.image.load('img/misc/wallpaper.jpeg')
    #Variables
    FPS = 60
    ayuda = 0
    movimiento_izq = True
    movimiento_der = True
    score = 0
    score_enemy_dead = 0
    font = pygame.font.SysFont('Pixeled', 30)
    aumentar_stats = 2
    mayor_puntaje = 0
    #Player-corazones
    corazon_y = screen_y - 50
    corazon_1 = pygame.image.load('img/misc/corazon.png').convert_alpha()
    corazon_1_x = 10
    corazon_2 = pygame.image.load('img/misc/corazon.png').convert_alpha()
    corazon_2_x = 70
    corazon_3 = pygame.image.load('img/misc/corazon.png').convert_alpha()
    corazon_3_x = 130
    lista_corazones = [corazon_1, corazon_2, corazon_3]
    coordenadas_corazones = [corazon_3_x,
                            corazon_2_x,
                            corazon_1_x,
                            corazon_y,]

    #Objetos
    spaceship = Nave(3) #Crear Objeto-Jugador
    bala_spaceship = Proyectil_Jugador(spaceship.spaceship_x,spaceship.spaceship_y) #Crear Objeto-Bala_Jugador
    enemigos_lista = []
    oleada_obj = Texto()
    oleada = oleada_obj.oleada
    oleada_dif_obj = Texto()
    oleada_dif = oleada_dif_obj.oleada_diff
    contador_oleada_boss = 5
    contador_oleada = 2
    crono_var = 1
    pausa = False
    def aumentar_dificultad():
        if oleada_obj.oleada > oleada_dif_obj.oleada_diff:
            oleada_dif_obj.oleada_diff += 2
    def dibujar_enemigos():
        if oleada_obj.oleada < contador_oleada_boss and spaceship.health > 0:
            #Abejas ROjas - Fila 0
            enemy_x = 100
            enemy_y = 110
            for i in range(1, 4):
                enemigo = Enemigo(1,2,enemy_x,enemy_y)
                enemigos_lista.append(enemigo)
                enemy_x += 200

            #Abejas Amarillas - FIla 1
            enemy_x = 100
            enemy_y = 210
            for i in range(1, 4):
                enemigo = Enemigo(0,1,enemy_x,enemy_y)
                enemigos_lista.append(enemigo)
                enemy_x += 200

            #Abejas Amarillas - FIla 2
            enemy_x = 100
            enemy_y = 310
            for i in range(1, 4):
                enemigo = Enemigo(0,1,enemy_x,enemy_y)
                enemigos_lista.append(enemigo)
                enemy_x += 200
        if oleada_obj.oleada == contador_oleada_boss:#Generar boss cada X oleadas
            enemy_x = 100
            enemy_y = 100
            for i in range(1):
                enemigo = Enemigo(3,10,enemy_x,300)
                enemigos_lista.append(enemigo)
                enemigo.speed = 4
                enemigo.contador_disparo = 8
    if spaceship.health > 0:
        dibujar_enemigos()
    def generar_enemigos():
        if len(enemigos_lista) == 0 and spaceship.health > 0:
            dibujar_enemigos()
            oleada_obj.agregar_wave()
    running = 1
    #BUCLE JUEGO PRINCIPAL
    while running == 1:
        #Decidir Pausa
        #Imprimir Wallpaper
        screen.blit(wallpaper, (wallpaper_x,wallpaper_y))
        #screen.blit(template,(template_x, template_y))
        generar_enemigos()
        if crono_var == aumentar_stats:
            for enemigo in enemigos_lista:
                enemigo.agregar_dificultad()
            aumentar_stats += 1

        #Imprimir corazones - # 545-485-425
        if spaceship.health > 0:
            screen.blit(lista_corazones[0], (corazon_1_x,coordenadas_corazones[3]))
        if spaceship.health > 1:
            screen.blit(lista_corazones[1], (corazon_2_x,coordenadas_corazones[3]))
        if spaceship.health > 2:
            screen.blit(lista_corazones[2], (corazon_3_x,coordenadas_corazones[3]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                #Si se precionan las teclas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pausa = True
                if event.key == pygame.K_o:
                    pausa = False
                if event.key == pygame.K_ESCAPE:
                    running = 0
                if event.key == pygame.K_a and movimiento_izq == True:
                    spaceship.spaceship_x -= spaceship.speed

                if event.key == pygame.K_d and movimiento_der == True:
                    spaceship.spaceship_x += spaceship.speed

                if spaceship.health > 0:
                    if event.key == pygame.K_SPACE and spaceship.poder_disparar == True:
                        spaceship.disparar(spaceship.spaceship_x,spaceship.spaceship_y)
                #Delimitiar el movimiento
                if spaceship.spaceship_x == 475:
                    movimiento_der = False
                else:
                    movimiento_der = True
                if spaceship.spaceship_x == -5:
                    movimiento_izq = False
                else:
                    movimiento_izq = True
                
                #######################
        #Disparar-Jugador
        if len(spaceship.balas) > 0:
            for bala in spaceship.balas:
                bala.dibujar_bala_jugador(screen)
                bala.mover_bala_jugador()
                if bala.pos_y < -300:
                    spaceship.balas.remove(bala)
                else:#Muerte Enemigos
                    for enemigo in enemigos_lista:
                        if enemigo.enemy_x - bala.pos_x < 0 and enemigo.enemy_x - bala.pos_x > -85 and enemigo.enemy_y >= bala.pos_y and bala.pos_y > -10:
                            enemigo.health -= 1
                            enemigo.sound_dead.play()
                            bala.pos_y = -400
                            if enemigo.health == 0:
                                enemigo.muerte_enemigo()
                                bala.pos_y = -400
                                enemigos_lista.remove(enemigo)
                                score_enemy_dead += 1
                                if enemigo.select_img == 0:
                                    score += 150
                                    if score > mayor_puntaje:
                                        mayor_puntaje  += 150
                                if enemigo.select_img == 1:
                                    score += 300
                                    if score > mayor_puntaje:
                                        mayor_puntaje  += 300
                                if enemigo.select_img == 2:
                                    score += 600
                                    if score > mayor_puntaje:
                                        mayor_puntaje  += 600
                                if enemigo.select_img == 3:
                                    contador_oleada_boss += 5
                                    score += 1000
                                    if score > mayor_puntaje:
                                        mayor_puntaje += 1000


        #Dibujar Balas-Enemigo
        if len(enemigos_lista) > 0:
            for enemigo in enemigos_lista:
                enemigo.mostrar_enemigo(screen)
                if enemigo.select_img == 3:
                    enemigo.speed = 2
                enemigo.activar_disparo()
                enemigo.movimiento_enemigo()
                if spaceship.spaceship_x - enemigo.enemy_x < 0 and spaceship.spaceship_x - enemigo.enemy_x > -85 and enemigo.enemy_y > spaceship.spaceship_y:
                    spaceship.perder_vida_nave()
                    spaceship.muerte_nave()
                if len(enemigo.lista_balas_enemigo) > 0:
                    for bala in enemigo.lista_balas_enemigo:
                        bala.dibujar_bala_enemigo(screen)#
                        bala.mover_bala_enemigo()
                        #Muerte Jugador
                        if spaceship.spaceship_x - bala.pos_x < 0 and spaceship.spaceship_x - bala.pos_x > -120 and spaceship.spaceship_y < bala.trayectoria_y and bala.trayectoria_y < 800:
                            enemigo.lista_balas_enemigo.remove(bala)
                            spaceship.perder_vida_nave()
                            spaceship.muerte_nave()
                        if spaceship.health <= 0:
                            for bala in enemigo.lista_balas_enemigo:
                                enemigo.lista_balas_enemigo.remove(bala)
                        if bala.pos_y > 800:
                            enemigo.lista_balas_enemigo.remove(bala)
                        else:
                            for bala in spaceship.balas:
                                if spaceship.spaceship_x - bala.pos_x < 0 and spaceship.spaceship_x - bala.pos_x > -85 and bala.pos_y > 1000:
                                    spaceship.balas.remove(bala)

        #Textos-puntaje
        texto_puntaje = font.render(("PUNTAJE"), True, (255, 0, 0))
        texto_score = font.render((str(score).zfill(5)), True, (255, 255, 255))
        screen.blit(texto_puntaje,(20,10))
        screen.blit(texto_score,(40,36))

        #Textos-puntaje
        texto_oleada = font.render(("OLEADA"), True, (255, 255, 0))
        texto_oleada_puntos = font.render((str(oleada_obj.oleada).zfill(3)), True, (255, 255, 255))
        screen.blit(texto_oleada,(500,corazon_y-15))
        screen.blit(texto_oleada_puntos,(525,corazon_y+20))

        #cronometro
        crono = int(pygame.time.get_ticks()/1000)
        if crono_var == crono:
            crono_var += 1
        texto_cronometro = font.render("TIEMPO", True, (255, 0, 0))
        texto_cronometro_tiempo = font.render((str(crono).zfill(3)), True, (255, 255, 255))
        screen.blit(texto_cronometro,(220,10))
        screen.blit(texto_cronometro_tiempo,(245,36))
        #Mayor puntaje
        texto_puntaje_mayor = font.render(("PUNTAJE MÁS ALTO"), True, (255, 0, 0))
        texto_score_mayor = font.render((str(mayor_puntaje).zfill(5)), True, (255, 255, 255))
        screen.blit(texto_puntaje_mayor,(390,6))
        screen.blit(texto_score_mayor,(460,36))
        #Imprimir Personaje
        tiempo = [int(pygame.time.get_ticks()/1200)] #Cambia la animacion de la nave cada x tiempo
        tiempo_1 = int(pygame.time.get_ticks()/380)
        spaceship.animacion_nave(tiempo[0])
        spaceship.animacion_propulsores(tiempo_1)
        spaceship.animacion_explosiones(tiempo_1)
        spaceship.dibujar_nave(screen)

        clock.tick(FPS)
        if spaceship.health < 0:
            for enemigo in enemigos_lista:
                enemigo.health = 0
                if enemigo.health == 0:
                    enemigo.muerte_enemigo()
                    enemigos_lista.remove(enemigo)
        if spaceship.health <= -150:
            score = 0
            score_enemy_dead = 0
            oleada_obj.oleada = 0
            crono = 0
            spaceship.spaceship_x = 235
            spaceship.spaceship_y = 750
            spaceship.health = 3
        pygame.display.update()
    pygame.quit()
    quit()
