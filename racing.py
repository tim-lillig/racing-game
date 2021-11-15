import pygame
import math
import random
import sys
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        for i in range(1,9):
            img = pygame.image.load(os.path.join('images', 'car' + str(i) + '.png')).convert()
            img.set_colorkey((255,255,255))
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.speed = 0
        self.angle = 0


WIDTH = 1012
HEIGHT = 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("racing game")

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)


pygame.init()
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join('images','track.png'))
backgroundbox = WIN.get_rect()

player = Player()
computer = Player()

player.rect.x = 435
player.rect.y = 45
computer.rect.x = 435
computer.rect.y = 65

player_list = pygame.sprite.Group()
player_list.add(player)
player_list.add(computer)


speedChange = 0
player.angle = 0.0
changeAngle = 0

keyList = []


def playerAnimation():
    global keyList

    player.angle += changeAngle

    if 'UP' not in keyList and player.speed > 0:
        player.speed -= 10
    elif 'DOWN' not in keyList and player.speed < 0:
        player.speed += 5

    if -400 <= player.speed + speedChange <= 700:
        player.speed += speedChange

    if 0 <= player.angle < 45:
        player.image = player.images[0]

    if 45 <= player.angle < 90:
        player.image = player.images[1]

    if 90 <= player.angle < 135:
        player.image = player.images[2]

    if 135 <= player.angle < 180:
        player.image = player.images[3]

    if 180 <= player.angle < 225:
        player.image = player.images[4]

    if 225 <= player.angle < 270:
        player.image = player.images[5]

    if 270 <= player.angle < 315:
        player.image = player.images[6]

    if 315 <= player.angle < 360:
        player.image = player.images[7]

    if player.angle >= 360:
        player.angle -= 360
    elif player.angle < 0:
        player.angle += 360

    #print('current speed: {}'.format(player.speed/10.0))
    #print('current angle: {}'.format(player.angle))

    player.rect.x += int(player.speed/100 * math.cos(math.radians(player.angle)))
    player.rect.y += int(player.speed/100 * math.sin(math.radians(player.angle)))

    keyList = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keyList.append('UP')
                speedChange = 15
            if event.key == pygame.K_DOWN:
                keyList.append('DOWN')
                speedChange = -10
            if event.key == pygame.K_LEFT:
                changeAngle -= 5
            if event.key == pygame.K_RIGHT:
                changeAngle += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                speedChange = 0
            if event.key == pygame.K_DOWN:
                speedChange = 0
            if event.key == pygame.K_LEFT:
                changeAngle += 5
            if event.key == pygame.K_RIGHT:
                changeAngle -= 5

    playerAnimation()

    WIN.blit(background, backgroundbox)
    player_list.draw(WIN)
    pygame.display.flip()
    clock.tick(60)
