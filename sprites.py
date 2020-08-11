import pygame as pg
import random
from logic import get_distance
from settings import *

class Food():
    
    def __init__(self, game: object, x: int, y: int):
        self.game = game
        self.radius = random.choice(range(10,15))
        self.color = random.choice([(125,0,0),(0,0,125),(0,125,0)])
        self.x = x
        self.y = y
        self.speed = self.radius / 2
        
    
    def draw(self):
        pg.draw.circle(self.game.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def set_radius(self, radius: int):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_color(self, color: tuple):
        self.color = color
        
    def get_color(self):
        return self.color


class Player(Food):
    def __init__(self, game: object, x: int, y: int):
        super().__init__(game,x,y)
        self.radius = 20
        self.color = (0,0,0)

    def move(self):
        mouse = pg.mouse.get_pos()
        distance  = get_distance((mouse), (self.x, self.y))
        dx = mouse[0] - self.x
        dy = mouse[1] - self.y
        if  distance > self.radius /2:
            dx /= distance
            dy /= distance
            # speed-pixel vector in the same direction
            dx *= self.speed
            dy *= self.speed
            # And now we move:
            self.x += dx
            self.y += dy

    def eat(self):
        for food in self.game.food:
            if get_distance((self.x, self.y), (food.x, food.y)) <=self.radius:
                self.radius += abs(int(food.radius /10))
                self.game.food.remove(food)
    def update(self):
        self.move()
        self.eat()

    
    


