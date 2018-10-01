# The difference between ingredients and ìngredient is that the first is a 
# list containing strings, while the latter is a string.

# There are two loops because you first want to run over the different lists
# contained inside the list_of_lists variable, then the string elements in each of the lists.

# How to write the same code using just one for-loop:

list_of_lists = [
    ['Gin', 'Vermouth', 'Campari', 'Orange peel'],
    ['White port', 'Tonic water'],
    ['Vodka', 'Triple sec', 'Cranberry juice', 'Lime juice'],
    ['Vodka', 'Tequila', 'Light rum', 'Triple sec', 'Gin', 'Cola'],
    ['Vodka', 'Tomato juice', 'Worcestershire sauce']] 

for ingredients in list_of_lists:
    print('For this drink I need the following ingredients:')
    print(', '.join(ingredients), end =', ')
    print('and that was it!\n')

# or alternately with two changes

for ingredients in list_of_lists:
    print('For this drink I need the following ingredients:')
    print(', '.join(ingredients) + ', and that was it!')
    print()