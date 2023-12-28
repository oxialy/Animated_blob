from src import settings as sett


import pygame.font
import random

from random import sample


pygame.font.init()

FONT30 = pygame.font.SysFont('arial', 30)
FONT35 = pygame.font.SysFont('arial', 35)
FONT40 = pygame.font.SysFont('arial', 40)


def write_text(win, data, pos, col='grey'):
    text_surf = sett.FONT20.render(str(data), 1, col)

    win.blit(text_surf, pos)

def add_log(logs, data):
    if data not in logs:
        logs.append(data)
        print(data, len(logs))
    return logs











