# Write a program paren_checker.py, which can check that parentheses in a Python program are balanced

# Write your command-line program paren_checker.py so that it receives
# a path to another Python program -the one to check- as a command-line argument

import sys

filename = sys.argv[1]

with open(filename) as file: 
    parentheses = 0 
    for line in file:
        for character in line:
            if character == '(':
                parentheses += 1
            if character == ')':
                parentheses -= 1
                
if parentheses == 0:
    print("I think all parenthesis are balanced.")
else:
    print("Looks like you forgot to close some parenthesis...")
