import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

# 글로벌 변수
is_moving = False
mouse_points = []
cur_pos = [TUK_WIDTH//2, TUK_HEIGHT//2] # 플레이어 처음 위치 중앙으로 초기화
running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame, i = 0, 0

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


# 마우스 무작위 위치 생성
def generate_random_mouse():
    global mouse_points, is_moving

    if is_moving:
        return # 움직이는 동안은 마우스 위치를 갱신하지 않는다

    mouse_points = [random.randint(10, TUK_WIDTH-10), random.randint(10, TUK_HEIGHT-10)]
    is_moving = True

# 리셋
def reset():
    global i, is_moving, cur_pos, mouse_points
    i = 0
    is_moving = False

    # 현재 위치 갱신
    cur_pos = mouse_points

# 선 그리기
def update_character_pos(p1, p2):
    global cur_pos, mouse_points, x, y, i, is_moving

    # 마우스가 새로 갱신되는 동안 움직임
    if not is_moving:
        return

    # i가 100이면 다 도달 했다는 뜻으로 다시 리셋
    if i >= 100:
        reset()
        return

    x1, y1 = cur_pos[0], cur_pos[1]
    x2, y2 = mouse_points[0], mouse_points[1]

    i = i + 0.1
    t = i / 100
    x = (1 - t) * x1 + t * x2
    y = (1 - t) * y1 + t * y2

def render_frame():
    global frame
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    generate_random_mouse()
    mouse.draw(mouse_points[0], mouse_points[1])
    update_character_pos(mouse_points[0], mouse_points[1])
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

while running:
    clear_canvas()
    render_frame()
    handle_events()

close_canvas()