import pygame

class Item:
    def __init__(self, name):
        self.name = name
    def __init_subclass__(cls, name="???"):
        cls.name = name
        cls.image = pygame.image.load("Item/"+name+".png")
        cls.image.set_colorkey(cls.image.get_at((0, 0)))
        cls.size = cls.image.get_size()
    def draw(self, screen, x, y, w, h):
        screen.blit(pygame.transform.scale(self.image, (w, h)), (x, y))

class WoodenSword(Item, name="Wooden Sword"):
    def __init__(self):
        super().__init__(self.name)

class GoldHelmet(Item, name="Gold Helmet"):
    def __init__(self):
        super().__init__(self.name)
