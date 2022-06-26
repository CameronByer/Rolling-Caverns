import pygame

class Interface:

    def __init__(self, pieces):
        self.pieces = pieces

    def draw(self, screen):
        for piece in self.pieces:
            piece.draw(screen)

    def click(self, pos):
        for piece in self.pieces:
            if piece.contains(pos):
                piece.click()

class Slot:

    def __init__(self, pos, size=50):
        self.pos = pos
        self.size = size

class ItemSlot(Slot):

    def __init__(self, item, pos, size=50):
        self.item = item
        super().__init(pos, size)

    def contains(self, point):
        return self.pos[0] < point[0] < self.pos[0]+self.size and self.pos[1] < point[1] < self.pos[1]+self.size

class DieSlot(Slot):

    def __init__(self, die, pos, size=50):
        self.item = die
        super().__init(pos, size)
