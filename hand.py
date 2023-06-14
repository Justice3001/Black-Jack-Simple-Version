from card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_score(self):
        score = sum([int(card.rank) if card.rank.isdigit() else 10 for card in self.cards])
        if any(card.rank == "A" for card in self.cards) and score <= 11:
            score += 10
        return score
