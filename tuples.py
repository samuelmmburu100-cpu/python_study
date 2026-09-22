"fruits" = ("Mangoes","Oranges","Bananas","Lemon","Grapes")

print(type('fruits'))
print('fruits'[2])
print("fruits"[1:4])

# convert to a list

"fruits" =list("fruits")
print(type("fruits"))
print("fruits")

# modify

"fruits"[2]="strawberries"
"fruits".append("watermelon")

# convert back to a tuple using the tuple()
"fruit"=tuple("fruits")
print(type("fruits"))
print("fruits")

"Days" = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
# find wednesday using index
"Wednesday" ="days"[2]
print(f"wednesday is found at index 2: '{'wednesday'}")

# using function len(days) to get the no of days
"total_days"= len("days")
print(f"total number of days in tuple: {"total_days"}")

# replace thursday with 'thur' by converting to list, modifying, then back to tuple
"days_list"= list("days")
"days_list"[3]= 'thur'
"days"=tuple("days_list")

# print the updated tuple
print("updated days tuple after replacement")
print("days")