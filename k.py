import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((852,480))
pygame.display.set_caption("catch eggs")
icon = pygame.image.load('basket.png')
pygame.display.set_icon(icon)
background = pygame.image.load('backimg.jpg')
hen = pygame.image.load('hen.png')
henx = random.randint(0,788)
heny = 0
henx_change = 0.3
heny_change = 0
basket = pygame.image.load('bbsket.png')
basketx = 20
baskety = 400
basketx_change = 0
baskety_change = 0
egg = pygame.image.load('egg.png')
eggx = henx
eggy = heny
eggx_change = 0
eggy_change = 0.3
score = 0
missed = 0
font = pygame.font.Font('freesansbold.ttf',32)
def displayScore(show,x,y):
    scrnscore = font.render ("Egg Score : "+str(score), show, (255,255,255))
    screen.blit(scrnscore, (x, y))
def displayMissedScore(show,x,y):
    missedScrnScore = font.render ("Missed : "+str(missed), show, (255,255,255))
    screen.blit(missedScrnScore, (x,y))
def isCollided(ex, ey, bx, by):
    distance = math.sqrt((math.pow(bx - ex, 2)) + (math.pow(by - ey, 2)))
    if distance < 40:
        return True
    else:
        return False
def putegg(x,y):
    screen.blit(egg, (x, y))
game_over = False
while not game_over:
    screen.blit(background, (0, 0))
    screen.blit(hen, (henx, heny))
    screen.blit(basket, (basketx, baskety))
    putegg(eggx,eggy)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                basketx_change = -0.6
            if event.key == pygame.K_RIGHT:
                basketx_change = +0.6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                basketx_change = 0
    basketx += basketx_change
    if basketx <= 0:
        basketx = 0
    elif basketx >= 788:
        basketx = 788
    henx += henx_change
    if henx <= 0:
        henx_change = 0.3
        heny += heny_change
        if heny >= 416:
            heny=50
    elif henx >= 788:
        henx_change = -0.3
        heny += heny_change
        if heny >= 416 :
            heny = 50
    if eggy >= 0:
        eggy += eggy_change
    if eggy >= 450:
        eggy,eggx = 0,henx
    eggy += eggy_change
    collision = isCollided(eggx, eggy, basketx, baskety)
    if collision:
        eggy , eggx = 0 , henx
        score +=1
        henx = random.randint(0,788)
        heny = 0
    elif collision == False and eggy>=449:
        missed+=0.5
    if missed >= 30.1:
        screen.fill((255,240,200))
        msg = pygame.font.SysFont('comicsansms', 60).render("GAME OVER", True, (112, 114, 255))
        screen.blit(msg, [270, 150])
    displayScore(True,10,10)
    displayMissedScore(True,10,50)
    pygame.display.update()
pygame.quit()
quit()