# SNAKE IN PYTHON!!!

def printf(str): # render part of level
    print(str, end='')

# IMPORTS
import random as r;
import time as t;
import os as o;
import keyboard as k;

# GAME SETUP
grid = 0;
gs = [0,0];
FPS = 5;

def gen_grid(x,y):
    global grid, gs;
    grid = [];
    gs = (x,y);
    for i in range(y):
        a = [];
        for j in range(x):
            a.append(0);
        grid.append(a);

snakepos = {
    'x': 0,
    'y': 0
}
snakedir = 0 # 1 = left, 2 = right, 3 = up, 4 = down
snaketrail = [];
snakesize = 1;

def spawnSnake():
    global snakepos, snakedir;
    snakepos['x'] = int(gs[0]/2); snakepos['y'] = int(gs[1]/2)
    snakedir = 0;

def render(clear=1): # render the level
    global grid;
    if clear == 1:
        o.system('cls')
    for i in range(gs[1]): # y coordinate
        for j in range(gs[0]): # x coordinate
            SnakeHead = 0; SnakeTrail = 0
            if snakepos['x'] == j and snakepos['y'] == i: # render snake head
                printf('Q')
                SnakeHead = 1
            if SnakeHead == 0 and SnakeTrail == 0:
                for trail in snaketrail:
                    if trail[0] == j and trail[1] == i: # render snake tail
                        printf('O')
                        SnakeTrail = 1
            if not SnakeHead == 1 and not SnakeTrail == 1: # render food/stage
                if grid[i][j] == 1:
                    printf('8');
                else:
                    printf('.');
        print() # newline

def movement(): # move the player
    # 1 = left, 2 = right, 3 = up, 4 = down
    global snakepos, snakedir;
    if snakedir == 1:
        snakepos['x'] -= 1
    elif snakedir == 2:
        snakepos['x'] += 1
    elif snakedir == 3:
        snakepos['y'] -= 1
    elif snakedir == 4:
        snakepos['y'] += 1

def controller(): # control the player
    # 1 = left, 2 = right, 3 = up, 4 = down
    global snakedir;
    if k.is_pressed('w') or k.is_pressed('up'):
        snakedir = 3
    elif k.is_pressed('a') or k.is_pressed('left'):
        snakedir = 1
    elif k.is_pressed('s') or k.is_pressed('down'):
        snakedir = 4
    elif k.is_pressed('d') or k.is_pressed('right'):
        snakedir = 2

gen_grid(50,40)
spawnSnake()
while True:
    render()
    movement()
    controller()
    t.sleep(1/FPS)