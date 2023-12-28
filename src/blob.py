from src import game_functions as gf
from src import msc

from src.settings import WIDTH, HEIGHT
from src.drawing_variables import colors


import pygame
import math
import random

from pygame import Vector2
from math import sqrt, cos, sin
from random import randrange, choice


class Blob:

    COLORS_NAME = ['blue2', 'green2', 'yellow1', 'red1', 'purple1', 'black1', 'orange2']

    def __init__(self, pos, rad, col=colors['lightblue1']):
        self.pos = Vector2(pos)
        self.rad = rad
        self.true_rad = rad
        self.angle = 1

        self.col = col

        self.vel = Vector2(0, 0)
        self.max_vel = 4

        self.ejection_intensity = 3
        self.reduce_amount = 1

        self.SHOW = True
        self.COLLIDED = False

    def __repr__(self):
        return repr(self.angle)

    def draw(self, win):
        if self.SHOW:
            pygame.draw.circle(win, self.col, self.pos, self.rad)
        else:
            pygame.draw.circle(win, self.col, self.pos, self.rad, 2)


    def move(self):
        self.pos += self.vel

    def decelerate(self):
        x, y = self.vel
        self.vel[0] = x - ((0.1 * x) + (x**2 / 60))
        self.vel[1] = y - ((0.1 * y) + (y**2 / 60))

    def spawn(self, radius_range=(5,10)):
        start, end = radius_range
        rad = randrange(start, end)
        dist = randrange(0, int(self.rad) - rad )
        angle = randrange(0, 620) / 100

        pos = gf.get_point_from_angle(self.pos, dist, angle)

        color_name = choice(self.COLORS_NAME)
        col = colors[color_name]

        new_blob = Blob(pos, rad, col=col)
        new_blob.angle = angle

        self.true_rad -= self.reduce_amount
        self.true_rad = max(self.reduce_amount + 10, self.true_rad)

        return new_blob

    def eject(self, angle):
        self.vel += Vector2(cos(angle), sin(angle)) * self.ejection_intensity

    def push(self, angle):
        self.vel += Vector2(cos(angle), sin(angle)) * self.ejection_intensity


    def cap_velocity(self):
        if self.vel != (0,0):
            x, y = self.vel

            norm = sqrt(x**2 + y**2)
            k = self.max_vel / norm

            if norm >= self.max_vel:
                self.vel *= k

    def shrink(self, rate):
        if self.rad > self.true_rad:
            self.rad -= rate

    def check_collision(self, all_elem):
        for elem in all_elem:
            x, y = elem.pos
            w = h = 2 * elem.rad

            rect = msc.centered_rect((x, y, w, h))
            if self != elem and rect.collidepoint(self.pos):
                return elem


def spawn_blobs(parent, n):
    spawned = []

    for i in range(n):
        new_blob = parent.spawn()
        spawned.append(new_blob)

    return spawned

def check_all_collisions(all_blobs):
    for blob in all_blobs:
        collided = blob.check_collision(all_blobs)
        if collided and blob.rad < collided.rad:
            angle = msc.get_angle(collided.pos, blob.pos)
            blob.eject(angle)

def update_all(blobs):
    for blob in blobs:
        blob.move()
        blob.decelerate()

        blob.cap_velocity()


def push_all(blobs):
    for blob in blobs:
        blob2 = choice(blobs)
        angle = msc.get_angle(blob2.pos, blob.pos)
        blob.push(angle)







