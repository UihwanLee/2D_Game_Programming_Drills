from pico2d import *
import math

open_canvas()

# fill here

grass = load_image('grass.png')
character = load_image('character.png')

pos = [0, 90]
temp = [0, 0]
option = 0
is_rect = True
x = 0
while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(pos[0], pos[1])

    # 사각운동
    if(option == 0):
        if((pos[0] == 0 or pos[0] == 400) and pos[1] == 90):
            temp[0] = 2
            temp[1] = 0
            
        if(pos[0] == 800 and pos[1] == 90):
            temp[0] = 0
            temp[1] = 2

        if(pos[0] == 800 and pos[1] == 600):
            temp[0] = -2
            temp[1] = 0

        if(pos[0] == 0 and pos[1] == 600):
            temp[0] = 0
            temp[1] = -2

            
    else :
        is_rect[0] = 0
        temp[0] = 800 * math.sin(x/360 * 2 * math.pi)
        temp[1] = 600 * math.cos(x/360 * 2 * math.pi)
        x = x + 2
        print("Hello")
        
    pos[0] = pos[0] + temp[0]
    pos[1] = pos[1] + temp[1]

    if(pos[0] == 0 and pos[1] == 600):
        is_rect = False

    if(pos[0] == 400 and pos[1] == 300 and is_rect==False):
            option = 1
            temp[0] = 0
            temp[1] = 0

    delay(0.01)

close_canvas()
