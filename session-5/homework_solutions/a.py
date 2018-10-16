# The assignment is not that explicit so the first thing to 
# do is reflect on what needs to be done.

# The contents of file needs to be read. Like in the counting
# words exercise I need to check if some words are equal to 
# something specific... So I want the contents of the file as 
# a string, split the string into a list of words and then 
# do a for loop through the words and if some conditional is 
# True then ask for input. Put the input into the list. 
# To put the input into the list I need the index of the current
# word. So maybe I should do a while loop instead. 
# Afterwards I join the list back to a string, print it, and
# save it to a file. 

# But now that I think about it, I could skip the splitting and
# joining if I use .replace(). I could have a while loop that runs
# as long as the 'NOUN', 'ADJECTIVE', or 'VERB' are still in the 
# string. The problem is that .replace() replaces all instances 
# of the pattern with the substitution... I'll try the first
# method first and then maybe elaborate. 

# I've commented out the first attempts so you can see that it
# is a process and no-one gets it in the first try

# mad_libs = open('/home/morten/Documents/qsp_2018autumn/qualification-seminar-2018-fall/session_5/homework_solutions/mad_libs.txt', 'r')
# mad_string = mad_libs.read()
# mad_libs.close()
# mad_words = mad_string.split()
# index = 0
# while index < len(mad_words): #instead of while we could have used
# # a for loop over enumerate(mad_words) which give both index and word
#     word = mad_words[index]
#     if word == 'ADJECTIVE':
#         mad_words[index] = input("Enter an adjective:\n")
#     if word == 'NOUN':
#         mad_words[index] = input("Enter a noun:\n")
#     if word == 'ADVERB':
#         mad_words[index] = input("Enter an adverb:\n")
#     if word == 'VERB':
#         mad_words[index] = input("Enter a verb:\n")
#     index = index +1

# print(mad_words)
# Here I tested whether it worked with the code at that point.
# The problem was that VERB ends with a period so I have to take 
# that into account or I won't get those words. 

# mad_libs = open('/home/morten/Documents/qsp_2018autumn/qualification-seminar-2018-fall/session_5/homework_solutions/mad_libs.txt', 'r')
# mad_string = mad_libs.read()
# mad_libs.close()
# mad_words = mad_string.split()
# index = 0
# while index < len(mad_words): #instead of while we could have used
# # a for loop over enumerate(mad_words) which give both index and word
#     word = mad_words[index]
#     if word == 'ADJECTIVE' or word == 'ADJECTIVE.' or word == 'ADJECTIVE,':
#         mad_words[index] = input("Enter an adjective:\n")
#     if word == 'NOUN' or word == 'NOUN.' or word == 'NOUN,':
#         mad_words[index] = input("Enter a noun:\n")
#     if word == 'ADVERB' or word == 'ADVERB.' or word == 'ADVERB,':
#         mad_words[index] = input("Enter an adverb:\n")
#     if word == 'VERB' or word == 'VERB.' or word == 'VERB,':
#         mad_words[index] = input("Enter a verb:\n")
#     index = index +1

# print(mad_words)

# This is better but I am overwriting the punctuation now. I should 
# use .replace() instead

mad_libs = open('mad_libs.txt', 'r')
#mad_libs = open('/home/morten/Documents/qsp_2018autumn/qualification-seminar-2018-fall/session_5/homework_solutions/mad_libs.txt', 'r')
mad_string = mad_libs.read()
mad_libs.close()
mad_words = mad_string.split()

# instead of while we could have used a for loop
# over enumerate(mad_words) which give both index and word
index = 0
while index < len(mad_words): 
    word = mad_words[index]
    if word == 'ADJECTIVE' or word == 'ADJECTIVE.' or word == 'ADJECTIVE,':
        new_word = input("Enter an adjective:\n")
        mad_words[index] = mad_words[index].replace('ADJECTIVE', new_word)
    if word == 'NOUN' or word == 'NOUN.' or word == 'NOUN,':
        new_word = input("Enter a noun:\n")
        mad_words[index] = mad_words[index].replace('NOUN', new_word)
    if word == 'ADVERB' or word == 'ADVERB.' or word == 'ADVERB,':
        new_word = input("Enter an adverb:\n")
        mad_words[index] = mad_words[index].replace('ADVERB', new_word)
    if word == 'VERB' or word == 'VERB.' or word == 'VERB,':
        new_word = input("Enter a verb:\n")
        mad_words[index] = mad_words[index].replace('VERB', new_word)
    index = index +1

# print(mad_words)
# This is pretty good. Let's do the printing and writing into a file.
new_string = ' '.join(mad_words)
print(new_string)
new_libs = open('new_libs.txt', 'w')
#new_libs = open('/home/morten/Documents/qsp_2018autumn/qualification-seminar-2018-fall/session_5/homework_solutions/new_libs.txt', 'w')
new_libs.write(new_string)
new_libs.close()

# This works hurrah! 
# We could pretty it up by replacing the if statements like
# if word == 'VERB' or word == 'VERB.' or word == 'VERB,':
# with simpler ones like 
# if 'VERB' in word:
# because that will check if the series of characters VERB are
# anywhere in the series of characters held in the variable word