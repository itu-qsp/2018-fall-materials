# There's a function. It takes a string as input and returns the same string
# but with " really" added onto the end. 
# Then there are five variables where the first is a string, the second and third
# contain the result returned from the function. The fourth variable is going to
# contain the same as the third because Jens is being tricky. 
# In the fifth variable " like icecream" is getting concatenated onto the string.
# So the first print will be 
# I really really
# and the second print will be 
# I really really like icecream

# The line `augmented_string = input_string + " really"` is run three times

# second_variable == "I really"

def augment(input_string):
    augmented_string = input_string + " really"
    return augmented_string
    
initial_variable = "I"
second_variable = augment(initial_variable)
third_variable = augment(second_variable)
print(third_variable)
fourth_variable = augment(second_variable)
fifth_variable = fourth_variable + " like icecream"
print(fifth_variable)