my_ds = [45,"Kevin",(720,),["Lesson","Python",{"currency": "KES","student": {"name": "James",
    "age": 23},"subjects": ["Python", "SQL", "HTML", "CSS"]}],834,(91, "Mary", ["HTML", "CSS", "JavaScript"])
]
# 1. Print KES.
# 2. Print 720 from the tuple.
# 3. Print Python from the nested list.
# 4. Print the student's name "James".
# 5. Print SQL from the subjects list inside the dictionary.
# 6. Print HTML from the subjects list inside the dictionary.
# 7. Add a new key called "amount" to the dictionary with a value of 1500.
# 8. Change the student's name from "James" to "Brian".
# 9. Add "Django" to the end of the subjects list.
# 10. Change "CSS" in the subjects list to "Bootstrap".
# 11. Print 834 reversed as 438.
#     Do not use an inbuilt reverse method.
#     Do not manually assign 438.
#     Hint: Convert the number to a string and use [::].
# 12. Print "Mary" from the last tuple.
# 13. Print "JavaScript" from the list inside the last tuple.
# 14. Change "JavaScript" to "React".
# 15. Print the entire updated my_ds.

# myds_task2.py
my_ds = [45,"Kevin",(720,),["Lesson","Python",{"currency": "KES","student": {"name": "James",
    "age": 23},"subjects": ["Python", "SQL", "HTML", "CSS"]}],834,(91, "Mary", ["HTML", "CSS", "JavaScript"])
]

# 1. Print KES
print("1. KES:", my_ds[3][2]["currency"])

# 2. Print 720 from the tuple
print("2. 720:", my_ds[2][0])

# 3. Print Python from the nested list
print("3. Python:", my_ds[3][1])

# 4. Print the student's name "James"
print("4. Student name:", my_ds[3][2]["student"]["name"])

# 5. Print SQL from the subjects list inside the dictionary
print("5. SQL:", my_ds[3][2]["subjects"][1])

# 6. Print HTML from the subjects list inside the dictionary
print("6. HTML:", my_ds[3][2]["subjects"][2])

# 7. Add a new key called "amount" to the dictionary with a value of 1500
my_ds[3][2]["amount"] = 1500
print("7. Added amount:", my_ds[3][2])

# 8. Change the student's name from "James" to "Brian"
my_ds[3][2]["student"]["name"] = "Brian"
print("8. Changed James to Brian:", my_ds[3][2]["student"])

# 9. Add "Django" to the end of the subjects list
my_ds[3][2]["subjects"].append("Django")
print("9. Added Django:", my_ds[3][2]["subjects"])

# 10. Change "CSS" in the subjects list to "Bootstrap"
# CSS is at index 3
my_ds[3][2]["subjects"][3] = "Bootstrap"
print("10. CSS to Bootstrap:", my_ds[3][2]["subjects"])

# 11. Print 834 reversed as 438
reversed_834 = int(str(my_ds[4])[::-1])
print("11. Reversed 834:", reversed_834)

# 12. Print "Mary" from the last tuple
print("12. Mary:", my_ds[5][1])

# 13. Print "JavaScript" from the list inside the last tuple
print("13. JavaScript:", my_ds[5][2][2])

# 14. Change "JavaScript" to "React"
my_ds[5][2][2] = "React"
print("14. Changed JavaScript to React:", my_ds[5][2])

# 15. Print the entire updated my_ds
print("\n15. Final my_ds:")
print(my_ds)

# BONUS CHALLENGE
print("\n--- BONUS ---")
print(f"Currency: {my_ds[3][2]['currency']}")
print(f"Amount: {my_ds[3][2]['amount']}")
print(f"Student: {my_ds[3][2]['student']['name']}")
print(f"Subject: {my_ds[3][2]['subjects'][-1]}") # Django
print(f"Technology: {my_ds[5][2][2]}") # React