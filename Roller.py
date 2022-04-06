import pygame

class Roller:

    def __init__(self, name, health, dice, frames=1):
        self.name = name
        self.frames = frames
        self.frame = 0
        self.health = health
        self.dice = dice

    def __str__(self):
        return self.name + ": " + str(self.health)

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
        for slot, die in enumerate(self.dice):
            die.draw(screen, x-60, y+slot*60)

    def roll(self):
        result = {}
        for die in self.dice:
            outcome = die.roll()
            for stat in outcome.item.stats:
                if not stat in result:
                    result[stat] = 0
                result[stat] += outcome.item.stats[stat]
        return result
