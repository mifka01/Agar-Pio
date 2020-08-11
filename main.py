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
        self.tick_count = 0
        self.food = []

    def new(self):
        self.player = Player(self, 500, 600)
        for _ in range(0,100):
            self.food.append(Food(self, random.choice(range(0,1080)),random.choice(range(0,1920))))
        self.playing = True

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def update(self):
        self.draw()
        self.player.update()
        pg.display.update()

    def draw(self):
        self.screen.fill((255,255,255))
        for food in self.food:
            food.draw()
        self.player.draw()
        
    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.update()
            self.tick_count += 1
            self.events()
            if self.tick_count % 60 == 0:
                pass

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