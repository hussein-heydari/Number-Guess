from game_logic.num_generator import rand_num_generator, check_num
from game_logic.command_sys import get_num, give_feedback, init
from game_logic.hint import hint
from game_logic.scoring import Score

#making an instance of the Score class to handle scoring functionality
score = Score()
#generating a random number
rand_num = rand_num_generator()
#getting the user's initial guess
guess = init()
#using a while loop as a switch
status = True
while status:
    #comparing the user's guess with the random number
    result = check_num(rand_num, guess)
    #based on the result of the comparison a feedback is given the the user
    print(give_feedback(result))
    if not result:
        #if the last guess is wrong a hint and a scoring penalty is implemented,
        # then the latest score is printed
        print(hint(rand_num, guess))
        score.penalty()
        print(f"Your current score: {score.score}")
    if result:
        #if the last guess is correct the switch turns off,
        # the final score is printed and the program shuts down
        status = False
        print(f"Your final score: {score.score}")
        break
    #getting a new guess from the user in case the last guess was wrong
    guess = get_num()
