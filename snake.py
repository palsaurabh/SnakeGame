import os
import random as rand
import pygame as pg
from pygame.locals import *
from pygame.compat import geterror

NO_DIR = 0
UP_DIR = 1
DOWN_DIR = 2
LEFT_DIR = 3
RIGHT_DIR = 4
WINDOWHEIGHT = 500
WINDOWWIDTH = 500
GRIDCOLUMNWIDTH = 25
numRows = int(WINDOWHEIGHT / GRIDCOLUMNWIDTH)
numColumns = int(WINDOWWIDTH / GRIDCOLUMNWIDTH)
gameWindow = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


class box:

    def __init__(self, xLoc, yLoc, direc = NO_DIR, colour = (255, 0, 0)):
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.direc = direc
        self.colour = colour

    def moveBox(self, direction):
        if direction == UP_DIR:
            if self.yLoc - 1 > 0:
                self.yLoc -= 1
        elif direction == DOWN_DIR:
            if self.yLoc + 1 <= numRows:
                self.yLoc += 1
        elif direction == LEFT_DIR:
            if self.xLoc - 1 > 0:
                self.xLoc -= 1
        elif direction == RIGHT_DIR:
            if self.xLoc + 1 <= numColumns:
                self.xLoc += 1

    def updateLoc(self, xLoc, yLoc):
        self.xLoc = xLoc
        self.yLoc = yLoc

    def updateDir(self, dirIn):
        self.direc = dirIn

    def drawBox(self, surface):
        pg.draw.rect(surface, self.colour, ((self.xLoc - 1) * GRIDCOLUMNWIDTH, (self.yLoc - 1) * GRIDCOLUMNWIDTH,
                                            GRIDCOLUMNWIDTH,
                                            GRIDCOLUMNWIDTH))


#
# class snake:
#     def __init__(self):
#         babySnake = box(int(numRows/2), int(numColumns/2))
#         self.snakeBody = []
#         self.snakeTurns = []
#         self.snakeBody.append(babySnake)
#
#     def turnSnake(self, direction):


snake = [box(int(numRows / 2), int(numColumns / 2))]
print(type(snake))
randomBox = box(rand.randrange(0, numColumns - 2, 1), rand.randrange(0, numRows - 2, 1), NO_DIR, (0, 255, 255))


def moveSnake():
    for count in range(len(snake)):
        snake[count].moveBox(snake[count].direc)


def drawSnake():
    global gameWindow
    for count in range(len(snake)):
        snake[count].drawBox(gameWindow)


def turnSnake(direction):
    global snake
    for i in range(len(snake)):
        index = len(snake) - 1 - i
        if index <= 0:
            break
        else:
            snake[index].updateDir(snake[index - 1].direc)

    snake[0].direc = direction
    # for i in range(len(snake)):
    #     print("{}:{}:{}".format(snake[i].xLoc, snake[i].yLoc, snake[i].direc))


def growSnake(tail):
    global snake
    snake.append(tail)


def drawWindow():
    global gameWindow
    global randomBox
    gameWindow.fill((0, 0, 0))

    # draw grid

    for count in range(int(WINDOWHEIGHT / GRIDCOLUMNWIDTH)):
        # drawing columns
        pg.draw.line(gameWindow, (255, 255, 255), (count * GRIDCOLUMNWIDTH, 0), (count * GRIDCOLUMNWIDTH, WINDOWHEIGHT),
                     1)
        # drawing rows
        pg.draw.line(gameWindow, (255, 255, 255), (0, count * GRIDCOLUMNWIDTH), (WINDOWWIDTH, count * GRIDCOLUMNWIDTH),
                     1)
    randomBox.drawBox(gameWindow)
    drawSnake()
    pg.display.update()


def main():
    global gameWindow
    global snake
    global randomBox
    tail = box(0, 0)
    snakeGrown = 0
    snakeMovementDir = NO_DIR

    clock = pg.time.Clock()
    runGame = True
    while runGame:
        pg.time.delay(200)

        if randomBox.xLoc == snake[0].xLoc and randomBox.yLoc == snake[0].yLoc:
            randomBox.updateLoc(rand.randrange(1, numColumns - 2, 1), rand.randrange(1, numRows - 2, 1))
            snakeGrown = 1

        for event in pg.event.get():
            if event.type == QUIT:
                runGame = False
                print("Game Closed")
            elif event.type == pg.KEYDOWN:
                keyPressed = pg.key.get_pressed()
                for key in keyPressed:
                    if keyPressed[K_RIGHT]:
                        snakeMovementDir = RIGHT_DIR
                        # print("Right: {0} {1}".format(Box.xLoc, Box.yLoc))
                    if keyPressed[K_LEFT]:
                        snakeMovementDir = LEFT_DIR
                        # print("Left: {0} {1}".format(Box.xLoc, Box.yLoc))
                    if keyPressed[K_DOWN]:
                        snakeMovementDir = DOWN_DIR
                        # print("Down: {0} {1}".format(Box.xLoc, Box.yLoc))
                    if keyPressed[K_UP]:
                        snakeMovementDir = UP_DIR
                        # print("UP: {0} {1}".format(Box.xLoc, Box.yLoc))

        tail.xLoc = snake[-1].xLoc
        tail.yLoc = snake[-1].yLoc
        tail.direc = snake[-1].direc
        turnSnake(snakeMovementDir)
        moveSnake()
        if snakeGrown:
            # growSnake(tail)
            snake.append(box(tail.xLoc, tail.yLoc, tail.direc))
            snakeGrown = 0
            print("Snake Len:{} Head Loc: {}, {}".format(len(snake), snake[0].xLoc, snake[0].yLoc))
            print("Snake Len:{} Tail Loc: {}, {}".format(len(snake), snake[-1].xLoc, snake[-1].yLoc))
        drawWindow()


main()

# keyPressed = pg.key.get_pressed()
# for key in keyPressed:
#     if keyPressed[K_RIGHT]:
#         snakeMovementDir = RIGHT_DIR
#         # print("Right: {0} {1}".format(Box.xLoc, Box.yLoc))
#     if keyPressed[K_LEFT]:
#         snakeMovementDir = LEFT_DIR
#         # print("Left: {0} {1}".format(Box.xLoc, Box.yLoc))
#     if keyPressed[K_DOWN]:
#         snakeMovementDir = DOWN_DIR
#         # print("Down: {0} {1}".format(Box.xLoc, Box.yLoc))
#     if keyPressed[K_UP]:
#         snakeMovementDir = UP_DIR
        # print("UP: {0} {1}".format(Box.xLoc, Box.yLoc))

# import tkinter as tk
# from tkinter import messagebox


# width = 500
# height = 500

# cols = 25
# rows = 20


# class cube():
#     rows = 20
#     w = 500
#     def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
#         self.pos = start
#         self.dirnx = dirnx
#         self.dirny = dirny # "L", "R", "U", "D"
#         self.color = color

#     def move(self, dirnx, dirny):
#         self.dirnx = dirnx
#         self.dirny = dirny
#         self.pos  = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)


#     def draw(self, surface, eyes=False):
#         dis = self.w // self.rows
#         i = self.pos[0]
#         j = self.pos[1]
#         pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2))
#         if eyes:
#             centre = dis//2
#             radius = 3
#             circleMiddle = (i*dis+centre-radius,j*dis+8)
#             circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
#             pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
#             pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


# class snake():
#     body = []
#     turns = {}

#     def __init__(self, color, pos):
#         #pos is given as coordinates on the grid ex (1,5)
#         self.color = color
#         self.head = cube(pos)
#         self.body.append(self.head)
#         self.dirnx = 0
#         self.dirny = 1

#     def move(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             keys = pygame.key.get_pressed()

#             for key in keys:
#                 if keys[pygame.K_LEFT]:
#                     self.dirnx = -1
#                     self.dirny = 0
#                     self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
#                 elif keys[pygame.K_RIGHT]:
#                     self.dirnx = 1
#                     self.dirny = 0
#                     self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
#                 elif keys[pygame.K_UP]:
#                     self.dirny = -1
#                     self.dirnx = 0
#                     self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
#                 elif keys[pygame.K_DOWN]:
#                     self.dirny = 1
#                     self.dirnx = 0
#                     self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]

#         for i, c in enumerate(self.body):
#             p = c.pos[:]
#             if p in self.turns:
#                 turn = self.turns[p]
#                 c.move(turn[0], turn[1])
#                 if i == len(self.body)-1:
#                     self.turns.pop(p)
#             else:
#                 c.move(c.dirnx,c.dirny)


#     def reset(self,pos):
#         self.head = cube(pos)
#         self.body = []
#         self.body.append(self.head)
#         self.turns = {}
#         self.dirnx = 0
#         self.dirny = 1

#     def addCube(self):
#         tail = self.body[-1]
#         dx, dy = tail.dirnx, tail.dirny

#         if dx == 1 and dy == 0:
#             self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
#         elif dx == -1 and dy == 0:
#             self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
#         elif dx == 0 and dy == 1:
#             self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
#         elif dx == 0 and dy == -1:
#             self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

#         self.body[-1].dirnx = dx
#         self.body[-1].dirny = dy

#     def draw(self, surface):
#         for i,c in enumerate(self.body):
#             if i == 0:
#                 c.draw(surface, True)
#             else:
#                 c.draw(surface)


# def redrawWindow():
#     global win
#     win.fill((0,0,0))
#     drawGrid(width, rows, win)
#     s.draw(win)
#     snack.draw(win)
#     pygame.display.update()
#     pass


# def drawGrid(w, rows, surface):
#     sizeBtwn = w // rows

#     x = 0
#     y = 0
#     for l in range(rows):
#         x = x + sizeBtwn
#         y = y +sizeBtwn

#         pygame.draw.line(surface, (255,255,255), (x, 0),(x,w))
#         pygame.draw.line(surface, (255,255,255), (0, y),(w,y))


# def randomSnack(rows, item):
#     positions = item.body

#     while True:
#         x = random.randrange(1,rows-1)
#         y = random.randrange(1,rows-1)
#         if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
#                continue
#         else:
#                break

#     return (x,y)


# def main():
#     global s, snack, win
#     win = pygame.display.set_mode((width,height))

#     breakpoint();

#     s = snake((255,0,0), (10,10))
#     s.addCube()
#     snack = cube(randomSnack(rows,s), color=(0,255,0))
#     flag = True
#     clock = pygame.time.Clock()

#     while flag:
#         pygame.time.delay(50)
#         clock.tick(10)
#         s.move()
#         headPos = s.head.pos
#         if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] < 0:
#             print("Score:", len(s.body))
#             s.reset((10, 10))

#         if s.body[0].pos == snack.pos:
#             s.addCube()
#             snack = cube(randomSnack(rows,s), color=(0,255,0))

#         for x in range(len(s.body)):
#             if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
#                 print("Score:", len(s.body))
#                 s.reset((10,10))
#                 break

#         redrawWindow()

# main()
