import Roller

class Enemy(Roller.Roller):

    def __init__(self, name, health, dice, drops):
        super().__init__(name, health, dice)
        self.drops = drops
