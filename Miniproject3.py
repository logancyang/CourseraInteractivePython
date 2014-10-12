#!/usr/bin/env python

# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
position = [85, 110]
num_success = 0
num_stop = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t%600 == 0:
        return str(t/600)+":00.0"
    elif t%600 < 10:
        return str(t/600)+":00."+str((t%600)%10)
    elif t%600 >= 10 and t%600 < 100:
        return str(t/600)+":0"+str((t%600)/10)+"."+str((t%600)%10)
    else:
        return str(t/600)+":"+str((t%600)/10)+"."+str((t%600)%10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True

def stop():
    global num_stop, num_success, counter, running
    timer.stop()
    if running == False:
        return
    num_stop += 1
    if counter%10 == 0:
        num_success += 1
    running = False

def reset():
    global counter, num_stop, num_success
    timer.stop()
    counter = 0
    num_stop = 0
    num_success = 0

def tick():
    global counter
    counter += 1


# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, tick)

# define draw handler
def draw(canvas):
    canvas.draw_text(format(counter), position, 36, "White")
    canvas.draw_text(str(num_success)+"/"+str(num_stop),
                     [200, 30], 26, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch",250,200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 150)
frame.add_button("Stop", stop, 150)
frame.add_button("Reset", reset, 150)


# start frame
frame.start()


# Please remember to review the grading rubric