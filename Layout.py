
class Layout:

    def __init__(self, draw_funcs):
        self.draw_funcs = draw_funcs

    def draw(self, screen, rollers):
        if len(rollers) > len(self.draw_funcs):
            pass
        for index, roller in enumerate(rollers):
            self.draw_funcs[index](screen, roller)
            

def left_under(screen, roller):
    screen.blit(roller.image, (100, 600-roller.image.get_height()-90))
    for slot, die in enumerate(roller.dice):
        die.draw(screen, 50+slot*70, 530)

def right_under(screen, roller):
    screen.blit(roller.image, (700-roller.image.get_width(), 600-roller.image.get_height()-90))
    for slot, die in enumerate(roller.dice):
        die.draw(screen, 750-50-slot*70, 530)

basic = Layout([left_under, right_under])
