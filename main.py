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
        self.tick_count = 0

    def new(self):
        self.player = Player(self, WIDTH/2, HEIGHT/2)
        for _ in range(0, 10):
            temp = Food(self, random.choice(range(-WIDTH, WIDTH*2)),
                        random.choice(range(-HEIGHT, HEIGHT*2)))
            self.food.append(temp)
        self.playing = True

    def reset(self):
        self.player = None
        self.food = []

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.split()
                if event.key == pg.K_w:
                    self.player.feed()

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
