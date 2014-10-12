#!/usr/bin/env python

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0.0, 0.0]


paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == LEFT:
        ball_vel[0] = random.randrange(-240,-120)/60.0
        ball_vel[1] = random.randrange(-180,-60)/60.0
    else:
        ball_vel[0] = random.randrange(120,240)/60.0
        ball_vel[1] = random.randrange(-180,-60)/60.0

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    RandNum = random.randrange(1,3)
    if RandNum == 1:
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel
 
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Green", "White")
    
    # collide and reflect off of ceiling and the bottom
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    # test if the ball collides with the left gutter
    elif ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        # if hits no pad
        if paddle1_pos > ball_pos[1] + HALF_PAD_HEIGHT or paddle1_pos < ball_pos[1] - HALF_PAD_HEIGHT:
            spawn_ball(RIGHT)
            score2 += 1
        # if hits pad
        else:
            ball_vel[0] = - ball_vel[0]
            # velocity increases by 10% after every pad hit
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1
            
    # test if the ball collides with the right gutter
    elif ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS - PAD_WIDTH:
        # if hits no pad
        if paddle2_pos > ball_pos[1] + HALF_PAD_HEIGHT or paddle2_pos < ball_pos[1] - HALF_PAD_HEIGHT:
            spawn_ball(LEFT)
            score1 += 1
        # if hits pad
        else:
            ball_vel[0] = - ball_vel[0]
            # velocity increases by 10% after every pad hit
            ball_vel[0] = ball_vel[0] * 1.1
            ball_vel[1] = ball_vel[1] * 1.1

    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos >= HALF_PAD_HEIGHT and paddle1_pos <= HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    elif paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif paddle1_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    
    if paddle2_pos >= HALF_PAD_HEIGHT and paddle2_pos <= HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    elif paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif paddle2_pos > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
        
    # draw paddles
    # pad1 (left)
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], 
                     [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT],
                     PAD_WIDTH, 'White')
    # pad2 (right)
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 
                     [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], 
                     PAD_WIDTH, 'White')
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/2 - 50, 100), 50, 'Green')
    canvas.draw_text(str(score2), (WIDTH/2 + 50, 100), 50, 'Green')
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    acc = 10
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel = acc
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel = -acc
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = acc
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = -acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game)


# start frame
new_game()
frame.start()