def get_num():
    inp = int(input("I have a number between 1 and 100. Can you guess it?: "))
    return inp

def give_feedback(a):
    feedback = ""
    if a:
        feedback = "You got it right, good job!"
    else:
        feedback = "Oops! Try again!"
    return feedback
