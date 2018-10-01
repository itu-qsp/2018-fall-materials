# So here you should first try to paste the line (line 9) that is commented out
# inside the cli_program.py into your command line, in the folder where you have
# saved the file (check current folder with pwd and contents with ls). This 
# should return something like this in your command interface window:

# My dog looks weirdly.\nThe neighbours dog too...\n

# if you get an error message then inspect the error message. 
# The command suggested in the file probably supposes that the file is called
# cli_replace.py and not cli_program.py 

# So, after further inspection you should discover that the program takes the
# output of echo (which is the same string as the one input), and in the example this is 
# "My cat looks weirdly.\nThe neighbours cat too...\n" as an input. It also 
# takes the two strings after the name of the python file as arguments. It then swaps all
# incidens of the first argument, with the second in the string. In other words;
# the string get returned, where the word cat is replaced by dog.

# -- What does sys.argv[1] mean?
# It gives you the first argument after the filename, when provided/run from the
# command line. Where sys.argv is a list with the filename as first element and
# what is written after in the command line as following elements.

# -- What does for line in sys.stdin mean?
# stdin is used for all interactive input (it is similar to the function ìnput()
# that you know from earlier). In this program the input is the string
# "My cat looks weirdly.\nThe neighbours cat too...\n" from the program echo
# for line in sys.stdin means that it takes the input, and read it line for line
# (in the example you only have one line though, but you can do the same for
# a whole book or documents when you want to do something with it, line by line).

# -- What does line.replace(...) mean?
# The function (method actually but you'll learn about the difference later) 
# takes the string in the variable called line and looks for the first 
# argument (which is saved in sys.argv[1]) and replaces 
# it with the second argument (which is saved in sys.argv[2]) 