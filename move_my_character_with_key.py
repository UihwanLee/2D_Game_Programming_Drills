from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_GROUND = load_image('TUK_GROUND.png')
Sprite_Sheet = load_image('sprite_sheet.png')

running = True

while running:
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    update_canvas()

close_canvas()