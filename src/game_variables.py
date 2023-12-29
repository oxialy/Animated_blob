from src import drawing_variables as DV
from src import game_functions as GF
from src import settings as sett
from src import msc

from .drawing_variables import colors
from .settings import WIDTH, HEIGHT
from .blob import Blob


import pygame

all_blobs = []

blob1 = Blob((300,300), 50)

all_blobs = [blob1]


SPAWNBLOB = pygame.USEREVENT

START_EVENT = {
    SPAWNBLOB: {'timer': 200}
}

questions = [
    {'title': 1, 'answers': [1,2,3]},
    {'title': 2, 'answers': [1,2,3]},
    {'title': 3, 'answers': [1,2,3]}
]






