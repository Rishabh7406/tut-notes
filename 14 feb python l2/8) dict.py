# Dictionary Methods in Python

# Sample Dictionary
student = {"name": "Alice", "age": 20, "marks": 90}

# Get keys and values
print(student.keys())  # dict_keys(['name', 'age', 'marks'])
print(student.values())  # dict_values(['Alice', 20, 90])

# Get key-value pairs
print(student.items())

# Safe key lookup
print(student.get("city", "Not Found"))

# Add and update dictionary
student.update({"city": "New York"})
print(student)

# Remove a key
student.pop("age")
print(student)

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")
