from random import choice
from itu_queue import Queue
from us_names import SURNAMES, FEMALE_NAMES, MALE_NAMES
import time
import sys
import os

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
        print()
        busy = False


def get_queue_length_from_file(filename):
    filename = os.path.join(sys.path[0], filename)
    with open(filename, 'r') as file_pointer:
        contents = file_pointer.read()
    return int(contents)

def run_simulation():

    ismejeriet = Queue()
    amount_of_customers = get_queue_length_from_file('queue1.txt')
    # Let's say we have 10 customers queueing
    for customer in range(amount_of_customers):
        customer_gender = choice(['female', 'male', 'unknown'])
        new_customer = Customer(customer_gender)
        ismejeriet.enqueue(new_customer)

    shop_assistant = ShopAssistant(2)

    while not ismejeriet.is_empty():
        customer = ismejeriet.dequeue()
        shop_assistant.serve_icecream_to(customer)
        print(f'{ismejeriet.size()} customers left in queue')


if __name__ == '__main__':
    run_simulation()