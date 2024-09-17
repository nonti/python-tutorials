def sum_digits(n, level=1):
    if n == 0:
        print(" " * (level - 1) + f"Level {level}: sum_digits(0)")
        print("  " * (level - 1) + f"Returning 0")
        return 0
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        print(" " * (level - 1) + f"Level {level}: sum_digits({n})")
        result = last_digit + sum_digits(remaining_digits, level + 1)
        print(" " * (level - 1) + f"Returning {result}")
        return result

# Input: 123
result = sum_digits(123)
