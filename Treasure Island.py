# Treasure Island Game

print("Welcome to treasure island game! \n")
print("Your mission is to find the treasure\n")

choice1 = input("You're at a crossroad, where do you want to go? Type 'Left' or 'right'\n").lower()

if choice1 =="left":
    # continue the game
    choice2 = input("You're come to lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim acorss \n").lower()
    if choice2 == "wait":
        # Game will continue
        choice3 = input("you're arrived at the island unnamed. There is house with three door's. One red, one yellow and one blue. Which color do you choose? Type 'red', 'yellow' or 'blue'\n").lower()
        if choice3 == "Red":
            print("It's room full of fire. Game Over!")
        elif choice3 == "yellow":
            print("You found the treasure you won.")
        elif choice3 == "blue":
            print("You were killed by the tiger. Game Over!")
        else:
            print("You choose the door that doesn't exist. Game Over!")
    else:
        print("You got attaked by angry trout. Game Over!")
else:
    print("You fell into a hole. Game Over!.")



