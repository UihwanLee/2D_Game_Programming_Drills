import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

# 글로벌 변수
mouse_points = []

# 마우스 무작위 위치 생성
def generate_random_mouse():
    global mouse_points
    mouse_points = [random.randint(10, TUK_WIDTH-10), random.randint(10, TUK_HEIGHT-10)]

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    generate_random_mouse()
    mouse.draw(mouse_points[0], mouse_points[1])
    update_canvas()
    delay(1)
    #frame = (frame + 1) % 8

close_canvas()