'@@'-0,0 +1,37 
#custom functions
#don't add any logic
#only arrange code into reusable blocks
#creating custom functions
#define function using the def keyword
#followed by the name
#syntax below
#def function_name():
#block of code

#are of a square using a function
def square_area():
    side=10
    side=10
    area=side*side
    print(area)
square_area()

#area of circle
def circle_area():
    pi=3.14
    radius=20
    area=pi*radius*radius
    print(area)
circle_area()
#parameters are variables used inside a function
#arguments are exact values passed when calling a function
def square_area(side):
    area=side*side
    print(area)
square_area(10)

#funstion that calculates area of rectangle 
def rectangle_area(lenght,width):
    area=lenght*width
    print(area)
rectangle_area(20,10)

'@@' -1,11 +1,11 
#Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
lst7=list(range(1,4))
lst7=list(range(1))
print(lst7)
attempts=4
for i in lst7:
   pin=input('enter password')
   correct_pin='admin@123'
   if pin==correct_pin:
   'password'=input('enter password')
   correct_password='admin@123'
   if "password"=="password":
      print('Access Granted')
      break
   else:
      print('Invalid password')
      break
#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
#ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
#Display the total quantity of the 3 above.
numbers_1_to_50 = list(range(1, 51))
print("1. Numbers 1 to 50:")
print(numbers_1_to_50)
print("-" * 50)
