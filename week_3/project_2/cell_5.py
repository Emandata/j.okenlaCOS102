print("Welcome to Izfin Technology of Nigeria")

# Function to get valid integer input
def get_valid_input(prompt):
    while True:
        try:
        
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

name = input("What is your name? ")
age = get_valid_input("How old are you? ")
years_of_experience = get_valid_input("How many years of experience? ")


if years_of_experience > 25 and age >= 55:
    atr = 5600000
    message = f"{name}, Your Annual Tax Revenue is N{atr:,}."
elif years_of_experience > 20 and age >= 45:
    atr = 4480000
    message = f"{name}, Your Annual Tax Revenue is N{atr:,}."
elif years_of_experience > 10 and age >= 35:
    atr = 1500000
    message = f"{name}, Your Annual Tax Revenue is N{atr:,}."
else:
    atr = 550000
    message = f"{name}, Your Annual Tax Revenue is N{atr:,}."

# Print the result
print(message)
