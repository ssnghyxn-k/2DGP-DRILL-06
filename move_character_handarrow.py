from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

boy_x = TUK_WIDTH // 2
boy_y = TUK_HEIGHT / 2
hand_x = random.randint(0, TUK_WIDTH)
hand_y = random.randint(0, TUK_HEIGHT)

