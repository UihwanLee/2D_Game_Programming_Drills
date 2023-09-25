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
dir = 0
pos_x = 100

def Init_Anim():
    global anim_frame_list

    # anim_IDLE
    anim_frame_IDLE = anim_frame()
    anim_frame_IDLE.left = [82, 105, 120, 150, 120, 105]
    anim_frame_IDLE.bottom = [420, 420, 420, 420, 420, 420]
    anim_frame_IDLE.width = [20, 20, 30, 30, 30, 20]
    anim_frame_IDLE.height = [60, 60, 60, 60, 60, 60]
    anim_frame_list.append(anim_frame_IDLE)

    # anim_walking
    anim_frame_walking = anim_frame()
    anim_frame_walking.left = [205, 227, 250, 281, 310, 335, 357, 386, 415, 445]
    anim_frame_walking.bottom = [420, 420, 420, 420, 420, 420, 420, 420, 420, 420]
    anim_frame_walking.width = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
    anim_frame_walking.height = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60]
    anim_frame_list.append(anim_frame_walking)

    # anim_running
    anim_frame_running = anim_frame()
    anim_frame_running.left =[135, 166, 200, 235, 269, 293, 321, 350, 387, 419, 444, 473, 505]
    anim_frame_running.bottom = [355, 355, 355, 355, 355, 355, 355, 355, 355, 355, 355, 355, 355]
    anim_frame_running.width = [30, 30, 35, 35, 30, 30, 35, 35, 35, 35, 35, 35, 35]
    anim_frame_running.height = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60]
    anim_frame_list.append(anim_frame_running)

def handle_events():
    global running, dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_RIGHT:
                dir += 1

def render_frame(frame, left, bottom, width, height, x, y, xScale, yScale, time):
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    Sprite_Sheet.clip_draw(left[frame], bottom[frame], width[frame], height[frame], x, y, xScale, yScale)
    update_canvas()
    delay(time)


def anim_IDLE():
    global anim_frame_list, pos_x

    anim = anim_frame_list[0]
    frame = 0

    for frame in range(0, len(anim.left), 1):
        render_frame(frame, anim.left, anim.bottom, anim.width, anim.height, pos_x, 500, 100, 100, 0.5)



frame_walking = 0
def anim_walking():
    global anim_frame_list, frame_walking, pos_x, dir

    anim = anim_frame_list[1]
    frame = 0

    render_frame(frame_walking, anim.left, anim.bottom, anim.width, anim.height, pos_x, 500, 100, 100, 0.2)
    frame_walking = (frame_walking + 1) % len(anim.left)
    pos_x += dir * 20

def anim_running():
    global anim_frame_list

    anim = anim_frame_list[2]
    frame = 0

    for frame in range(0, len(anim.left), 1):
        render_frame(frame, anim.left, anim.bottom, anim.width, anim.height, 90, 500, 100, 100, 0.2)

Init_Anim()
while running:
    #anim_IDLE()
    anim_walking()
    #anim_running()
    handle_events()

close_canvas()