import random

def create_deck():
    deck = []
    suits = ["♠", "♣", "♦", "♥"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop(0)

def calculate_score(hand):
    score = 0
    num_aces = 0
    for card in hand:
        rank = card[:-1]
        if rank.isdigit():
            score += int(rank)
        elif rank in ["J", "Q", "K"]:
            score += 10
        elif rank == "A":
            score += 11
            num_aces += 1

    while score > 21 and num_aces > 0:
        score -= 10
        num_aces -= 1

    return score

def play_game():
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    for _ in range(2):
        player_hand.append(deal_card(deck))
        dealer_hand.append(deal_card(deck))

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print("Your cards:", player_hand, "Score:", player_score)
        print("Dealer's card:", dealer_hand[0])

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Do you want to draw another card? Type 'y' or 'n': ")
            if should_continue == "y":
                player_hand.append(deal_card(deck))
            else:
                game_over = True

    while dealer_score < 17 and dealer_score <= player_score and player_score <= 21:
        dealer_hand.append(deal_card(deck))
        dealer_score = calculate_score(dealer_hand)

    print("\nYour final hand:", player_hand, "Score:", player_score)
    print("Dealer's final hand:", dealer_hand, "Score:", dealer_score)
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

play_game()
