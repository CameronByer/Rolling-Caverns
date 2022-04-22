import pygame

class Item:
    stats = {}
    def __init__(self, **kwargs):
        if "name" in kwargs:
            self.name = kwargs.pop("name")
        else:
            self.name = type(self).__name__.replace("_", " ")
        if "image" in kwargs:
            self.image = kwargs.pop("image")
        if not self.stats:
            self.stats = kwargs
    def __init_subclass__(cls, **kwargs):
        name = cls.__name__.replace("_", " ")
        image_path = "Item/"
        if "image_path" in kwargs:
            image_path = kwargs.pop("image_path")
        cls.stats = kwargs
        cls.image = pygame.image.load(image_path+name+".png")
        cls.image.set_colorkey(cls.image.get_at((0, 0)))
        cls.size = cls.image.get_size()
    def draw(self, screen, x, y, w, h):
        screen.blit(pygame.transform.scale(self.image, (w, h)), (x, y))

class Dud(Item):
    def __init__(self):
        super().__init__()

class Gold_Helmet(Item, block=15):
    def __init__(self):
        super().__init__()

class Potion(Item, heal=10):
    def __init__(self):
        super().__init__()
        
class Wooden_Sword(Item, damage=7):
    def __init__(self):
        super().__init__()


dud = Dud()
