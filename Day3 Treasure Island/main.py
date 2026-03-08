logo = """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""'-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
"""

print(logo)

print("Welcome to the treasure Island.\nYour mission is to find the treasure.")
turn = input("You're at the cross road. Where you want to go?\nType \"left\" or \"right\"\n").lower()
if turn == "right":
    print("You fell into hole. Game Over.")
else:
    print("You have come to a lake. There is an island in the middle of the lake.")
    choice = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if choice == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You arrived at the island unharmed. There is house with 3 doors.")
        door = input("One red, one yellow, and one blue. Which colour do you choose?\n").lower()

        if door == "yellow":
            print("You find the treasure! You Win!")
        elif door == "red":
            print("It's a room full of fire. Game Over.")
        else:
            print("You enter a room of beast. Game Over.")
