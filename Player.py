import pygame

import Roller

class Player(Roller.Roller):
    def __init__(self, health, dice):
        super().__init__("Player", health, dice)
        self.image = pygame.image.load("Other/Player.png")

    def turn(self, enemy):
        player_result = self.roll()
        enemy_result = enemy.roll()

        enemy_attack = enemy_result["attack"]-player_result["block"]
        if enemy_attack > 0:
            self.damage(enemy_attack)
        player_attack = player_result["attack"]-enemy_result["block"]
        if player_attack > 0:
            enemy.damage(player_attack)

        self.heal(player_result["heal"])
                    
