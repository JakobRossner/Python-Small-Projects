#NUMBER GUESSING GAME

import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
custom_level_turns = 22
WELCOME_MESSAGE = """

 __      __     _                        _          _    _     _                         _                                         _                                      
 \ \    / /___ | | __  ___  _ __   ___  | |_  ___  | |_ | |_  (_) ___  _ _  _  _  _ __  | |__  ___  _ _   __ _  _  _  ___  ___ ___(_) _ _   __ _   __ _  __ _  _ __   ___ 
  \ \/\/ // -_)| |/ _|/ _ \| '  \ / -_) |  _|/ _ \ |  _|| ' \ | |(_-< | ' \| || || '  \ | '_ \/ -_)| '_| / _` || || |/ -_)(_-<(_-<| || ' \ / _` | / _` |/ _` || '  \ / -_)
   \_/\_/ \___||_|\__|\___/|_|_|_|\___|  \__|\___/  \__||_||_||_|/__/ |_||_|\_,_||_|_|_||_.__/\___||_|   \__, | \_,_|\___|/__//__/|_||_||_|\__, | \__, |\__,_||_|_|_|\___|
                                                                                                         |___/                             |___/  |___/                   

"""


#function to check user's answer against the actual answer
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining"""
    if guess > answer:
        print ("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print (f"Well done correct. You've won. Correct answer was {answer}.")

# function to set difficulty
def set_difficulty():
   level = input("Choose difficulty. Type 'easy', 'hard' or 'custom': ")
   if level == "easy":
       return EASY_LEVEL_TURNS
   elif level == "hard":
       return HARD_LEVEL_TURNS
   elif level == "custom":
        custom_level_turns = int(input("Set a custom number of attempts: "))
        return custom_level_turns
   else:
    print("------Input not recognized. Try again.")
    #set_difficulty()

def game():    
    # Welcome message
    print( WELCOME_MESSAGE)

    # Random number between 1  and 100
    answer = (random.randrange(1, 100))
    turns = set_difficulty()

    try:
        turns is None
    except ValueError:
        print("ValueError")
    # if turns is None:
    #     print("Error turns is NONE")
    #     turns = 44
    #print(f"psst, the correct answer is {answer}")
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let user guess a number
        guess = int(input("Pick a number: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print (f"You have lost.The right number was {answer}")
            return

game()
