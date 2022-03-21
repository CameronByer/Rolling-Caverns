
class Roller:

    def __init__(self, name, health, dice, size, img_dir=""):
        self.health = health
        self.dice = dice

    def __str__(self):
        return self.name + ": " + self.health

    def roll(self):
        result = {"attack": 0, "block": 0, "energy": 0}
        for die in dice:
            if die.cost <= result["energy"]:
                result["energy"] -= die.cost
                outcome = die.roll()
                for item in outcome:
                    result[item] += outcome[item]
        return result
