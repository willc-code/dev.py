from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

print("Welcome to the Love Calculator!")

# prompting the user to to input the names
name1 = input("What is your name? ").lower()
name2 = input("what is your crush's name? ").lower()

# variable to store the scores for the words 'true' and 'love'
score1 = 0
score2 = 0

# for every characters in 'true' and 'love' matching the characters in the names will add one point
for char in name1 + name2:
    if char == "t":
        score1 += 1
    elif char == "r":
        score1 += 1
    elif char == "u":
        score1 += 1
    elif char == "e":
        score1 += 1

for char in name1 + name2:
    if char == "l":
        score2 += 1
    elif char == "o":
        score2 += 1
    elif char == "v":
        score2 += 1
    elif char == "e":
        score2 += 1

# printing the final score
print(f"Love Score is: {score1}{score2}")

# LEARNING OUTCOMES
# - for loop and addition assignment operator (+=) combo.
# - if/elif
# - defining functions with two parameters.

# BELOW IS ANOTHER VERSION defining function with two parameters.
# However, this version does not prompt user to input the names.
# The names are cirectly put into the defined function in the code.

# print("Welcome to the Love Calculator!")
#
# def calculate_love_score(name1, name2):
#     score1 = 0
#     score2 = 0
#     for char in name1 + name2:
#         if char == "t":
#             score1 += 1
#         elif char == "r":
#             score1 += 1
#         elif char == "u":
#             score1 += 1
#         elif char == "e":
#             score1 += 1
#
#     for char in name1 + name2:
#         if char == "l":
#             score2 += 1
#         elif char == "o":
#             score2 += 1
#         elif char == "v":
#             score2 += 1
#         elif char == "e":
#             score2 += 1
#
#     print(f"Love Score is: {score1}{score2}")
#
# calculate_love_score("Knightly Kiera", "Jack Hugh")