from random import choice
from itu_queue import Queue
from us_names import SURNAMES, FEMALE_NAMES, MALE_NAMES
import time

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


class ShopAssistant():
    def __init__(self, speed):
        self.serving_speed = speed
        self.name = 'Doreen'
        self.busy = False
        
    def serve_icecream_to(self, customer):
        busy = True
        print("Hi, I'm " + self.name + ". What's your name?")
        name = customer.say_name()
        print("And what can I get for you today, " + name + "?")
        order = customer.choose_icecream()
        size_order = len(order)
        print(len(order), "scoops coming up")
        time.sleep(1.5 * size_order / self.serving_speed)
        print(', '.join(order) + ". Here you go " + name +".")
        busy = False

doreen = ShopAssistant(3)
doreen.serve_icecream_to(john_doe)