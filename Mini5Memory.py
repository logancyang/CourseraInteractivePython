#!/usr/bin/env python

# implementation of card game - Memory

import simplegui
import random

print "Game starts"
card_pair = [0,0]
    
# helper function to initialize globals
def new_game():
    global lst, state, exposed, turns
    state = 0
    turns = 0
    lst1 = range(8)
    lst2 = range(8)
    lst = lst1 + lst2
    random.shuffle(lst)
    
    label.set_text('Turns = ' + str(turns))
    exposed = []
    for i in range(len(lst)):
        exposed.append(False)

def card_clicked(coordinate):
    return coordinate[0]//50

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, turns, card_pair
    idx = card_clicked(pos)
    
    # check if clicking on an exposed card, if yes, do nothing
    if not exposed[idx]:
        exposed[idx] = True
        if state == 0:
            state = 1
            card_pair[0] = card_clicked(pos)
            #print card_pair[0]
            #print "state = ", state
            #print "turns = ", turns
        elif state == 1:
            state = 2
            card_pair[1] = card_clicked(pos)
            turns += 1
            label.set_text('Turns = ' + str(turns))
            #print card_pair[1]
            #print "state = ", state
            #print "turns = ", turns
        else:
            # state 2, test if the previous 2 cards match
            state = 1
            
            #print card_pair
            #print "l1 = ", lst[card_pair[0]]
            #print "l2 = ", lst[card_pair[1]]
            if lst[card_pair[0]] == lst[card_pair[1]]:
                exposed[card_pair[0]] = True
                exposed[card_pair[1]] = True
            else:
                exposed[card_pair[0]] = False
                exposed[card_pair[1]] = False
            card_pair[0] = card_clicked(pos)
        
            #print "state = ", state
            #print "turns = ", turns
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global state, exposed
    pos = 1
    for num in lst:
        canvas.draw_text(str(num),[pos*50 - 30, 55], 25,
                         'White')
        pos += 1
    
    for i, j in enumerate(exposed):
        if not j:
            canvas.draw_line([50*i+25, 0], [50*i+25, 100],
                            45, 'Green')
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric