def get_even_numbers(n):
    even_numbers = []
    
    for x in range(1, n + 1):
        even_number = 2 * x
        even_numbers.append(even_number)
    return even_numbers

first_five_n = 5
result_five = get_even_numbers(first_five_n)
print(result_five)
first_ten_n = 10
result_ten = get_even_numbers(first_ten_n)
print(result_ten)