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
        result = {}
        for die in dice:
            outcome = die.roll()
            for item in outcome:
                if not item in result:
                    result[item] = 0
                result[item] += outcome[item]
        return result
