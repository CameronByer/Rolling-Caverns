
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DIE_PADDING = 20
DIE_SIZE = 50
XINDENT = 100
YINDENT = 90

class Layout:

    def __init__(self, draw_funcs):
        self.draw_funcs = draw_funcs

    def draw(self, screen, rollers):
        if len(rollers) > len(self.draw_funcs):
            pass
        for index, roller in enumerate(rollers):
            self.draw_funcs[index](screen, roller)
            

def left_under(screen, roller):
    screen.blit(roller.image, (XINDENT, SCREEN_HEIGHT-roller.image.get_height()-YINDENT))
    for slot, die in enumerate(roller.dice):
        die.draw(screen, DIE_PADDING+slot*(DIE_SIZE+DIE_PADDING), SCREEN_HEIGHT-DIE_SIZE-DIE_PADDING)

def right_under(screen, roller):
    screen.blit(roller.image, (SCREEN_WIDTH-XINDENT-roller.image.get_width(), SCREEN_HEIGHT-roller.image.get_height()-YINDENT))
    for slot, die in enumerate(roller.dice):
        die.draw(screen, SCREEN_WIDTH-DIE_SIZE-DIE_PADDING-slot*(DIE_SIZE+DIE_PADDING), SCREEN_HEIGHT-DIE_SIZE-DIE_PADDING)

basic = Layout([left_under, right_under])
