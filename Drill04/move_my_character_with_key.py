from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_GROUND = load_image('TUK_GROUND.png')
Sprite_Sheet = load_image('sprite_sheet.png')


'''
    <조작키>
    방향키 -> 걷기
    방향키 + 왼쪽 SHIFT -> 뛰기
'''


# 애니메이션 프레임 구조체
class anim_frame():
    left = []
    bottom = []
    width = []
    height = []

# 글로벌 변수
running = True
anim_frame_list = []
dir_x = 0
dir_y = 0
pos_x = 100
pos_y = 500
frame_walking = 0
frame_running = 0
is_forward = True
is_walking = False
is_running = False

# 프레임 리스트 초기화
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

# input 처리 함수
def handle_events():
    global running, dir_x, dir_y, is_forward, is_running, is_walking

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT or event.key == SDLK_LEFT or event.key == SDLK_UP or event.key == SDLK_DOWN:
                is_walking = True
                if event.key == SDLK_RIGHT :
                    is_forward = True
                    dir_x += 1
                elif event.key == SDLK_LEFT:
                    is_forward = False
                    dir_x -= 1
                elif event.key == SDLK_UP:
                    dir_y += 1
                elif event.key == SDLK_DOWN:
                    dir_y -= 1

            if is_walking:
                if event.key == SDLK_LSHIFT:
                    is_running = True

        elif event.type == SDL_KEYUP:
            is_walking = False
            is_running = False
            if event.key == SDLK_RIGHT:
                dir_x = 0
            elif event.key == SDLK_RIGHT:
                dir_x = 0
            elif event.key == SDLK_UP:
                dir_y = 0
            elif event.key == SDLK_DOWN:
                dir_y = 0

        if is_running:
            if event.type == SDL_KEYUP and event.key == SDLK_LSHIFT:
                is_running = False

# 충돌체크
def check_collision(pos, dist, MAX_DIST):

    if pos + dist <= 0 or pos + dist >= MAX_DIST:
        return True

    return False

# 애니메이션 프레임 구동
def render_frame(frame, left, bottom, width, height, x, y, xScale, yScale, time, dir):
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    # dir에 따른 방향 조정
    if dir :
        Sprite_Sheet.clip_draw(left[frame], bottom[frame], width[frame], height[frame], x, y, xScale, yScale)
    else :
        Sprite_Sheet.clip_composite_draw(left[frame], bottom[frame], width[frame], height[frame], 0, 'h', x, y, xScale, yScale)
    update_canvas()
    handle_events()
    delay(time)


def anim_IDLE():
    global anim_frame_list, pos_x, pos_y, is_walking, is_running, is_forward

    # 걷거나 뛰는 중이면 반환
    if is_walking or is_running : return

    anim = anim_frame_list[0]
    frame = 0

    for frame in range(0, len(anim.left), 1):
        render_frame(frame, anim.left, anim.bottom, anim.width, anim.height, pos_x, pos_y, 100, 100, 0.2, is_forward)


def anim_walking():
    global anim_frame_list, frame_walking, pos_x, pos_y, dir_x, dir_y, is_walking, is_forward

    if not is_walking : return
    if is_running : return

    if check_collision(pos_x, dir_x * 20, TUK_WIDTH) or check_collision(pos_y, dir_y * 20, TUK_HEIGHT):
        return

    anim = anim_frame_list[1]

    render_frame(frame_walking, anim.left, anim.bottom, anim.width, anim.height, pos_x, pos_y, 100, 100, 0.2, is_forward)
    frame_walking = (frame_walking + 1) % len(anim.left)
    pos_x += dir_x * 20
    pos_y += dir_y * 20

def anim_running():
    global anim_frame_list, frame_running, dir_x, dir_y, pos_x, pos_y, is_running, is_forward

    if not is_running : return

    if check_collision(pos_x, dir_x * 40, TUK_WIDTH) or check_collision(pos_y, dir_y * 40, TUK_HEIGHT):
        return

    anim = anim_frame_list[2]

    render_frame(frame_running, anim.left, anim.bottom, anim.width, anim.height, pos_x, pos_y, 100, 100, 0.2, is_forward)
    frame_running = (frame_running + 1) % len(anim.left)
    pos_x += dir_x * 40
    pos_y += dir_y * 40

Init_Anim()
while running:
    anim_IDLE()
    anim_walking()
    anim_running()
    handle_events()

close_canvas()