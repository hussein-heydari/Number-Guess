from game_logic.num_generator import rand_num_generator, check_num
from game_logic.command_sys import get_num, give_feedback, init
from game_logic.hint import hint
from game_logic.scoring import Score

#making an instance of the Score class to handle scoring functionality
score = Score()
#generating a random number
rand_num = rand_num_generator()

#a function take user inputs and handle ValueErrors raised by invalid inputs
def prompt(func):
    while True:
        try:
            guess = func()
            #this is in case the user tries to quit on the first command
            if guess == "quit":
                global status
                status = False
                return None
            break
        except ValueError as e:
            #handling inputs that can't be converted to integers
            if "literal" in str(e):
                print("Use a valid number.")
            else:
                print(f"{e}")
    return guess

#the program's switch
status = True
#getting the user's initial guess
guess = prompt(init)
#TODO: the command message should be different the very first time it pops
# compared to subsequent times in case of catching errors
#using a while loop as a switch
while status:
    #comparing the user's guess with the random number
    result = check_num(rand_num, guess)
    #if the latest guess is wrong a point is deducted from the score,
    #unless the score is already 1, in which case the game ends,
    #then feedback is given, a hint and the latest score are printed
    if not result:
        score.penalty()
        if not result and score.score == 1:
            print("Sorry, Game Over!")
            break
        print(give_feedback(result))
        print(hint(rand_num, guess))
        print(f"Your current score: {score.score}")
    #if the latest guess is correct feedback is given, the final score is printed,
    # the switch turns off and the program shuts down
    if result:
        print(give_feedback(result))
        print(f"Your final score: {score.score}")
        break
    #getting a new guess from the user in case the last guess was wrong
    guess = prompt(get_num)
