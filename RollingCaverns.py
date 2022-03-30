import pygame
import random

import Die
import Enemy
import Layout
import Item

WIDTH = 800
HEIGHT = 600
FPS = 60

## initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rolling Caverns")
clock = pygame.time.Clock() ## For syncing the FPS

zombie = Enemy.Zombie()
eos = Enemy.Eater_Of_Souls()
eoc = Enemy.Eye_Of_Cthulhu()

ws = Item.Wooden_Sword()
gh = Item.Gold_Helmet()

player_die = Die.Die(0, [Die.Face(ws, None) for i in range(3)]+[Die.Face(gh, None) for i in range(3)])

enemies = [zombie, eos, eoc]

## Game loop
running = True
while running:

    clock.tick(FPS) ## will make the loop run at the same speed all the time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #Left Click
                player_die.roll()
                for enemy in enemies:
                    for die in enemy.dice:
                        die.roll()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #Left Click
                pass

    screen.fill((255, 255, 255))

    for pos, enemy in enumerate(enemies):
        enemy.draw(screen, 80+pos*150, 50)
    Layout.basic.draw(screen, enemies[1:3])

    player_die.draw(screen, 650, 170)
    player_die.draw_expanded(screen, 600, 50)

    pygame.display.flip()

pygame.quit()
