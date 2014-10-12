#!/usr/bin/env python

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import math
import simplegui

# initialize global variables used in your code
num_range = 100
answer = 0
count = 0

# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    global answer, count
    answer = random.randrange(0,num_range)
    
    # reset count
    count = 0
    max_guess = math.ceil(math.log(num_range + 1, 2))
    max_guess = int(max_guess)
    print ""
    print "New game, range is from", 0, "to", num_range
    print "Number of remaining guesses is", max_guess - count

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100 
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000   
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global answer, count
    guess = int(guess)
    max_guess = math.ceil(math.log(num_range + 1, 2))
    max_guess = int(max_guess)
    count += 1
    
    if count < max_guess:
        if guess < answer:
            print ""
            print "Guess was",guess
            print "Number of remaining guesses is", max_guess - count
            print "Higher!"
        elif guess > answer:
            print ""
            print "Guess was",guess
            print "Number of remaining guesses is", max_guess - count
            print "Lower!"
        else:
            print ""
            print "Guess was",guess
            print "Number of remaining guesses is", max_guess - count
            print "You win! The answer is", guess
            new_game()
    else:
        print ""
        print "Guess was",guess
        print "Out of guesses. You lose!"
        new_game()

    

    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess:", input_guess, 200)


# call new_game and start frame
new_game()
f.start()

# always remember to check your completed program against the grading rubric