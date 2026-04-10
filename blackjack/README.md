# The Blackjack!

About: Risk it all in a fun Blackjack, CLI python game against the computer.  

## How to use 

Run `python main.py` and follow the prompts to input the relevant responses. 

## What it does

Helping you to encode or decode your secret messages according to your preference. 

## Other files

draft.py - This was coded right off the bat without looking at tutorials and the solution. I uncovered a lot of weaknesses of the program with comments noted in the code. 
suggested_solution.py - This is the suggested solution by Angela Yu's 100 days of code course. Saving it here for reference. 
blackjack_art.py - contains the logo of the game in ASCII art, which is then imported to main.py

### Learning notes 

- The codes in main.py was my second attempt after learning from the weaknesses in my draft version in draft.py
- This version was also done without looking at tutorials or suggested solution, except for the list of cards.
- After realising that the completed solution contains card number 11, I briefly looked at the suggested solution.
- I took the list of cards from the suggested solution which mirrors the card deck better and improve the odds more realistically.
- The List: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- Alas, this version of mine still has a weakness and I have missed out an important part of the real Blackjack game:
- That if 11 is in cards and the sum of cards is above 21, 11 will be counted as 1:
- It is structurally difficult to include this feature without a major revamp.
- Therefore I am keeping this version here as a testament to writing them without looking at the solution.
- Possibility of revisiting and rewriting this in the future. 
- For future solution, Claude has suggested: Rewrite just the score calculation — add a calculate_score() function to your existing code that handles the ace rule. You don't need to restructure everything.
