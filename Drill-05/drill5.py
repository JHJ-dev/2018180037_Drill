#Drill 05 2018180037
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y     #시작 좌표
    global x1, y1   #끝 좌표
    global x2, y2   #캐릭터 좌표
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
            dir = 1
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x1, y1 = event.x-25, KPU_HEIGHT - 1 - event.y +25
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass
    
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x2, y2 = KPU_WIDTH // 2, KPU_HEIGHT // 2
dis = 3
x1 = x2
y1 = y2
frame = 0
hide_cursor()

while running:
    move_x = (x1-x2)/20
    move_y = (y1-y2)/20
    x2 += move_x
    y2 += move_y

    if x1 - x2 < 0:
        dis = 0
    elif x1 - x2 > 0:
        dis = 1
    elif x1 - x2 == 0:
        dis =3
        
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(x, y)
    character.clip_draw(frame * 100, 100 * dis, 100, 100, x2, y2)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()

close_canvas()
