# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import game_world
import game_framework
import random


# state event check
# ( state event type, event value )

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def space_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


def time_out(e):
    return e[0] == 'TIME_OUT'


# time_out = lambda e : e[0] == 'TIME_OUT'

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 40.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Bird Idle Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

# Bird Fly Action Speed
TIME_PER_ACTION_FLY = 0.5
ACTION_PER_TIME_FLY = 1.0 / TIME_PER_ACTION_FLY
FRAMES_PER_ACTION_FLY = 4

# Bird Size
BIRD_SIZE = 80


class Idle:

    @staticmethod
    def enter(bird, e):
        bird.action = 0
        bird.dir = 0
        bird.frame = 0
        bird.wait_time = get_time()  # pico2d import 필요
        pass

    @staticmethod
    def exit(bird, e):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if get_time() - bird.wait_time > 2:
            bird.state_machine.handle_event(('TIME_OUT', 0))

    @staticmethod
    def draw(bird):
        bird.image.clip_draw(int(bird.frame) * 183, bird.action * 101, 170, 150, bird.x, bird.y, BIRD_SIZE, BIRD_SIZE)


class Fly:

    @staticmethod
    def enter(bird, e):
        bird.dir, bird.action, bird.face_dir = -1, 0, -1
        temp = random.randint(1, 2)
        if temp == 1:
            bird.dir = 1.0
        else:
            bird.dir = -1.0
        bird.wait_time = get_time()

    @staticmethod
    def exit(bird, e):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION_FLY * ACTION_PER_TIME_FLY * game_framework.frame_time) % 4
        bird.x += bird.dir * RUN_SPEED_PPS * game_framework.frame_time
        if get_time() - bird.wait_time > bird.fly_time:
            bird.dir *= -1.0
            bird.wait_time = get_time()

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 183, 150, 170, 150, bird.x, bird.y, BIRD_SIZE, BIRD_SIZE)
        else:
            bird.image.clip_composite_draw(int(bird.frame) * 183, bird.action * 101, 170, 150, 0, 'h', bird.x, bird.y, BIRD_SIZE, BIRD_SIZE)

class StateMachine:
    def __init__(self, bird):
        self.bird = bird
        self.cur_state = Idle
        self.transitions = {
            Idle: {time_out : Fly},
            Fly : {}
        }

    def start(self):
        self.cur_state.enter(self.bird, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.bird)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.bird, e)
                self.cur_state = next_state
                self.cur_state.enter(self.bird, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.bird)


class Bird:
    def __init__(self, pos_x, fly_time):
        self.x, self.y = pos_x, 90
        self.frame = 0
        self.action = 3
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.fly_time = fly_time

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))

    def draw(self):
        self.state_machine.draw()
