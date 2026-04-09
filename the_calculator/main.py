from calculator_art import logo

print(logo)

# Defining the four mathematical functions:
def divide(a, b):
    return (a / b)

def multiply(a, b):
    return (a * b)

def add(a, b):
    return (a + b)

def subtract(a, b):
    return (a - b)

# A placeholder for the while loop to be continuing unless the user decides not to continue.
continue_calculator = True

# Putting the first number outside of the while loop so that the calculator can continue with the answer from previous calculation.
first_no = 0
first_no = float(input("What's the first number? "))

# While loop which continues calculating using the answer from the previous calculation unless the user decides not to continue.
while continue_calculator == True:

    operation = input("Pick an operation: + - / * : ")
    next_no = float(input("What's the next number? "))

    # The if/elif statements which applies the selected operation to the input numbers.
    if operation == "+":
        answer = add(first_no, next_no)
    elif operation == "-":
        answer = subtract(first_no, next_no)
    elif operation == "*":
        answer = multiply(first_no, next_no)
    elif operation == "/":
        answer = divide(first_no, next_no)
    else:
        print("Operation entered not valid")
        break

    # This is the answer statement.
    print(f"{first_no} {operation} {next_no} = {answer}\n")

    # If the user decides to continue, the value of the answer will be assigned to the first number, and the while loop continues.
    cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation ")
    if cont == "y":
        first_no = answer
    elif cont == "n":
        print("\n" *20)
        break




