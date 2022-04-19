import pygame

import Roller

class Player(Roller.Roller):
    def __init__(self, health, dice):
        super().__init__("Player", health, dice)
        self.image = pygame.image.load("Other/Player.png")

    def turn(self, enemies):
        enemies_result = {}
        for enemy in enemies:
            roll = enemy.roll()
            for result in roll:
                if not result in enemies_result:
                    enemies_result[result] = 0
                enemies_result[result] += roll[result]
        player_result =  self.roll()

        print(enemies_result)
        print(player_result)
        print()
                    
