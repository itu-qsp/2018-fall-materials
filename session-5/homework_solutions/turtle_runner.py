# Let your program consume one argument from the command-line, which is a
# path to a script file.
# Let your program read such a script file line by line and let it split 
# each line's content on a space.
# Assign the two resulting elements to two variables
# command, value = line.split(' ')
# Convert the value in the variable called value into an int.
# Write a function def do_line(turtle, command, value):, 
# which lets a turtle object passed to the function do_line so what is given in
# For example, when the command is Walk the you shall call the turtles 
# forward method with the argument given in value.
# When the command is Turn the you shall call the turtles right method with
# the argument given in value.

import sys
from turtle import Turtle, done

def do_line(turtle, command, value):
    if command == 'Walk':o
        turtle.forward(value)
    if command == 'Turn':
        turtle.right(value)
    
def main(path_to_file):
    dave = Turtle()
    dave.shape("turtle")
    dave.shapesize(5, 5, 12)
    with open(path_to_file, 'r') as script:
        for line in script:
            command, value = line.split(' ')
            value = int(value)
            do_line(dave, command, value)

if __name__ == '__main__':
    main(sys.argv[1])
    done()