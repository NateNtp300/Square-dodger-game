import pygame
from pygame.locals import *
import os
import random
import time
pygame.font.init()
pygame.init()

screenWidth = 720
screenHeight = 720
win = pygame.display.set_mode((screenWidth,screenHeight))
keys = pygame.key.get_pressed()
FPS = 60
screenColor = (0,0,0) #black
red =(255,0,0)

pygame.display.set_caption("Dodger") #window name

projectilesLen = 50
projectiles = [None]*projectilesLen

startImg = pygame.image.load('buttons/start.png').convert_alpha()
quitImg = pygame.image.load('buttons/quit.png').convert_alpha()
shopImg = pygame.image.load('buttons/shop.png').convert_alpha()
backImg = pygame.image.load('buttons/back.png').convert_alpha()
buyBlueImg = pygame.image.load('buttons/buy_blue.png').convert_alpha()
buyGreenImg = pygame.image.load('buttons/buy_green.png').convert_alpha()
playAgainImg = pygame.image.load('buttons/play_again.png').convert_alpha()
menuImg = pygame.image.load('buttons/menu.png').convert_alpha()
equipGreenImg = pygame.image.load('buttons/equip_green.png').convert_alpha()
equipRedImg = pygame.image.load('buttons/equip_red.png').convert_alpha()
equipBlueImg = pygame.image.load('buttons/equip_blue.png').convert_alpha()


class SquareClass():
    def __init__(self,x,y, width, height, coins):
        self.x=x
        self.y=y
        self.width = width
        self.height = height
        self.coins = coins
        self.speed = 8
        self.finish = False
        self.dead = False
        self.squareColor = (255,0,0)
        self.squareHitbox = (self.x, self.y, self.width, self.height)
        self.squareRect = (0,0,0,0)
        self.red = True
        self.green = False
        self.blue = False
    
    

class Projectiles():
    def __init__(self, y, width, height, speed):
        self.x=random.randint(10,700)
        self.y=y
        self.speed = speed
        self.width = width
        self.height = height
        self.offScreen = False
        self.kill = False
        self.projectileColor = (0,255,255)
        self.projectileHitbox = (self.x, self.y, self.width, self.height)
        self.projectileRect = (0,0,0,0)

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.over = False
    
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check if mouse is over button and check click conditions
        if self.rect.collidepoint(pos):
            
            #[0] means left click
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                #print('clicked')
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        win.blit(self.image, (self.rect.x, self.rect.y))

        return action

equipGreenBtn = Button(100, 500, equipGreenImg, 0.5)
equipBlueBtn = Button(300, 500, equipBlueImg, 0.5)
equipRedBtn = Button(500, 500, equipRedImg, 0.5)

startBtn = Button( screenWidth//2 - 190, 100, startImg, 0.8)
shopBtn = Button( screenWidth//2 - 190, 300, shopImg, 0.8)
quitBtn = Button( screenWidth//2 - 140, 500, quitImg, 0.5)
menuBtn = Button( 400, 600, menuImg, 0.5)
backBtn = Button( 50, 650, backImg, 0.5)
buyBlueBtn = Button( 50, 200, buyBlueImg, 0.5)
buyGreenBtn = Button( 300, 200, buyGreenImg, 0.5)
playAgainBtn = Button(100, 600, playAgainImg, 0.5)



def createProjectiles():
    i = 0
    #while i < 10:
    for i in range(10):
        #if i >=0 and i <=10:
        projectiles[i] = Projectiles(0, 10, 64, 10)
    i = 10
    while i < 20:
        projectiles[i] = Projectiles(-500, 10, 64, 10)
        i+=1
    i = 20
    while i < 30:
        projectiles[i] = Projectiles(-1000, 10, 64, 10)
        i+=1
    i = 30
    while i < 40:
        projectiles[i] = Projectiles(-1500, 10, 64, 10)
        i+=1
    i = 40
    while i < 50:
        projectiles[i] = Projectiles(-2000, 10, 64, 10)
        i+=1
        

square = SquareClass(100,640, 64, 64, 0)
squareRedDisplay = SquareClass(640,640,64,64,0)
squareBlueDisplay = SquareClass(640,640,64,64,0)
squareGreenDisplay = SquareClass(640,640,64,64,0)


def drawProjectiles():
    i = 0
    
    z = 0
    
        
    
    while z < projectilesLen:
        projectiles[z].projectileRect = pygame.Rect(projectiles[z].x, projectiles[z].y, projectiles[z].width, projectiles[z].height)
        z+=1

    while i < projectilesLen: #and projectiles[i].y <= screenHeight - 100:
        if projectiles[i].y <= screenHeight + 100:
            pygame.draw.rect(win, projectiles[i].projectileColor, projectiles[i].projectileRect)
            projectiles[i].y += projectiles[i].speed
        if  projectiles[projectilesLen-1].y > screenHeight+100:
            #roundWin()
            square.finish = True
 
        i+=1
            
 

               


def roundWin():
    win.fill(screenColor)
    winMessage = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface2 = winMessage.render('Round win', False, (255, 255, 255))
    win.blit(text_surface2, (screenWidth//2,screenHeight//2))    
    


def drawSquare():
    i=0

    square.squareRect = pygame.Rect(square.x, square.y, square.width, square.height)

    while i < projectilesLen and square.dead == False:
        if square.squareRect.colliderect(projectiles[i].projectileRect):
            #print(f'hit {i} ')
            #deathMessage()
            square.dead = True
            
        else:
            if square.red == True:
                pygame.draw.rect(win, (255,0,0), square.squareRect)
            if square.green == True:
                pygame.draw.rect(win, (0,250,0), square.squareRect)
            if square.blue == True:
                pygame.draw.rect(win, (0,0,250), square.squareRect)
        i+=1
        
            
    
def checkDeath():
    #A more complex algorithm to check for collision

    #projectiles[0].projectileHitbox = (projectiles[0].x, projectiles[0].y, projectiles[0].width, projectiles[0].height)
    #square.squareHitbox = (square.x, square.y, square.width, square.height)
        
    #if square.y - 0 < projectiles[0].projectileHitbox[1] + projectiles[0].projectileHitbox[3] and square.y + 64 > projectiles[0].projectileHitbox[1]:
        # if square.x + 64 > projectiles[0].projectileHitbox[0] and square.x - 0< projectiles[0].projectileHitbox[0] + projectiles[0].projectileHitbox[2]:
                
        #     square.dead = True
    
    pass
    
         
        
    

def redrawScreen():
    win.fill(screenColor)
    drawProjectiles()
    drawSquare()
    pygame.display.update()
  


def squareMovement():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and square.x > 0:
        square.x -= square.speed

    if keys[pygame.K_d] and square.x < screenWidth - square.width:
        square.x += square.speed

    if keys[pygame.K_w] and square.y > 0:
        square.y -= square.speed

    if keys[pygame.K_s] and square.y < screenHeight - square.height:
        square.y += square.speed

def printCountdown():
        win.fill(screenColor)
        font1 = pygame.font.SysFont('Comic Sans MS', 30)
        surface1 = font1.render('3', False, (255,0,255))
        win.blit(surface1, (200,100))
    #pygame.time.wait(1000)
        #pygame.time.delay(1000)

   

clock = pygame.time.Clock()

def menu():
    run = True
    while run:
        win.fill((0,0,0))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if startBtn.draw():
            square.finish = False
            run = False
            print('play again')
            gamePlayLoop()
        if shopBtn.draw():
            run = False
            print('shop')
            shopMenu()
        if quitBtn.draw():
            run = False
        pygame.display.update()


boughtBlue = False
boughtGreen = False
equipBlue = False
equipGreen = False
equipRed = True
def shopMenu():
    run = True
    global boughtBlue
    global boughtGreen
    global equipBlue
    global equipGreen
    global equipRed
    notEnough = False
    
    while run:
        
        pygame.event.get()
        win.fill((0,0,0))
        my_font = pygame.font.SysFont('freesansbold.ttf', 30)
        clock.tick(FPS)

        text_surface = my_font.render('Your coins: ' + str(square.coins), False, (250, 250, 250))
        win.blit(text_surface, (50,50))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
            
        if backBtn.draw():
            run = False
            menu()
        if boughtBlue == False:
            text_surface = my_font.render('Blue costs: 10', False, (250, 250, 250))
            win.blit(text_surface, (50,160))
            if square.coins <=9 and buyBlueBtn.draw():
                notEnough = True
                print('not enough')
            if buyBlueBtn.draw() and square.coins >=10:
                square.coins -=10
                square.red = False
                square.green = False
                square.blue = True
                boughtBlue = True
            
        if boughtGreen == False:
            text_surface = my_font.render('Green costs: 20', False, (250, 250, 250))
            win.blit(text_surface, (300,160))
            if square.coins <=19 and buyGreenBtn.draw():
                notEnough = True
                print('not enough')
            if buyGreenBtn.draw() and square.coins >=20:
                square.red = False
                square.green = True
                square.blue = False
                boughtGreen = True
                square.coins -=20
        
        if boughtBlue == True:
            if equipBlueBtn.draw() and equipBlue == False:
                square.red = False
                square.green = False
                square.blue = True

                equipBlue = True
                equipGreen = False
                equipRed = False

        if boughtGreen == True:
            if equipGreenBtn.draw() and equipGreen == False:
                square.red = False
                square.green = True
                square.blue = False

                equipBlue = False
                equipGreen = True
                equipRed = False

        if equipRedBtn.draw() and equipRed == False:
            square.red = True
            square.green = False
            square.blue = False

            equipBlue = False
            equipGreen = False
            equipRed = True

        if equipBlue == True:
            #rectangle1 = pygame.Rect(100, 600, 64, 64)
            squareBlueDisplay.squareRect = pygame.Rect(squareBlueDisplay.x, squareBlueDisplay.y, squareBlueDisplay.width, squareBlueDisplay.height)
            pygame.draw.rect(win, (0,0,250), squareBlueDisplay.squareRect)
        
        if equipGreen == True:
            #rectangle1 = pygame.Rect(100, 600, 64, 64)
            squareGreenDisplay.squareRect = pygame.Rect(squareGreenDisplay.x, squareGreenDisplay.y, squareGreenDisplay.width, squareGreenDisplay.height)
            pygame.draw.rect(win, (0,250,0), squareGreenDisplay.squareRect)
        
        if equipRed == True:
            squareRedDisplay.squareRect = pygame.Rect(squareRedDisplay.x, squareRedDisplay.y, squareRedDisplay.width, squareRedDisplay.height)
            pygame.draw.rect(win, (250,0,0), squareRedDisplay.squareRect)

        
            

            
        
            
            

        if notEnough == True:
            text_surface = my_font.render('Not enough coins', False, (250, 250, 250))
            win.blit(text_surface, (300,300)) 
       

        pygame.display.update()

def winScreenLoop():
    run = True
    while run:
        win.fill((0,100,200))
        my_font = pygame.font.SysFont('freesansbold.ttf', 30)
        text_surface = my_font.render('You won 10 coins', False, (0, 0, 0))
        win.blit(text_surface, (screenWidth//2,screenHeight//2))
        text_surface2 = my_font.render('Your total coins: ' + str(square.coins), False, (0, 0, 0))
        win.blit(text_surface2, (50,50))
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if playAgainBtn.draw():
            square.finish = False
            run = False
            print('play again')
            gamePlayLoop()
        if menuBtn.draw():
            square.finish = False
            run = False
            print('menu')
            menu()

        pygame.display.update()


def deathScreenLoop():
    run = True
    while run:
        win.fill((red))
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render('You Died', False, (0, 0, 0))
        win.blit(text_surface, (screenWidth//2,screenHeight//2))  
        
        clock.tick(FPS)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                run = False

        if playAgainBtn.draw():
            square.dead = False
            run = False
            print('play again')
            gamePlayLoop()
        
        if menuBtn.draw():
            square.dead = False
            run = False
            menu()
        pygame.display.update()

def gamePlayLoop():
    run = True
    createProjectiles()
    while run:
        win.fill(screenColor)
        
        squareMovement()
        drawProjectiles()
        drawSquare()    
        clock.tick(FPS)

        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                run = False


        if square.dead == True:
            
            run = False
            square.dead = False
            deathScreenLoop()
        

        # if projectiles[projectilesLen-1].y > screenHeight+100:
        #     run = False
        #     winScreenLoop()
        if square.finish == True:
            run = False
            square.coins +=10
            print(square.coins)
            square.finish = False
            winScreenLoop()

        
        # else:
        #     squareMovement()
        #     #projectileMovement()
        #     redrawScreen() 
        pygame.display.update()
    

#gamePlayLoop()
menu()
pygame.quit()