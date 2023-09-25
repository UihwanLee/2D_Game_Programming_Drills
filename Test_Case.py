from pico2d import *

open_canvas()

sprite_sheet = load_image('sprite_sheet.png')

frame_left =   []
frame_bottom = []
frame_width = []
frame_height = []

frame = 0

while True:
    print(frame, " : ", frame_left[frame], ", ", frame_width[frame])
    sprite_sheet.clip_draw(frame_left[frame], frame_bottom[frame], frame_width[frame], frame_height[frame], 100, 90)
    update_canvas()
    delay(2)
    break



close_canvas()
