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
    global anim_frame_list

    # anim_IDLE
    anim_frame_IDLE = anim_frame()
    anim_frame_IDLE.left = [82, 105, 120, 150, 120, 105, 82]
    anim_frame_IDLE.bottom = [420, 420, 420, 420, 420, 420, 420]
    anim_frame_IDLE.width = [20, 20, 30, 30, 30, 20, 20]
    anim_frame_IDLE.height = [60, 60, 60, 60, 60, 60, 60]
    anim_frame_list.append(anim_frame_IDLE)

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def render_frame(frame, left, bottom, width, height, x, y, xScale, yScale, time):
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    Sprite_Sheet.clip_draw(left[frame], bottom[frame], width[frame], height[frame], x, y, xScale, yScale)
    update_canvas()
    delay(time)


def anim_IDLE():
    global anim_frame_list

    anim = anim_frame_list[0]
    frame = 0

    for frame in range(0, len(anim.left), 1):
        render_frame(frame, anim.left, anim.bottom, anim.width, anim.height, 90, 500, 100, 100, 0.5)


def anim_walking():
    pass

def anim_running():
    pass

Init_Anim()
while running:
    anim_IDLE()
    anim_walking()
    anim_running()
    handle_events()

close_canvas()