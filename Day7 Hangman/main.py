import random
from hangman_lives import stages
words_list = ["apple", "clouds", "book"]
word = random.choice(words_list)

max_lives = 6
lives = max_lives
letter_guessed = ['_'] * len(word)

def display_guessed_letters(letter_guessed):
    print(f"Word to guess:", " ".join(letter_guessed))

def update_letters(letter, word, letter_guessed):
    for i in range(len(word)):
        if word[i] == letter:
            letter_guessed[i] = letter

def check_word(letter_guessed):
    return '_' not in letter_guessed
while lives > 0 :
    display_guessed_letters(letter_guessed)
    letter = input("Guess a letter: ").lower()
    if letter in word :
        update_letters(letter, word, letter_guessed)
        print(stages[lives])
        print(f"You guessed '{letter}', that's in the word. Good Job!")

        if check_word(letter_guessed):
            print("Congratulations, you win!")
            break
    else:
        lives = lives - 1
        print(stages[lives])
        print(f"You guessed '{letter}', that's not in the word. You lose a life.\n")

        print(f"************************** {lives}/{max_lives} **************************")

if lives == 0:
    print("Game Over")