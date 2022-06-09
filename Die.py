import pygame
import random

class Die:

    def __init__(self, cost, faces):
        self.cost = cost
        self.faces = faces
        self.expanded = False
        self.pos = (0, 0)
        self.face_size = 0
        self.expanded_pos = (0, 0)
        self.expanded_face_size = 0
        self.roll()

    def click(self):
        self.expanded = not self.expanded

    def click_expanded(self):
        #relative
        pass

    def contains(self, point):
        rect = pygame.Rect(self.pos, (self.face_size, self.face_size))
        return self.pos[0] <= point[0] and self.pos[1] <= point[1] and self.pos[0]+self.face_size > point[0] and self.pos[1]+self.face_size > point[1]

    def contains_expanded(self, point):
        pass

    def draw(self, screen, border=2):
        self.top.draw(screen, self.pos, self.face_size, border)
        if self.expanded:
            self.draw_expanded(screen, (300, 200), border)

    def draw_expanded(self, screen, pos, border=2):
        offsets = [(i%3, i//3) for i in range(len(self.faces))]
        for f in range(len(self.faces)):
            self.faces[f].draw(screen, (pos[0]+offsets[f][0]*(self.face_size-border), pos[1]+offsets[f][1]*(self.face_size-border)))

    def roll(self):
        self.top = random.choice(self.faces)
        return self.top

class Face:

    def __init__(self, item):
        self.item = item

    def draw(self, screen, pos, face_size=50, border=2):
        pygame.draw.rect(screen, (0, 0, 0), (pos[0], pos[1], face_size, face_size))
        pygame.draw.rect(screen, (255, 255, 255), (pos[0]+border, pos[1]+border, face_size-2*border, face_size-2*border))
        self.item.draw(screen, pos[0]+border+5, pos[1]+border+5, face_size-2*border-10, face_size-2*border-10)
