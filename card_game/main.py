from deck import Deck
from player import Player

CARDS_PER_PLAYER_DEFAULT = 26
CARDS_FOR_WAR_DEFAULT = 5

class Gameplay():
    player_one_cards = []
    player_two_cards = []

    def __init__(
            self,
            player_one,
            player_two,
            deck,
            cards_per_player = CARDS_PER_PLAYER_DEFAULT,
            cards_for_war = CARDS_FOR_WAR_DEFAULT
            ):
        self.player_one = player_one
        self.player_two = player_two
        self.deck = deck
        self.cards_per_player = cards_per_player
        self.cards_for_war = cards_for_war
        self.deck.shuffle_deck()
        self.deal_initial_hands()

    def deal_initial_hands(self):
        for x in range(self.cards_per_player):
            card_one = self.deck.deal_one()
            card_two = self.deck.deal_one()
            self.player_one.add_cards(card_one)
            self.player_two.add_cards(card_two)

    def gameplay_loop(self):
        game_on = True
        round_number = 0

        while game_on:
            round_number += 1
            print(f"Current round is {round_number}")

            player_won = self.check_player_won()
            if player_won:
                game_on = False
                break

            self.player_one_cards.append(self.player_one.remove_one())
            self.player_two_cards.append(self.player_two.remove_one())

            at_war = True

            while at_war:
                p1_value = self.player_one_cards[-1].value
                p2_value = self.player_two_cards[-1].value

                if p1_value > p2_value:
                    self.player_one.add_cards(self.player_one_cards)
                    self.player_one.add_cards(self.player_two_cards)

                    at_war = False

                elif p1_value < p2_value:
                    self.player_one.add_cards(self.player_one_cards)
                    self.player_one.add_cards(self.player_two_cards)

                    at_war = False

                else:
                    print("War!")

                    if len(self.player_one.all_cards) < self.cards_for_war:
                        print("Player two wins")
                        game_on = False
                        break
                    elif len(self.player_two.all_cards) < self.cards_for_war:
                        print("Player one wins")
                        game_on = False
                        break
                    else:
                        for num in range(self.cards_for_war):
                            self.player_one_cards.append(self.player_one.remove_one())
                            self.player_two_cards.append(self.player_two.remove_one())
                        

    def check_player_won(self):
        winner_name = ""
        loser_name = ""
        player_one_cards_amount = len(self.player_one.all_cards)
        player_two_cards_amount = len(self.player_two.all_cards)

        if player_one_cards_amount == 0:
            winner_name = self.player_two.name
            loser_name = self.player_one.name
        if player_two_cards_amount == 0:
            winner_name = self.player_one.name
            loser_name = self.player_two.name

        
        if len(winner_name) > 0:
            print(f"{loser_name} has no cards, {winner_name} has won!")
            return True
        
        return False



game = Gameplay(Player("Jimmy"), Player("Billy"), Deck())
game.gameplay_loop()