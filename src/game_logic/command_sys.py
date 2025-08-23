from functools import wraps

def input_valid(func):
    @wraps(func)
    def wrapper():
        input = func()
        if not input.isdigit():
            if input == "quit":
                return input
            else:
                raise ValueError("Invalid input! Please insert a number.")
        else:
            input = int(input)
            if not (1 <= input <= 100):
                raise ValueError("Out of range! Please insert a number between 1 and 100.")
            else:
                return input
    return wrapper

@input_valid
def init():
    inp = input("I have a number between 1 and 100. Can you guess it?: ")
    return inp

@input_valid
def get_num():
    inp = input("Take a new guess: ")
    return inp

#TODO:the prompts and feedback messages should be tidied up, linespace should be added
def give_feedback(a):
    feedback = ""
    if a:
        feedback = "You got it right, good job!"
    else:
        feedback = "Oops! Try again!"
    return feedback
