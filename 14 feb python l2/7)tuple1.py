# Tuple Basics
numbers = (10, 20, 30, 40)

# Immutable - Can't modify elements
# numbers[1] = 99  # ❌ This will give an error

# Accessing elements
print(numbers[0])  # Output: 10

# Slicing
print(numbers[1:3])  # Output: (20, 30)

# Unpacking
a, b, c, d = numbers
print(a, b, c, d)  # Output: 10 20 30 40
