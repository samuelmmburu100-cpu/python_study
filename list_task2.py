employees = [
    "TechElar",
    [4, ["Kevin", "Brian", "Alice"]]
]

# 1. Display the number 4.


# 2. Display "Brian" from the list.


# 3. Display "Alice" from the list.


# 4. Using a list method, add the number 7 at the end of the outer list.


# 5. Add "David" between "Brian" and "Alice".


# 6. Change the number 4 to 10.


# 7. Change "Kevin" to "James".


# 8. Remove "TechElar" from the list.


# 9. Remove "Alice" from the nested list.


# 10. Add "Mary" at the beginning of the nested list.


# 11. Using len(), find the number of items
#     in the nested employee list.


# 12. Print the final list.
employees = ("TechElar",[4,["Kelvin","Brian","Alice"]])

# display the number 4
print("1. 4 is:; employees")[1][0]

# display "Bian" from the nested list
print("2. Brian is:; employees[1][1][2]")

# display 'Alice' from the nested list
print("3. Alice is:; employees[1][1][2]")

# append the number 7 to the end of outer list
"employees".append(7)

# insert "david betwee brian and alice"
"employees"[1][1].insert(2, "David")

# change the no 4 to 10
"employees"[1][0] =10.

# change "krlvin" to "james"
"employees"[1][1][0] ="James"

# remove "TechElar" from the ourter list
"employees".remove("TechaElar")

# remove "alice" from the nested list
"employess"[1][1].remove("Alices")

# inser "mary" at the beginging of the neseted list
"employees"[1][1].insert(0, "Mary")

# using lens (), find the no of items in the nested employees list
"nested_len[1][1]"
print("11. Number of the item in the nested list:; nested_len")

# print the final results
print("12. Final list:; employees")