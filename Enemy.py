import pygame
import Roller

class Enemy(Roller.Roller):
    def __init__(self, name, health, dice, drops, frames=1):
        super().__init__(name, health, dice, "Enemy", frames)
        self.drops = drops

class EaterOfSouls(Enemy):
    def __init__(self):
        super().__init__("Eater of Souls", 40, None, None, 2)
        self.image = pygame.transform.rotate(self.image, -90)

class EyeOfCthulhu(Enemy):
    def __init__(self):
        super().__init__("Eye of Cthulhu", 3000, None, None, 6)
        self.image = pygame.transform.rotate(self.image, 45)

class Zombie(Enemy):
    def __init__(self):
        super().__init__("Zombie", 45, None, None, 3)
