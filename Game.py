import pygame
from Function import *

heartPic = pygame.image.load('heart.png')
homeImg = pygame.image.load('Sudoku_img.png')
howToPlayImg = pygame.image.load('howToPlay.png')
box_width = 60
pygame.init()
win = pygame.display.set_mode((box_width * 9, box_width * 10))
pygame.display.set_caption('Sudoku')

clock = pygame.time.Clock()
buttons = [[None] * 9, [None] * 9, [None] * 9, [None] * 9, [None] * 9, [None] * 9, [None] * 9, [None] * 9, [None] * 9]

autoSolveButton = BigButton((0, 0, 255), 320, 550, 200, 40, 25, 'Auto Solve')
doneButton = BigButton((0, 0, 255), 400, 550, 100, 40, 30, 'Done')
newGameButton = BigButton((0, 0, 255), 175, 300, 200, 50, 35, 'New Game')
howToPlayButton = BigButton((0, 0, 255), 175, 375, 200, 50, 35, 'How To Play')
easyButton = BigButton((0, 0, 255), 55, 350, 125, 50, 30, 'Easy')
mediumButton = BigButton((0, 0, 255), 205, 350, 125, 50, 30, 'Medium')
hardButton = BigButton((0, 0, 255), 355, 350, 125, 50, 30, 'Hard')
backButton = BigButton((0, 0, 255), 430, 550, 100, 40, 30, 'Back')
congoButton = BigButton((255, 255, 255), 100, 550, 200, 50, 30, 'CONGRATULATION!!')
skipButton = BigButton((0, 0, 255), 400, 550, 100, 40, 30, 'Skip')


def reDrawHomeWindow():
    global win
    win.fill((255, 255, 255))
    win.blit(homeImg, (20, 50))

    newGameButton.draw(win, (0, 0, 0))
    howToPlayButton.draw(win, (0, 0, 0))


def reDrawHowToPlayWindow():
    global win
    win.blit(howToPlayImg, (0, 0))
    win.blit(homeImg, (20, 50))

    backButton.draw(win, (0, 0, 0))


def reDrawDifficultyWindow():
    win.fill((255, 255, 255))
    win.blit(homeImg, (20, 50))

    easyButton.draw(win, (0, 0, 0))
    mediumButton.draw(win, (0, 0, 0))
    hardButton.draw(win, (0, 0, 0))


def createButtons():
    global buttons

    for i in range(9):
        x = 0 - box_width
        y = box_width * i
        for j in range(9):
            x += box_width
            buttons[i][j] = Button(x, y)


createButtons()


def drawBoard():
    global win

    win.fill((255, 255, 255))
    for i in buttons:
        for j in i:
            j.draw(win)

    pygame.draw.line(win, (0, 0, 0), (box_width * 3, 0), (box_width * 3, box_width * 9), 2)
    pygame.draw.line(win, (0, 0, 0), (box_width * 6, 0), (box_width * 6, box_width * 9), 2)
    pygame.draw.line(win, (0, 0, 0), (0, box_width * 3), (box_width * 9, box_width * 3), 2)
    pygame.draw.line(win, (0, 0, 0), (0, box_width * 6), (box_width * 9, box_width * 6), 2)
    pygame.draw.line(win, (0, 0, 0), (0, box_width * 9 + 1), (box_width * 9, box_width * 9 + 1), 2)

    if heart >= 1:
        win.blit(heartPic, (10, 545))
    if heart >= 2:
        win.blit(heartPic, (60, 545))
    if heart >= 3:
        win.blit(heartPic, (110, 545))
    if heart == 4:
        win.blit(heartPic, (160, 545))

    if not autoSolve and not done:
        autoSolveButton.draw(win, (0, 0, 0))

    if done:
        doneButton.draw(win, (0, 0, 0))

    if gameOver:
        congoButton.draw(win)


def addNumbers():
    global win, board, heart

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                buttons[i][j].text = 0
                buttons[i][j].temp_text = 0
                buttons[i][j].done = False
            else:
                buttons[i][j].text = board[i][j]
                buttons[i][j].done = True


def autoSolveProtocol(game):
    found = find_emp(game)
    if found is not None:
        row, col = found

    else:
        return True

    for i in range(1, 10):
        if check(i, row, col, game):
            buttons[row][col].text = i
            game[row][col] = i
            buttons[row][col].colour = (0, 255, 0)

            drawBoard()
            pygame.display.update()

            if autoSolveProtocol(game):
                return True

            buttons[row][col].text = 0
            game[row][col] = 0
            buttons[row][col].colour = (255, 0, 0)

            drawBoard()
            pygame.display.update()


def reDrawGameWindow():
    drawBoard()


homePage = True
difficultyPage = howToPlayPage = gamePage = gameOver = autoSolveTime = False
run = True
while run:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            run = False

    if homePage:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if newGameButton.isOver(pos):
                difficultyPage = True
                homePage = False
                clicked = confirm = autoSolve = done = easyGame = interGame = hardGame = False
                row = col = num = 0
                heart = 4
                pygame.time.delay(1000)

            if howToPlayButton.isOver(pos):
                howToPlayPage = True
                homePage = False
                pygame.time.delay(1000)

        if event.type == pygame.MOUSEMOTION:
            if newGameButton.isOver(pos):
                newGameButton.colour = (0, 255, 0)
            else:
                newGameButton.colour = (0, 0, 255)

            if howToPlayButton.isOver(pos):
                howToPlayButton.colour = (0, 255, 0)
            else:
                howToPlayButton.colour = (0, 0, 255)

        reDrawHomeWindow()

    if howToPlayPage:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                homePage = True
                howToPlayPage = False
                pygame.time.delay(1000)

        if event.type == pygame.MOUSEMOTION:
            if backButton.isOver(pos):
                backButton.colour = (0, 255, 0)
            else:
                backButton.colour = (0, 0, 255)

        reDrawHowToPlayWindow()

    if difficultyPage:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easyButton.isOver(pos):
                easyGame = True
                difficultyPage = False
                gamePage = True
                solvedBoard = gameBoard()
                board = easyBoard(solvedBoard)
                addNumbers()
                pygame.time.delay(1000)

            if mediumButton.isOver(pos):
                interGame = True
                difficultyPage = False
                gamePage = True
                solvedBoard = gameBoard()
                board = mediumBoard(solvedBoard)
                addNumbers()
                pygame.time.delay(1000)

            if hardButton.isOver(pos):
                hardGame = True
                difficultyPage = False
                gamePage = True
                solvedBoard = gameBoard()
                board = hardBoard(solvedBoard)
                addNumbers()
                pygame.time.delay(1000)

        if event.type == pygame.MOUSEMOTION:
            if easyButton.isOver(pos):
                easyButton.colour = (0, 255, 0)
            else:
                easyButton.colour = (0, 0, 255)

            if mediumButton.isOver(pos):
                mediumButton.colour = (0, 255, 0)
            else:
                mediumButton.colour = (0, 0, 255)

            if hardButton.isOver(pos):
                hardButton.colour = (0, 255, 0)
            else:
                hardButton.colour = (0, 0, 255)

        reDrawDifficultyWindow()

    if gamePage:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(9):
                for j in range(9):
                    if buttons[i][j].isOver(pos):
                        row, col = i, j
                        clicked = True
                        confirm = False

        if not confirm:
            for i in range(9):
                for j in range(9):
                    if i == row and j == col:
                        if buttons[row][col].done is False:
                            buttons[row][col].colour = (0, 0, 255)
                    else:
                        buttons[i][j].colour = (255, 255, 255)

        if clicked:
            if keys[pygame.K_1]:
                num = 1
            elif keys[pygame.K_2]:
                num = 2
            elif keys[pygame.K_3]:
                num = 3
            elif keys[pygame.K_4]:
                num = 4
            elif keys[pygame.K_5]:
                num = 5
            elif keys[pygame.K_6]:
                num = 6
            elif keys[pygame.K_7]:
                num = 7
            elif keys[pygame.K_8]:
                num = 8
            elif keys[pygame.K_9]:
                num = 9

            if num != 0:
                buttons[row][col].temp_text = num
                clicked = False
                confirm = True
                num = 0

        if buttons[row][col].temp_text != 0 and buttons[row][col].done is False:
            if keys[pygame.K_RETURN]:
                guess = buttons[row][col].temp_text
                buttons[row][col].text = buttons[row][col].temp_text
                buttons[row][col].temp_text = 0
                pygame.time.delay(250)

                if str(guess) == str(solvedBoard[row][col]):
                    buttons[row][col].colour = (0, 255, 0)
                    pygame.time.delay(500)

                    buttons[row][col].done = True
                    board[row][col] = int(guess)

                else:
                    buttons[row][col].colour = (255, 0, 0)
                    pygame.time.delay(500)
                    heart -= 1
                    buttons[row][col].text = 0

        if done:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if doneButton.isOver(pos):
                    homePage = True
                    gamePage = False
                    gameOver = False
                    pygame.time.delay(1000)

            if event.type == pygame.MOUSEMOTION:
                if doneButton.isOver(pos):
                    doneButton.colour = (0, 255, 0)
                else:
                    doneButton.colour = (0, 0, 255)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if autoSolveButton.isOver(pos):
                autoSolve = True
                pygame.time.delay(1000)

        if event.type == pygame.MOUSEMOTION:
            if autoSolveButton.isOver(pos):
                autoSolveButton.colour = (0, 255, 0)
            else:
                autoSolveButton.colour = (0, 0, 255)

        if autoSolve is True or heart == 0:
            gamePage = False
            autoSolveTime = True
            autoSolve = True

        emptySpace = find_emp(board)
        if emptySpace is None:
            gameOver = True
            done = True
            heart = -1

        reDrawGameWindow()

    if autoSolveTime:
        emptySpace = find_emp(board)
        if emptySpace is None:
            done = True
            autoSolve = False
            heart = -1

        if done:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if doneButton.isOver(pos):
                    homePage = True
                    autoSolveTime = False
                    pygame.time.delay(1000)

            if event.type == pygame.MOUSEMOTION:
                if doneButton.isOver(pos):
                    doneButton.colour = (0, 255, 0)
                else:
                    doneButton.colour = (0, 0, 255)

        if autoSolve:
            autoSolveProtocol(board)

        for i in range(9):
            for j in range(9):
                buttons[i][j].colour = (255, 255, 255)

        reDrawGameWindow()

    pygame.display.update()

pygame.quit()
