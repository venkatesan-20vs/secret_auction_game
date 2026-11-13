from art import logo
print(logo)

def find_highest_bid(bidders):
    highest_bid = 0
    winner = ""
    for key in bidders:
        if bidders[key] > highest_bid:
            highest_bid = bidders[key]
            winner = key
    print(f"The winner is {winner} with a highest bid of ${highest_bid}")


auction_list = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?")
    bid = int(input("What is your bid?: $"))
    auction_list[name] = bid
    new_input = input("Are there any other bidders?  Type 'yes or 'no").lower()
    if new_input == "no":
        continue_bidding = False
        find_highest_bid(auction_list)
    elif new_input == "yes":
        print("\n"*50)


