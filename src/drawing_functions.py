
from src import settings as sett
from src import game_variables as GV
from src import drawing_variables as dv
from src import msc, logs

from .drawing_variables import bg_color, colors


import pygame
import random
from random import randrange, choice


def draw_test(win):
    def write_words(n):
        for i in range(n):
            word = 'non' * i
            write_text()


def draw_screen(win):
    win.fill(bg_color)

    draw_elem(win, GV.all_blobs)

    #draw_test(win)


def draw_elem(win, elements):
    for elem in elements:
        elem.draw(win)


def write_text(win, data, pos, col=colors['grey1'], resize_limit=0):
    #font = pygame.font.SysFont('arial', 30)

    text_surf = sett.FONT20.render(str(data), 1, col)
    size = text_surf.get_size()

    if resize_limit != 0 and size[0] > resize_limit:
        text_surf = sett.FONT15.render(str(data), 1, col)
        size = text_surf.get_size()

    x = pos[0] - size[0] // 2
    y = pos[1] - size[1] // 2

    win.blit(text_surf, (x,y))













