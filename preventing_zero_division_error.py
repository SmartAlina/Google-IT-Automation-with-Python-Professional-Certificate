def safe_division(numerator, denominator):
    if denominator == 0:
        result = 0
    else:
        result = numerator/denominator
    return result

print(safe_division(5, 5)) # Should print 1.0
print(safe_division(5, 4)) # Should print 1.25
print(safe_division(5, 0)) # Should print 0
print(safe_division(0, 5)) # Should print 0.0
