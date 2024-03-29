from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from brick import Brick

name = "MainState"

boy = None
grass = None
brick = None
balls = []
big_balls = []


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(20)]
    game_world.add_objects(balls, 1)

    global brick
    brick = Brick()
    game_world.add_object(brick, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

#소년 & 공 충돌
    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)

#잔디 & 공 충돌
    for ball in balls:
        if collide(grass, ball):
            ball.stop()

#발판 & 공 충돌
    for ball in balls:
        if collide(brick, ball) and ball.y > brick.y + 20:
            ball.stop()
            ball.x += brick.dir * 200 * game_framework.frame_time

#소년 & 잔디 충돌
    if collide(grass, boy):
        boy.stop()

#소년 & 발판 충돌
    if collide(brick, boy) and boy.y > brick.y + 20:
        boy.isjump = False
        boy.x += brick.dir * 200 * game_framework.frame_time
        if(boy.x < brick.x - 100 or brick.x + 100 < boy.x):
            boy.isjump = True

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






