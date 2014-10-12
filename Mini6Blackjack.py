#!/usr/bin/env python

# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_list = []	# create Hand object

    def __str__(self):
        # return a string representation of a hand
        hand_string = "Hand contains "
        for i in range(len(self.hand_list)):
            hand_string += str(self.hand_list[i]) + ' '
        return hand_string
    
    def add_card(self, card):
        # add a card object to a hand
        self.hand_list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_sum = 0
        ace_count = 0
        for i in range(len(self.hand_list)):
            temp = self.hand_list[i].get_rank()
            if temp == 'A':
                ace_count += 1
            hand_sum += VALUES[temp]
            
        if ace_count == 1 and hand_sum + 10 <= 21:
            hand_sum += 10
        
        return hand_sum
        
        
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.hand_list)):
            pos[0] = i*80 + 20
            self.hand_list[i].draw(canvas, pos)
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = [Card(i, j) for i in SUITS for j in RANKS]

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        deck_string = "Deck contains "
        for i in range(len(self.deck)):
            deck_string += str(self.deck[i]) + ' '
        return deck_string


#define event handlers for buttons
def deal():
    global outcome, in_play, current_deck
    global dealer_hand, player_hand, score
    
    outcome = "Hit or Stand?"
    
    if in_play == True:
        outcome = "You lose the last round! Hit or Stand?"
        print outcome
        score -= 1
    
    # restart the game by dealing 2 cards to each person
    current_deck = Deck()
    current_deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    # deal 2 cards to both the dealer and the player
    dealer_hand.add_card(current_deck.deal_card())
    dealer_hand.add_card(current_deck.deal_card())
    player_hand.add_card(current_deck.deal_card())
    player_hand.add_card(current_deck.deal_card())
    print "The dealer " + str(dealer_hand)
    print "The player " + str(player_hand)
    
    in_play = True

def hit():
    # replace with your code below
    global outcome, in_play, current_deck
    global dealer_hand, player_hand, score
    
    # if the hand is in play, hit the player
    if in_play == True and player_hand.get_value() <= 21:
        player_hand.add_card(current_deck.deal_card())
        print "The player " + str(player_hand)
        # if busted, assign a message to outcome, update in_play and score
        if player_hand.get_value() > 21:
            outcome = "You have busted!"
            print outcome
            score -= 1
            in_play = False
        
def stand():
    # replace with your code below
    global outcome, in_play, current_deck
    global dealer_hand, player_hand, score
    
    if in_play == False:
        outcome = "Deal to play again!"  
        print outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(current_deck.deal_card())
        
        print "The dealer " + str(dealer_hand)
        # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() > 21:
            outcome = "You win!"
            print outcome
            in_play = False
            score += 1
        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                outcome = "You lose!"
                print outcome
                in_play = False
                score -= 1
            else:
                outcome = "You win!"
                print outcome
                in_play = False
                score += 1
        
# intialize for draw handler
dealer_hand = Hand()
player_hand = Hand()
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    player_pos = [20, 350]
    dealer_pos = [20, 140]
    player_hand.draw(canvas, player_pos)
    dealer_hand.draw(canvas, dealer_pos)
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                          [dealer_pos[0] - CARD_BACK_CENTER[0] - 9, dealer_pos[1] + CARD_BACK_CENTER[1]], 
                          CARD_BACK_SIZE)
    
    # draw Blackjack text
    canvas.draw_text('BLACKJACK', (30, 50), 36, 'Black', 'monospace')
    
    # draw outcome
    canvas.draw_text(outcome, (200, 100), 24, 'White')
    canvas.draw_text("score: " + str(score), (400, 40), 24, 'Yellow')
    canvas.draw_text("Dealer", (20, 120), 24, 'White')
    canvas.draw_text("Player", (20, 330), 24, 'White')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
