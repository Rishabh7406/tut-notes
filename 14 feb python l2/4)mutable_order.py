# ✅ Lists are Mutable and Ordered
numbers = [1, 2, 3, 4]
numbers[2] = 99  # Changing value at index 2
print("List:", numbers)  # Output: [1, 2, 99, 4]

# ❌ Tuples are Immutable but Ordered
tuple_numbers = (1, 2, 3, 4)
# tuple_numbers[2] = 99  # ❌ This will cause an error

# ✅ Dictionaries are Mutable and Ordered (Python 3.7+)
student = {"name": "Alice", "age": 20}
student["age"] = 21  # Changing value of key 'age'
print("Dictionary:", student)  # Output: {'name': 'Alice', 'age': 21}

# ❌ Strings are Immutable but Ordered
text = "hello"
# text[0] = "H"  # ❌ This will cause an error

# ✅ Sets are Mutable but Unordered
colors = {"red", "green", "blue"}
colors.add("yellow")  # Adding element
print("Set:", colors)  # Output: Unordered set
