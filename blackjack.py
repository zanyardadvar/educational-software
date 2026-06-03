import random
def play_game():
    def deal_card():
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        if sum(cards)==21 and len(cards)==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
    def compare(user_score,computer_score):
        if user_score == computer_score:
            return "draw"
        elif computer_score == 0:
            return "lose,has blackjack"
        elif user_score == 0:
            return "win,with a blackjack"
        elif user_score > 21:
            return "you lose"
        elif computer_score > 21:
            return "you win"
        elif user_score > computer_score:
            return "you win"
        else:
            return "you lose"

    game_is_over = False
    user_card = []
    computer_card = []
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not game_is_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print("yor cards: ",user_card,"score: ",user_score)
        print("computer first card: ",computer_card[0])
        if computer_score == 0 or user_score == 0 or user_score>21:
            game_is_over = True
        else:
            user_should = input("do you want card? yes or no ")
            if user_should =="yes":
                user_card.append(deal_card())
            else:
                game_is_over = True
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    while computer_score != 0 and computer_score <17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print("your final hand: ",user_card,"final score: ",user_score)
    print("computer final hand: ",computer_card,"final score: ",computer_score)
    print(compare(user_score,computer_score))
while input("do you want play a game of blackjack? yes or no ") == "yes":
     play_game()



