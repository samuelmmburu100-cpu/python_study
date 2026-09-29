# 1. Take three inputs separately. Print the largest
# Hint: input() gives string, so convert to int

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest is:", num2)
else:
    print("Largest is:", num3)

# 2. Temperature check
temp = int(input("Enter temperature: "))

if temp > 30:
    print("The temperature is too high")
elif temp > 15:
    print("Normal temperature")
else:
    print("Cold temperature")

# 3. Check x between 10 and 20 inclusive and y > 100
x = int(input("Enter x: "))
y = int(input("Enter y: "))

if 10 <= x <= 20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")

# 4. Check password is "secret123"
password = input("Enter password: ")

if password == "secret123":
    print("Access granted")
else:
    print("Access denied")



    # 1. Date period check
start_date = '2024-01-01'
end_date = '2024-12-31'

if start_date < end_date:
    print("Valid period")
elif start_date > end_date:
    print("Invalid period")
else:
    print("One-day period")

# 2. String length check
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) > len(str2):
    print("str1 is longer")
elif len(str2) > len(str1):
    print("str2 is longer")
else:
    print("Both are of equal length")


    # 3. Check if user_id is in valid_ids
valid_ids = [101, 102, 103]
user_id = 105

if user_id in valid_ids:
    print("Access Granted")
else:
    print("Access Denied")

# 4. Detect type of value
value = "hello"  # try changing this to 100 or 3.5 or True to test

if type(value) == str:
    print("String Detected")
elif type(value) == int:
    print("Integer Detected")
else:
    print("Unknown Type")

