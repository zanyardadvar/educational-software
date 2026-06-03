import random
def game():
    stage = ['''
         +---+
         |   |
         0   |
        /|\  |
        / \  |
             |
       =========

    ''','''
         +---+
         |   |
         0   |
        /|\  |
        /    |
             |
       =========''','''
        +---+
         |   |
         0   |
        /|\  |
             |
             |
       =========''','''
        +---+
         |   |
         0   |
        /|   |
             |
             |
       =========''','''
        +---+
         |   |
         0   |
         |   |
             |
             |
       =========''','''
        +---+
         |   |
             |
             |
             |
             |
       ========='''
             ]
    print("welcome to the hangman game :)")
    print(stage[0])
    word_list = ["apple","pear","dog","baboon","camel","drive","car"]
    chosen_word = random.choice(word_list)
    display = []
    for _ in range(len(chosen_word)):
        display += "_"
    print(display)
    live = 5
    end_game = False
    while not end_game:
        guess = input("guess a letter: ")
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter
        print("great ;)")
        print(display)
        if guess not in chosen_word:
            print("you guessed ",guess," that not in the word. you lose a life. :(")
            live = live-1
            if live == 0:
                end_game = True
                print("you lose!")
        if "_" not in display:
            end_game = True
            print("you win!")
        print(stage[live])

while input("do you want play hangman game? yes or no ")=="yes":
    game()
