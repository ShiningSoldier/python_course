import game_data
import card
import random

class Deck:
    def __init__(self):
        self.all_cards = self.create_deck()

    def create_deck(self):
        deck = []
        for suit in game_data.suits:
            for rank in game_data.ranks:
                created_card = card.Card(suit, rank)
                deck.append(created_card)
        return deck
    
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()