from src import game_functions as GF
from src import game_variables as GV
from src import logs
from src import settings as sett


from src.settings import WIDTH, HEIGHT, clock, FPS
from src.blob import spawn_blobs, check_all_collisions, update_all, push_all
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

def init_userevent():
    pygame.time.set_timer(GV.NEXT_TILES, 5000)


def main():

    #init_userevent()

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

                if event.key == K_RETURN:
                    pass

                if event.key == K_SPACE:
                    spawned = spawn_blobs(GV.blob1, 4)
                    GV.all_blobs += spawned

                    GV.blob1.SHOW = False

                if event.key == K_l:
                    logs.print_logs(logs.LOG_FILE)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

        GV.blob1.shrink(30/FPS)
        check_all_collisions(GV.all_blobs)
        update_all(GV.all_blobs)

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()



main()



