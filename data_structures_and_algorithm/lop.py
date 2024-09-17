def sum_digits(n, level=1):
    # Print the current level and input value for tracing
    print(f"Level {level}: sum_digits({n})")

    # Base case: If n is 0, return 0
    if n == 0:
        print(f"   {' ' * 3 * (level-1)}Returning 0")
        print()
        return 0
    
    # Base case: If n is a single digit, return n
    if n < 10:
        print(f"   {' ' * 3 * (level-1)}Returning {n}")
        return n
    
    # Recursive case: Sum the last digit and the sum of the remaining digits
    last_digit = n % 10
    remaining_digits = n // 10
    
    # Make the recursive call and increase the level
    sum_of_remaining_digits = sum_digits(remaining_digits, level + 1)
    
    # Calculate the total sum
    total_sum = last_digit + sum_of_remaining_digits
    
    # Print the return value after computation
    print(f"   {' ' * 3 * (level-1)}Returning {total_sum}")
    
    return total_sum

# Example usage
result = sum_digits(123)
print("Sum of digits:", result)
