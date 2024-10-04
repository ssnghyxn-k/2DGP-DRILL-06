from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

boy_x = TUK_WIDTH // 2
boy_y = TUK_HEIGHT // 2
hand_x = random.randint(0, TUK_WIDTH)
hand_y = random.randint(0, TUK_HEIGHT)
face_right = True

while True:
    clear_canvas()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(hand_x, hand_y)

    if boy_x < hand_x:
        boy_x += 5
        face_right = True    
    elif boy_x > hand_x:
        boy_x -= 5
        face_right = False

    if boy_y < hand_y:
        boy_y += 5
    elif boy_y > hand_y:
        boy_y -= 5

    if face_right:
        character.clip_draw(0,0,100,100,boy_x, boy_y)
    else:
        character.clip_composite_draw(0, 0, 100, 100, 0, 'h', boy_x, boy_y, 100, 100)

    if abs(boy_x - hand_x) < 10 and abs(boy_y - hand_y) < 10:
        hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

    update_canvas()
    delay(0.01)

close_canvas()