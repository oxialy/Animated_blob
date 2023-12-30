from src import game_functions as gf
from src import msc

from src.settings import WIDTH, HEIGHT
from src.drawing_variables import colors, colB


import pygame
import math
import random

from pygame import Vector2
from math import sqrt, cos, sin
from random import randrange, choice



class Hole:
    def __init__(self, pos, size=6):
        self.pos = pos
        self.size = size

        self.col = colors['red1']
        self.timer = 0

    def draw(self, win):
        pygame.draw.circle(win, self.col, self.pos, self.size, 2)

    def add_timer(self):
        self.timer += 1


def update_holes(holes):
    for hole in holes:
        hole.add_timer()

        if hole.timer <= 0:
            holes.remove(hole)

    return holes









