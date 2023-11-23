from pico2d import *
import game_world
import game_framework
import random

import server


class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

        self.sx, self.sy = self.x - server.boy.x, self.y - server.boy.y

    def draw(self):
        self.sx = self.x - server.boy.x
        self.sy = self.y - server.boy.y

        self.image.draw(self.sx, self.sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        # Ball 위치 업데이트
        # self.x = clamp(50, self.x, server.background.w - 50)
        # self.y = clamp(50, self.y, server.background.h - 50)

        pass

    def get_bb(self):
        return self.sx - 10, self.sy - 10, self.sx + 10, self.sy + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)

