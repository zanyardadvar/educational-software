import random
vs = '''
 -     _
| |   / /___
| |  / / __/
| | / (__ )
|___/____(_)
'''
data = [
    {
    'name':'Instagram',
    'follower_count':346,
    'description':'social media platform',
    'country':'united states'
    },
    {
    'name':'Cr ronaldo',
    'follower_count':215,
    'description':'footballer',
    'country':'portugal'
    },
    {
    'name':'Ariana grande',
    'follower_count':183,
    'description':'Musician',
    'country':'united states'
    },
    {
    'name':'Dwayne johnson',
    'follower_count':183,
    'description':'Actor',
    'country':'united states'
    },
    {
    'name':'L missi',
    'follower_count':246,
    'description':'Footballer',
    'country':'Argentina'
    },
    {
    'name':'Elon musk',
    'follower_count':150,
    'description':'capitalist',
    'country':'united states'
    },
    {
    'name':'Magnus carlsen',
    'follower_count':196,
    'description':'chess player',
    'country':'Norway'
    }
]
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return account_name, account_descr," from ",account_country
def check_answer(guess,a_followers,b_followers):
    if a_followers>b_followers:
        return guess == "A"
    else:
        return guess == "B"
score = 0
game = True
while game:
    account_b = random.choice(data)
    while game:
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
        print("Compare A: ",format_data(account_a))
        print(vs)
        print("Against B: ", format_data(account_b))
        guess = input("who has more followers? typ A or B. ")
        a_follower_account = account_a["follower_count"]
        b_follower_account = account_b["follower_count"]
        is_correct = check_answer(guess,a_follower_account,b_follower_account)
        if is_correct:
            score += 1
            print("your right! current score: ",score)
        else:
            game = False
            print("sorry, it's wrong. final score: ",score)
    if input("do you want play a game again? typ yes or no. ")=="yes":
        score = 0
        game = True
    else:
        game = False