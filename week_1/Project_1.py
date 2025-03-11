def simple_interest(P, R, T):
    """Calculate Simple Interest"""
    A = P * (1 + (R / 100) * T)
    return A

def compound_interest(P, R, n, t):
    """Calculate Compound Interest"""
    A = P * (1 + R / n) ** (n * t)
    return A

def annuity_plan(PMT, R, n, t):
    """Calculate Annuity Plan"""
    A = PMT * ((1 + R / n) ** (n * t) - 1) / (R / n)
    return A

def get_float_input(prompt):
    """Repeatedly asks the user for a valid float input"""
    while True:
        try:
            return float(input(prompt))  # Try converting input to float
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_int_input(prompt):
    """Repeatedly asks the user for a valid integer input"""
    while True:
        try:
            return int(input(prompt))  # Try converting input to int
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")

while True:  # Infinite loop to keep running
    print("\nChoose an option:")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Annuity Plan")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        P = get_float_input("Enter Principal Amount: ")
        R = get_float_input("Enter Rate of Interest (%): ")
        T = get_float_input("Enter Time in Years: ")
        amount = simple_interest(P, R, T)
        print(f"Final Amount with Simple Interest: {amount:.2f}")

    elif choice == "2":
        P = get_float_input("Enter Principal Amount: ")
        R = get_float_input("Enter Annual Interest Rate (%): ") / 100  # Convert to decimal
        n = get_int_input("Enter Number of Times Interest is Compounded Per Year: ")
        t = get_int_input("Enter Time in Years: ")
        amount = compound_interest(P, R, n, t)
        print(f"Final Amount with Compound Interest: {amount:.2f}")

    elif choice == "3":
        PMT = get_float_input("Enter Regular Payment Amount: ")
        R = get_float_input("Enter Annual Interest Rate (%): ") / 100
        n = get_int_input("Enter Number of Payments Per Year: ")
        t = get_int_input("Enter Time in Years: ")
        amount = annuity_plan(PMT, R, n, t)
        print(f"Total Value of Annuity Plan: {amount:.2f}")

    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and end the program

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
