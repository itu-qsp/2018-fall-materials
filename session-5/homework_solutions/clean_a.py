# Mu may not want to open a file in the current directory so
# you may have to write out the full path and I've shown an
# example in as a comment. 

mad_libs = open('mad_libs.txt', 'r')
#mad_libs = open('/home/morten/Documents/qsp_2018autumn/qualification-seminar-2018-fall/session_5/homework_solutions/mad_libs.txt', 'r')
mad_string = mad_libs.read()
mad_libs.close()
mad_words = mad_string.split()

for index, word in enumerate(mad_words): 
    if 'ADJECTIVE' in word:
        new_word = input("Enter an adjective:\n")
        mad_words[index] = mad_words[index].replace('ADJECTIVE', new_word)
    if 'NOUN' in word:
        new_word = input("Enter a noun:\n")
        mad_words[index] = mad_words[index].replace('NOUN', new_word)
    if 'ADVERB' in word:
        new_word = input("Enter an adverb:\n")
        mad_words[index] = mad_words[index].replace('ADVERB', new_word)
    if 'VERB' in word:
        new_word = input("Enter a verb:\n")
        mad_words[index] = mad_words[index].replace('VERB', new_word)

new_string = ' '.join(mad_words)
print(new_string)
new_libs = open('new_libs.txt', 'w')
#new_libs = open('/home/morten/Documents/qsp_2018autumn/qualification-seminar-2018-fall/session_5/homework_solutions/new_libs.txt', 'w')
new_libs.write(new_string)
new_libs.close()
