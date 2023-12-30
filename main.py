from src import game_functions as GF
from src import game_variables as GV
from src import logs
from src import settings as sett


from src.settings import WIDTH, HEIGHT, clock, FPS
from src.blob import spawn_blobs, check_all_collisions, update_all, push_all
from src.hole import update_holes
from src.drawing_functions import draw_screen

import pygame
import random

from pygame.locals import *
from random import randrange, choice


#data = {'test': 'test'}

#logs.save_data(logs.LOG_FILE, data)
logs.init_log(logs.LOG_FILE)


WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def initialize_grid(grid):
    i, j = GV.tile1.pos
    grid[j][i] = GV.tile1

    return grid

def init_userevent(events):
    for event, spec in events.items():
        pygame.time.set_timer(event, spec['timer'])


def reduce_timer(event):
    GV.START_EVENT

def main():

    #init_userevent(GV.START_EVENT)

    run_main = True

    while run_main:

        draw_screen(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_main = False
            if event.type == pygame.KEYDOWN:
                if event.key in [K_q, K_ESCAPE]:
                    run_main = False

                if event.key == K_p:
                    push_all(GV.all_blobs)

                if event.key == K_s:
                    pygame.time.set_timer(GV.SPAWNBLOB, 0)

                if event.key == K_RETURN:
                    if len(GV.all_blobs) > 6:
                        GV.all_blobs = [GV.blob1, GV.blob0]
                        GV.blob1.reset()
                    else:
                        pygame.time.set_timer(GV.SPAWNBLOB, 90)


                if event.key == K_SPACE:
                    n = randrange(3, 11)
                    spawned = spawn_blobs(GV.blob1, n)
                    GV.all_blobs += spawned

                    GV.blob1.SHOW = False

                    if len(GV.all_blobs) > 100:
                        for _ in range(30):
                            i = randrange(len(GV.all_blobs))
                            if GV.blob1 != GV.all_blobs[i]:
                                GV.all_blobs.pop(i)


                if event.key == K_l:
                    logs.print_logs(logs.LOG_FILE)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            if event.type == GV.SPAWNBLOB:
                if len(GV.all_blobs) <= 15:
                    b = GV.blob1.spawn((5,12))
                    GV.all_blobs.append(b)

                    event_spec = GV.START_EVENT[GV.SPAWNBLOB]
                else:
                    pygame.time.set_timer(GV.SPAWNBLOB, 0)


        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

        GV.blob1.shrink(30/FPS)
        check_all_collisions(GV.all_blobs)
        GV.all_blobs, GV.all_holes = update_all(GV.all_blobs, GV.all_holes)
        GV.all_holes = update_holes(GV.all_holes)

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()



main()



