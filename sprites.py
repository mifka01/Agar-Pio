import pygame as pg
import random

class Food(pg.sprite.Sprite):
    def __init__(self, game: object, x: int, y: int):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.radius = random.choice(range(5,10))
        self.color = random.choice([(125,0,0),(0,0,125),(0,125,0)])
        self.image = pg.Surface((self.radius*2, self.radius*2))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x,y))
        self.rect.x = x
        self.rect.y = y
        
    
    def draw(self):
        pg.draw.circle(self.game.screen, self.color, (self.rect.x,self.rect.y), self.radius)

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
        pos = pg.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.move()

    
    


