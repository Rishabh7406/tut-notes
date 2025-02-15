
# Demonstrating range() function in different ways
x=(range(1, 5, 2))
print(type(x))
print(type(list(x)))
print("end")    





# Basic range with stop only
print("range(5):", list(range(5)))  # [0, 1, 2, 3, 4]

# Range with start and stop
print("range(1, 6):", list(range(1, 6)))  # [1, 2, 3, 4, 5]

# Range with step value (even numbers)
print("range(2, 11, 2):", list(range(2, 11, 2)))  # [2, 4, 6, 8, 10]

# Range with negative step (reverse order)
print("range(10, 0, -2):", list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

# Empty range when step is positive but start > stop
print("range(5, 2):", list(range(5, 2)))  # []

# Empty range when step is negative but start < stop
print("range(2, 5, -1):", list(range(2, 5, -1)))  # []

# Using range() inside a loop
print("\nLooping with range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5
print()

# Generating a list of squares using range()
squares = [x**2 for x in range(1, 6)]
print("\nSquares of numbers 1-5:", squares)  # [1, 4, 9, 16, 25]

# Sum of first 10 natural numbers using range()
sum_of_numbers = sum(range(1, 11))
print("\nSum of numbers 1-10:", sum_of_numbers)  # 55
