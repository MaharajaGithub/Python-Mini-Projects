from random import randint

Easy_level_turns = 10
Hard_level_turns = 5
turns = 0

def check_answer(guess,answer,turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return Hard_level_turns
    else:
        return Easy_level_turns

def game():
    print("Welcome to the Number Guessing Game! \n")
    print("Guess the number between 1 to 100\n")
    answer = randint(1,100)
    #print(f"Testing purpose answer is  {answer}")
    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You ran out of guesses")
        elif guess != answer :
            print("Guess Again")
game()