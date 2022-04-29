import pygame

import Roller

class Player(Roller.Roller):
    def __init__(self, health, dice):
        super().__init__("Player", health, dice)
        self.image = pygame.image.load("Other/Player.png")

    def kill(self):
        self.health = self.maxhealth
        print("DEATH")

    def turn(self, enemy):
        player_result = self.roll()
        enemy_result = enemy.roll()

        self.attack(enemy)
        enemy.attack(self)

        if self.health <= 0:
            self.kill()
        else:
            self.heal(player_result["heal"])
                    
