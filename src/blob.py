from src import game_functions as gf
from src import msc


from src.settings import WIDTH, HEIGHT
from src.drawing_variables import colors, colB
from src.hole import Hole


import pygame
import math
import random

from pygame import Vector2
from math import sqrt, cos, sin
from random import randrange, choice


class Blob:

    COLORS_NAME = ['blue2', 'green2', 'yellow1', 'red1', 'purple1', 'black1', 'orange2']
    COLORS_NAME = ['blue2', 'red1', 'purple1', 'black1']

    def __init__(self, pos, rad, color_name='lightblue1'):
        self.pos = Vector2(pos)
        self.rad = rad
        self.true_rad = rad
        self.smallest_rad = 26
        self.angle = 1

        self.color_name = color_name
        self.col1 = colors[color_name]
        self.col2 = colors['lightgrey1']
        self.col3 = colB[color_name]

        self.vel = Vector2(0, 0)
        self.max_vel = 18

        self.ejection_intensity = 2
        self.reduce_amount = 4

        self.positions = []
        self.track_cd = 10

        self.paired = None

        self.type = 2
        self.SHOW = True
        self.COLLIDED = False
        self.STATUS = 1
        self.SHRINKING = False
        self.ANIMATE = 0
        self.STOPPED = 0

        self.shake_vector = Vector2(0, 1)

        self.timer = 0

    def __repr__(self):
        return repr(self.type)

    def draw(self, win):
        if self.SHOW:
            x,y = self.pos
            w = h = self.rad * 2 * 0.75

            rect = msc.centered_rect((x,y,w,h))
            a = 2.1
            b = 2.5
            c = 3.5
            d = 5.3

            pygame.draw.circle(win, self.col1, self.pos, self.rad)
            pygame.draw.arc(win, self.col2, rect, a, b, 1)
            pygame.draw.arc(win, self.col3, rect, c, d, 1)
        else:
            pass

        if self.rad in [6,11]:
            self.draw_positions(win)

    def draw_positions(self, win):
        for pos in self.positions:
            x, y = pos
            pygame.draw.circle(win, self.col2, (x,y), 2)

    def move(self):
        self.pos += self.vel
        self.angle = msc.get_angle((0,0), self.vel)

    def decelerate(self):
        if self.vel != (0,0):
            x, y = self.vel

            norm = sqrt((x**2 + y**2))

            new_norm = norm - ((0.12 * norm) + (norm**2 / 150)) - 0.1
            new_norm = max(0, new_norm)

            k = new_norm / norm

            self.vel[0] = x * k
            self.vel[1] = y * k

    def spawn(self, radius_range=(5,10)):
        start, end = radius_range
        rad = randrange(start, end)
        dist = 2
        angle = randrange(0, 620) / 100
        intensity = randrange(5,40)

        pos = gf.get_point_from_angle(self.pos, dist, angle)
        pos2 = msc.get_point_from_angle(pos, intensity, angle)

        force = msc.get_force(pos, pos2, 0, 5)

        color_name = choice(self.COLORS_NAME)
        col = colors[color_name]

        new_blob = Blob(pos, rad, color_name=color_name)
        new_blob.angle = angle
        new_blob.vel += force * intensity

        self.true_rad -= self.reduce_amount
        #self.true_rad = max(self.smallest_rad, self.true_rad)

        return new_blob

    def eject(self, angle):
        self.vel += Vector2(cos(angle), sin(angle)) * self.ejection_intensity

    def push(self, angle):
        self.vel += Vector2(cos(angle), sin(angle)) * self.ejection_intensity

    def apply_force(self):
        if self.paired:
            force = msc.get_force(self.paired.pos, self.pos, 0, 14)

            self.vel += force

    def cap_velocity(self):
        if self.vel != (0,0):
            x, y = self.vel

            norm = sqrt(x**2 + y**2)
            k = self.max_vel / norm

            if norm >= self.max_vel:
                self.vel *= k

    def shrink(self, rate):
        if self.type == 1:
            if self.rad > self.true_rad:
                self.rad -= rate
        else:
            self.rad -= rate

    def reset(self):
        self.rad = 50
        self.true_rad = 50
        self.STATUS = 1

    def add_pos(self):
        if len(self.positions) < 50:
            x, y = self.pos
            self.positions.append((x,y))

    def add_timer(self):
        self.track_cd -= 1

    def check_collision(self, all_elem):
        for elem in all_elem:
            x, y = elem.pos
            w = h = 2 * elem.rad

            rect = msc.centered_rect((x, y, w, h))
            if self != elem and rect.collidepoint(self.pos):
                return elem

    def spawn_hole(self):
        pos = msc.get_point_from_angle(self.pos, -self.angle, 4)

        new_hole = Hole(pos)

        self.paired = new_hole
        new_hole.paired = self

        return new_hole

def spawn_blobs(parent, n):
    spawned = []

    for i in range(n):
        rad_range = 2,25
        new_blob = parent.spawn(rad_range)
        spawned.append(new_blob)

    return spawned

def check_all_collisions(all_blobs):
    for blob in all_blobs:
        collided = blob.check_collision(all_blobs[::-1])
        if collided and blob.type != 1 and collided.type == 0:
            angle = msc.get_angle(collided.pos, blob.pos)
            blob.eject(angle)


def update_all(blobs, holes):
    for blob in blobs:
        blob.move()
        blob.decelerate()

        if blob.paired:
            blob.apply_force()

        blob.cap_velocity()
        blob.track_cd += 1

        norm = sqrt(blob.vel[0]**2 + blob.vel[1]**2)
        if blob.type != 1 and norm < 0.3 and not blob.paired and blob.STATUS != 'stop' and blob.timer > 8:
            new_hole = blob.spawn_hole()
            holes.append(new_hole)

        if blob.rad < 2:
            blob.STATUS = 0
        if not blob.STATUS:
            blobs.remove(blob)

        blob.timer += 1

        '''if blob.track_cd >= 10:
            blob.add_pos()
            blob.track_cd = 0'''

    return blobs, holes


def push_all(blobs):
    for blob in blobs:
        blob2 = choice(blobs)
        angle = msc.get_angle(blob2.pos, blob.pos)
        blob.push(angle)







