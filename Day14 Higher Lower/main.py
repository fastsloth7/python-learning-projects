from game_data import data
import random

def check(x, y, bet):
    answer = ''
    if x > y:
        answer = 'A'
    else : answer = 'B'

    if bet == answer:
        return True
    else :
        return False

def display(x, y) :
    print(f"\nCompare A: {x['name']}, a {x['description']}, from {x['country']}")
    print("VS")
    print(f"B: {y['name']}, a {y['description']}, from {y['country']}")

def compare(ob1, data_list):
    score = 0
    while True:
        ob2 = random.choice(data_list)
        if ob1 == ob2:
            continue

        display(ob1, ob2)

        choice = input("Who has more followers? A or B: ").upper()
        fl_ob1 = ob1["follower_count"]
        fl_ob2 = ob2["follower_count"]
        is_true = check(fl_ob1, fl_ob2, choice)
        if is_true:
            ob1 = ob2
            score += 1
            print(f"\nYou're correct, your score is {score}")
        else :
            print(f"\nThat's incorrect, your score is {score}")
            break

while True:
    a = random.choice(data)
    compare(a, data)
    play = input("Type 'y' to play again.")
    if play != 'y':
        break
