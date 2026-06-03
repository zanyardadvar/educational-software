import random
rock = '''

    _______
---'    ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''

    ______
---'   ___)____
        _______)
       _________)
       ________)
---.__________)


'''
scissors = '''

    _______
---'    ____)____
          _______)
        __________)
      (____)
---.__(___)

'''
def play_game():
    computer_choose = random.randint(0,2)
    user_choose = int(input("what do you choose? typ 0 for rock, 1 for paper, 2 for scissors."))
    if user_choose == 0:
        print("you choose: ")
        print(rock)
        if computer_choose == 0:
            print("computer choose: ")
            print(rock)
            print("it's a draw.")
        elif computer_choose == 1:
            print("computer choose: ")
            print(paper)
            print("you lose :(")
        elif computer_choose == 2:
            print("computer choose: ")
            print(scissors)
            print("you win ;)")
    if user_choose == 1:
        print("you choose: ")
        print(paper)
        if computer_choose == 1:
            print("computer choose: ")
            print(paper)
            print("it's a draw.")
        elif computer_choose == 0:
            print("computer choose: ")
            print(rock)
            print("you win ;)")
        elif computer_choose == 2:
            print("computer choose: ")
            print(scissors)
            print("you lose :(")
    if user_choose == 2:
        print("you choose: ")
        print(scissors)
        if computer_choose == 2:
            print("computer choose: ")
            print(scissors)
            print("it's a draw.")
        elif computer_choose == 1:
            print("computer choose: ")
            print(paper)
            print("you win ;)")
        elif computer_choose == 0:
            print("computer choose: ")
            print(rock)
            print("you lose :(")
print("welcome to the rock,paper,scissors game.")
while input("do you want play a game? typ yes or no.") == "yes":
    play_game()


