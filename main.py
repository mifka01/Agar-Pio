import pygame as pg
from settings import *
from sprites import * 

class Game():
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        pg.font.init()
        self.clock = pg.time.Clock()
        self.mixer = pg.mixer.init()
        self.font = pg.font.Font(pg.font.get_default_font(), 40)
        self.running = True
        self.playing = False
        self.food = []
        
        
    
    def new(self):
        self.player = Player(self, "1", WIDTH/2, HEIGHT/2)
        
        for _ in range(0,1000):
            temp = Food(self, random.choice(range(-WIDTH,WIDTH*2)),random.choice(range(-HEIGHT,HEIGHT*2)))
            self.food.append(temp)
        self.playing = True

    def reset(self):
        self.player = None
        self.food = []

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
    def update(self):
        pg.display.update()
        
    def draw(self):
        self.screen.fill((255,255,255))
        for food in self.food:
            food.draw(WIDTH /2 - food.pos.x,HEIGHT /2- food.pos.y)
            food.update()
            self.player.eat(food)
        self.player.draw(self.player.pos.x, self.player.pos.y)
         
    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.draw()
            self.update()
            self.events()
                

    def quit(self):
        if self.playing:
            self.playing = False
        self.running = False
        pg.quit()
        exit()

g = Game()
g.new()
while g.running:
    g.run()
g.quit()