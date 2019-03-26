# 1.	Take the input from the user for(Total number of people,Number of seats for bus. Based on two inputs
# Decide how many number of buses required

people = int(input("Number of people: "))
seats = int(input("Number of seats in a bus: "))
if (people % seats) is 0:
    buses = int(people/seats)
else:
    buses = int(people/seats) + 1
print("Number of required buses are:", buses)

# # 2.take temperature from the user and convert foreign heat -> Celsius.

f = float(input("Enter temperature in fahrenheit: "))
c = float((f-32) * (5/9))
print("The temperature in celsius is: ", c)

# 3.take temperature from the user and convert Celsius → foreign heat.

c = float(input("Enter temperature in celsius: "))
f = float(c * 9/5 + 32)
print("The temperature in fahrenheit is: ", f)

# 4.take four number from the user
#  Do the below operations
#  aa)(a+b)**2, (c+d)**3
# ab)variance
# ac)standard deviation: sqrt(variance):  User math module. Math.sqrt(variance)
# ad)Regression
# 	y=mx+b
#           All a,b,c,d are consider as (x1,x2,x3,x4)
#           m=1.23
#           b=0.045
#           find out y
#           y=m*(x1+x2+x3+x4)+b
#  ae)Find the average of four numbers
# af)Find the sum of four numbers

import math
x1 = float(input("Enter the value of x1: "))
x2 = float(input("Enter the value of x2: "))
x3 = float(input("Enter the value of x3: "))
x4 = float(input("Enter the value of x4: "))

aa = (x1 + x2)**2
aa2 = (x3 + x4)**3
print(("Evaluating equation aa and aa2: ", aa, aa2))
xbar = float(x1 + x2 + x3 + x4)/4
variance = float((x1 - xbar)**2+(x2 - xbar)**2+(x3-xbar)**2+(x4-xbar)**2) / 4
print("The variance is:", variance)
sd = float(math.sqrt(variance))
print("The standard deviation is: ", sd)
m = 1.23
b = 0.045
y = m*(x1+x2+x3+x4) + b
print("Regression value:", y)
average = (x1+x2+x3+x4)/4
print("Average is:", average)
sum = (x1+x2+x3+x4)
print("sum is: ", sum)

# 5.Take the distance in km
#     	Show that in cm, meters, in milli meters, cents, feets

d = float((input("Enter distance in km:")))
print("In meters:", (d*1000))
print("In centi meters", (d*100000))
print("In mm: ", (d*10000000))
print("In feet:", (d*3280.84))

# 6.Take the size of your hard disk in GB
#      	Show that in MB, KB, TB,

gb = float((input("Enter memory in gb:")))
print("In mb:", (gb*1024))
print("In kb", (gb*1024*1024))
print("In tb: ", (gb/1024))

# 7.  Take name, age, height from the user and print like below
# The details of the person: Name:name of the person, Age:age of the person, Height:height of the person
# Note: make sure that no space between : and a value and should be space after “COMA”

name = input("Enter name:")
age = int(input("Enter age:"))
height = float(input("Enter height:"))
print("Name:%s, Age:%s, Height:%s" % (name, age, height))

# 8. BMI calculation: take required parameters for BMI calculation from the user and calculate BMI of the person.

weight = float(input("Enter weight in pounds:"))
height = float(input("Enter height in inches:"))
BMI = (weight*0.45)/(height*0.025)**2
print("The BMI is:", BMI)

# 9. name="Jayaram"
# age=1.6
# height=3.5356234
# weight=10.343856783
# By using above inputs print the output
# Name:Jayaram, Age:1.6, Height:3.54, Weight:10.344
# Note: Use format specifiers(%s, %d, %f)

name = "Jayaram"
age = 1.6
height = 3.5356234
weight = 10.343856783
print("Name:%s, Age:%.1f, Height:%.2f, Weight:%.3f" % (name, age, height, weight))

# 10. Take three upper case letters from the user convert in to small case.

upper = input("Enter three upper case letters:")
print(upper.lower())

# 11. take base and exponent value from the user and print like in mathematics:
#   example: base=2, exponent=3: 23

base = float(input("Enter value of base:"))
exponent = float(input("Enter value of exponent:"))
print("The value is:", (base*10+exponent))

# 12. Take some groceries cost prices and print total cost and average cost, what is the max cost, what is the
# minimum cost.

mango = float(input("Enter value of mango:"))
apple = float(input("Enter value of apple:"))
banana = float(input("Enter value of banana:"))
cilantro = float(input("Enter value of cilantro:"))

Total = mango + apple + banana + cilantro
average = Total/4


