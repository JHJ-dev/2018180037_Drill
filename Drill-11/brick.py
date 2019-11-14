from pico2d import *
import game_framework

class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y = 0, 200
        self.dir = 1
        self.velocity = 200

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def update(self):
        self.x += self.velocity * game_framework.frame_time
        if self.x >= 1600:
            self.velocity = -200
            self.dir = -1
        elif self.x <= 0:
            self.velocity = 200
            self.dir = 1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

