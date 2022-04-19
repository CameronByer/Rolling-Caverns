import pygame
import random

import Die
import Enemy
import Layout
import Item
import Player

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

gh = Item.Gold_Helmet()
po = Item.Potion()
ws = Item.Wooden_Sword()

player_dice = [Die.Die(0, [Die.Face(ws, None) for i in range(3)]+[Die.Face(gh, None) for i in range(2)]+[Die.Face(po, None) for i in range(1)]) for i in range(3)]

player = Player.Player(100, player_dice)

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
                player.turn(enemies)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #Left Click
                pass

    screen.fill((255, 255, 255))

    for pos, enemy in enumerate(enemies):
        enemy.draw(screen, 80+pos*150, 50)
        enemy.drawdice(screen, 80+pos*150, 50)
    Layout.basic.draw(screen, (player, enemies[0]))

    pygame.display.flip()

pygame.quit()

'''
### ROADMAP ###

1) Functional Fight
    a) Player Class --- DONE ---
    b) Item Effects --- DONE ---
    c) Turn Resolution
    d) Fight Resolution
    
2) 10 Enemies
    a) Green Slime
    b) Skeleton
    c) Hornet
    d) Blood Crawler
    e) Harpy
    f) Shark
    g) Vulture
    h) Tim
    i) Antlion
    j) Demon

3) 20 Items
    a) Copper Broadsword
    b) Iron Broadsword
    c) Silver Broadsword
    d) Gold Broadsword
    e) Wooden Bow
    f) Copper Bow
    g) Iron Bow
    h) Silver Bow
    i) Gold Bow
    j) Arrow
    k) Wand of Sparking
    l) Crimson Rod
    m) Vilethorn
    n) Space Gun
    o) Waterbolt
    p) Mana Crystal
    q) Mana Potion
    r) Lesser Healing Potion
    s) Wood Armor
    t) Iron Armor
    u) Silver Armor
    v) Gold Armor

4) Die Customization

5) Game Map

###
'''
