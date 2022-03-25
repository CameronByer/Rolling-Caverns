import pygame
import Roller

class Enemy(Roller.Roller):
    def __init__(self, name, health, dice, drops, frames=1):
        super().__init__(name, health, dice, frames)
        self.drops = drops
    def __init_subclass__(cls, name="???", frames=1):
        cls.name = name
        cls.frames = frames
        uncropped = pygame.image.load("Enemy/"+name+".png")
        w, h = uncropped.get_size()
        h = h//frames-2
        cropped = pygame.Surface((w, h))
        cropped.blit(uncropped, (0, 0, w, h))
        cropped.set_colorkey(cropped.get_at((0, 0)))
        cls.image = cropped
        cls.size = w, h

class EaterOfSouls(Enemy, name="Eater of Souls", frames=2):
    def __init__(self):
        super().__init__(self.name, 40, None, None, self.frames)
        #self.image = pygame.transform.rotate(self.image, -90)

class EyeOfCthulhu(Enemy, name="Eye of Cthulhu", frames=6):
    def __init__(self):
        super().__init__(self.name, 3000, None, None, self.frames)

class Zombie(Enemy, name="Zombie", frames=3):
    def __init__(self):
        super().__init__(self.name, 45, None, None, self.frames)
