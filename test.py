import pygame
import numpy as np
import sys
from time import sleep
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

def initialize():
    global blockSize
    global columns
    global rows
    blockSize = 20
    columns = range(0, WINDOW_WIDTH, blockSize)
    rows = range(0, WINDOW_HEIGHT, blockSize)

def draw(board):
    screen.fill(WHITE)
    width = 1
    for y in rows:
        for x in columns:
            rect = pygame.Rect(x, y, blockSize, blockSize)
            if board[rows.index(y)][columns.index(x)] == 1:
                width = 0
            elif board[rows.index(y)][columns.index(x)] == 0:
                width = 1
            pygame.draw.rect(screen, BLACK, rect, width)

def check(board):
    newBoard = np.zeros((len(rows), len(columns)), dtype=np.int16)
    for y in range(len(rows)):
        for x in range(0, len(columns)):
            neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
            alive_neighbors = 0
            test = []
            for i in neighbors:
                if i[0] < 0 or i[1] < 0:
                    neighbors.remove(i)
                    continue
                elif i[0] > (len(columns)-1) or i[1] > (len(rows)-1):
                    neighbors.remove(i)
                    continue
                elif board[i[1]][i[0]] == 1:
                    alive_neighbors += 1
                    test.append(i)

            if board[y][x] == 1:
                if alive_neighbors < 2:
                    newBoard[y][x] = 0
                elif alive_neighbors == 2 or alive_neighbors == 3:
                    newBoard[y][x] = 1
                elif alive_neighbors > 3:
                    newBoard[y][x] = 0
            elif board[y][x] == 0:
                if alive_neighbors == 3:
                    newBoard[y][x] = 1
    return newBoard

def addGlider(x, y, board):
    blocks = [(x-1, y), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1)]
    for i in blocks:
        board[i[1]][i[0]] = 1

def randomLife(board):
    for y in range(len(rows)):
        for x in range(len(columns)):
            num = random.randint(0, 1)
            if num == 0:
                board[y][x] = 1


def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(WHITE)

    initialize()
    board = np.zeros((len(rows), len(columns)), dtype=np.int16)
    # addGlider(10, 10, board)
    randomLife(board)
    generation = 0
    while True:
        generation += 1
        print(f"{generation = }", end="\r")
        draw(board)
        board = check(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        # sleep(0.5)

if __name__=="__main__":
    main()
