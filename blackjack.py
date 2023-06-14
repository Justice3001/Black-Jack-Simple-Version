from card import Card
from deck import Deck
from hand import Hand

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.game_over = False

    def start_game(self):
        self.deck.create_deck()
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())

    def display_hands(self):
        player_score = self.player_hand.calculate_score()
        dealer_score = self.dealer_hand.calculate_score()

        print("Your cards:", ", ".join(str(card) for card in self.player_hand.cards), "Score:", player_score)
        print("Dealer's card:", self.dealer_hand.cards[0])
        print("Dealer's score:", dealer_score)
        print()

    def play_round(self):
        while not self.game_over:
            self.display_hands()
            player_score = self.player_hand.calculate_score()
            dealer_score = self.dealer_hand.calculate_score()

            if player_score == 21 or dealer_score == 21 or player_score > 21:
                self.game_over = True
            else:
                valid_input = False
                while not valid_input:
                    choice = input("Do you want to draw another card? Type 'y' or 'n': ")
                    if choice.isdigit():
                        print("Invalid input. Please enter 'y' or 'n'.")
                    elif choice.lower() in ["y", "n"]:
                        valid_input = True
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")

                if choice == "y":
                    self.player_hand.add_card(self.deck.deal_card())
                else:
                    self.game_over = True

        while dealer_score < 17 and dealer_score <= player_score and player_score <= 21:
            self.dealer_hand.add_card(self.deck.deal_card())
            dealer_score = self.dealer_hand.calculate_score()

        self.display_hands()
        self.display_result()

    def display_result(self):
        player_score = self.player_hand.calculate_score()
        dealer_score = self.dealer_hand.calculate_score()

        print("\nYour final hand:", ", ".join(str(card) for card in self.player_hand.cards), "Score:", player_score)
        print("Dealer's final hand:", ", ".join(str(card) for card in self.dealer_hand.cards), "Score:", dealer_score)
        print()

        if player_score > 21:
            print("You went over. You lose!")
        elif dealer_score > 21:
            print("Dealer went over. You win!")
        elif player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("You lose!")
        else:
            print("It's a draw!")
