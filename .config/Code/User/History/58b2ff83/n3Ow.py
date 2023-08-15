#!/bin/bash

# this projet will simulate a galton board.
# to make it more basic, the balls will not collide with eachother,
# and we make the assumtion that it is a 50 50 probabilaty per peg to fall left or right.
# made by Berend Veldthuis

# imporst
from random import randint

# vars for board setup
total_balls = 100
depth_pegs = 5

# general vars
buckets = {}

# function definitions
def sim_ball(): # simulate a falling ball
    ball_value = 0
    for i in range(0, depth_pegs): # calculate the ball value for depth_pegs
        
        if bool(randint(0,1)): # add 1 when false (fall right) subtract 1 when false (fall left)
            ball_value = ball_value + 1
        else:
            ball_value = ball_value + -1
        
        try:
            buckets.


# main program
