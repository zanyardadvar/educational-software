import random
def play_game():
    print("welcome to the number guessing game!")
    print("i'm think of a number between 1 and 100.")
    difficulty = input("choose difficulty. typ 'easy' or 'hard': ")
    choose = random.randint(0,100)
    end_game = False
    round1 = 5
    round2 = 10
    while not end_game:
        if difficulty == "hard":
            if round1 != 0:
                round1 -= 1
                number = int(input("make a guess: "))
                if number == choose:
                    print(" you got it! thr answer was ",number,".")
                    end_game = True
                elif number > choose:
                    print("too high")
                    print("you have a ",round1," attempts remaining to guess the number.")
                elif number < choose:
                    print("too low")
                    print("you have a ",round1," attempts remaining to guess the number.")
        else:
            if round2 != 0:
                round2 -= 1
                number = int(input("make a guess: "))
                if number == choose:
                    print(" you got it! thr answer was ",number,".")
                    end_game = True
                elif number > choose:
                    print("too high")
                    print("you have a ",round2," attempts remaining to guess the number.")
                elif number < choose:
                    print("too low")
                    print("you have a ",round2," attempts remaining to guess the number.")
        if round1 == 0 or round2 == 0:
            print("you lose. :(")
            end_game = True
        elif end_game == True:
            print("you win. :)")
while input("do you want play a guess number game? typ 'yes' or 'no' ")=="yes":
    play_game()


