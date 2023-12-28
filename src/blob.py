from src import game_functions as gf

from src.settings import WIDTH, HEIGHT
from src.drawing_variables import colors


import pygame
import math
import random

from pygame import Vector2
from math import sqrt, cos, sin
from random import randrange, choice


class Blob:

    COLORS_NAME = ['blue2', 'green2', 'yellow1', 'red1', 'purple1', 'black', 'orange2']

    def __init__(self, pos, rad, col=colors['lightblue1']):
        self.pos = Vector2(pos)
        self.rad = rad

        self.col = col

        self.vel = Vector2(0, 0)

        self.max_vel = 10

    def draw(self, win):
        pass

    def move(self):
        self.pos += self.vel

    def decelerate(self):
        x, y = self.vel
        self.vel[0] = x - 0.1 * x - x**2 / 60
        self.vel[1] = y - 0.1 * y - y**2 / 60

    def spawn_blob(self, rad):
        x, y = self.pos

        min_x = int(x - self.rad)
        max_x = int(x + self.rad)

        pos = randrange(min_x, max_x)

        new_blob = Blob(pos, rad)
        return new_blob

    def spawn(self, rad):
        x, y = self.pos

        dist = randrange(0, self.rad)
        angle = randrange(0, 620) / 100

        pos = gf.get_point_from_angle(self.pos, dist, angle)

        new_blob = Blob(pos, rad)
        return new_blob


    def cap_velocity(self):
        pass


def spawn_blobs(parent, n):
    spawned = []

    for i in range(n):
        new_blob = parent.spawn(5)
        spawned.append(new_blob)

    return spawned










