import pygame

import Roller

class Player(Roller.Roller):
    def __init__(self, health, dice):
        super().__init__("Player", health, dice)
        self.image = pygame.image.load("Other/Player.png")

    def turn(self, enemy):
        player_result = self.roll()
        enemy_result = enemy.roll()

        self.attack(enemy)
        enemy.attack(self)

        self.heal(player_result["heal"])
                    
