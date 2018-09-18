
# Pseudo-code version
# The computer should print something to let the user know what's going on. Maybe "Hi! Think of a number from 1 to 10 and I'll guess it!"
# Then the program repeat it's behaviour so I need a loop
# inside the loop I want the computer to print it's guess and then ask for input, right or wrong?
# If the program has a variable with it's guess then it can update the variable to guess something new each time the loop repeats
# If the guess is right I want to program to say something about how awesome it is and exit 
# If the guess is wrong the loop should simply repeat
# The program could simply start by guessing 1 and then increase by one for each wrong guess

# If the number of guesses is limited then there should also be a counter in the loop and an additional check if the counter is higher than the number of guesses allowed (and break when it's over that number)

# If the computer should change it's strategy then maybe it could guess a random number from 1 to 10? If it had a list of the numbers from 1 to 10 then maybe it could even keep track of what it has already guessed.

# If the computer guesses wrong then it should ask if the number is higher or lower. If it's higher than all values lower than the guess should be discarded (maybe I can do this with list slicing?). If lower then discard those greater than. 

# simple solution
welcome = "Hi! Think of an integer from 1 to 10 and I'll try to guess it!"
print(welcome)
guess = 1
while True:
    guess_str = "Are you thinking of the number " + str(guess) + "[y/n]?"
    print(guess_str)
    was_i_right = input()
    if was_i_right == 'y':
        print("WOOOO BABY! I guessed your number!")
        break
    elif was_i_right == 'n':
        guess = guess +1
    else:
        print("y or n, please")

# limited guesses
welcome = "Hi! Think of an integer from 1 to 10 and I'll try to guess it!"
print(welcome)
guess = 1
counter = 0
while counter < 4:
    counter = counter +1
    guess_str = "Are you thinking of the number " + str(guess) + "[y/n]?"
    print(guess_str)
    was_i_right = input()
    if was_i_right == 'y':
        print("WOOOO BABY! I guessed your number!")
        break
    elif was_i_right == 'n':
        guess = guess +1
    else:
        print("y or n, please")
if counter == 4:
    print("Bored now")

# random order
import random
welcome = "Hi! Think of an integer from 1 to 10 and I'll try to guess it!"
print(welcome)
guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
while counter < 4:
    counter = counter +1
    random_list_index = random.randint(0, len(guesses) -1)
    guess = guesses.pop(random_list_index)
    guess_str = "Are you thinking of the number " + str(guess) + "[y/n]?"
    print(guess_str)
    was_i_right = input()
    if was_i_right == 'y':
        print("WOOOO BABY! I guessed your number!")
        break
    elif was_i_right == 'n':
        pass
    else:
        print("y or n, please")
if counter == 4:
    print("Bored now")

# higher or lower
import random
welcome = "Hi! Think of an integer from 1 to 10 and I'll try to guess it!"
print(welcome)
guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
while counter < 4:
    counter = counter +1
    random_list_index = random.randint(0, len(guesses) -1)
    guess = guesses[random_list_index]
    guess_str = "Are you thinking of the number " + str(guess) + "[y/n]?"
    print(guess_str)
    was_i_right = input()
    if was_i_right == 'y':
        print("WOOOO BABY! I guessed your number!")
        break
    elif was_i_right == 'n':
        higher_lower = input("Okay, is your number [higher] or [lower]?")
        if higher_lower == 'higher':
            guesses = guesses[random_list_index+1:len(guesses)]
        elif higher_lower == 'lower':
            guesses = guesses[0:random_list_index]
        else:
            print("Well, that wasn't helpful")
            guesses.pop(random_list_index)
    else:
        print("y or n, please")
if counter == 4:
    print("Bored now")

# debugging: random_list_index = 3, guess = 4, higher guesses[4:10] ([5, 6, 7, 8, 9, 10]), lower guesses[0:3] ([[1, 2, 3])