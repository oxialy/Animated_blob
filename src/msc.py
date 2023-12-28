from src import settings as sett


import pygame
import random
import math

from pygame import Vector2
from random import sample
from math import sqrt, cos, sin, atan2


pygame.font.init()

FONT30 = pygame.font.SysFont('arial', 30)
FONT35 = pygame.font.SysFont('arial', 35)
FONT40 = pygame.font.SysFont('arial', 40)


def centered_rect(rect):
    x,y,w,h = rect

    x -= w // 2
    y -= h // 2

    return pygame.Rect((x,y,w,h))

def get_dist(A, B):
    x1, y1 = A
    x2, y2 = B

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_angle(A, B):
    x1, y1 = A
    x2, y2 = B

    return atan2((y2-y1), (x2-x1))


def get_point_from_angle(pos, angle, dist):
    x1, y1 = pos

    a = sin(angle) / cos(angle)

    x2 = x1 + cos(angle) * dist
    y2 = y1 + sin(angle) * dist

    return x2, y2


def get_average_point(A, B):
    x1, y1 = A
    x2, y2 = B

    return (x1 + x2) / 2, (y1 + y2) /2


def get_tail_resting_pos(body):
    tail = body[-1]
    left_link = tail.left_link
    rad = tail.size[0]

    force = get_force(tail.pos, left_link.pos, rad)


def get_force(A, B, rad, force_factor=30, min_force=0):
    dist = get_dist(A, B)
    angle = get_angle(A, B)

    force_x = cos(angle) * (dist - rad + min_force) / force_factor
    force_y = sin(angle) * (dist - rad + min_force) / force_factor

    force_x = min(1.5, force_x)
    force_y = min(1.7, force_y)

    return Vector2(force_x, force_y)


def write_text(win, data, pos, col='grey'):
    text_surf = sett.FONT20.render(str(data), 1, col)

    win.blit(text_surf, pos)

def add_log(logs, data):
    if data not in logs:
        logs.append(data)
        print(data, len(logs))
    return logs











