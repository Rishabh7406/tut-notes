# 1️⃣ Basic for loop
print("1. Basic for loop:")
for i in range(5):
    print(i)  # Output: 0 1 2 3 4
print()

# 2️⃣ Loop with start, stop, step
print("2. Loop with range(start, stop, step):")
for i in range(1, 10, 2):
    print(i)  # Output: 1 3 5 7 9
print()

# 3️⃣ Loop in reverse order
print("3. Reverse loop:")
for i in range(10, 0, -2):
    print(i)  # Output: 10 8 6 4 2
print()

# 4️⃣ Looping over a list
print("4. Looping over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple banana cherry
print()

# 5️⃣ Looping over a string
print("5. Looping over a string:")
for char in "Python":
    print(char, end=" ")  # Output: P y t h o n
print("\n")

# 6️⃣ Using enumerate() to get index
print("6. Using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
print()

# 7️⃣ Nested for loop
print("7. Nested for loop (Multiplication Table of 3):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
print()

# 8️⃣ Loop with else
print("8. Loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop completed!")
print()

# 9️⃣ Breaking the loop early
print("9. Breaking the loop early:")
for i in range(10):
    if i == 5:
        print("Breaking at 5")
        break
    print(i)
print()

# 🔟 Skipping iterations using continue
print("10. Skipping 5 using continue:")
for i in range(10):
    if i == 5:
        continue
    print(i)
print()
