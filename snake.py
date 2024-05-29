"""
SNAKE IN PYTHON
made by wheatbred#0000
runs in terminal at ~30fps
"""

def printf(str): # render part of level
    print(str, end=' ')

# IMPORTS
import random as r;
import time as t;
import os as o;

# GAME SETUP
grid = 0;
gs = (0,0);
FPS = 30;

def gen_grid(x,y):
    global grid, gs;
    grid = [];
    gs = (x,y);
    for i in range(y):
        a = [];
        for j in range(x):
            a.append(0);
        grid.append(a);

snakepos = (0,0);
snakedir = 0 # 1 = left, 2 = right, 3 = up, 4 = down
snaketrail = [];
snakesize = 1;

def spawnSnake():
    global snakepos, snakedir;
    snakepos = (int(gs[0]/2),int(gs[1]/2));
    snakedir = 0;

def render(clear=1):
    global grid;
    if clear == 1:
        o.system('cls')
    for i in range(gs[1]): # y coordinate
        for j in range(gs[0]): # x coordinate
            SnakeHead = 0; SnakeTrail = 0
            if snakepos[0] == j and snakepos[1] == i: # render snake head
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

gen_grid(10,10)
spawnSnake()
while True:
    render()
    t.sleep(1/FPS)