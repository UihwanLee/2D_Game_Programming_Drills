from pico2d import *

open_canvas()

sprite_sheet = load_image('sprite_sheet.png')

frame_left =   [205, 227, 250, 281, 310, 335, 357, 386, 415, 445]
frame_bottom = [420, 420, 420, 420, 420, 420, 420, 420, 420, 420]
frame_width = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
frame_height = [60, 60, 60, 60, 60, 60, 60, 60, 60, 60]

frame = 0

while True:
    print(frame, " : ", frame_left[frame], ", ", frame_width[frame])
    sprite_sheet.clip_draw(frame_left[frame], frame_bottom[frame], frame_width[frame], frame_height[frame], 100, 90)
    update_canvas()
    delay(2)
    break



close_canvas()
