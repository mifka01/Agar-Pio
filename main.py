import pygame as pg
import random
from pygame.locals import QUIT, KEYDOWN, K_w, K_SPACE
from settings import WIDTH, HEIGHT, TITLE, FPS 
from math import sqrt, pi
from food import Food
from player import Player
from camera import Camera


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
        self.tick_count = 0
        self.camera = Camera()

    def new(self):
        self.player = Player(self, WIDTH/2, HEIGHT/2)
        
        self.playing = True

    def reset(self):
        self.player = None
        self.food = []

    def events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.player.split()
                if event.key == K_w:
                    self.player.feed()

    def generate_food(self, amount: int):
        for _ in range(0, amount):
            temp = Food(self, random.choice(range(-WIDTH, WIDTH*2)),
                        random.choice(range(-HEIGHT, HEIGHT*2)))
            self.food.append(temp)
    def update(self):
        pg.display.update()

    def draw(self):
        self.screen.fill((255, 255, 255))
        for food in self.food:
            food.draw(WIDTH / 2 - food.pos.x, HEIGHT / 2 - food.pos.y)
            food.update()
            for ball in self.player.balls:
                ball.eat(food)
        for ball in self.player.balls:
            ball.draw()
            

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.camera.zoom = 100/(self.player.radius)+0.3
            self.camera.centre(self.player)
            self.events()
            self.draw()
            if self.tick_count % 40 == 0:
                for ball in self.player.balls:
                    ball.loss()
                    
            if self.tick_count % 1000 == 0:
                area_sum = self.player.area
                for ball in self.player.balls[1:]:
                    area_sum += ball.area
                    self.player.balls.remove(ball)
                self.player.set_radius(sqrt(area_sum / pi))

            # 18 000 == 5 min (5x60x60)
            if self.tick_count % 6000 == 0:
                self.generate_food(1000)

            self.tick_count += 1
            self.update()

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
