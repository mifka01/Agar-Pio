from os import path
import pygame as pg

# WINDOW SETTINGS
WIDTH = 1920
HEIGHT = 1080
TITLE = "Agar.Pio"

# GAME SETTINGS
FPS = 60
BASE_PLAYER_RADIUS = 20
BASE_FOOD_RADIUS = 7

NUMBER_OF_PLAYERS = 2
AMOUNT_OF_FOOD = 400
LENGHT_OF_GAME = 5 # minutes

#IMAGES 
BACKGROUND = pg.image.load(path.join('images','background.png'))