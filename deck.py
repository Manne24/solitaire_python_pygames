from card import *
from settings import *
import os
import pygame


class Deck:
    def __init__(self, card_image={}):
        self.cards = []
        # self.image_size = pygame.transform.scale(self.card_image, (100, 150))
        self.card_image = card_image
        self.create()

    def create(self):
        for suit in ("hearts", "spades", "clubs", "diamonds"):
            for value in (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"):
                card_image = os.path.join(card_folder, f"{value}_of_{suit}.png")
                self.card_image[card_image] = pygame.image.load(card_image).convert()
                self.cards.append(Card(value, suit, card_image))
