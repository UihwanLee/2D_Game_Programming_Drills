from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

# 글로벌 변수
running = True
is_arrival = False
mouse_points = [TUK_WIDTH // 2, TUK_HEIGHT // 2]
player_pos = [TUK_WIDTH // 2, TUK_HEIGHT // 2]
cur_pos = [TUK_WIDTH // 2, TUK_HEIGHT // 2]
frame, i = 0, 0
hide_cursor()

mouse_trace = [] # 마우스 흔적 리스트

def generate_mouse_trace(x, y):
    mouse_trace.append((x, y))

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_points[0], mouse_points[1] = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT: # 마우스 왼쪽 버튼 클릭
            generate_mouse_trace(event.x, TUK_HEIGHT - 1 - event.y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


# 플레이어 위치 업데이트
def update_character_pos():
    global i, mouse_trace

    if not mouse_trace:
        return

    # i가 100이면 다 도달 했다는 뜻으로 다시 리셋
    if i >= 100:
        update_mouse_trace()
        return

    arrival_point = mouse_trace[0]

    x1, y1 = player_pos[0], player_pos[1]
    x2, y2 = arrival_point[0], arrival_point[1]

    i = i + 0.1
    t = i / 100
    cur_pos[0] = (1 - t) * x1 + t * x2
    cur_pos[1] = (1 - t) * y1 + t * y2

def update_mouse_trace():
    global i, is_arrival, player_pos, mouse_trace

    if not mouse_trace:
        return

    i = 0
    is_arrival = False
    player_pos = mouse_trace[0] # 현재 위치 갱신

    del mouse_trace[0] # 가장 마지막 마우스 삭제


# 여태까지 찍은 마우스 그리기
def draw_mouse_trace():
    global mouse_trace

    for trace in mouse_trace:
        mouse.draw(trace[0], trace[1])

# 마우스와 캐릭터 위치관계에 따른 이동 방향 설정
def set_character_dir():
    arrival_points = []
    if mouse_trace :
        arrival_points = mouse_trace[0]
    else :
        arrival_points = [TUK_WIDTH // 2, TUK_HEIGHT // 2]

    if player_pos[0] <= arrival_points[0]:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, cur_pos[0], cur_pos[1], 100, 100)
    else:
        character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', cur_pos[0], cur_pos[1], 100, 100)
def render_frame():
    global frame
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    mouse.draw(mouse_points[0], mouse_points[1])
    draw_mouse_trace()
    update_character_pos()
    set_character_dir()
    update_canvas()
    frame = (frame + 1) % 8

while running:
    clear_canvas()
    render_frame()
    handle_events()

close_canvas()