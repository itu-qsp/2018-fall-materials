from turtle import *

angle = 170
movement = 200
number_of_moves = 36
while number_of_moves > 0:
    forward(movement)
    left(angle)
    number_of_moves -= 1
