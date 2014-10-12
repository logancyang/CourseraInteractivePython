#!/usr/bin/env python

# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

# global state

result = 1
iteration = 0
max_iterations = 100
list1 = []
# helper functions

def init(start):
    """Initializes n."""
    global result
    result = start
    print "Input is", result
    
def get_next(current):
    """???  Part of mystery computation."""
    if current%2 == 0:
        return current/2
    else:
        return current*3 + 1
    

# timer callback

def update():
    """???  Part of mystery computation."""
    global iteration, result, list1
    iteration += 1
    
    # Stop iterating after max_iterations
    if iteration >= max_iterations or result == 1:
        timer.stop()
        print "Output is", result
        print list1
        print max(list1)
    else:
        result = get_next(result)
        # print "time",iteration,":",result
        list1.append(result)

# register event handlers

timer = simplegui.create_timer(10, update)

# start program
init(217)
timer.start()

# this won't print the list1 after the timer updates
# it only prints the initial empty list1

# print list1
