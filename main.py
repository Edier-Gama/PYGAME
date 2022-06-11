import random
import pygame, sys
from button import Button

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("menu.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
  

SCREEN = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def play():
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("music.mp3")
 pygame.mixer.music.play()
 pygame.mixer.music.set_volume(0.5)
  

    
 black = 0, 0, 0
 white = 255, 255, 255
 green = 0, 255, 0
 red = 255, 0, 0
    
    # CReacion de las clases
   
 class Jugador(pygame.sprite.Sprite):
        
        def __init__(self):
            self.image = pygame.image.load("jugador.png").convert_alpha()
            self.rect = self.image.get_rect()
            
  
 class Tejo(pygame.sprite.Sprite):
        
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("tejo.png").convert_alpha()
            self.rect = self.image.get_rect()
    
    
 class Mechas(pygame.sprite.Sprite):
            
        def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("mecha.png").convert_alpha()
          self.rect = self.image.get_rect()
            
                
 ancho = 800
 alto = 600
 tejo_lista = pygame.sprite.Group()
 mechaLista = pygame.sprite.Group()
    
 ventana = pygame.display.set_mode((ancho, alto))
 clock = pygame.time.Clock()
 pygame.mouse.set_visible(True)
 pygame.display.set_caption("Tejo")   
 fondo = pygame.image.load("imagen_principal.jpg").convert()    
    
 jugador = Jugador()
    

 mecha = Mechas()
 mecha.rect.x =  random.randrange(310, 700)
 mecha.rect.y =  310
 mechaLista.add(mecha)

 mecha = Mechas()
 mecha.rect.x =  135
 mecha.rect.y =  290
 mechaLista.add(mecha)

 mecha = Mechas()
 mecha.rect.x =  680
 mecha.rect.y =  290
 mechaLista.add(mecha)
  
 mecha = Mechas()
 mecha.rect.x =  527
 mecha.rect.y =  223
 mechaLista.add(mecha)
  
 mecha = Mechas()
 mecha.rect.x =  230
 mecha.rect.y =  240
 mechaLista.add(mecha)

 cord_x = 0
 cord_y = 480
 speed_x = 3
 speed_y = 3

 contador = 0
 font = pygame.font.SysFont("Arial", 20)
 eje_y = int(input("Ingrese un numero del 1 al 10 para medir la fuerza con la que lanzará el tejo, siendo 10 la fuerza maxima: "))

 while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            
    if event.type == pygame.MOUSEBUTTONDOWN:
            tejo = Tejo()
            tejo.rect.x = x+10
            tejo.rect.y = 600 -10
            #     tejo.rect.y = y-50
            # elif eje_y == 2:
            #     tejo.rect.y = y-100
            # elif eje_y == 3:
            #     tejo.rect.y = y-150
            # elif eje_y == 4:
            #     tejo.rect.y = y-200
            # elif eje_y == 5:
            #     tejo.rect.y = y-250
            # elif eje_y == 6:
            #     tejo.rect.y = y-300
            # elif eje_y == 7:
            #     tejo.rect.y = y-350
            # elif eje_y == 8:
            #     tejo.rect.y = y-400
            # elif eje_y == 9:
            #     tejo.rect.y = y-450
            # elif eje_y == 10:
            #     tejo.rect.y = y-500                                                             
            tejo_lista.add(tejo)

                    
    tejo_lista.update()
    for tiro in tejo_lista:
        if pygame.sprite.spritecollide(tiro, mechaLista, True):
            contador += 1
            print(contador)
        if contador == 5:
            print("Ganaste")
            sys.exit()    
        
           
    cord_x += speed_x
    if cord_x > 770 or cord_x < 0:
        speed_x *= -1
            
    ventana.blit(fondo, [0,0])
    x,y = cord_x, cord_y
    mechaLista.draw(ventana)
    tejo_lista.draw(ventana)
    ventana.blit(jugador.image, (cord_x, cord_y))
    
    clock.tick(100)    
    pygame.display.flip()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(15).render("Para jugar sigue las siguientes instrucciones: ", True, "Black")
        
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(450, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(450, 550), 
                            text_input="ATRÁS", font=get_font(35), base_color="Black", hovering_color="Green")
        TEXTO_1 = Button(image=None, pos=(450, 150),text_input="Al darle a jugar irás a la arena del tejo donde tendrás", font=get_font(13), base_color="Black", hovering_color="Green")
        TEXTO_2 = Button(image=None, pos=(450, 200),text_input="que darle clic a la pantalla para frenar tu mano e", font=get_font(13), base_color="Black", hovering_color="Green")
        TEXTO_3 = Button(image=None, pos=(450, 250),text_input="ingresar un valor entre 1 y 600:", font=get_font(13), base_color="Black", hovering_color="Green")
        TEXTO_4 = Button(image=None, pos=(450, 300),text_input="1 es lanzar el tejo casi saliendo del juego, y 600 al revés, ", font=get_font(13), base_color="Black", hovering_color="Green")
        TEXTO_5 = Button(image=None, pos=(450, 350),text_input="tendrás el tejo a 1 cm de tu mano, tu tarea es atinar", font=get_font(13), base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        TEXTO_1.update(SCREEN)
        TEXTO_2.update(SCREEN)
        TEXTO_3.update(SCREEN)
        TEXTO_4.update(SCREEN)
        TEXTO_5.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(35).render("TEJO CON PYGAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(450, 250), 
                            text_input="Jugar", font=get_font(35), base_color="#d7fcd4", hovering_color="green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(450, 400), 
                            text_input="Como jugar", font=get_font(35), base_color="#d7fcd4", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(450, 550), 
                            text_input="Salir", font=get_font(35), base_color="#d7fcd4", hovering_color="red")

        CREDITOS = Button(image=None, pos=(450, 650),text_input="Gloria Gama, Jeison Olivares, Julian xd", font=get_font(13), base_color="white", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, CREDITOS]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()