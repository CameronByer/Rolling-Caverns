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

player_dice = [Die.Die(0, [Die.Face(Item.Dud()) for f in range(6)]) for d in range(3)]

player = Player.Player(100, player_dice)

enemies = [random.choice(enemy_list)() for i in range(6)]

## Game loop
running = True
combat = False
while running:

    clock.tick(FPS) ## will make the loop run at the same speed all the time
    enemy = enemies[0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT or not player.active:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                player.inventory_open = not player.inventory_open
            if combat:
                if event.button == 1:
                    player.turn(enemies[0])
                    if enemies[0].health <= 0:
                        enemies = enemies[1:]
                        while len(enemies) < 6:
                            enemies.append(random.choice(enemy_list)())
                        combat = False
                if event.button == 3: #Right Click
                    for die in player.dice:
                        if die.contains(event.pos):
                            for other_die in player.dice:
                                other_die.selected = False
                            die.click()
                        expandedFaceIndex = die.get_expanded_index(event.pos)
                        if expandedFaceIndex != None:
                            for face in die.faces:
                                face.selected = False
                            die.faces[expandedFaceIndex].selected = True
                            player.inventory_open = True
                            #die.faces[expandedFaceIndex] = Die.Face(Item.Item.random_item())
                    if player.get_inventory_index(event.pos) and player.get_selected_index():
                        die_index, face_index = player.get_selected_index()
                        inventory_index = player.get_inventory_index(event.pos)
                        player.dice[die_index].faces[face_index], player.inventory[inventory_index] = player.inventory[inventory_index], player.dice[die_index].faces[face_index]
                        player.dice[die_index].faces[face_index].selected = False
                        player.inventory[inventory_index].selected = False
            else:
                if event.button == 1: #Left Click
                    enemies = [enemies[0]]+enemies[2:]
                    combat = True
                if event.button == 3: #Right Click
                    enemies = [enemies[1]]+enemies[2:]
                    combat = True
                    

    screen.fill((255, 255, 255))

    if combat:
        Layout.basic.draw(screen, (player, enemies[0]))
    else:
        for pos, enemy in enumerate(enemies):
            xpos = pos//2
            ypos = pos%2
            enemy.draw(screen, 80+xpos*200, 50+ypos*200)
            #enemy.drawdice(screen, 80+pos*200, 50)

    pygame.display.flip()

pygame.quit()

'''
### ROADMAP ###

1) Inventory

2) Modifiable Dice from Inventory

3) Rework Player Death

4) Enemy Loot

###
'''
