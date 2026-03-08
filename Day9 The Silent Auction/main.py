bidders = {}

while True:
    name = input("What is your name?\n")
    while True :
        try :
            bid = int(input("How much do you want to bid? $"))
            if bid <= 0:
                raise ValueError("Please, enter a positive amount")
            break
        except ValueError :
            print("Please, enter a valid amount.")
    bidders[name] = bid
    more_bidders = input("Are there any more bidders? ").lower()
    if more_bidders == 'no' :
        break

if bidders :
    highest_bid = max(bidders.values())
    bidder_name = [key for key, value in bidders.items() if value == highest_bid]
    print(f"The winner is {''.join(bidder_name)}")
else :
    print("There are no bidders.")
