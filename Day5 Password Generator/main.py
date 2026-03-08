import random
import string
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

password_char = []
print("Welcome to the Password Generator")
no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_digits = int(input("How many digits would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like in your password?\n"))

if no_of_letters < 1 or no_of_digits < 1 or no_of_symbols < 1:
    print("Invalid Input")
    exit()

total_char = no_of_symbols + no_of_digits + no_of_letters
if total_char <= 5:
   print("Password should be of at least 6 characters long.")
   exit()

for character in range(no_of_letters):
    password_char.append(random.choice(letters))

for character in range(no_of_digits):
    password_char.append(random.choice(numbers))

for character in range(no_of_symbols):
    password_char.append(random.choice(symbols))


random.shuffle(password_char)
password = ''.join(password_char)

print(f"Your Password: {password}")

