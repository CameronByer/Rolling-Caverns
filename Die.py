import random

class Die:

    def __init__(self, cost, faces):
        self.cost = cost
        self.faces = faces
        self.top = faces[0]
        self.roll()

    def draw(self, x, y, face_size):
        self.top.draw(self, x, y, face_size)

    def draw_expanded(self, x, y, face_size):
        offsets = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]
        for f in range(len(faces)):
            faces[f].draw(x+offsets[f]*face_size, y+offsets[f]*face_size)

    def roll(self):
        self.top = random.choice(self.faces)
        return self.top


class Face:

    def __init__(self, value):
        self.value = value

    def draw(self, x, y, face_size):
        print(self.value, x, y, face_size)
