import pygame as pg
import random
from settings import *
from math import *

class Food():
    
    def __init__(self, game: object, x: int, y: int):
        self.game = game
        self.radius = 5
        self.area = int(pi * self.radius **2)
        self.color = random.choice([(125,0,0),(0,0,125),(0,125,0)])
        self.pos = pg.math.Vector2(x, y)
        self.width = self.radius *2
        self.height = self.radius *2
        self.speed = 5

    
    def draw(self, x:int, y: int):
        pg.draw.circle(self.game.screen, self.color, (int(x), int(y)), int(self.radius))

    def set_radius(self, radius: int):
        self.radius = ceil(radius)
        self.area = int(pi * self.radius)

    def get_radius(self):
        return self.radius

    def set_color(self, color: tuple):
        self.color = color
        
    def get_color(self):
        return self.color
    
    def move(self):
        mouse = pg.mouse.get_pos()
        vel = pg.math.Vector2(mouse[0] - WIDTH/2, mouse[1] - HEIGHT/2)
        vel.scale_to_length(self.speed)
        self.pos += vel
                                    
    def update(self):
        self.move()

class Player(Food):
    def __init__(self, game: object, name: str, x: int, y: int):
        super().__init__(game,x,y)
        self.radius = 10
        self.area = int(pi * self.radius **2)
        self.color = (0,0,0)
        self.pos = pg.math.Vector2(x, y)
        self.name = name
        

    def eat(self, food):     
        temp_pos = pg.Vector2(0,0)
        if temp_pos.distance_to(food.pos) < self.radius + food.radius:    
            if self.area > food.area:
                area_sum = self.area + food.area
                self.radius = sqrt(area_sum/ pi)
                self.area = int(pi * self.radius **2)
                self.game.food.remove(food)