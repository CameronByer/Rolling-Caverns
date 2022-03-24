import pygame

class Roller:

    def __init__(self, name, health, dice, frames):
        self.frames = frames
        self.frame = 0
        self.health = health
        self.dice = dice

    def __str__(self):
        return self.name + ": " + self.health

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

    def roll(self):
        result = {"attack": 0, "block": 0, "energy": 0}
        for die in dice:
            if die.cost <= result["energy"]:
                result["energy"] -= die.cost
                outcome = die.roll()
                for item in outcome:
                    result[item] += outcome[item]
        return result
