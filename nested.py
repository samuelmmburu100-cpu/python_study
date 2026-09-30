         # Nested if
# series of if statement inside another statement
# nested if statement depends on the results of the previous condition
# if condition1:
     # if condition2:
          #
        # else:
#else:
1.# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive
# 1. Age and drivers license check

age = int(input("Enter your age: "))

if age >= 18:
    license = input("Do you have a driver's license? (yes/no): ").lower()
    
    # Nested if
    if license == "yes":
        print("You are eligible to drive")
    else:
        print("You are not eligible to drive")
else:
    print("You are too young to drive")

# 2. Credit score and income check

credit_score = int(input("Enter your credit score: "))

if credit_score > 700:
    income = int(input("Enter your annual income: "))

    # Nested if
    if income > 50000:
        print("Loan approved.")
    else:
        print("Income requirement not met.")
else:
    print("Credit score too low.")
           
           









