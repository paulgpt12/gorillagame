#Importieren der benötigten Module

import pygame # Spiele-Modul
import sys # zum Schließen des Fensters
import numpy # Modul für einfachen Umgang mit großen Arrays; ich benutze es für das Generieren von Zufallszahlen
from pygame import mixer # Musik-Modul in Pygame

# Initialisierung von Pygame ; immer notwendig

pygame.init()

# Bilder/Bildermodifikation, Fenster, Fenstertitel, Funktion für Zeit für Mainloop-Durchlauf, Hintergrundmusik und Soundeffekte

clock = pygame.time.Clock() # Funktion zum "tracken" der Zeit; dadurch können die Frames per second für den Mainloop-Durchlauf begrenzt werden
window = pygame.display.set_mode((900,700)) # Erstellen des Fensters
pygame.display.set_caption("GorillaGame") # Fenstertitel
# Importieren und Skalieren der Bilder
image_dschungel = pygame.image.load("DschungelHintergrund.png")
image_dschungel = pygame.transform.scale(image_dschungel, (900,700))
image_schlange = pygame.image.load("Schlange.png")
image_schlange = pygame.transform.scale(image_schlange, (60, 60))
image_bombe = pygame.image.load("Bombe.png")
image_bombe = pygame.transform.scale(image_bombe, (60,60))
image_gorilla = pygame.image.load("Gorilla.png")
image_gorilla = pygame.transform.scale(image_gorilla, (60, 60))
image_banane = pygame.image.load("Banane.png")
image_banane = pygame.transform.scale(image_banane, (40, 30))
# Importieren und Abspielen der Hintergrundmusik
mixer.music.load("Hintergrundmusik.mp3")
mixer.music.play(-1) # -1 bedeutet Endlosschleife

# Start-Loop
run = False

while run == False:
    clock.tick(70)
    window.blit(image_dschungel, (0, 0))
    font_start = pygame.font.Font("Chainwhacks.otf", 40)
    start_font = font_start.render("Start!", True, (255, 255, 255))
    window.blit(start_font, (355, 330))
    startbutton_x = 343
    startbutton_y = 325
    startbutton_laenge = 155
    startbutton_hoehe = 50
    farbe_inaktiv = (162, 205, 90)
    farbe_aktiv = (188, 238, 104)
    farbe_rand = (255, 255, 255)
    maus = pygame.mouse.get_pos() # damit wird Position der Maus registriert
    maus_click = pygame.mouse.get_pressed() # damit wird registriert ob Maus geklickt wird -> 1 => wird gedrückt, 0 => wird nicht gedrückt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if maus [0] > startbutton_x and maus[0] < (startbutton_x + startbutton_laenge) and maus[1] > startbutton_y and maus[1] < (startbutton_y + startbutton_hoehe):
            pygame.draw.rect(window, farbe_aktiv,(startbutton_x, startbutton_y, startbutton_laenge, startbutton_hoehe))
            window.blit(start_font, (355, 330))
            if maus_click[0] == 1:
                  # Variablen für Mainloop
                run = True # Variable gibt an ob Mainloop durchlaufen darf/kann oder nicht -> run = False wenn Gorilla tot
                direction = True # Variable zu Änderung der Ausrichtung des Gorillas
                go = True # Variable für Generieren der Zufallskoordinaten für Anfangsposition der Banane
                start = True # Variable für Platzierung der Banane in Anfangsposition mit Zufallskoordinaten
                score = 0
                g = 30 # anfängliche x-Koordinate des Gorillas
                o = 30 # anfängliche y-Koordinate des Gorillas
                c = 0 # Zählt Anzahl der Mainloop-Durchläufe
                m = -1 # Variable für anfängliche Bewegungsrichtung der Schlange
                n = -1 # Variable für anfägliche Bewegungsrichtung der Bombe
                schlange_X = 400 # anfänglicher x-Koordinate der Schlange
                schlange_Y = 200 # anfänglicher y-Koordinate der Schlange
                bombe_X = 300 # anfänglicher x-Koordinate der Bombe
                bombe_Y = 400 # anfänglicher y-Koordinate der Bombe
                schlange_v = 2 # Geschwindigkeit der Schlange
                bombe_v = 3 # Geschwindigkeit der Bombe
                pygame.time.wait(150)
                break
        else:
            pygame.draw.rect(window, farbe_inaktiv, (startbutton_x, startbutton_y, startbutton_laenge, startbutton_hoehe))
            window.blit(start_font, (355, 330))
        pygame.display.update()


# Mainloop

while run == True:
    clock.tick(70)
    window.blit(image_dschungel, (0, 0))
    window.blit(image_bombe, (bombe_X,bombe_Y))
    window.blit(image_schlange, (schlange_X, schlange_Y))
    font = pygame.font.Font("Chainwhacks.otf", 32) # weitere Fonts zum Download: https://www.dafont.com/de/new.php
    showscore = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(showscore, (750, 20))
    # Anzeigen der Banane und regelmäßige Positionsänderung
    if go == True:
        x = numpy.random.randint(0,861)
        y = numpy.random.randint(0,671)
        go = False
    if c == 200:
        x = numpy.random.randint(0,861)
        y = numpy.random.randint(0,671)
        c = 0
    if start == True:
        window.blit(image_banane, (x, y))
        pygame.display.update()
    elif start == False:
        if c == 200:
            window.blit(image_banane, (x, y))
            pygame.display.update()
        else:
            window.blit(image_banane, (x, y))
    # Anzeigen, Steuern/Bewegen und Drehen(Änderung der Ausrichtung) des Gorillas
    if direction == True:
        window.blit(image_gorilla, (g, o))
        pygame.display.update()
    if direction == False:
        window.blit(pygame.transform.flip(image_gorilla, True, False), (g, o))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = True
            if event.key == pygame.K_RIGHT:
                direction = False
    key_pressed_is = pygame.key.get_pressed()
    if key_pressed_is [pygame.K_RIGHT]:
         g += 3
         pygame.display.update()
    if key_pressed_is [pygame.K_LEFT]:
         g -= 3
         pygame.display.update()
    if key_pressed_is [pygame.K_DOWN]:
         o += 3
         pygame.display.update()
    if key_pressed_is [pygame.K_UP]:
         o -= 3
         pygame.display.update()
    # Begrenzen des Spielfeldes (für Gorilla)
    if g <= 0:
        g = 0
    if g >= 840:
        g = 840
    if o <= 0:
        o = 0
    if o >= 640:
        o = 640
    c += 1 # Zählen der Loop-Durchläufe
    # Kollision von Banane mit Gorilla
    if g >= x and g <= (x + 40):
        if o >= y and o <= (y + 30):
            score += 1
            c = 200
            sound_banana = mixer.Sound("SoundBanana.wav")
            sound_banana.play()
            pygame.display.update()
    if (g + 60) >= x and (g + 60) <= (x + 40):
        if o >= y and o <= (y + 30):
            score += 1
            c = 200
            sound_banana = mixer.Sound("SoundBanana.wav")
            sound_banana.play()
            pygame.display.update()
    if g >= x and g <= (x + 40):
        if (o + 60) >= y and (o + 60) <= (y + 30):
            score += 1
            c = 200
            sound_banana = mixer.Sound("SoundBanana.wav")
            sound_banana.play()
            pygame.display.update()
    if (g + 60) >= x and (g + 60) <= (x + 40):
        if (o + 60) >= y and (o + 60) <= (y + 30):
            score += 1
            c = 200
            sound_banana = mixer.Sound("SoundBanana.wav")
            sound_banana.play()
            pygame.display.update()
    if (g + 30) >= x and (g + 30) <= (x + 40):
        if (o + 30) >= y and (o + 30) <= (y + 30):
            score += 1
            c = 200
            sound_banana = mixer.Sound("SoundBanana.wav")
            sound_banana.play()
            pygame.display.update()
    # zufällige Bewegung und Begrenzung des Bewegungradius der Schlange
    if m == -1 or c == 200:
        a = numpy.random.randint(0,8)
        m = 0
    if a == 0:
        schlange_Y -= schlange_v
    if a == 1:
        schlange_X += schlange_v
        schlange_Y -= schlange_v
    if a == 2:
        schlange_X += schlange_v
    if a == 3:
        schlange_X += schlange_v
        schlange_Y += schlange_v
    if a == 4:
        schlange_Y += schlange_v
    if a == 5:
        schlange_X -= schlange_v
        schlange_Y += schlange_v
    if a == 6:
        schlange_X -= schlange_v
    if a == 7:
        schlange_X -= schlange_v
        schlange_Y -= schlange_v
    if schlange_X <= 0:
        list1 = [0,1,2,3,4]
        a = numpy.random.choice(list1)
    if (schlange_X + 60) >= 900:
        list2 = [0,4,5,6,7]
        a = numpy.random.choice(list2)
    if schlange_Y <= 0:
        list3 = [2,3,4,5,6]
        a = numpy.random.choice(list3)
    if (schlange_Y + 60) >= 700:
        list4 = [0,1,2,6,7]
        a = numpy.random.choice(list4)
    # zufällige Bewegung und Begrenzung des Bewegungsradius der Bombe
    if n == -1 or c == 200:
        b = numpy.random.randint(0,8)
        n = 0
    if b == 0:
        bombe_Y -= bombe_v
    if b == 1:
        bombe_X += bombe_v
        bombe_Y -= bombe_v
    if b == 2:
        bombe_X += bombe_v
    if b == 3:
        bombe_X += bombe_v
        bombe_Y += bombe_v
    if b == 4:
        bombe_Y += bombe_v
    if b == 5:
        bombe_X -= bombe_v
        bombe_Y += bombe_v
    if b == 6:
        bombe_X -= bombe_v
    if b == 7:
        bombe_X -= bombe_v
        bombe_Y -= bombe_v
    if bombe_X <= 0:
        list5 = [0,1,2,3,4]
        b = numpy.random.choice(list5)
    if (bombe_X + 60) >= 900:
        list6 = [0,4,5,6]
        b = numpy.random.choice(list6)
    if bombe_Y <= 0:
        list7 = [2,3,4,5,6]
        b = numpy.random.choice(list7)
    if (bombe_Y + 60) >= 700:
        list8 = [0,1,2,6,7]
        b = numpy.random.choice(list8)
    # Kollision Schlange und Gorilla
    if g >= schlange_X and g <= (schlange_X + 60):
        if o >= schlange_Y and o <= (schlange_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    if (g + 60) >= schlange_X and (g + 60) <= (schlange_X + 60):
        if o >= schlange_Y and o <= (schlange_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    if g >= schlange_X and g <= (schlange_X + 60):
        if (o + 60) >= schlange_Y and (o + 60) <= (schlange_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    if (g + 60) >= schlange_X and (g + 60) <= (schlange_X + 60):
        if (o + 60) >= schlange_Y and (o + 60) <= (schlange_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    if (g + 30) >= schlange_X and (g + 30) <= (schlange_X + 60):
        if (o + 30) >= schlange_Y and (o + 30) <= (schlange_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    # Kollision Bombe und Gorilla
    if g >= bombe_X and g <= (bombe_X + 60):
        if o >= bombe_Y and o <= (bombe_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    if (g + 60) >= bombe_X and (g + 60) <= (bombe_X + 60):
        if o >= bombe_Y and o <= (bombe_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    if g >= bombe_X and g <= (bombe_X + 60):
        if (o + 60) >= bombe_Y and (o + 60) <= (bombe_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    if (g + 60) >= bombe_X and (g + 60) <= (bombe_X + 60):
        if (o + 60) >= bombe_Y and (o + 60) <= (bombe_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    if (g + 30) >= bombe_X and (g + 30) <= (bombe_X + 60):
        if (o + 30) >= bombe_Y and (o + 30) <= (bombe_Y + 60):
            run = False
            sound_game_over = mixer.Sound("GameOver.wav")
            sound_game_over.play()
            pygame.display.update()
    if score == 10:
        schlange_v = 4
        bombe_v = 4
    if score == 25:
        schlange_v = 5
        bombe_v = 5
    if score == 35:
        schlange_v = 6
        bombe_v = 6
    if score == 45:
        schlange_v = 7
        bombe_v = 7
    start = False
    # GameOver-Loop
    if run == False:
        while run == False:
            clock.tick(70)
            window.blit(image_dschungel, (0, 0))
            font2 = pygame.font.Font("Chainwhacks.otf", 40)
            font3 = pygame.font.Font("Chainwhacks.otf", 25)
            game_over = font2.render("Game Over", True, (255, 255, 255))
            show_score_2 = font2.render("Score: " + str(score), True, (255, 255, 255))
            start_again = font3.render("Start Again", True, (255, 255, 255))
            window.blit(game_over, (325, 225))
            window.blit(show_score_2, (343, 275))
            button_x = 343
            button_y = 325
            button_laenge = 155
            button_hoehe = 50
            farbe_inaktiv = (162, 205, 90)
            farbe_aktiv = (188, 238, 104)
            farbe_rand = (255, 255, 255)
            maus = pygame.mouse.get_pos() # damit wird Position der Maus registriert
            maus_click = pygame.mouse.get_pressed() # damit wird registriert ob Maus geklickt wird -> 1 => wird gedrückt, 0 => wird nicht gedrückt
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if maus [0] > button_x and maus[0] < (button_x + button_laenge) and maus[1] > button_y and maus[1] < (button_y + button_hoehe):
                    pygame.draw.rect(window, farbe_aktiv,(button_x, button_y, button_laenge, button_hoehe))
                    window.blit(start_again, (347, 337))
                    pygame.draw.rect(window, farbe_rand,(button_x, button_y, button_laenge, button_hoehe), 1)
                    if maus_click[0] == 1:
                        run = True
                        direction = True
                        go = True
                        start = True
                        score = 0
                        g = 30
                        o = 30
                        c = 0
                        m = -1
                        n = -1
                        schlange_X = 600
                        schlange_Y = 400
                        bombe_X = 100
                        bombe_Y = 200
                        schlange_v = 2
                        bombe_v = 3
                        pygame.time.wait(150)
                else:
                    pygame.draw.rect(window, farbe_inaktiv, (button_x, button_y, button_laenge, button_hoehe))
                    window.blit(start_again, (347, 337))
                    pygame.draw.rect(window, farbe_rand,(button_x, button_y, button_laenge, button_hoehe), 1)
                pygame.display.update()
