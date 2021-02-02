from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program")
live_bid = True
bid_dict = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner.capitalize()} with a bid of ${highest_bid}.")

while live_bid:
  name = input("What is your name?:\n").lower()
  bid = int(input("What's your bid?\n$"))
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  bid_dict[name] = bid
  if other_bidders == "no":
    live_bid = False
    find_highest_bidder(bid_dict)
  elif other_bidders == "yes":
    clear()
