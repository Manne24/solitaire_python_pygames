import pygame
import random
from settings import *


class Game:
    def __init__(self):
        # initialize game window

        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = True
        self.running = True
        pygame.display.set_caption(TITLE)
        icon = pygame.image.load(ICON)
        pygame.display.set_icon(icon)

    def new(self):
        self.all_sprites = pygame.sprite.Group()

    def run(self):
        # Game Loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()

    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop - Draw
        self.window.fill(GREEN)
        self.all_sprites.draw(self.window)
        pygame.display.update()


game = Game()

while game.running:
    game.new()
    game.run()
pygame.quit()
