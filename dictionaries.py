# =>stores multiple properties in kye-value pairs key:(value)
# enclosed with {curly braces}
# keys are always strings but values can be of any type
# keys are unique
# class 'dict'

"students1"={
    "name:" "alex",
    "age:" "20",
    "admn:" "tech2323",
    "city:" "Nairobi",
}

print("student1")
print(type("student1"))

# display values
print("student1"['name'])
print("student1"['city'])

# display adm
print("student1"['tech2323'])

# adding and updating

# adding
"student1"['Gender']='Male'
print("student1")

# add a new key email with a value
print("student1"['email'])='value'

# updating
"student1"['age']=30
print("student1")

# update name with a diff name
print(type('student1'))



# dictionaries.py - Python Dictionaries Practice

print("--- Q1. Create a dictionary ---")
student = {
    "name": "Jane",
    "age": 21,
    "course": "Maths",
    "currency": "KES"
}
print(student)

print("\n--- Q2. Access values ---")
# Print name and currency
print("Name:", student["name"])
print("Currency:", student.get("currency"))

print("\n--- Q3. Add / Update ---")
# Add amount = 90 and update age to 22
student["amount"] = 90
student["age"] = 22
print(student)

print("\n--- Q4. Nested Dictionary ---")
my_ds = {
    "student": "John",
    "marks": [80, 75, 90],
    "details": {"lesson": "Maths", "currency": "KES"}
}
# Print Maths
print("Lesson:", my_ds["details"]["lesson"])
# Print KES
print("KES:", my_ds["details"]["currency"])

print("\n--- Q5. Loop through dictionary ---")
for key, value in student.items():
    print(f"{key} : {value}")

print("\n--- Q6. Remove a key ---")
student.pop("course")
print(student)

print("\n--- Q7. Check if key exists ---")
print("Is 'amount' in student?", "amount" in student)

print("\n--- Q8. Real Task - Shopping ---")
shopping = {"apple": 50, "banana": 30, "mango": 80}
# Add orange 60, increase banana to 40
shopping["orange"] = 60
shopping["banana"] = 40
# Print total price
print("Shopping:", shopping)
print("Total:", sum(shopping.values()))
