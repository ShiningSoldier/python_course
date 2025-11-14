import game_data

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = game_data.values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit