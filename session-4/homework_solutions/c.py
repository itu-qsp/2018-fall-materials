# Imagine you were to write a function called count_word_in_text
# that counts the occurrence of a single word from some text. 
# Write down a few lines about how you would break this down into 
# smaller problems. Think about this: what is the input? What is 
# the expected output? What things might you need to save in 
# variables as the program runs?

# Yay, pseudo-code! 

# I want to make a function. It looks for one word, in some text.
# So I want to input the word I'm looking for and the text. 
# It returns how many times the word is in the text.
# So I need a counter variable that starts at zero and increases 
# for each time the word is in the text. 
# I need to compare each word **of the text** to the word I am 
# looking for. 
# So if I can split the text into a list of the individual words
# than that would be great because I can then do a for loop for 
# the words of the text. 