from pico2d import *
import random

WIDTH, HEIGHT = 1280, 1024

global x, y, running

def draw_curve_10_points(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    
    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p10[0] + (3*t**3 - 5*t**2 + 2)*p1[0] + (-3*t**3 + 4*t**2 + t)*p2[0] + (t**3 - t**2)*p3[0])/2
        y = ((-t**3 + 2*t**2 - t)*p10[1] + (3*t**3 - 5*t**2 + 2)*p1[1] + (-3*t**3 + 4*t**2 + t)*p2[1] + (t**3 - t**2)*p3[1])/2

    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        
    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p2[0] + (3*t**3 - 5*t**2 + 2)*p3[0] + (-3*t**3 + 4*t**2 + t)*p4[0] + (t**3 - t**2)*p5[0])/2
        y = ((-t**3 + 2*t**2 - t)*p2[1] + (3*t**3 - 5*t**2 + 2)*p3[1] + (-3*t**3 + 4*t**2 + t)*p4[1] + (t**3 - t**2)*p5[1])/2
        
    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p3[0] + (3*t**3 - 5*t**2 + 2)*p4[0] + (-3*t**3 + 4*t**2 + t)*p5[0] + (t**3 - t**2)*p6[0])/2
        y = ((-t**3 + 2*t**2 - t)*p3[1] + (3*t**3 - 5*t**2 + 2)*p4[1] + (-3*t**3 + 4*t**2 + t)*p5[1] + (t**3 - t**2)*p6[1])/2
        
    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p4[0] + (3*t**3 - 5*t**2 + 2)*p5[0] + (-3*t**3 + 4*t**2 + t)*p6[0] + (t**3 - t**2)*p7[0])/2
        y = ((-t**3 + 2*t**2 - t)*p4[1] + (3*t**3 - 5*t**2 + 2)*p5[1] + (-3*t**3 + 4*t**2 + t)*p6[1] + (t**3 - t**2)*p7[1])/2

    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p5[0] + (3*t**3 - 5*t**2 + 2)*p6[0] + (-3*t**3 + 4*t**2 + t)*p7[0] + (t**3 - t**2)*p8[0])/2
        y = ((-t**3 + 2*t**2 - t)*p5[1] + (3*t**3 - 5*t**2 + 2)*p6[1] + (-3*t**3 + 4*t**2 + t)*p7[1] + (t**3 - t**2)*p8[1])/2

    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p6[0] + (3*t**3 - 5*t**2 + 2)*p7[0] + (-3*t**3 + 4*t**2 + t)*p8[0] + (t**3 - t**2)*p9[0])/2
        y = ((-t**3 + 2*t**2 - t)*p6[1] + (3*t**3 - 5*t**2 + 2)*p7[1] + (-3*t**3 + 4*t**2 + t)*p8[1] + (t**3 - t**2)*p9[1])/2

    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p7[0] + (3*t**3 - 5*t**2 + 2)*p8[0] + (-3*t**3 + 4*t**2 + t)*p9[0] + (t**3 - t**2)*p10[0])/2
        y = ((-t**3 + 2*t**2 - t)*p7[1] + (3*t**3 - 5*t**2 + 2)*p8[1] + (-3*t**3 + 4*t**2 + t)*p9[1] + (t**3 - t**2)*p10[1])/2

    for i in range(0, 100, 4):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p8[0] + (3*t**3 - 5*t**2 + 2)*p9[0] + (-3*t**3 + 4*t**2 + t)*p10[0] + (t**3 - t**2)*p1[0])/2
        y = ((-t**3 + 2*t**2 - t)*p8[1] + (3*t**3 - 5*t**2 + 2)*p9[1] + (-3*t**3 + 4*t**2 + t)*p10[1] + (t**3 - t**2)*p1[1])/2
        
open_canvas(WIDTH, HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
frame = 0

while running:
    clear_canvas()
    kpu_ground.draw(WIDTH // 2, HEIGHT // 2)
    draw_curve_10_points((random.randint(0,WIDTH),random.randint(0,HEIGHT)),(random.randint(0,WIDTH),random.randint(0,HEIGHT)),(random.randint(0,WIDTH),random.randint(0,HEIGHT)),(random.randint(0,WIDTH),random.randint(0,HEIGHT)),(random.randint(0,WIDTH),random.randint(0,HEIGHT)),
                      (random.randint(0,WIDTH),random.randint(0,HEIGHT)),(random.randint(0,WIDTH),random.randint(0,HEIGHT)),(random.randint(0,WIDTH),random.randint(0,HEIGHT)),(random.randint(0,WIDTH),random.randint(0,HEIGHT)),(random.randint(0,WIDTH),random.randint(0,HEIGHT)))

    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
close_canvas()
