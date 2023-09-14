import turtle

# 글로벌 변수
g_turtle_trace = []                 # 거북이 행적 데이터를 담는 리스트 (x좌표, y좌표, 머리방향)
g_cur_pos = [0, 0]                  # 거북이 현재 위치를 저장하는 리스트
g_move_dist = 50                    # 거북이 이동 거리
g_game_option = ['G']               # 게임 옵션('G' : 거북이 행적을 그림, 'H' : 거북이 행적을 지움)


# 스크린 관련 변수
screen = turtle.Screen()
WIDTH, HEIGHT = 800, 600


# 초기화 함수 : 게임 시작 시 한번만 호출되는 초기화 함수
def __Init__():
    # 프로그램 창 제목 짓기
    turtle.title("Control Turtle Program")
    
    # 거북이 형태로 형태 변환
    turtle.shape('turtle')

    # 스크린 사이즈 초기화 및 tracer 기초
    screen.setup(width = WIDTH, height = HEIGHT)
    screen.tracer(0)

# 도움말 출력 함수 : 게임 옵션 도움말을 나타내는 함수
def ShowMessage():
    turtle.penup()
    turtle.goto(-WIDTH/2+10, HEIGHT/2-40)
    turtle.pendown()
    turtle.write('현재 option : (' + g_game_option[0] + ')', align="left", font=("휴먼옛체", 20))
    turtle.penup()
    turtle.goto(-WIDTH/2+10, HEIGHT/2-70)
    turtle.pendown()
    turtle.write('option : 표적 남기기 모드 (''G'')', align="left", font=("휴먼옛체", 20))
    turtle.penup()
    turtle.goto(-WIDTH/2+10, HEIGHT/2 - 100)
    turtle.pendown()
    turtle.write('option : 표적 지우기 모드 (''H'')', align="left", font=("휴먼옛체", 20))
    turtle.penup()


# 옵션 변환 함수 : 변경된 옵션에 맞춰 행적 그리기/지우기 등 처리하여 한번에 스크린에 출력하는 함수
def Change_Option(_option):
    screen.tracer(0)
    g_game_option[0] = _option
    turtle.clear()
    ShowMessage()

    # 현재 옵션이 표적 남기기 모드라면 (0,0)부터 행적 그리기(한번에 출력해야함)
    if(_option == 'G'):
        turtle.penup()
        turtle.goto(0, 0)
        for x, y, h in g_turtle_trace:
            turtle.pendown()
            turtle.setheading(h)
            turtle.goto(x, y)
            turtle.stamp()

    elif(_option == 'H'):
        turtle.penup()
        turtle.goto(g_cur_pos[0], g_cur_pos[1])
        turtle.pendown()
        turtle.stamp()

    turtle.penup()
    screen.update()
    screen.tracer(1)

def Change_Option_G():
    g_game_option[0] = 'G'
    Change_Option('G')
        
def Change_Option_H():
    g_game_option[0] = 'H'
    Change_Option('H')
    

# 키보드 입력 받은 key에 따라 움직이는 함수 : 옵션에 따라 여러가지 제약을 둘 수 있게 한다

def TryMove(idx, dist):
    # 예외처리 체크 : 여러가지 충돌처리를 통해 움직일 수 있는지 판단
    if(idx == 0 and (g_cur_pos[idx] + dist) ** 2 >= 160000) : return
    if(idx == 1 and (g_cur_pos[idx] + dist) ** 2 >= 90000) : return
    g_cur_pos[idx] += dist
    Move()
    

def Move():
    if(g_game_option[0] == 'H') : turtle.clearstamps()
    if(g_game_option[0] == 'H') : turtle.penup()
    g_turtle_trace.append((g_cur_pos[0], g_cur_pos[1], turtle.heading()))
    if(g_game_option[0] == 'G') : turtle.pendown()
    turtle.goto(g_cur_pos[0], g_cur_pos[1])
    turtle.stamp()
    screen.update()
    
def Move_up():
    turtle.setheading(90)
    #g_cur_pos[1] += g_move_dist
    TryMove(1, g_move_dist)

def Move_down():
    turtle.setheading(270)
    #g_cur_pos[1] -= g_move_dist
    TryMove(1, -g_move_dist)
    
def Move_right():
    turtle.setheading(180)
    #g_cur_pos[0] -= g_move_dist
    TryMove(0, -g_move_dist)

def Move_left():
    turtle.setheading(0)
    #g_cur_pos[0] += g_move_dist
    TryMove(0, g_move_dist)

# 게임 리셋
def Restart():
    screen.tracer(0)
    turtle.reset()
    ShowMessage()
    turtle.goto(0,0)
    g_cur_pos[0] = 0
    g_cur_pos[1] = 0
    g_turtle_trace.clear()
    g_turtle_trace.append((g_cur_pos[0], g_cur_pos[1], turtle.heading()))
    turtle.pendown()
    turtle.stamp()
    turtle.penup()
    screen.update()

#init
__Init__()
Restart()

#input
turtle.onkey(Restart, 'Escape')

turtle.onkey(Change_Option_G, 'g')
turtle.onkey(Change_Option_H, 'h')
turtle.onkey(Change_Option_G, 'G')
turtle.onkey(Change_Option_H, 'H')

turtle.onkey(Move_up, 'W')
turtle.onkey(Move_down, 'S')
turtle.onkey(Move_right, 'A')
turtle.onkey(Move_left, 'D')

turtle.onkey(Move_up, 'w')
turtle.onkey(Move_down, 's')
turtle.onkey(Move_right, 'a')
turtle.onkey(Move_left, 'd')

turtle.listen()
turtle.exitonclick()


