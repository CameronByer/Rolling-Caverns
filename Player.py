import pygame

import Die, Item, Roller

class Player(Roller.Roller):
    def __init__(self, health, dice):
        super().__init__("Player", health, dice)
        self.image = pygame.image.load("Other/Player.png")
        self.active = True
        self.inventory_open = False
        self.inventory = [Die.Face(Item.Item.random_item()) for i in range(9)]
        self.inventorypos = (100, 100)

    def draw(self, screen, x, y):
        super().draw(screen, x, y)
        if self.inventory_open:
            self.drawinventory(screen)

    def drawinventory(self, screen, die_size = 50):
        for index, item in enumerate(self.inventory):
            x = self.inventorypos[0] + (index%3) * die_size
            y = self.inventorypos[1] + (index//3) * die_size
            item.draw(screen, (x, y), die_size)

    def get_inventory_index(self, point, die_size = 50):
        if not self.inventory_open:
            return None
        COLUMNS = 3
        relative = (point[0]-self.inventorypos[0], point[1]-self.inventorypos[1])
        if relative[0] >= 0 and relative[0] < die_size*COLUMNS:
            x = relative[0] // die_size
            y = relative[1] // die_size
            index = y*COLUMNS + x
            if index >= 0 and index < len(self.inventory):
                return index#player.self.inventory[index]
        return None

    def get_selected_index(self):
        for die in range(len(self.dice)):
            for face in range(len(self.dice[die].faces)):
                if self.dice[die].faces[face].selected:
                    return die, face
        return None

    def kill(self):
        self.active = False
        self.health = self.maxhealth
        print("DEATH")

    def turn(self, enemy):
        player_result = self.roll()
        enemy_result = enemy.roll()

        self.attack(enemy)
        enemy.attack(self)

        if self.health <= 0:
            self.kill()
        else:
            self.heal(player_result["heal"])
                    
