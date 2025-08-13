import random

def rand_num_generator():
    return random.randint(0, 100)

def check_num(num_1, num_2):
    guess = False
    if num_1 == num_2:
        guess = True
    return guess
