import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the Rock Paper Scissor game \n")
gameImages = [rock, paper, scissors]


def playGame():
    userChoice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper and 2 for Scissor\n"))
    if userChoice > 0 and userChoice >= 3:
        print("You enter an invalid choice ! You Lose.")

    else:
        print(f"You choose:\n{gameImages[userChoice]}")
        computerChoice = random.randint(0, 2)
        print(f"Computer choosen:\n{gameImages[computerChoice]}")

        if userChoice == computerChoice:
            print("It's a draw !")
        elif userChoice == 0 and computerChoice == 2:

            print("You wins !")
        elif computerChoice == 0 and userChoice == 2:
            print("You Lose !")
        elif userChoice < computerChoice:
            print("You Lose !")
        elif userChoice > computerChoice:
            print("You Wins!")
    play_again = input("Do you wanna play again ? Press 'y' or 'n'").lower()
    if play_again == 'y':
        playGame()


playGame()
