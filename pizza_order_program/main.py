print("Welcome to Python Pizza Delivery!")

# asks user about the size, adding peperoni and adding cheese option
size = input("What pizza size do you want? S, M or L? ")

peperoni = input("Do you want peperoni on your pizza? Y or N? ")

cheese = input("Do you want extra cheese? Y or N? ")

bill = 0

# Pizza sizes and price S = $15, M = $20, L = $25
if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25
  
# Add peperoni for S pizza = $2, for M and L pizza = $3
if peperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "L":
        bill += 3


# Add cheese = $1
if cheese == "Y":
    bill += 1

# final bill amount
print(f"Your final bill is ${bill}.")