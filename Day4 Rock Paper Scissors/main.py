import random
logo =["""    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",

"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n"))
print(logo[user_choice])

computer_choice = random.randint(0, 2)

print("Computer chose: ")
print(logo[computer_choice])

if user_choice == computer_choice:
    print("it's draw")
elif (user_choice - computer_choice) % 3 == 1:
    print("You win!")
else:
    print("You lose!")