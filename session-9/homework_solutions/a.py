from random import choice
from itu_queue import Queue
from us_names import SURNAMES, FEMALE_NAMES, MALE_NAMES

class Customer():
    def __init__(self, gender):
        if gender == 'male':
            self.name = choice(MALE_NAMES) + ' ' + choice(SURNAMES)
        elif gender == 'female':
            self.name = choice(FEMALE_NAMES) + ' ' + choice(SURNAMES)
        else:
            self.name = 'Cookie Monster'
    
    def say_name(self):
        return self.name
    
    def choose_icecream(self):
        balls = choice([1, 2, 3, 4, 5])
        order = []
        flavs = ['Strawberry', 'Chocolate', 'Vanilla', 'Sea Buckthorn', 'Lime', 'Mango']
        for ball in range(balls):
            flavour = choice(flavs)
            flavs.remove(flavour)
            order.append(flavour)
        return order


john_doe = Customer('muppet')
print("I am", john_doe.say_name())
print("I want", john_doe.choose_icecream())