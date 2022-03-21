import pygame
import Roller

class Enemy(Roller.Roller):

    def __init__(self, name, health, dice, drops, frames=1):
        super().__init__(name, health, dice)
        self.drops = drops
        self.frames = frames
        self.frame = 0
        uncropped = pygame.image.load("Enemy/"+name+".png")
        w, h = uncropped.get_size
        cropped = pygame.Surface(w, h//frames-2)
        cropped.blit(uncropped, (0, 0, w, h//frames-2))
        self.image = cropped

    def draw(self, x, y):
        pass
