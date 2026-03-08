import random
def calculate_total(card_list):
    total = sum(card_list)
    for index in range(len(card_list)):
        if (card_list[index] == 11) and total > 21:
            card_list[index] = 1
            total = sum(card_list)
    return card_list

def deal_user_cards(cards_user, deck):
    cards_user.append(deck.pop())
    cards_user = calculate_total(cards_user)
    return cards_user

def deal_dealer_cards(cards_dealer, deck):
    if sum(cards_dealer) < 17:
        cards_dealer.append(deck.pop())
        cards_dealer = calculate_total(cards_dealer)
    return cards_dealer

def check(card_user, card_dealer):
    user_sum = sum(card_user)
    dealer_sum = sum(card_dealer)
    if user_sum <= 21 :
        if(dealer_sum > 21) or (user_sum > dealer_sum):
            print("You Win")
        elif dealer_sum == user_sum:
            print("It's Draw")
        else :
            print("You Lose")
    elif user_sum > 21:
        print("You Lose")

    print(f"Your cards are {card_user}, and sum is {user_sum}")
    print(f"Dealer's cards are {card_dealer}, and sum is {dealer_sum}")



def play(card):
    user_card = []
    dealer_card = []

    for i in range(2):
        user_card.append(card.pop())
        dealer_card.append(card.pop())

    print(f"Your card are {user_card}, with total sum {sum(user_card)}")
    print(f"Dealer's one card is {dealer_card[0]}")

    game_on = True


    while game_on:
        deal = input("Press 'y' to deal another card. Press 'n' to pass ").lower()
        if deal == 'y' :
            user_card = deal_user_cards(user_card, card)
            dealer_card = deal_dealer_cards(dealer_card, card)
            print(f"Your card are {user_card}, with total sum {sum(user_card)}")
            print(f"Dealer's one card is {dealer_card[0]}")
        else:
            check(user_card, dealer_card)
            game_on = False




want_to_play_again = input("Type 'y' to play . Type 'n' to end the game ")
while want_to_play_again == 'y':
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
             10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9,
             10, 10, 10, 10, 11, 2, 3, 4, 5, 6,
             7, 8, 9, 10, 10, 10, 10, 11, 2, 3,
             4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(cards)
    play(cards)
    want_to_play_again = input("Type 'y' to play . Type 'n' to end the game ")