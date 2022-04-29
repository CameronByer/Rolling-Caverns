import pygame

import Die
import Item
import Roller

class Enemy(Roller.Roller):
    def __init__(self, health, dice, drops, frames=1):
        super().__init__(type(self).__name__.replace("_", " "), health, dice, frames)
        self.drops = drops
    def __init_subclass__(cls, damage=0, frames=1):
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
        cls.damage = damage
        cls.default_attack = Die.Face(Item.Item(name=name, image=cls.image, damage=cls.damage), "VALUE")

class Antlion(Enemy, damage=15, frames=5):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*4+[Die.Face(Item.dud, "VALUE")]*2) for d in range(1)]
        super().__init__(45, dice, None, self.frames)

class Blood_Crawler(Enemy, damage=20, frames=5):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*2+[Die.Face(Item.dud, "VALUE")]*4) for d in range(2)]
        super().__init__(60, dice, None, self.frames)

class Demon(Enemy, damage=20, frames=5):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*3+[Die.Face(Item.dud, "VALUE")]*3) for d in range(2)]
        super().__init__(120, dice, None, self.frames)    

class Eater_Of_Souls(Enemy, damage=7, frames=2):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*3+[Die.Face(Item.dud, "VALUE")]*3) for d in range(3)]
        super().__init__(40, dice, None, self.frames)
        #self.image = pygame.transform.rotate(self.image, -90)

class Eye_Of_Cthulhu(Enemy, damage=7, frames=6):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*5+[Die.Face(Item.dud, "VALUE")]*1) for d in range(5)]
        super().__init__(3000, dice, None, self.frames)

class Harpy(Enemy, damage=10, frames=6):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*3+[Die.Face(Item.dud, "VALUE")]*3) for d in range(4)]
        super().__init__(100, dice, None, self.frames)

class Hornet(Enemy, damage=12, frames=3):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*2+[Die.Face(Item.dud, "VALUE")]*4) for d in range(4)]
        super().__init__(48, dice, None, self.frames)

class Ice_Slime(Enemy, damage=9, frames=2):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*5+[Die.Face(Item.dud, "VALUE")]*1) for d in range(2)]
        super().__init__(30, dice, None, self.frames)

class Shark(Enemy, damage=22, frames=4):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*1+[Die.Face(Item.dud, "VALUE")]*5) for d in range(3)]
        super().__init__(300, dice, None, self.frames)

class Skeleton(Enemy, damage=8, frames=6):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*3+[Die.Face(Item.dud, "VALUE")]*3) for d in range(3)]
        super().__init__(60, dice, None, self.frames)

class Tim(Enemy, damage=10, frames=3):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*2+[Die.Face(Item.dud, "VALUE")]*4) for d in range(5)]
        super().__init__(200, dice, None, self.frames)

class Vulture(Enemy, damage=6, frames=6):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*4+[Die.Face(Item.dud, "VALUE")]*2) for d in range(2)]
        super().__init__(40, dice, None, self.frames)

class Zombie(Enemy, damage=8, frames=3):
    def __init__(self):
        dice = [Die.Die("COST", [self.default_attack]*4+[Die.Face(Item.dud, "VALUE")]*2) for d in range(2)]
        super().__init__(45, dice, None, self.frames)
