import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 300
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame_x = 0
        self.frame_y = 0
        self.frame = 0


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.frame_x = int(self.frame) % 5
        if int(self.frame) % 14 == 0:
            self.frame_y = 2
        if int(self.frame) % 14 == 5:
            self.frame_y = 1
        if int(self.frame) % 14 == 10:
            self.frame_y = 0

        self.x += self.velocity * game_framework.frame_time
        if self.x >= 1600:
            self.velocity = -RUN_SPEED_PPS
            self.dir = -1
        elif self.x <= 0:
            self.velocity = RUN_SPEED_PPS
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame_x) * 182, int(self.frame_y) * 168, 182, 168, self.x, self.y, 182, 168)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame_x) * 182, int(self.frame_y) * 168, 182, 168, 0.0, 'h', self.x,
                                           self.y, 182, 168)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
