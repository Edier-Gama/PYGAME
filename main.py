import random
import pygame, sys
from botones import Button

pygame.init()

#Creación de la panatlla del menú

SCREEN = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/fondo.jpg")
FG = pygame.image.load("assets/fondo_ganador.jpg")
FP = pygame.image.load("assets/fondo_perdedor.jpg")


def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def play():   
    
 black = 0, 0, 0
 white = 255, 255, 255
 green = 0, 255, 0
 red = 255, 0, 0
 gray = 128, 128, 128
 

 #Contador de puntos
 
 def lives(surface, text, size, x, y):
   font = pygame.font.Font("assets/font.ttf", size)
   text_surface = font.render(text, True, (255, 255, 255))
   text_rect = text_surface.get_rect()
   text_rect.midtop = (x, y)
   surface.blit(text_surface, text_rect)
 
 def contador(surface, text, size, x, y):
   font = pygame.font.Font("assets/font.ttf", size)
   text_surface = font.render(text, True, (255, 255, 255))
   text_rect = text_surface.get_rect()
   text_rect.midtop = (x, y)
   surface.blit(text_surface, text_rect)

 #Contador de puntos del bot
 
 def bot(surface, text, size, x, y):
   font = pygame.font.Font("assets/font.ttf", size)
   text_surface = font.render(text, True, (255, 255, 255))
   text_rect = text_surface.get_rect()
   text_rect.midtop = (x, y)
   surface.blit(text_surface, text_rect)

 #Creacion de las clases 
   
 class Jugador(pygame.sprite.Sprite):
        
        def __init__(self):
            self.image = pygame.image.load("assets/jugador.png").convert_alpha()
            self.rect = self.image.get_rect()
            
  
 class Tejo(pygame.sprite.Sprite):
        
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("assets/tejo.png").convert_alpha()
            self.rect = self.image.get_rect()
    
    
 class Mechas(pygame.sprite.Sprite):
            
        def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("assets/mecha.png").convert_alpha()
          self.rect = self.image.get_rect()
 
 class ArenaSuperior(pygame.sprite.Sprite):
     
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("assets/arena_superior.png").convert_alpha()
          self.rect = self.image.get_rect()
          
 class ArenaInferior(pygame.sprite.Sprite):
     
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("assets/arena_inferior.png").convert_alpha()
          self.rect = self.image.get_rect() 
                  
 class ArenaIz(pygame.sprite.Sprite):
     
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("assets/arena_iz.png").convert_alpha()
          self.rect = self.image.get_rect()
          
 class ArenaDe(pygame.sprite.Sprite):
     
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("assets/arena_d.png").convert_alpha()
          self.rect = self.image.get_rect()

 class Bosin(pygame.sprite.Sprite):
     
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("assets/bocin.png").convert_alpha()
          self.rect = self.image.get_rect()                                 
                
 #Sprites con los que se interactua pasados a listas
 
 tejo_lista = pygame.sprite.Group()
 mechaLista = pygame.sprite.Group()
 arenaS = pygame.sprite.Group()
 arenaDer = pygame.sprite.Group()
 arenaIzq = pygame.sprite.Group()
 arenaIn = pygame.sprite.Group()
 bosinC = pygame.sprite.Group()
 
 
 #Creacion de la pantalla de juego
 ancho = 800
 alto = 600   
 ventana = pygame.display.set_mode((ancho, alto))
 pygame.mouse.set_visible(True)
 pygame.display.set_caption("Tejo")   
 fondo = pygame.image.load("assets/imagen_principal.jpg").convert()    
    
 jugador = Jugador()
    
 # Posicionamiento de las mechas y demas areas
 mecha = Mechas()
 mecha.rect.x =  420
 mecha.rect.y =  240
 mechaLista.add(mecha)
  
 mecha = Mechas()
 mecha.rect.x =  375
 mecha.rect.y =  240
 mechaLista.add(mecha)
 
 arena_s = ArenaSuperior()
 arena_s.rect.x =  380
 arena_s.rect.y =  210
 arenaS.add(arena_s)
 
 arena_iz = ArenaIz()
 arena_iz.rect.x =  340
 arena_iz.rect.y =  210
 arenaIzq.add(arena_iz)
 
 arena_de = ArenaDe()
 arena_de.rect.x =  440
 arena_de.rect.y =  210
 arenaDer.add(arena_de)
 
 arena_in = ArenaInferior()
 arena_in.rect.x =  350
 arena_in.rect.y =  270
 arenaIn.add(arena_in)
 
 bosin = Bosin()
 bosin.rect.x =  390
 bosin.rect.y = 240
 bosinC.add(bosin)
  
 #Posicionamiento de la mano del jugador
 cord_x = 0
 cord_y = 480
 speed_x = 3
 speed_y = 3
 clock = pygame.time.Clock()
 #Puntos iniciados en 0
 score = 0
 score_bot = 0
 vidas = 10
 font = pygame.font.SysFont("Arial", 20)
 
 #Bucle princcipal del juego
 
 while True:
    clock.tick(100)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
     
    # Creacion de la mecanica de movimiento del tejo:
    
    #Depende de la fuerza irá a un eje Y estiamdo entre los
    # valores que se le asignen
            
    if event.type == pygame.MOUSEBUTTONDOWN:
            vidas -= 1
            tejo = Tejo()
            tejo.rect.x = x+10
            tejo.rect.y = int(input("Ingrese un numero del 1 al 10 para medir la fuerza con la que lanzará el tejo, siendo 10 la fuerza maxima: "))
            if tejo.rect.y == 10:
               tejo.rect.y = random.randrange(50, 99)
            elif tejo.rect.y == 9:
                tejo.rect.y = random.randrange(100, 149)
            elif tejo.rect.y  == 8:
                tejo.rect.y = random.randrange(150, 199)
            elif tejo.rect.y  == 7:
                tejo.rect.y = random.randrange(200, 249)
            elif tejo.rect.y  == 6:
                tejo.rect.y = random.randrange(250, 299)
            elif tejo.rect.y  == 5:
                tejo.rect.y = random.randrange(300, 350)
            elif tejo.rect.y  == 4:
                tejo.rect.y = random.randrange(350, 399)
            elif tejo.rect.y  == 3:
                tejo.rect.y = random.randrange(400, 450)
            elif tejo.rect.y  == 2:
                tejo.rect.y = random.randrange(450, 499)
            elif tejo.rect.y  == 1:
                tejo.rect.y = random.randrange(500, 600)
            elif tejo.rect.y > 10:
                print("El numero ingresado no es valido")
                                                                                
            tejo_lista.add(tejo)
    
    # Coliciones con los sprites, segun el area de la arena en que de el tej
    # suma cierta cantidad de puntos al jugador
                   
    tejo_lista.update()
    for tiro in tejo_lista:
        if pygame.sprite.spritecollide(tiro, mechaLista, True):
            score += 2
            score_bot += random.randint(1,2)

    
    tejo_lista.update()
    for tiro in tejo_lista:
        if pygame.sprite.spritecollide(tiro, arenaS, True):
            score += 1
            score_bot += random.randint(1,2)
            
            
    tejo_lista.update()
    for tiro in tejo_lista:
        if pygame.sprite.spritecollide(tiro, arenaIn, True):
            score += 1 
            score_bot += random.randint(1,2)
            

    tejo_lista.update()
    for tiro in tejo_lista:
        if pygame.sprite.spritecollide(tiro, arenaDer, True):
            score += 1              
            score_bot += random.randint(1,2)
            
            
    tejo_lista.update()
    for tiro in tejo_lista:
        if pygame.sprite.spritecollide(tiro, arenaIzq, True):
            score += 1
            score_bot += random.randint(1,2)
            
            
    tejo_lista.update()
    for tiro in tejo_lista:
        if pygame.sprite.spritecollide(tiro, bosinC, True):
            score += 3
            score_bot += random.randint(1,3)
            vidas - 2

    
    if score_bot > score and vidas <= 0:
        menu_final()
    if score > score_bot and vidas <= 0:
        menu_final_ganador()
    if score == score_bot and vidas <= 0:
        menu_final_empate()    
                
    # Animacion principal de la mano
    cord_x += speed_x
    if cord_x > 770 or cord_x < 0:
        speed_x *= -1
    
    # Dibujando todo en la pantalla de juego
            
    ventana.blit(fondo, [0,0])
    x,y = cord_x, cord_y
    mechaLista.draw(ventana)
    tejo_lista.draw(ventana)
    arenaS.draw(ventana)
    arenaIn.draw(ventana)
    arenaDer.draw(ventana)
    arenaIzq.draw(ventana)
    bosinC.draw(ventana)
    ventana.blit(jugador.image, (cord_x, cord_y))
    pygame.draw.rect(ventana, (0, 0, 0), (0, 0, 330, 70))
    pygame.draw.rect(ventana, (0, 0, 0), (470, 0, 330, 70))
    pygame.draw.rect(ventana, (gray), (330, 0, 140, 70))
    bot(ventana, str("Jugador 100% real no fake"), 16, 900 - 270, 10)
    bot(ventana, str("Tu puntaje es: "), 16, 900 - 270, 35)
    bot(ventana, str(score_bot), 15, 900 - 190, 35)
    lives(ventana, str("VIDAS"), 25, 900 - 500, 10)
    lives(ventana, str(vidas), 19, 900 - 500, 40) 
    contador(ventana, str("JUGADOR 1"), 16, 900 - 750, 10)
    contador(ventana, str("Tu puntaje es: "), 16, 900 - 750, 35)
    contador(ventana, str(score), 15, 900 - 670, 35)   
    pygame.display.flip()
    
    #Inicio del menu de instrucciones
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(18).render("Para jugar sigue las siguientes instrucciones: ", True, "Black")
        
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(450, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(450, 550),text_input="ATRAS", font=get_font(35), base_color="Black", hovering_color="red")
        TEXTO_1 = Button(image=None, pos=(450, 150),text_input="Al darle a jugar iras a la arena del tejo donde tendras", font=get_font(18), base_color="Black", hovering_color="Green")
        TEXTO_2 = Button(image=None, pos=(450, 200),text_input="que darle clic a la pantalla para frenar tu mano e", font=get_font(18), base_color="Black", hovering_color="Green")
        TEXTO_3 = Button(image=None, pos=(450, 250),text_input="ingresar un valor entre 1 y 10 en tu consola", font=get_font(18), base_color="Black", hovering_color="Green")
        TEXTO_4 = Button(image=None, pos=(450, 300),text_input="1 es la fuerza minima, y 10 es la fuerza maxima, bien: ", font=get_font(18), base_color="Black", hovering_color="Green")
        TEXTO_5 = Button(image=None, pos=(450, 350),text_input="tu tarea es hacer < Bosin > o hacer el maximo puntaje", font=get_font(18), base_color="Black", hovering_color="Green")
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
        
    #Menu principal del juego    

def menu_final():
    while True:
        SCREEN.blit(FP, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(35).render("HAS PERDIDO:( TUS PUNTOS NO DAN", True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 30))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 300), 
                            text_input="JUGAR DE NUEVO", font=get_font(35), base_color="black", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 420), 
                            text_input="SALIR", font=get_font(35), base_color="black", hovering_color="red")

        CREDITOS = Button(image=None, pos=(400, 650),text_input="Gloria Gama, Jeyson Olivare, Julian", font=get_font(20), base_color="white", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        

        for button in [PLAY_BUTTON, QUIT_BUTTON, CREDITOS]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
def menu_final_ganador():
    while True:
        SCREEN.blit(FG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(35).render("GANASTE :D TU PUNTAJE FUE GANADOR", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 30))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), 
                            text_input="JUGAR DE NUEVO", font=get_font(35), base_color="black", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 350), 
                            text_input="SALIR", font=get_font(35), base_color="black", hovering_color="red")

        CREDITOS = Button(image=None, pos=(400, 650),text_input="Gloria Gama, Jeyson Olivare, Julian", font=get_font(20), base_color="white", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        

        for button in [PLAY_BUTTON, QUIT_BUTTON, CREDITOS]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()        


def menu_final_empate():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(35).render("ESTO HA SIDO UN EMPATE :0", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 30))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 250), 
                            text_input="JUGAR DE NUEVO", font=get_font(35), base_color="black", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 350), 
                            text_input="Salir", font=get_font(35), base_color="black", hovering_color="red")

        CREDITOS = Button(image=None, pos=(400, 650),text_input="Gloria Gama, Jeyson Olivare, Julian", font=get_font(20), base_color="white", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        

        for button in [PLAY_BUTTON, QUIT_BUTTON, CREDITOS]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()  

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(35).render("TEJO CON PYGAME", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 30))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(450, 250), 
                            text_input="Jugar", font=get_font(35), base_color="black", hovering_color="green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(450, 400), 
                            text_input="Como jugar", font=get_font(35), base_color="black", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(450, 550), 
                            text_input="Salir", font=get_font(35), base_color="black", hovering_color="red")

        CREDITOS = Button(image=None, pos=(450, 650),text_input="Gloria Gama, Jeyson Olivare, Julian", font=get_font(20), base_color="white", hovering_color="Green")

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