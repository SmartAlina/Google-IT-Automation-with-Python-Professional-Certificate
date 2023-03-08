def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n:
        if current_number % 2 == 0:
            count += 1
        current_number += 1
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1
