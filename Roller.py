import pygame

class Roller:

    def __init__(self, name, health, dice, img_dir="", frames=1):
        self.frames = frames
        self.frame = 0
        self.health = health
        self.dice = dice
        uncropped = pygame.image.load(img_dir+"/"+name+".png")
        w, h = uncropped.get_size()
        h = h//frames-2
        cropped = pygame.Surface((w, h))
        cropped.blit(uncropped, (0, 0, w, h))
        cropped.set_colorkey(cropped.get_at((0, 0)))
        self.image = cropped
        self.size = w, h

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
