# Developer: Shen Z.
# Time: 2023-06-29 9:23 p.m.
import pygame
from copy import deepcopy

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH = (400, 500)
W, H = WIDTH

running = True
reset = True
cheat = False
turn = 0
win = ''

row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']
board = [row1, row2, row3]
font_name = pygame.font.match_font('arial')
show_init = True
show_end = False


def start():
    pygame.init()
    screen = pygame.display.set_mode(WIDTH)
    pygame.display.set_caption('Tic Tac Toe')
    draw_text(screen, 'Tic Tac Toe', 80, W/2, H/5)
    draw_text(screen, 'The ultimate competition between ', 30, W/2, H/2.3)
    draw_text(screen, 'x and o', 70, W/2, H/2)
    draw_text(screen, 'Press Mouse to Start', 18, W/2, H*3/4)
    pygame.display.update()
    waiting = True

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
                done =True
                pygame.quit()

                return True
            elif event.type == pygame.MOUSEBUTTONUP:
                waiting = False
                return False


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)
def draw_x(m_pos):

    font = pygame.font.Font(font_name, 70)
    text_surface = font.render('X', True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx, text_rect.centery = m_pos
    screen.blit(text_surface, text_rect)
    pygame.display.update()
def draw_o(m_pos):
    pygame.draw.circle(screen, WHITE, m_pos, 30)
    pygame.draw.circle(screen, BLACK, m_pos, 25)
    pygame.display.update()
def center_pos(m_pos):
    m_posx, m_posy = m_pos

    if m_posx>50 and m_posx<150:
        posx = 100
    elif m_posx>150 and m_posx<250:
        posx = 200
    elif m_posx>250 and m_posx<350:
        posx = 300
    else:
        posx = m_posx
    if m_posy>150 and m_posy<250:
        posy = 200
    elif m_posy>250 and m_posy<350:
        posy = 300
    elif m_posy>350 and m_posy<450:
        posy = 400
    else:
        posy = m_posy

    pos = (posx, posy)
    return pos
def check_game(pos, x, o):

    if pos == (100,200):
        if x:
            row1[0] = 'x'
            x=0
        if o:
            row1[0] = 'o'
            o = 0
    if pos == (200,200):
        if x:
            row1[1] = 'x'
            x=0
        if o:
            row1[1] = 'o'
            o = 0
    if pos == (300,200):
        if x:
            row1[2] = 'x'
            x=0
        if o:
            row1[2] = 'o'
            o = 0

    if pos == (100,300):
        if x:
            row2[0] = 'x'
            x = 0
        if o:
            row2[0] = 'o'
            o = 0
    if pos == (200,300):
        if x:
            row2[1] = 'x'
            x = 0
        if o:
            row2[1] = 'o'
            o = 0
    if pos == (300,300):
        if x:
            row2[2] = 'x'
            x = 0
        if o:
            row2[2] = 'o'
            o = 0

    if pos == (100,400):
        if x:
            row3[0] = 'x'
            x = 0
        if o:
            row3[0] = 'o'
            o = 0
    if pos == (200,400):
        if x:
            row3[1] = 'x'
            x = 0
        if o:
            row3[1] = 'o'
            o = 0
    if pos == (300,400):
        if x:
            row3[2] = 'x'
            x = 0
        if o:
            row3[2] = 'o'
            o = 0
def check_win(bd):
    for r in bd:
        check(r,bd)
    for i in range(0,3):
        c = [row[i] for row in bd]
        check(c,bd)

def check(row, bd):
    if '' not in row:
        e1, e2, e3 = row
        if e1 == e2 and e2 == e3:
            global win
            win = e1
        r1, r2, r3 = bd
        e1, e2, e3 = r1
        e4, e5, e6 = r2
        e7, e8, e9 = r3
        if e1 == e5 and e5 == e9:
            win = e5
        if e7 == e5 and e5 == e3:
            win = e5


def check_cheat(begin, end):
    for i in range(0,3):
        for i2 in range(0,3):
            if begin[i][i2] == 'x' and end[i][i2] == 'o':
                draw_text(screen, 'Player o cheated, player x is the winner', 20, W / 2, H / 10)
                pygame.display.update()
                return True
                pass
            if begin[i][i2]== 'o' and end[i][i2] == 'x':
                draw_text(screen, 'Player x cheated, player o is the winner', 20, W / 2, H / 10)
                pygame.display.update()
                return True
                pass
    return False




while running:
    while reset:
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        WIDTH = (400, 500)
        W, H = WIDTH

        running = True
        cheat = False
        turn = 0
        win = ''

        row1 = ['', '', '']
        row2 = ['', '', '']
        row3 = ['', '', '']
        board = [row1, row2, row3]
        font_name = pygame.font.match_font('arial')
        show_init = True
        show_end = False
        reset = False
    if show_init:
        close = start()
        if close:
            break
        show_init = False
        pygame.init()
        screen = pygame.display.set_mode(WIDTH)
        pygame.display.set_caption('Tic Tac Toe')
        pygame.draw.line(screen, WHITE, (150, 150), (150, 450), 5)
        pygame.draw.line(screen, WHITE, (250, 150), (250, 450), 5)
        pygame.draw.line(screen, WHITE, (50, 250), (350, 250), 5)
        pygame.draw.line(screen, WHITE, (50, 350), (350, 350), 5)
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            done = True
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONUP:
            for i in range(0, 1):
                b = deepcopy(board)

            pos = pygame.mouse.get_pos()
            pos = center_pos(pos)
            if turn%2 == 0:
                draw_x(pos)
                turn += 1
                x = 1
                check_game(pos, x, 0)
                check_win(board)
            else:
                draw_o(pos)
                turn += 1
                o = 1
                check_game(pos, 0, o)
                check_win(board)
            cheat = check_cheat(b, board)
            if cheat:
                show_end = True
            if win =='x':
                show_end = True
            if win == 'o':
                show_end = True

    if show_end:
        pygame.draw.rect(screen, BLACK, (0, 100, 400, 500))
        if win == 'x':
            draw_text(screen, 'x is the winner', 50, W / 2, H / 2)
        if win == 'o':
            draw_text(screen, 'o is the winner', 50, W / 2, H / 2)
        draw_text(screen, 'Press Mouse to Continue', 18, W / 2, H * 3 / 4)
        pygame.display.update()
        waiting = True

        while waiting:
            pygame.init()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    reset = True
                    waiting = False
                    show_init = True
                    show_end = False






