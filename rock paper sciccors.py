import random

"""
Rock Paper Sciccors Gsme

INSTRUCTIONS:
Player1 vs.Computer
3 count down to make your move ("Rock..Paper..Scissors..[shoot]!)
Rock > Scissors
Scissors > paper
paper > rock
paper = paper: Tie
rock = rock: Tie
Scissors = Scissors: Tie


    Good luck!


"""
user_score = 0  # player score
computer_score = 0  # CPU score


# function for user when press the following options
def Player_option():
    user1_input = input("choose: Rock, Paper, Sciccors: ")
    if user1_input in ["Rock", "rock" "R", "r"]:  # any option will return rock
        user1_input = "r"

    # any option will return scissors
    elif user1_input in ["Sciccors", "sciccors", "S", "s"]:
        user1_input = "s"

    elif user1_input in ["Paper", "paper", "P", "p"]:  # Any option will return scissors
        user1_input = "p"
    else:
        # Enter the correct options to procced
        print("Choose valid option")
        Player_option()
    return user1_input


def Computer_option():
    computer_choice = random.randint(1, 3)  # 1-3 ("rock,paper,scissors)
    if computer_choice == 1:                # CPU use random numbers to pick option to face User
        computer_choice = "r"
    elif computer_choice == 2:
        computer_choice = "p"
    else:
        computer_choice = "s"
    return computer_choice


while True:
    print("")
    user_choice = Player_option()  # User input
    computer_choice = Computer_option()  # random CPU input

    print("")
    if user_choice == "r":
        if computer_choice == "r":
            # User - CPU = tie
            print("you choose rock, the computer choose rock, its a tie!")

        elif computer_choice == "p":
            print("you choose rock,computer choose paper.you lose")
            computer_score += 1

        elif computer_choice == "s":
            print("you choose rock,computer choose sciccors.You win!")
            user_score += 1

    elif user_choice == "p":
        if computer_choice == "r":
            print("You chose paper.The computer chose rock. You win")
            user_score += 1

        elif computer_choice == "p":
            print("you choose paper.The computer choose paper.You tied")

        elif computer_choice == "s":
            print("you choose paper,computer choose sciccors.You lose")
            computer_score += 1

    elif user_choice == "s":
        if computer_choice == "r":
            print("you chose scissors.The computer chose rock,you lose")
            computer_score += 1
        elif computer_choice == "p":
            print("you chose the scissors.The computer chose paper,You win!")
            user_score += 1
        elif computer_choice == "s":
            print("you chose scissors.The computer picked scissors,Tie!")
    print("")
    # implement User and CPU score total as a string
    print("User_score: " + str(user_score))
    print("computer_score: " + str(computer_score))
    user_choice = input("you want to try again? (Y/N)")
    if user_choice in ["Yes", "y", "Y", "yes"]:             # Continue game
        pass
    elif user_choice in ["No", "no", "n", "N"]:             # End game
        break
    else:
        break
