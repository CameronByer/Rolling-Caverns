import pygame

class Item:
    def __init__(self, name=None, image=None):
        if name == None:
            self.name = type(self).__name__.replace("_", " ")
        else:
            self.name = name
        if image != None:
            self.image = image
    def __init_subclass__(cls, image_path="Item/"):
        name = cls.__name__.replace("_", " ")
        cls.image = pygame.image.load(image_path+name+".png")
        cls.image.set_colorkey(cls.image.get_at((0, 0)))
        cls.size = cls.image.get_size()
    def draw(self, screen, x, y, w, h):
        screen.blit(pygame.transform.scale(self.image, (w, h)), (x, y))

class Dud(Item):
    def __init__(self):
        super().__init__()

class Gold_Helmet(Item):
    def __init__(self):
        super().__init__()

class Potion(Item):
    def __init__(self):
        super().__init__()
        
class Wooden_Sword(Item):
    def __init__(self):
        super().__init__()


dud = Dud()
