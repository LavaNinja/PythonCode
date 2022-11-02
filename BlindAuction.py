from replit import clear

# HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Hello!! Welcome to Secret Bidding.")

bids = {}
bidding_finished = False


def find_winner():
    highest_bid = 0
    winner = ""
    for bidder, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
            # print(highest_bid)
            clear()
        else:
            pass

    print(f"The winner is {winner} with a bid of {highest_bid}!")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no' ")
    if should_continue == "no":
        bidding_finished = True
        find_winner()
    elif should_continue == "yes":
        clear()




