# mydstask.py

my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]

# 1. Print KES
print("1. KES:", my_ds[3][2]["currency"])

# 2. Print 560
print("2. 560:", my_ds[2])

# 3. Print Maths
print("3. Maths:", my_ds[3][1])

# 4. In the dictionary with the key currency, add another key "amount" with value 90
my_ds[3][2]["amount"] = 90
print("4. After adding amount:", my_ds[3][2])

# 5. Reverse 987 to 789 without using an inbuilt-method or Assigning 789 manually
# Hint: Strings can be reversed using [::]
reversed_num = int(str(my_ds[4])[::-1])
print("5. Reversed 987:", reversed_num)

# 6. Change the name "John" to "Jane"
# my_ds[5] is a tuple (76,"John") which is immutable, so we recreate it
my_ds[5] = (my_ds[5][0], "Jane")
print("6. Changed John to Jane:", my_ds[5])

print("\nFinal my_ds:", my_ds)