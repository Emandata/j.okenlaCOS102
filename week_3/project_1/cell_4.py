import pandas as pd

# Data for the girls
girls_data = {
    "Name": ["Evelyn", "Jessica", "Somto", "Edith", "Liza", "Madonna", "Waje", "Tola", "Aisha", "Latifa"],
    "Age": [17, 16, 17, 18, 16, 18, 17, 20, 19, 17],
    "Height": [5.5, 6.0, 5.4, 5.9, 5.6, 5.6, 5.6, 6.0, 5.7, 5.5],
    "Score": [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]
}

# Data for the boys
boys_data = {
    "Name": ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"],
    "Age": [19, 16, 18, 17, 20, 19, 16, 18, 17, 19],
    "Height": [5.7, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8, 5.7],
    "Score": [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]
}

# Create dataframes for girls and boys
girls_df = pd.DataFrame(girls_data)
boys_df = pd.DataFrame(boys_data)

# Combine the dataframes into one table
students_df = pd.concat([girls_df, boys_df], ignore_index=True)

# Display the data
print("Student Data Table:")
print(students_df.to_string(index=False))

# Save to a CSV file (optional)
students_df.to_csv("students_data.csv", index=False)
