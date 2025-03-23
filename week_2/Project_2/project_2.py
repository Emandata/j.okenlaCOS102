# Input names and ages
name1 = input("Enter the first name: ")
age1 = int(input(f"Enter {name1}'s age: "))
name2 = input("Enter the second name: ")
age2 = int(input(f"Enter {name2}'s age: "))

# Swapping the ages
age1, age2 = age2, age1

# Display the result
print(f"{name1}'s new age is {age1}")
print(f"{name2}'s new age is {age2}")
