import sys
import os

def get_queue_length_from_file(filename):
    filename = os.path.join(sys.path[0], filename)
    with open(filename, 'r') as file_pointer:
        contents = file_pointer.read()
    return int(contents)

number = get_queue_length_from_file('queue3.txt')
print(number)