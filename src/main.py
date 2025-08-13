from game_logic.num_generator import rand_num_generator, check_num
from game_logic.command_sys import get_num, give_feedback
from game_logic.hint import hint
from game_logic.scoring import Score

#making an instance of the Score class to handle scoring functionality
score = Score()
#using while loop as an "on" button
status = True
while status:
    #generating a number, getting a guess from the user, comparing these two 
    rand_num = rand_num_generator()
    print(rand_num)
    guess = get_num()
    result = check_num(rand_num, guess)
    #based on the result of the comparison scoring, feedback and hints to user is handled,
    # if the guess is correct the button turns off
    print(give_feedback(result))
    if not result:
        print(hint(rand_num, guess))
        score.wrong()
        # print(score.score)
        print(f"Your current score: {score.score}")
    if result:
        status = False
        print(f"Your final score: {score.score}")
