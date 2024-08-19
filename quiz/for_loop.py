
for num in range(1, 6):
    factorial = 1  # Initialize factorial to 1 for each number
    
    # Calculate the factorial using a nested loop
    for i in range(1, num + 1):
        factorial *= i
    
    # Print the result using formatted strings
    print(f"The factorial of {num} is {factorial}")