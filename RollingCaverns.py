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

enemy_list = (Enemy.Antlion,
              Enemy.Blood_Crawler,
              Enemy.Demon,
              Enemy.Eater_Of_Souls,
              Enemy.Harpy,
              Enemy.Hornet,
              Enemy.Ice_Slime,
              Enemy.Shark,
              Enemy.Skeleton,
              Enemy.Tim,
              Enemy.Vulture,
              Enemy.Zombie)

player_dice = [Die.Die(0, [Die.Face(random.choice(list(Item.Item.items.values()))(), None) for f in range(20)]) for d in range(4)]

player = Player.Player(100, player_dice)

enemies = [random.choice(enemy_list)() for i in range(3)]

## Game loop
running = True
while running:

    clock.tick(FPS) ## will make the loop run at the same speed all the time
    enemy = enemies[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #Left Click
                while len(enemies)>0 and enemies[0].health<=0:
                    enemies = enemies[1:]
                while len(enemies) < 3:
                    enemies.append(random.choice(enemy_list)())
                player.turn(enemies[0])
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #Left Click
                pass

    screen.fill((255, 255, 255))

    for pos, enemy in enumerate(enemies):
        enemy.draw(screen, 80+pos*200, 50)
        enemy.drawdice(screen, 80+pos*200, 50)
    Layout.basic.draw(screen, (player, enemies[0]))


    pygame.display.flip()

pygame.quit()

'''
### ROADMAP ###

1) Functional Fight --- DONE ---
    a) Player Class --- DONE ---
    b) Item Effects --- DONE ---
    c) Turn Resolution --- DONE ---
    d) Fight Resolution --- DONE ---
        i) For Enemies --- DONE ---
        ii) For Players --- DONE ---
    
2) 10 Enemies --- DONE ---
    a) Ice Slime --- DONE ---
    b) Skeleton --- DONE ---
    c) Hornet --- DONE ---
    d) Blood Crawler --- DONE ---
    e) Harpy --- DONE ---
    f) Shark --- DONE ---
    g) Vulture --- DONE ---
    h) Tim --- DONE ---
    i) Antlion --- DONE ---
    j) Demon --- DONE ---

3) 20 Items
    a) Copper Broadsword --- DONE ---
    b) Iron Broadsword --- DONE ---
    c) Silver Broadsword --- DONE ---
    d) Gold Broadsword --- DONE ---
    e) Wooden Bow --- DONE ---
    f) Copper Bow --- DONE ---
    g) Iron Bow --- DONE ---
    h) Silver Bow --- DONE ---
    i) Gold Bow --- DONE ---
    j) Arrow --- DONE ---
    k) Wand of Sparking
    l) Crimson Rod
    m) Vilethorn
    n) Space Gun
    o) Waterbolt
    p) Mana Crystal
    q) Mana Potion
    r) Lesser Healing Potion --- DONE ---
    s) Wood Armor
    t) Copper Armor --- DONE ---
    u) Iron Armor --- DONE ---
    v) Silver Armor --- DONE ---
    w) Gold Armor --- DONE ---

4) Die Customization

5) Game Map

###
'''
