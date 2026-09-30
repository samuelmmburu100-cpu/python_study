
# 5. student_score > 90 and attendance > 80 -> NESTED
student_score = int(input("\nEnter student_score: "))

if student_score > 90:
    attendance = int(input("Enter attendance: "))
    if attendance > 80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")
else:
    print("Score not high enough for excellent")


    # Transaction limit check

amount = float(input("Enter transaction amount: "))
account_type = input('Enter account type (Standard or Premium): ').strip()

# Normalize for comparison - to handle small/big letters
# .title() will make "standard" -> "Standard", "PREMIUM" -> "Premium"
account_type = account_type.title()

if account_type == "Standard":
    if amount > 500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved.")

elif account_type == "Premium":
    if amount > 1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")

else:
    print("Wrong account type")

    # 5. Even check with nested if

x = 7
y = 14

if x % 2 == 0:
    # x is even, now check y
    if y % 2 == 0:
        print("x and y are both even")
    else:
        print("Only x is even")
else:
    # x is odd, now check y
    if y % 2 == 0:
        print("Only y is even")
    else:
        print("Neither x nor y are even")

        x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x % 2 == 0:
    if y % 2 == 0:
        print("x and y are both even")
    else:
        print("Only x is even")
else:
    if y % 2 == 0:
        print("Only y is even")
    else:
        print("Neither x nor y are even")