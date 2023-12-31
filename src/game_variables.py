from src import drawing_variables as DV
from src import game_functions as GF
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import WIDTH, HEIGHT
from .blob import Blob


import pygame


pos = 300, 300

blob1 = Blob(pos, 35)
blob1.type = 1
blob0 = Blob(pos, 20)
blob0.type = 0
blob0.SHOW = False

all_blobs = [blob1, blob0]
all_holes = []

SPAWNBLOB = pygame.USEREVENT

START_EVENT = {
    SPAWNBLOB: {'timer': 470}
}

questions = [
    {'title': 1, 'answers': [1,2,3]},
    {'title': 2, 'answers': [1,2,3]},
    {'title': 3, 'answers': [1,2,3]}
]






