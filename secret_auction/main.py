# importing the gravel ASCII art logo
from secret_auction_art import logo

print(logo)
print("Welcome to the secret auction program.")

# A variable to indicate if the bid is complete or not, which will break the while loop if yes or true.
bidding_complete = False

# A dictionary list to hold the list of bidders and their bids.
bid_list = {}


while not bidding_complete:
    # Obtaining user's name and bid amount. Reminder to ensure that the bid is in integer type.
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    # Inputting the name and bid into the dictionary after obtaining them from the user.
    bid_list[name] = bid

    # If there are other bidders, we will appear to be clearing the screen by printing 100 new lines.
    # if there are no other bidders, bidding will be complete and the while loop will break.
    other_bidders = input("Are there other bidders? Type 'yes' or 'no' ").lower()
    if other_bidders == "yes":
        print("\n" * 100)
    elif other_bidders == "no":
        bidding_complete = True


# This is where we determine the top bidder and the top bid amount by looping.
# At the beginning, the top bidder list will be empty, and top bid will be zero.
top_bidder = ""
top_bid = 0

# We will loop through the name and bid amount in the bid list.
# The top bid amount will be updated each time there is a higher bid amount, until there is none.
for name in bid_list:
    bid_amount = bid_list[name]

    if bid_amount > top_bid:
        top_bid = bid_amount
        top_bidder = name

# Printing out the top bidder and the bid amount, which is also the top bid.
print(f"The winner and the highest bidder is {top_bidder}, with the bid amount of ${top_bid}!")

