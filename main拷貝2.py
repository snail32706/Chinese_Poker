import random  
import numpy as np

suits_symbols = ['♠', '♦', '♥', '♣']
suits = ['C', 'D', 'H', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class Player(object):
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.groups = []
        self.score = 0


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + self.suit

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

