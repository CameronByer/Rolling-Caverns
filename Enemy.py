import pygame

import Die
import Item
import Roller

class Enemy(Roller.Roller):
    def __init__(self, health, dice, drops, frames=1):
        super().__init__(type(self).__name__.replace("_", " "), health, dice, frames)
        self.drops = drops
    def __init_subclass__(cls, attack=0, frames=1):
        name = cls.__name__.replace("_", " ")
        cls.frames = frames
        uncropped = pygame.image.load("Enemy/"+name+".png")
        w, h = uncropped.get_size()
        h = h//frames-2
        cropped = pygame.Surface((w, h))
        cropped.blit(uncropped, (0, 0, w, h))
        cropped.set_colorkey(cropped.get_at((0, 0)))
        cls.image = cropped
        cls.size = w, h
        cls.attack = attack
        cls.default_attack = Die.Face(Item.Item(name=name, image=cls.image, attack=cls.attack), "VALUE")

class Eater_Of_Souls(Enemy, attack=12, frames=2):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*4+[Die.Face(Item.dud, "VALUE")]*2) for d in range(3)]
        super().__init__(40, dice, None, self.frames)
        #self.image = pygame.transform.rotate(self.image, -90)

class Eye_Of_Cthulhu(Enemy, attack=18, frames=6):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*4+[Die.Face(Item.dud, "VALUE")]*2) for d in range(4)]
        super().__init__(3000, dice, None, self.frames)

class Zombie(Enemy, attack=8, frames=3):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*4+[Die.Face(Item.dud, "VALUE")]*2) for d in range(2)]
        super().__init__(45, dice, None, self.frames)
