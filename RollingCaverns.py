import pygame
import random

import Die

WIDTH = 800
HEIGHT = 600
FPS = 60

def get_roll(dice):
    results = [die.roll() for die in dice]

## initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rolling Caverns")
clock = pygame.time.Clock() ## For syncing the FPS

## Game loop
running = True
while running:

    clock.tick(FPS) ## will make the loop run at the same speed all the time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #Left Click
                b.chargespot = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #Left Click
                b.launch(pygame.mouse.get_pos())

    screen.fill(DARKGREEN)

    b.update()
    b.draw(None)

    pygame.display.flip()       

pygame.quit()
