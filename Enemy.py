import pygame
import Roller

class Enemy(Roller.Roller):

    def __init__(self, name, health, dice, drops, frames=1):
        super().__init__(name, health, dice, "Enemy", frames)
        self.drops = drops
