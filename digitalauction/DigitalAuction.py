def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for name in bids:
        bid = bids[name]
        if highest_bid < bid:
            highest_bid = bid
            winner = name
    print(f"The highest bidder is {winner} and the bid is ${highest_bid}")

bids = {}
should_continue = True
while should_continue:
    name = input("What is the name of the bidder?\n")
    bid = int(input("Enter the bid: $ "))
    bids[name] = bid
    if_continue = input("Are there any other bidders? yes/no\n").lower()
    if if_continue == "yes":
        should_continue = True
    else:
        print("Thank you for the bidding.\n")
        highest_bidder(bids)
        should_continue = False