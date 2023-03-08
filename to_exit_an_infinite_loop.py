def is_power_of_two(number):
  while number != 0 and number % 2 == 0:
    number = number / 2
  if number == 1:
    return True
  return False

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
