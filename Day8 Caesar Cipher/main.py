def choice(no_of_shifts, text) :
    no_of_shifts %= 26
    result = ""
    for ch in text :
        if (ord(ch) >= ord('A')) and (ord(ch) <= ord('Z')) :
            result += chr(((ord(ch) - ord('A') + no_of_shifts) % 26) + ord('A'))
        elif (ord(ch) >= ord('a')) and (ord(ch) <= ord('z')) :
            result += chr(((ord(ch) - ord('a') + no_of_shifts) % 26) + ord('a'))
        else :
            result += ch

    return result

game_on = True
while game_on:
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n").lower()
    if (option != 'encode') and (option != 'decode'):
        print("Invalid Choice")
        continue
    message = input("Type your massage:\n")

    while True:
        try:
            shift_number = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("You entered invalid input! Enter an integer")

    if option == 'decode':
        shift_number *= -1

    cipher_message = choice(shift_number, message)
    print(f"Here is your cipher result: {cipher_message}\n\n")
    play = input("Type 'yes' to play again, type 'no' to end.")
    if play == 'no':
        game_on = False

