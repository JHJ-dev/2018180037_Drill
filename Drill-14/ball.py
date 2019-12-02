import random
from pico2d import *
import main_state


class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 1837
        self.h = 1109
        self.x, self.y = random.randint(0, 1837), random.randint(0, 1109)

    def set_center_object(self, back):
        self.center_object = back

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        draw_x = clamp(800//2, main_state.boy.x, 1837 - 800//2)
        draw_y = clamp(600//2, main_state.boy.y, 1109 - 600//2)
        self.image.draw(self.x - draw_x + 800//2, self.y - draw_y + 600//2)

    def update(self):
        self.window_left = clamp(-self.w - self.canvas_width,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)
        self.window_bottom = clamp(0,
                                   int(self.center_object.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height)
        pass