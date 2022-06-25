import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break

# if user spelled incorrect, the game should continue
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
# 0-rock, 1-paper, 2-scissor[randint reads the last value 2 as well]
    computer_picks = options[random_number]
    print("computer picks ", computer_picks + ".")

#3 conditions where user wins!
    if user_input == "rock" and computer_picks == "scissor":
        print("You won.")
        user_wins += 1

    elif user_input == "scissor" and computer_picks == "paper":
        print("You won.")
        user_wins += 1

    elif user_input == "paper" and computer_picks == "rock":
        print("You won.")
        user_wins += 1
    else:
        print("You lost, Computer won.")
        comp_wins += 1

print("You won by " + str(user_wins) + " points")
print("Computer won by " + str(comp_wins) + " points.")
print ("Good Bye !!!")