from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sprite.png')

def handle_events():
    global running, dir,diry,y,direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                direction = 'right'
                dir+=2
            elif event.key == SDLK_LEFT:
                direction = 'left'
                dir-=2
            elif event.key == SDLK_UP:
                direction = 'up'
                diry+=2
            elif event.key == SDLK_DOWN:
                direction = 'down'
                diry-=2
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                right=True
                dir-=2
            elif event.key == SDLK_LEFT:
                left = True
                dir +=2
            if event.key == SDLK_UP:
                up=True
                diry-=2
            elif event.key == SDLK_DOWN:
                down = True
                diry +=2

running = True
direction = 'right'

x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2

frame = 0
dir=0
diry=0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    if direction == 'right':
        character.clip_draw(frame*60,64,60,60,x,y,200,200)
    elif direction == 'left':
        character.clip_draw(frame * 60, 128, 60, 60, x, y, 200, 200)
    elif direction == 'up':
        character.clip_draw(frame * 60, 0, 60, 60, x, y, 200, 200)
    elif direction == 'down':
        character.clip_draw(frame * 60, 192, 60, 60, x, y, 200, 200)
    update_canvas()
    handle_events()
    frame = (frame+1)%4

    x += dir *5
    y += diry*5

    if x < 0:
        x = 0
    elif x > TUK_WIDTH:
        x = TUK_WIDTH

    if y < 0:
        y = 0
    elif y > TUK_HEIGHT:
        y = TUK_HEIGHT
    delay(0.1)


close_canvas()

