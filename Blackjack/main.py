"""
Blackjack Game

A command-line Blackjack game built in Python using object-oriented
programming principles. The game simulates standard Blackjack rules,
allowing a player to hit or stand against a dealer while tracking hand
values, blackjacks, and busts.

Author: Mal
"""

import random

class Card:
    """
    Represents a single playing card.

    Each card has a suit (spades, clubs, hearts, diamonds)
    and a rank with an associated Blackjack value.
    """
    def __init__(self, suit, rank):
        """
    Initializes a card with a suit and rank.

    :param suit: String representing the card suit
    :param rank: Dictionary containing card rank and value
    """
        self.suit = suit
        self.rank = rank
    def __str__(self):
        """
    Returns a readable string representation of the card.

    Example: 'A of Spades'
    """
        return f"{self.rank['rank']} of {self.suit.title()}"

class Deck:
    """
    Represents a standard 52-card deck.

    Handles deck creation, shuffling, and dealing cards.
    """
    def __init__(self):
        """
    Initializes a full deck of 52 playing cards.
    """
        self.cards = []
        suits = ['spades',  'clubs', 'hearts', 'diamonds']
        ranks = [
                {"rank" : "A", "value" : 11},
                {"rank" : "2", "value" : 2},
                {"rank" : "3", "value" : 3},
                {"rank" : "4", "value" : 4},
                {"rank" : "5", "value" : 5},
                {"rank" : "6", "value" : 6},
                {"rank" : "7", "value" : 7},
                {"rank" : "8", "value" : 8},
                {"rank" : "9", "value" : 9},
                {"rank" : "10", "value" : 10},
                {"rank" : "J", "value" : 10},
                {"rank" : "Q", "value" : 10},
                {"rank" : "K", "value" : 10}
                ]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """
    Randomly shuffles the deck if it contains more than one card.
    """
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        """
    Removes and returns a specified number of cards from the deck.

    :param number: Integer number of cards to deal
    :return: List of Card objects
    """
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

class Hand:
    """
    Represents a Blackjack hand.

    Stores cards, calculates hand value, and determines
    Blackjack conditions. Can represent either a player or dealer hand.
    """
    def __init__(self, dealer=False):
        """
    Initializes an empty hand.

    :param dealer: Boolean indicating if this is the dealer's hand
    """
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        """
    Adds one or more cards to the hand.

    :param card_list: List of Card objects
    """
        self.cards.extend(card_list)

    def calc_value(self):
        """
    Calculates the total value of the hand.

    Handles Ace value adjustment (11 or 1) to prevent busting.
    """
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank['rank'] == 'A':
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        """
    Returns the current total value of the hand.

    :return: Integer hand value
    """
        self.calc_value()
        return self.value

    def is_blackjack(self):
        """
    Checks if the hand is a Blackjack (value of 21).

    :return: Boolean
    """
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        """
    Displays the hand to the console.

    Dealer's first card remains hidden unless explicitly revealed.

    :param show_all_dealer_cards: Boolean to reveal dealer's full hand
    """
        print(f'''{"Dealer's" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
            and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)


        if not self.dealer:
            print("Value:", self.get_value())
        print()

class Game:
    """
    Controls the overall flow of the Blackjack game.

    Handles player input, dealer logic, game rounds,
    and win condition evaluation.
    """
    def play(self):
        def play(self):
            """
    Starts and manages the Blackjack game loop.

    Handles deck setup, card dealing, player decisions,
    dealer actions, and game results across multiple rounds.
    """
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games would you like to play?: "))
            except:
                print("Must enter a number.")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f'''Game {game_number} of {games_to_play}!''')
            print('*' * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                choice = input("Please choose 'Hit' or 'Stand' (H/S): ").lower()
                print()

                if choice in ['h', 'hit',]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
                elif choice in ['stand', 's']:
                    break
                else:
                    print("Invalid choice. Please enter Hit or Stand.")

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("your hand:", player_hand_value)
            print("dealer hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing!")

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        """
    Determines the outcome of the game.

    Evaluates busts, blackjacks, ties, and final hand comparisons.

    :param player_hand: Hand object for the player
    :param dealer_hand: Hand object for the dealer
    :param game_over: Boolean indicating final evaluation phase
    :return: Boolean indicating whether the round has ended
    """
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted! Dealer wins.")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted! You win.")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Double 21? A push if I have ever seen one!")
                return True
            elif player_hand.is_blackjack():
                print("That there is a blackjack! You win.")
                return True
            elif dealer_hand.is_blackjack():
                print("That there is a blackjack..but for the Dealer! Dealer win.")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("You tied! Even money.")
            else:
                print("Dealer win..you lose!")
            return True
        return False

g = Game()
g.play()
