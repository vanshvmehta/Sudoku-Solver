import copy
from random import randint
import pygame

boxWidth = 60


class BigButton:
    def __init__(self, colour, x, y, width, height, size, text=''):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = size

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comics', self.text_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width // 2 - text.get_width() // 2),
                self.y + (self.height // 2 - text.get_height() // 2)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True


class Button:
    def __init__(self, x, y):
        self.colour = (255, 255, 255)
        self.x = x
        self.y = y
        self.text = 0
        self.text_size = 35
        self.text_temp_size = 20
        self.temp_text = 0
        self.done = False

    def draw(self, win, outline=(0, 0, 0)):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 1, self.y - 1, boxWidth + 2, boxWidth + 2))

        pygame.draw.rect(win, self.colour, (self.x, self.y, boxWidth, boxWidth))

        if self.text != 0:
            font = pygame.font.SysFont('comics', self.text_size)
            text = font.render(str(self.text), 1, (0, 0, 0))
            win.blit(text, (
                self.x + (boxWidth // 2 - text.get_width() // 2),
                self.y + (boxWidth // 2 - text.get_height() // 2)))

        elif self.temp_text != 0:
            font = pygame.font.SysFont('comics', self.text_temp_size)
            text = font.render(str(self.temp_text), 1, (128, 128, 128))
            win.blit(text, (
                self.x + (boxWidth // 4 - text.get_width() // 4),
                self.y + (boxWidth // 4 - text.get_height() // 4)))

    def isOver(self, pos):
        if self.x < pos[0] < self.x + boxWidth:
            if self.y < pos[1] < self.y + boxWidth:
                return True

        return False


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def rand_list():
    rand = []

    done = False
    while not done:
        num = randint(1, 9)
        for i in rand:
            if i == num:
                break
        else:
            rand.append(num)

        if len(rand) == 9:
            done = True

    return rand


def randListDel():
    rand = []

    done = False
    while not done:
        num = randint(0, 8)
        for i in rand:
            if i == num:
                break
        else:
            rand.append(num)

        if len(rand) == 9:
            done = True

    return rand


def find_emp(game):
    for i in range(len(game)):
        for j in range(len(game[i])):
            if game[i][j] == 0:
                return i, j

    return None


def autoSolving(game):
    found = find_emp(game)
    if found is not None:
        row, col = found
        pygame.time.delay(500)

    else:
        return True

    for i in range(1, 10):
        if check(i, row, col, game):
            game[row][col] = i

            if autoSolving(game):
                return True

            game[row][col] = 0

    return False


def solve(game):
    rand = rand_list()

    found = find_emp(game)
    if found is not None:
        row, col = found

    else:
        return True

    for i in rand:
        if check(i, row, col, game):
            game[row][col] = i

            if solve(game):
                return True

            game[row][col] = 0

    return False


def check(num, row, col, game):
    # Check Row
    for i in game[row]:
        if num == i:
            return False

    # Check Column
    for i in game:
        if i[col] == num:
            return False

    # Check Box
    row_num = row // 3
    col_num = col // 3

    for i in range(row_num * 3, row_num * 3 + 3):
        for j in range(col_num * 3, col_num * 3 + 3):
            if game[i][j] == num:
                return False

    return True


def easyBoard(temp):
    game = copy.deepcopy(temp)
    for i in range(9):
        rand = randListDel()

        for j in range(5):
            game[i][rand[j]] = 0

    return game


def mediumBoard(temp):
    game = copy.deepcopy(temp)
    for i in range(9):
        rand = randListDel()

        delNum = randint(5, 6)
        for j in range(delNum):
            game[i][rand[j]] = 0

    return game


def hardBoard(temp):
    game = copy.deepcopy(temp)
    for i in range(9):
        rand = randListDel()

        delNum = randint(5, 7)
        for j in range(delNum):
            game[i][rand[j]] = 0

    return game


def gameBoard():
    solve(board)

    return board
