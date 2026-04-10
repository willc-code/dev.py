# Note: This was coded right off the bat without looking at tutorials and the solution.
# Issue: Did not take into account situation when user went over 21 points.
# Issue: Limited to only 3 cards.
# Issue: Even if more cards are added, the same blocks of codes will be repeated.
# Issue: This is not dynamic and feels hard-coded and not as elegant.
# Suggestion: To use a custom defined function and while loop

from blackjack_art import logo
import random

print(logo)
game_on = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")

if game_on == "y":
    your_cards = []
    your_first_card = random.randint(1, 10)
    your_second_card = random.randint(1, 10)
    your_cards.append(your_first_card)
    your_cards.append(your_second_card)
    your_score = your_first_card + your_second_card

    comp_cards = []
    comp_first_card = random.randint(1, 10)
    comp_second_card = random.randint(1, 10)
    comp_cards.append(comp_first_card)
    comp_cards.append(comp_second_card)
    comp_score = comp_first_card + comp_second_card
    if comp_score <= 15:
        comp_third_card = random.randint(1, 10)
        comp_cards.append(comp_third_card)
        final_comp_score = comp_first_card + comp_second_card + comp_third_card
    else:
        final_comp_score = comp_score

    print(f"Your cards are: {your_cards}, current score: {your_score}.")
    print(f"Computer's first card: {comp_first_card}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y":
        your_third_card = random.randint(1, 10)
        your_cards.append(your_third_card)
        final_your_score = your_first_card + your_second_card + your_third_card
    elif another_card == "n":
        final_your_score = your_score
    else:
        print("Invalid input. You don't get another card.")
        final_your_score = your_score

    print(f"Your final hand: {your_cards}, final score: {final_your_score}.")
    print(f"Computer's final hand: {comp_cards}, final score: {final_comp_score}.")
    if final_your_score > final_comp_score:
        print("You win!")
    elif final_your_score < final_comp_score:
        print("You lose!")
    elif final_your_score == final_comp_score:
        print("Draw!")

elif game_on == "n":
    print("\n" * 20)
    pass

else:
    print("Invalid input.")
    pass






