import pygame
import random

class Die:

    def __init__(self, cost, faces):
        self.cost = cost
        self.faces = faces
        self.top = faces[0]
        self.roll()

    def draw(self, screen, x, y, face_size=50):
        self.top.draw(screen, x, y, face_size)

    def draw_expanded(self, screen, x, y, face_size=50):
        offsets = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]
        for f in range(len(self.faces)):
            self.faces[f].draw(screen, x+offsets[f][0]*face_size, y+offsets[f][1]*face_size)

    def roll(self):
        self.top = random.choice(self.faces)
        return self.top


class Face:

    def __init__(self, item, value):
        self.item = item
        self.value = value

    def draw(self, screen, x, y, face_size=50):
        pygame.draw.rect(screen, (0, 0, 0), (x, y, face_size, face_size), 2)
        self.item.draw(screen, x+5, y+5, face_size-10, face_size-10)
