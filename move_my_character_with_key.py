from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_GROUND = load_image('TUK_GROUND.png')
Sprite_Sheet = load_image('sprite_sheet.png')


class anim_frame():
    left = []
    bottom = []
    width = []
    height = []

running = True
anim_frame_list = []

def Init_Anim():
    pass

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def anim_IDLE():
    pass

def anim_walking():
    pass

def anim_running():
    pass

Init_Anim()
while running:
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    anim_IDLE()
    anim_walking()
    anim_running()
    update_canvas()
    handle_events()

close_canvas()