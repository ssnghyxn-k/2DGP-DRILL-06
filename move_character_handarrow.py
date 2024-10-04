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
running = True
frame = 0
speed = 0.1

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

while running:
    clear_canvas()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(hand_x, hand_y)

    boy_x = (1 - speed) * boy_x + speed * hand_x
    boy_y = (1 - speed) * boy_y + speed * hand_y

    if boy_x < hand_x:
        face_right = False
    else:
        face_right = True

    if face_right:
        character.clip_draw(frame * 100, 0, 100, 100, boy_x, boy_y)
    else:
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', boy_x, boy_y, 100, 100)

    if abs(boy_x - hand_x) < 10 and abs(boy_y - hand_y) < 10:
        hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
    
    frame = (frame + 1) % 8

    update_canvas()
    handle_events()
    delay(0.05)

close_canvas()