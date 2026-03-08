import random


def choose_difficulty():
    while True:
        difficulty = input("Choose difficulty. Type 'hard' or 'easy'. ").lower()

        if difficulty == 'easy' or difficulty == 'hard' :
            return difficulty
        else :
            print("Invalid input please choose a correct option.")
def check(attempts, number_num):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == number_num:
            print(f"You got it! The number is {number_num}")
            break
        elif guess > number_num :
            print("Too high")
        else :
            print("Too low")
        attempts -= 1
        if attempts == 0:
            print("You have used your all attempts. You lose!")
            break

def play(num):
    level = choose_difficulty()
    if level == 'easy':
        number_of_attempt = 10
    else :
        number_of_attempt = 6

    check(number_of_attempt, num)

game_on = True
while game_on:
    want_to_play = input("Type 'y' to play. Type 'n' to end. ")
    print("I am thinking a number between 1 and 100.")
    number = random.randint(1, 100)
    if want_to_play == 'n':
        game_on = False
    else:
        play(number)