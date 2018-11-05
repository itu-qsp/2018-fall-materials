# Make sure that your program produces the correct reply also when there are
# too many closing parentheses

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
elif parentheses > 0:
    print("Looks like you forgot to close some parenthesis...")
else:
    print("You are closing a parenthesis without opening one...")    
