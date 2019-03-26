# 13. Take the input from the user for(Total number of people, total number of buses,
# Number of seats for bus, adjust factor).
# Based on four inputs
# Decide whether there is sufficient buses or not and give solution for how many extra buses required.

# 14.Take number from the user decide whether it is even or odd.

number = float(input("Enter a whole number: "))
if number % 2 == 0:
    print("The number is prime.")
else:
    print("The number is odd.")

# 15.take number from the user decide whether it is positive number or negative number.

number = float(input("Enter a number:"))
if number < 0:
    print("Number is negative.")
else:
    print("Number is positive.")

# 16.take a string from the user print the length. if the user not given anything then show an error message

strings = input("Enter a string: ")
if str != '':
    print(len(strings))
else:
    print("you must enter a valid string")

# 17.code to perform mathematical operations. take two numbers from the user and show the below menu
# 	1. add,
# 	2. sub,
# 	3. mul,
#  	4.div,
# 	5.quit
# 	Enter an option:
# 		based on the option need to perform an operations

number1 = float(input("Enter a number:"))
number2 = float(input("Enter a number:"))
operation = int(input("Enter your preference, 1 for add \n 2 for sub \n 3 for mul \n 4 for div \n 5 to quit: "))
if operation != 5:
    if operation == 1:
        print("addition is: ", number1+number2)
    elif operation == 2:
        print("subtraction is: ", number1-number2)
    elif operation == 3:
        print("multiplication is: ", number1*number2)
    elif operation == 4:
        print("division is: ", number1/number2)
    else:
        print("Enter a valid operation.")
else:
    print("Thank you for using the app.")

# 18. show the menu:
#    		 1. kids
#     		2. Men's
#    		 3. Women's
#     		Show the corresponding message based on the selection. Mention error 	message if he enter >3.

classify = float(input("Enter a category from Menu: \n 1. kids \n 2. Men's \n 3. Women's \n"))
if classify == 1:
    print("you are a kid.")
elif classify == 2:
    print("You are a male.")
elif classify == 3:
    print("you are a female.")
else:
    print("Enter a valid value.")

# 19. write a program to check given substring is there in actual string or not?
# example: act="python is a pure object oriented programing language"
# check whether “pure” is there in act or not.
# Note: Use in operator

given_string = input("Enter a string: ")
sub_string = input("Enter a substring to check: ")
if sub_string in given_string:
    print("yes it is present.")
else:
    print("It does not belong to the given string.")

# 20. Take three numbers from the user and decide which is big

number1 = float(input("Enter a number:"))
number2 = float(input("Enter a number:"))
number3 = float(input("Enter a number:"))

if number1 > (number2 and number3):
    print("The biggest number is:", number1)
elif number2 > (number1 and number3):
    print("The biggest number is:", number2)
else:
    print("The biggest number is:", number3)

# 21. Take age and gender from the user and decide whether he is eligible for 	marriage in India or not.
# Age criteria: men age>22, women>18

age = float(input("Enter your age:"))
gender = input("Enter your gender: \n male or female: ")
if gender == "male":
    if age > 22:
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")
elif gender == "female":
    if age > 18:
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")

# 22. Take an age  and gender from the user: and mention that what he/she can 	do in india.
# 	"""
# 		conditions
# 1. Theatre: 5 for men 7 for women
#     	2. Voting system: 18 for men and women
#     	3. Marriage in india: 23 for men and for women >21
#     	4. For govt jobs: (min:18, max:32)  for men and (min:18, max:34) for 	women
#    	 	5. For driving licence: (min:18, max:60) for men and women
# 	Eligibility:
#    		1. theatre
# 			2.  Voting system
# 			3.  Marriage in india
# 			4.  For govt jobs
# 			5. For driving licence:
# 	Enter an option:
# 		Gender:
# 			1. men
# 			2. women
# 	Enter an option:
# 		Enter an age of person:

age = float(input("Enter your age:"))
gender = float(input("Enter your gender: \n 1. male \n 2. female \n "))

if gender == 1:
    if age > 5:
        print("You are eligible for theatre.")
    else:
        print("You are not eligible for theatre.")
    if age >= 18:
        print("you are eligible for voting.")
    else:
        print("you are not eligible for voting.")
    if age > 21:
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")
    if (age >= 18) and (age <= 34):
        print("you are eligible for gov jobs.")
    else:
        print("you are not eligible for gov jobs.")
    if (age >= 18) and (age <= 60):
        print("you are eligible for drivers' license.")
    else:
        print("you are not eligible for drivers' license.")

elif gender == 2:
    if age > 7:
        print("You are eligible for theatre.")
    else:
        print("You are not eligible for theatre.")
    if age >= 18:
        print("you are eligible for voting.")
    else:
        print("you are not eligible for voting.")
    if age > 23:
        print("You are eligible for marriage.")
    else:
        print("You are not eligible for marriage.")
    if (age >= 18) and (age <= 32):
        print("you are eligible for gov jobs.")
    else:
        print("you are not eligible for gov jobs.")
    if (age >= 18) and (age <= 60):
        print("you are eligible for drivers' license.")
    else:
        print("you are not eligible for drivers' license.")

else:
    print("Enter a valid input.")

# 23. operating systems:
# 	1.windows
# 	2.android
# 	3.mac
# Enter an option:
#
# If the user enters 1 then show "Goto first floor and buy windows laptop or mobile"
# If the user enters 2 then show "Goto second floor and buy adroid mobiles"
# If the user enters 3 then show "Goto third floor and buy mac laptop or iphones"
# If the user enters other than 1 or 2 or 3 then show "There is only three floors, please select 1 or 2 or 3"

os = float(input("Enter from the menu: \n 1 for windows \n 2 for android \n 3 for mac \n"))
if os == 1:
    print("Goto first floor and buy windows laptop or mobile.")
elif os == 2:
    print("Goto second floor and buy android mobiles.")
elif os == 3:
    print("Goto third floor and buy mac laptop or iphones.")
else:
    print("There are only three floors, please select 1 or 2 or 3.")

# 24.Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.

age = float(input("Enter your age:"))
if age > 0:
    if (age <= 1):
        print("You are a baby.")
    elif age <= 3:
        print("You are a toddler.")
    elif age <= 12:
        print("You are a child")
    elif age <= 19:
        print("You are a teenager.")
    elif age <= 50:
        print("You are an adult.")
    elif age > 50:
        print("You are an old codger.")
else:
    print("enter a valid age.")


# 24.Take two number a,b from the user and check whether a is divisible by b or not

a = float(input("Enter a no. = "))
b = float(input("Enter a 2nd no. = "))
if a % b == 0:
    print("a is divisible by b.")
else:
    print("a is not divisible by b.")

