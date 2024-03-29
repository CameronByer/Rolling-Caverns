import pygame
import random

class Item:
    items = {}
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
        Item.items[name] = cls
    def draw(self, screen, x, y, w, h):
        screen.blit(pygame.transform.scale(self.image, (w, h)), (x, y))
    def random_item():
        return random.choice(list(Item.items.values()))()

class Dud(Item):
    def __init__(self):
        super().__init__()

class Copper_Broadsword(Item, damage=8):
    def __init__(self):
        super().__init__()

class Copper_Chainmail(Item, block=6):
    def __init__(self):
        super().__init__()

class Copper_Greaves(Item, block=3):
    def __init__(self):
        super().__init__()

class Copper_Helmet(Item, block=3):
    def __init__(self):
        super().__init__()

class Crimson_Rod(Item, damage=12):
    def __init__(self):
        super().__init__()    

class Gold_Bow(Item, damage=11):
    def __init__(self):
        super().__init__()

class Gold_Broadsword(Item, damage=13):
    def __init__(self):
        super().__init__()

class Gold_Chainmail(Item, block=15):
    def __init__(self):
        super().__init__()

class Gold_Greaves(Item, block=12):
    def __init__(self):
        super().__init__()

class Gold_Helmet(Item, block=12):
    def __init__(self):
        super().__init__()

class Iron_Bow(Item, damage=8):
    def __init__(self):
        super().__init__()

class Iron_Broadsword(Item, damage=10):
    def __init__(self):
        super().__init__()

class Iron_Chainmail(Item, block=9):
    def __init__(self):
        super().__init__()

class Iron_Greaves(Item, block=6):
    def __init__(self):
        super().__init__()

class Iron_Helmet(Item, block=6):
    def __init__(self):
        super().__init__()

class Lesser_Healing_Potion(Item, heal=50):
    def __init__(self):
        super().__init__()

class Lesser_Mana_Potion(Item, mana=50):
    def __init__(self):
        super().__init__()

class Life_Crystal(Item, maxhealth=20):
    def __init__(self):
        super().__init__()

class Mana_Crystal(Item, maxmana=20):
    def __init__(self):
        super().__init__()

class Silver_Bow(Item, damage=9):
    def __init__(self):
        super().__init__()

class Silver_Broadsword(Item, damage=11):
    def __init__(self):
        super().__init__()

class Silver_Chainmail(Item, block=12):
    def __init__(self):
        super().__init__()

class Silver_Greaves(Item, block=9):
    def __init__(self):
        super().__init__()

class Silver_Helmet(Item, block=9):
    def __init__(self):
        super().__init__()

class Space_Gun(Item, damage=16):
    def __init__(self):
        super().__init__()

class Vilethorn(Item, damage=10):
    def __init__(self):
        super().__init__()

class Wand_of_Sparking(Item, damage=14):
    def __init__(self):
        super().__init__()

class Water_Bolt(Item, damage=19):
    def __init__(self):
        super().__init__()

class Wood_Breastplate(Item, block=3):
    def __init__(self):
        super().__init__()

class Wood_Greaves(Item, block=3):
    def __init__(self):
        super().__init__()

class Wood_Helmet(Item, block=0):
    def __init__(self):
        super().__init__()

class Wooden_Arrow(Item, damage=4):
    def __init__(self):
        super().__init__()

class Wooden_Bow(Item, damage=4):
    def __init__(self):
        super().__init__()
        
class Wooden_Sword(Item, damage=7):
    def __init__(self):
        super().__init__()


dud = Dud()
