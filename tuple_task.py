# tuples_task.py

# 1. numbers = (10, 20, 30, 40, 50) Add 60 to the end, Replace 30 with 35
print("--- 1. numbers ---")
numbers = (10, 20, 30, 40, 50)
temp = list(numbers)
temp.append(60) # Add 60 to the end
temp[temp.index(30)] = 35 # Replace 30 with 35
numbers = tuple(temp)
print(numbers)

# 2. values = (15, 5, 30, 25, 10) arrange the elements in ascending order
print("\n--- 2. values ---")
values = (15, 5, 30, 25, 10)
values = tuple(sorted(values))
print(values)

# 3. fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
# Count occurrences of "banana", Remove all occurrences of "banana"
print("\n--- 3. fruits ---")
fruits = ("apple", "banana", "cherry", "banana", "mango", "banana")
count_banana = fruits.count("banana")
print(f'Count of "banana": {count_banana}')

# Remove all occurrences
fruits_no_banana = tuple(f for f in fruits if f != "banana")
print(f"After removing banana: {fruits_no_banana}")

# 4. names = ("Alice", "Bob", "Charlie", "David") Reverse the order using sort method
print("\n--- 4. names ---")
names = ("Alice", "Bob", "Charlie", "David")
names_list = list(names)
names_list.sort(reverse=True) # sort method to reverse
names = tuple(names_list)
print(names)

# 5. colors = ("red", "blue", "green") add "yellow" at index 1, Extend with ["purple", "orange"]
print("\n--- 5. colors ---")
colors = ("red", "blue", "green")
colors_list = list(colors)
colors_list.insert(1, "yellow") # add at index 1
colors_list.extend(["purple", "orange"]) # extend
colors = tuple(colors_list)
print(colors)