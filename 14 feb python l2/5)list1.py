# List Methods in Action
numbers = [10, 20, 30, 40, 50]
#[10, 20, 30, 40, 50]
numbers.append(60)  # Adds 60 at the end
#[10, 20, 30, 40, 50,60]
numbers.insert(2, 25)  # Inserts 25 at index 2
#[10, 20,25, 30, 40, 50]
numbers.remove(30)  # Removes first occurrence of 30
#[10, 20,25, 40, 50]
popped_item = numbers.pop()  # Removes last element
#[10, 20,25, 40]
numbers.sort(reverse=True)  # Sorts the list
#[40,25,20,10]
print(numbers.count(10))
print(numbers)  # Output: [10, 20, 25, 40, 50]
print("Popped item:", popped_item)  # Output: 60
