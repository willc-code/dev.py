# Welcome to the Secret Auction program!

About:
A python CLI program that that facilitates a "blind" or "secret" auction.
This program allows multiple users to enter their bids privately, ensuring that no one knows what the others have bid until the auction is over.

## How to use 

Run `python main.py` and follow the prompts to input the relevant responses. 

## What it does

The program follows a simple linear flow to maintain secrecy:

- Input Collection: Each user enters their name and their bid amount.
- Privacy Feature: After a bid is placed, the console "clears" (by printing multiple new lines) so the next bidder cannot see the previous entry.
- Storage: All names and bids are stored in a Python dictionary.
- Winner Calculation: Once all bids are collected, the program iterates through the dictionary to find the maximum value and announces the winner.

## Other files

suggested_solution.py - This is the suggested solution by Angela Yu's 100 days of code course. I am saving it here for future reference since this solution is more elegant than mine. 
secret_auction_art.py - contains the logo of the game in ASCII art, which is then imported to main.py

### Learning outcomes

- Dictionary Mapping: Uses key-value pairs to link bidder names to their respective prices.
- Using While Loops with boolean flags (continue_bidding) to keep the program going on or break it. 
- Manual looping to find the highest bidder and bid. 
