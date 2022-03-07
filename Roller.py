
class Roller:

    def __init__(self, dice):
        self.dice = dice

    def roll(self):
        result = {"attack": 0, "block": 0, "energy": 0}
        for die in dice:
            if die.cost <= result["energy"]:
                result["energy"] -= die.cost
                outcome = die.roll()
                for item in outcome:
                    result[item] += outcome[item]
