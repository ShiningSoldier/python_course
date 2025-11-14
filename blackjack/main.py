from deck import Deck
from hand import Hand
from chips import Chips

class Gameplay:
    def __init__(self, deck, player, dealer, chips):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.chips = chips
        self.playing = True

    def take_bet(self):
        while True:
            try:
                self.chips.bet = int(input("How many chips would you like to bet? "))
            except ValueError:
                print("The amount should be an integer.")
                continue
            if self.chips.bet > self.chips.total:
                print(f"Not enough chips. You have {self.chips.total}")
            elif self.chips.bet <= 0:
                print("Bet must be positive.")
            else:
                break

    def player_hit(self):
        single_card = self.deck.deal()
        self.player.add_card(single_card)
        self.player.adjust_for_ace()

    def hit_or_stand(self):
        while True:
            x = input("Hit or stand? Enter h or s: ")
            if x and x[0].lower() == "h":
                self.player_hit()
            elif x and x[0].lower() == "s":
                print("Player stands! Dealer's turn!")
                self.playing = False
            else:
                print("Wrong input, please enter h or s.")
                continue
            break

    def show_some(self):
        print("\nDealer's hand:")
        print(" <card hidden>")
        print(f" {self.dealer.cards[1]}")

        print("\nPlayer's hand:")
        for card in self.player.cards:
            print(f" {card}")
        print(f"Value in player's hand is: {self.player.value}")

    def show_all(self):
        print("\nDealer's hand:")
        for card in self.dealer.cards:
            print(f" {card}")
        print(f"Value in dealer's hand is: {self.dealer.value}")

        print("\nPlayer's hand:")
        for card in self.player.cards:
            print(f" {card}")
        print(f"Value in player's hand is: {self.player.value}")

    def player_busts(self):
        print("Player busts!")
        self.chips.lose_bet()

    def player_wins(self):
        print("Player wins!")
        self.chips.win_bet()

    def dealer_busts(self):
        print("Dealer busted, player wins!")
        self.chips.win_bet()

    def dealer_wins(self):
        print("Dealer wins!")
        self.chips.lose_bet()

    def push(self):
        print("Tie! Push.")

    def game_loop(self):
        while True:
            print("\nWelcome to Blackjack!")

            self.deck = Deck()
            self.deck.shuffle()

            self.player = Hand()
            self.player.add_card(self.deck.deal())
            self.player.add_card(self.deck.deal())

            self.dealer = Hand()
            self.dealer.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

            self.playing = True

            self.take_bet()
            self.show_some()

            while self.playing:
                self.hit_or_stand()
                self.show_some()

                if self.player.value > 21:
                    self.player_busts()
                    break

            if self.player.value <= 21:
                while self.dealer.value < 17:
                    self.dealer.add_card(self.deck.deal())
                    self.dealer.adjust_for_ace()

                self.show_all()

                if self.dealer.value > 21:
                    self.dealer_busts()
                elif self.dealer.value > self.player.value:
                    self.dealer_wins()
                elif self.dealer.value < self.player.value:
                    self.player_wins()
                else:
                    self.push()

            print(f"\nPlayer chips total: {self.chips.total}")
            new_game = input("Would you like to play a new hand? (y/n): ")
            if not new_game or new_game[0].lower() != "y":
                print("Thanks for playing!")
                break


player_chips = Chips()

new_deck = Deck()
new_deck.shuffle()
new_player = Hand()
new_dealer = Hand()

game = Gameplay(new_deck, new_player, new_dealer, player_chips)
game.game_loop()
