import pygame,sys,random,time
from pygame.locals import*
pygame.init()

FPS = 30
screen = pygame.display.set_mode((430,430))
screen.fill((0,0,0))
pygame.display.set_caption("Simon")

BEEP1 = pygame.mixer.Sound('beep1.ogg')
BEEP2 = pygame.mixer.Sound('beep2.ogg')
BEEP3 = pygame.mixer.Sound('beep3.ogg')
BEEP4 = pygame.mixer.Sound('beep4.ogg')

DIMYELLOW = (100,100,0)
DIMRED = (100,0,0)
DIMBLUE = (0,0,100)
DIMGREEN = (0,100,0)
BRIGHTYELLOW = (255,255,100)
BRIGHTRED = (255,0,100)
BRIGHTBLUE = (100,0,255)
BRIGHTGREEN = (0,255,100)
YELLOW = (255,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

def drawRects():
    pygame.draw.rect(screen, (YELLOW), (10, 10, 200, 200))
    pygame.draw.rect(screen, (RED), (10, 220, 200, 200))
    pygame.draw.rect(screen, (BLUE), (220, 10, 200, 200))
    pygame.draw.rect(screen, (GREEN), (220,220,200,200))

def drawStartRects():
    pygame.draw.rect(screen, (DIMYELLOW), (10, 10, 200, 200))
    pygame.draw.rect(screen, (DIMRED), (10, 220, 200, 200))
    pygame.draw.rect(screen, (DIMBLUE), (220, 10, 200, 200))
    pygame.draw.rect(screen, (DIMGREEN), (220,220,200,200))

YELLOWRECT = pygame.Rect(10, 10, 200, 200)
REDRECT = pygame.Rect(10, 220, 200, 200)
BLUERECT = pygame.Rect(220, 10, 200, 200)
GREENRECT = pygame.Rect(220,220,200,200)
STARTRECT = pygame.Rect(80,150,150,80)

colors = [YELLOW,RED,BLUE,GREEN]


def flashButtonAnimation(color):
    if color == YELLOW:
        sound = BEEP1
        sound.play()
        print ("yellow")
        pygame.draw.rect(screen, (BRIGHTYELLOW), (10, 10, 200, 200))
        pygame.display.update()
        pygame.time.delay(500)
        drawRects()
        pygame.display.update()
    elif color == RED:
        sound = BEEP2
        sound.play()
        print ("red")
        pygame.draw.rect(screen, (BRIGHTRED), (10, 220, 200, 200))
        pygame.display.update()
        pygame.time.delay(500)
        drawRects()
        pygame.display.update()
    elif color == BLUE:
        sound = BEEP3
        sound.play()
        print ("blue")
        pygame.draw.rect(screen, (BRIGHTBLUE), (220, 10, 200, 200))
        pygame.display.update()
        pygame.time.delay(500)
        drawRects()
        pygame.display.update()
    elif color == GREEN:
        sound = BEEP4
        sound.play()
        print ("green")
        pygame.draw.rect(screen, (BRIGHTGREEN), (220,220,200,200))
        pygame.display.update()
        pygame.time.delay(500)
        drawRects()
        pygame.display.update()

mode = "START"
pattern = []
score = 0

running = True
for event in pygame.event.get():
    if event.type == MOUSEBUTTONUP:
        running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 

        if event.type == MOUSEBUTTONUP:
            mousex,mousey = event.pos
            print(mousex,mousey)
            if mode == "START":
                if STARTRECT.collidepoint((mousex,mousey)):
                    screen.fill((0,0,0))
                    mode = "COMPUTER"
                    print(mode)
            if mode == "PLAYER":
                print (f"{move} move")
                print(f"Pattern:  {pattern}")
                if YELLOWRECT.collidepoint((mousex,mousey)):
                    flashButtonAnimation(YELLOW)
                    if pattern[move] == YELLOW:
                        move = move+1  
                        if move == len(pattern):
                            mode = "COMPUTER"
                    else:
                        print("GAME OVER")
                        mode = "GAME OVER"


                elif REDRECT.collidepoint((mousex,mousey)):
                    flashButtonAnimation(RED)
                    if pattern[move] == RED:
                        move = move+1  
                        if move == len(pattern):
                            mode = "COMPUTER"
                    else:
                        print("GAME OVER")
                        mode = "GAME OVER"

                elif BLUERECT.collidepoint((mousex,mousey)):
                    flashButtonAnimation(BLUE)
                    if pattern[move] == BLUE:
                        move = move+1  
                        if move == len(pattern):
                            mode = "COMPUTER"
                    else:
                        print("GAME OVER")
                        mode = "GAME OVER"


                elif GREENRECT.collidepoint((mousex,mousey)):

                    flashButtonAnimation(GREEN)
                    if pattern[move] == GREEN:
                        move = move+1  
                        if move == len(pattern):
                            mode = "COMPUTER"
                    else:
                        print("GAME OVER")
                        mode = "GAME OVER"

        if mode == "START":
            move = 0
            drawStartRects()
            fontObj = pygame.font.SysFont('tahoma', 96)
            fontSurfaceObj = fontObj.render("START",  True, (0, 255, 0), (255, 255, 255))
            screen.blit(fontSurfaceObj, (STARTRECT.topleft))
            fontObj = pygame.font.SysFont('tahoma', 24)
            fontSurfaceObj = fontObj.render("Click the squares to follow the pattern",  True, (0, 255, 0), (255, 255, 255))
            screen.blit(fontSurfaceObj, (10,250))
            pygame.display.update()

        if mode == "COMPUTER":
            move = 0
            drawRects()
            pattern.append(random.choice(colors))
            for c in pattern:
                if c == YELLOW:
                    flashButtonAnimation(YELLOW)
                if c == RED:
                    flashButtonAnimation(RED)
                if c == BLUE:
                    flashButtonAnimation(BLUE)
                if c == GREEN:
                    flashButtonAnimation(GREEN)
            print(pattern)
            pygame.time.delay(500)
            mode = "PLAYER"

        if mode == "GAME OVER":
            move = 0
            pattern.remove(all.colors)
            drawStartRects()
            fontObj = pygame.font.SysFont('tahoma', 84)
            fontSurfaceObj = fontObj.render("RESTART",  True, (0, 255, 0), (255, 255, 255))
            screen.blit(fontSurfaceObj, (STARTRECT.topleft))
            fontObj = pygame.font.SysFont('tahoma', 24)
    


