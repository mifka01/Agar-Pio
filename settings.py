from os import path
import pygame as pg

pg.mixer.init()
# DISPLAY SETTINGS
WIDTH = 1920
HEIGHT = 1080

# GAME SETTINGS
TITLE = "Agar.Pio"
FPS = 60

BASE_PLAYER_RADIUS = 20
BASE_FOOD_RADIUS = 7


#IMAGES 
BACKGROUND = pg.image.load(path.join('images','background.png'))