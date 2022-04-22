import pygame

class Roller:

    def __init__(self, name, health, dice, frames=1):
        self.name = name
        self.frames = frames
        self.frame = 0
        self.maxhealth = health
        self.health = health
        self.dice = dice

    def __str__(self):
        return self.name + ": " + str(self.health)

    def attack(self, other):
        damage = sum(die.top.item.stats["damage"] for die in self.dice if "damage" in die.top.item.stats)
        block = sum(die.top.item.stats["block"] for die in other.dice if "block" in die.top.item.stats)
        other.hurt(max(0, damage-block))

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))

    def drawdice(self, screen, x, y, die_size=50, padding=10):
        for slot, die in enumerate(self.dice):
            die.draw(screen, x-(die_size+padding), y+slot*(die_size+padding))

    def drawhealth(self, screen, x, y, width, height):
        pygame.draw.rect(screen, (0, 255, 0), (x, y, width, height))
        missing = (self.maxhealth-self.health)/self.maxhealth
        missing = min(max(0, missing), 1)
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height*missing))

    def heal(self, amount):
        self.health += amount
        self.health = min(self.health, self.maxhealth)

    def hurt(self, amount):
        self.health -= amount
        self.health = max(0, self.health)        

    def roll(self):
        result = {"damage": 0, "block":0, "heal":0}
        for die in self.dice:
            outcome = die.roll()
            for stat in outcome.item.stats:
                result[stat] += outcome.item.stats[stat]
        return result
