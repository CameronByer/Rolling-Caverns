import pygame
import random

import Die
import Enemy

WIDTH = 800
HEIGHT = 600
FPS = 60

## initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rolling Caverns")
clock = pygame.time.Clock() ## For syncing the FPS

zombie = Enemy.Zombie()
eos = Enemy.EaterOfSouls()
eoc = Enemy.EyeOfCthulhu()

## Game loop
running = True
while running:

    clock.tick(FPS) ## will make the loop run at the same speed all the time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #Left Click
                pass
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #Left Click
                pass

    screen.fill((255, 255, 255))

    zombie.draw(screen, 50, 100)
    eos.draw(screen, 500, 200)
    eoc.draw(screen, 150, 300)

    pygame.display.flip()       

pygame.quit()
