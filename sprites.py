import pygame as pg
import random
from logic import get_distance
from settings import *
import math

class Food():
    
    def __init__(self, game: object, x: int, y: int):
        self.game = game
        self.radius = random.choice(range(5,10))
        self.area = int(math.pi * self.radius)
        self.color = random.choice([(125,0,0),(0,0,125),(0,125,0)])
        self.pos = pg.math.Vector2(x, y)

    
    def draw(self, x:int, y: int):
        pg.draw.circle(self.game.screen, self.color, (int(x), int(y)), self.radius)

    def set_radius(self, radius: int):
        self.radius = math.ceil(radius)
        self.area = int(math.pi * self.radius)

    def get_radius(self):
        return self.radius

    def set_color(self, color: tuple):
        self.color = color
        
    def get_color(self):
        return self.color
    
    def move(self):
        mouse = pg.mouse.get_pos()
        vel = pg.math.Vector2(mouse[0] - WIDTH/2, mouse[1] - HEIGHT/2)
        vel.scale_to_length(5)
        self.pos += vel
                                    
    def update(self):
        self.move()


class Player(Food):
    def __init__(self, game: object, x: int, y: int):
        super().__init__(game,x,y)
        self.radius = 10
        self.area = int(math.pi * self.radius)
        self.color = (0,0,0)
        self.pos = pg.math.Vector2(x, y)
  
    def draw(self):
        pg.draw.circle(self.game.screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
    
    def update(self):
        self.eat()

    def eat(self):        
        temp_pos = self.pos - (WIDTH/2,HEIGHT/2)
        for food in self.game.food:
            if temp_pos.distance_to(food.pos) < self.radius + food.radius:
                if self.area > food.area:
                    area_sum = self.area + food.area
                    self.radius += math.ceil(math.sqrt(area_sum/ math.pi))
                    self.area = int(math.pi * self.radius)
                    self.game.food.remove(food)
    
    


