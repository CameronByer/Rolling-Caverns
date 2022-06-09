
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DIE_PADDING = 20
DIE_SIZE = 50
XINDENT = 100
YINDENT = 90
HEALTH_WIDTH = 50
HEALTH_HEIGHT = 100


class Layout:

    def __init__(self, draw_funcs):
        self.draw_funcs = draw_funcs

    def draw(self, screen, rollers):
        if len(rollers) > len(self.draw_funcs):
            pass
        for index, roller in enumerate(rollers):
            self.draw_funcs[index](screen, roller)
            

def left_under(screen, roller):
    roller.draw(screen, XINDENT, SCREEN_HEIGHT-roller.image.get_height()-YINDENT)
    roller.drawhealth(screen, DIE_PADDING, SCREEN_HEIGHT-HEALTH_HEIGHT-YINDENT, HEALTH_WIDTH, HEALTH_HEIGHT)
    for slot, die in enumerate(roller.dice):
        die.pos = (DIE_PADDING+slot*(DIE_SIZE+DIE_PADDING), SCREEN_HEIGHT-DIE_SIZE-DIE_PADDING)
        die.face_size = DIE_SIZE
        die.draw(screen)
        #die.draw(screen, DIE_PADDING+slot*(DIE_SIZE+DIE_PADDING), SCREEN_HEIGHT-DIE_SIZE-DIE_PADDING, DIE_SIZE)

def right_under(screen, roller):
    roller.draw(screen, SCREEN_WIDTH-XINDENT-roller.image.get_width(), SCREEN_HEIGHT-roller.image.get_height()-YINDENT)
    roller.drawhealth(screen, SCREEN_WIDTH-DIE_PADDING-HEALTH_WIDTH, SCREEN_HEIGHT-HEALTH_HEIGHT-YINDENT, HEALTH_WIDTH, HEALTH_HEIGHT)
    for slot, die in enumerate(roller.dice):
        die.pos = (SCREEN_WIDTH-DIE_SIZE-DIE_PADDING-slot*(DIE_SIZE+DIE_PADDING), SCREEN_HEIGHT-DIE_SIZE-DIE_PADDING)
        die.face_size = DIE_SIZE
        die.draw(screen)
        #die.draw(screen, SCREEN_WIDTH-DIE_SIZE-DIE_PADDING-slot*(DIE_SIZE+DIE_PADDING), SCREEN_HEIGHT-DIE_SIZE-DIE_PADDING, DIE_SIZE)
        

basic = Layout([left_under, right_under])
