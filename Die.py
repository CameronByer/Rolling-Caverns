import pygame
import random

class Die:

    def __init__(self, cost, faces):
        self.cost = cost
        self.faces = faces
        self.roll()

    def draw(self, screen, x, y, face_size=50, border=2):
        self.top.draw(screen, x, y, face_size, border)

    def draw_expanded(self, screen, x, y, face_size=50, border=2):
        offsets = [(i%3, i//3) for i in range(len(self.faces))]
        for f in range(len(self.faces)):
            self.faces[f].draw(screen, x+offsets[f][0]*(face_size-border), y+offsets[f][1]*(face_size-border))

    def on_click(self):
        self.expanded = not self.expanded
    
    def roll(self):
        self.top = random.choice(self.faces)
        return self.top


class Face:

    def __init__(self, item, value):
        self.item = item
        self.value = value

    def draw(self, screen, x, y, face_size=50, border=2):
        pygame.draw.rect(screen, (0, 0, 0), (x, y, face_size, face_size))
        pygame.draw.rect(screen, (255, 255, 255), (x+border, y+border, face_size-2*border, face_size-2*border))
        self.item.draw(screen, x+border+5, y+border+5, face_size-2*border-10, face_size-2*border-10)
