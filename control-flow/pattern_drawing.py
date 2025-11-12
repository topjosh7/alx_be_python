# pattern_drawing.py
# Program to draw a square pattern using nested loops

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing a row
    print()
    # Increment the row counter
    row += 1
