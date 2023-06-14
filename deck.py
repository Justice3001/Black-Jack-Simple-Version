from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
