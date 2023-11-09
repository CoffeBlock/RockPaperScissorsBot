import random

def game():
    botChoice = random.randrange(1, 4)
    wait = True
    while wait == True:
        userinput = input()
        try:
            userinput = int(userinput)
            wait = False
        except ValueError:
            print("Please enter a number")
    playerChoice = userinput
    if playerChoice == 1 or playerChoice == 2 or playerChoice == 3:
        if playerChoice == botChoice:
            print("Tie")
        elif (playerChoice - botChoice) % 3 == 1:
            print("You Win")
        else:
            print("You Lose")
    else:
        game()


game()

# 1 = rock
# 2 = paper
# 3 = scissors