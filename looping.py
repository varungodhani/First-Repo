# 25. take a number from the user and check whether it is prime?

number = int(input("Enter a number:"))
for i in range(2,number):
    if number % i == 0:
        print("Its not a prime no.")
        break
else:
    print("Its a prime no.")

# 26. take a string from the user and check contains only digits or not?

string = input("Enter a string: ")
if string.isnumeric() == True:
    print("yes its all digits.")
else:
    print("no it contains characters.")

# 27. take a string from the user and check contains only  alphabets or not?

string = input("Enter a string: ")
if string.isalpha() == True:
    print("Its all alphabets.")
else:
    print("It contains digits.")

# 28. take a string from the user and check contains only  special chars or not?

string = input("Enter a string: ")
if string.isalnum() == True:
    print("Its contains alphanumeric values.")
else:
    print("It contains all special characters.")

29.take a string from the user and check contains only  capital letters or not?

string = input("Enter a string: ")
if string.isupper() == True:
    print("Its contains all capitals.")
else:
    print("It contains lowercase.")

# 30.take a string from the user and check contains only  small letters or not?
#
string = input("Enter a string: ")
if string.islower() == True:
    print("Its contains all lowercase.")
else:
    print("It contains uppercase.")

# 31. WAP to replace last n occurrence.

string = "Mymymymymymymymymy"
l = string.rfind("my", 3)
print(l)

32. WAP to checfhmdk given string contains numbers or not. it should consider float numbers also.

string = input("Enter a string: ")
if string.isalpha() == True:
    print("Its all alphabets.")
else:
    print("It contains digits.")


# 33. Convert the total string in to lower case. Without using lower() function.

string = input("Enter a sting:")
lower_string = ""
for i in string:
    if i.isalpha() and ord(i) < 91:
        temp = ord(i)
        temp = temp + 32
        i = chr(temp)
        lower_string = lower_string + i
    else:
        lower_string = lower_string + i

print(lower_string)


# 34. Convert the total string in to upper case. Without using upper() function.

string = input("Enter a sting:")
upper_string = ""
for i in string:
    if i.isalpha() and ord(i) > 96:
        temp = ord(i)
        temp = temp - 32
        i = chr(temp)
        upper_string = upper_string + i
    else:
        upper_string = upper_string + i

print(upper_string)

# 35. Show the below menu to the user until and until user select quit and display corresponding os message
#
# '''
# Menu:
# 1. windows
# 2. Linux
# 3. Mac
# 4. quit
# '''

user_choice = 0
while user_choice != "4":
    user_choice = input("Menu: \n 1. windows \n 2.Linux \n 3. Mac \n 4. quit \n Enter your choice:")
    if user_choice == "1":
        print("You have selected windows.")
    elif(user_choice == "2"):
        print("You have selected Linux.")
    elif(user_choice == "3"):
        print("you have seleted MAc.")
    else:
        print('Enter a valid choice.')
print("Thank you for using the app.")


# 37. take a string from the user and check contains at least one alphabets or not?

string = input("Enter the string:")
for i in string:
    if i.isalpha():
        print("It has an alphabet")
        break
else:
    print('There is no alphabet')

# 38. take a string from the user and check contains at least one chars or not?

string = input("Enter the string:")
if string != "":
    print("This string has characters")

else:
    print("This string has no characters.")

# 39. take a string from the user and check contains at least one capital letter or not?

string = input("Enter a string: ")
for i in string:
    if i.isupper():
        print("the string contains uppercase.")
        break
else:
    print("The string doesnt contain uppercase.")


# 40. take a string from the user and check contains at least one small letter or not?

string = input("Enter a string: ")
for i in string:
    if i.islower():
        print("the string contains lowercase.")
        break
else:
    print("The string doesnt contain lowercase.")

# 41. Print the first 100 odd numbers

count = 0
i = 0
while count != 100:
    if i % 2 != 0:
        print(i)
        count += 1
    i += 1

# 42. Determine the factors of a number entered  by the user

number = int(input("Enter the number you wish to find factors for: "))

for i in range(1,number+1):
    if number % i == 0:
        print(i)



# 43. Play a number guessing game (User enters a guess, you print YES or Higher or Lower). This should continue
# until and until user gives a correct number or want to quit in the middle.

import random
random_number = random.randint(1,20)
guess = 0
game = 0
while guess != random_number:
    game = int(input("1. to continue playing \n 2. to quit the game. \n Enter your choice: "))

    if game == 2:
        print("Thank you for playing.")
        break
    elif (game > 2) & (game == 0) :
        print("Enter legal value.")
        continue
    guess = int(input("Enter the guessed number: "))
    if guess < random_number:
        print("Your guess is lower than the number.")
    elif guess > random_number:
        print("Your guess is higher.")

else:
    print("you guessed the right number.")
    print("Thank you for playing.")

# 44. Take two numbers from the user a,b check whether a is divisible by b or not?

no1 = float(input("Enter a number to be divided: "))
no2 = float(input("Enter the divisor: "))
try:
    if no1 % no2 == 0:
        print("no1 is divisible by no2.")
    else:
        print("no1 is not divisible by no2.")
except:
    print("Enter a valid input.")


# 45. Find the sum of all the multiples of 3 or 5 below 1000
#
sum = 0
for i in range(1000):
    if (i % 3 == 0) or (i % 5 == 0):
        sum += i
print(sum)


# 46. Write a program to find out big of two numbers

no1 = float(input("Enter number 1: "))
no2 = float(input("Enter number 2: "))
if no1 > no2:
    print("no1 is greater.")
else:
    print("no2 is greater.")


# 47. Write a program to find out biggest number in the given numbers.

number = []
for i in range(10):
    user_number = float(input("Enter a number: "))
    number.append(user_number)
number.sort()
print("The biggest value is:", number[-1])

# 48. find out third occurrence of given substring
# 49. find out nth occurrence of given substring

def findnth(string, substring, n):
    temp = string.split(substring, n)
    print((temp[-1]))
    if len(temp) <= n:
        return -1
    else:
        print(len(string),len(temp[-1]),len(substring))
        return len(string)-len(temp[-1])-len(substring)




# 50. Take some single digit numbers from the user and findout min, maximum, sum, average
#
n = int(input("Enter the count of numbers you want to operate on: "))
min = 10000
max = 0
sum = 0
for i in range(n):
    user_number = float(input("Enter a number: "))
    sum = sum + user_number
    if max < user_number:
        max = user_number
    if min > user_number:
        min = user_number
average = sum / n
print(f"Sum={sum}\nAverage = {average}\nMinimum = {min}\nMaximum = {max}")

# 51. WAP> 10 -> 000010
#        		100 ->  000100
#       		1000 ->  001000
#  		 2345678  ->  2345678

string = input("Enter the string:")
print(string.zfill(6))



# 52. names  ="emp1,emp2,emp3,emp4" iterate through the employee names.

names  ="emp1,emp2,emp3,emp4"
list_names = names.split(",")
for i in list_names:
    print(i)

# 53. Take actual string, source string, destination string. replce first nth occurrences of source string with destination string of actual string.

actual_string = input("Enter a string: ")
source_string = input("Entyer a string to be replaced: ")
dest_string = input("Enter a string to be placed instead of the source string: ")
n = int(input("enter the number of occurences to be replace: "))
temp = actual_string.split(source_string, n)
new_string = dest_string.join(temp)
print(new_string)

# 54. Take a two numbers from the user and do below menu driven operations
# 1. addition
# 2. multiples
# 3.division
# 4.sqrt
# 5. pow    a**b
# 6.subtraction
# After selection do the corresponding operation.
# Note: user may give int, or float numbers. You should check whether it is proper digits or not. I.e the user given string should be in the position to convert to float.
# Other wise show the “inproper string given” Error.

import math
while True:
    try:
        no1 = float(input("Enter no1: "))
        no2 = float(input("Enter no2: "))
    except:
        print("Enter a number common!")
    enter_choice = int(input("1. addition\n 2. multiples\n3.division\n4.sqrt\n5. pow\n6.subtraction\nanything else to quit: "))
    if enter_choice == 1:
        print("addition: ", no1+no2)
        # continue
    elif enter_choice == 2:
        print("Multiplication: ", no1*no2)
        continue
    elif enter_choice == 3:
        if no2 != 0:
            print("division: ", no1/no2)
        else:
            print("Divisor cant be zero.")
        continue
    elif enter_choice == 4:
        print(f"Square root of no1:{math.sqrt(no1)}, Square root of no2: {math.sqrt(no2)} ")
        continue
    elif enter_choice == 5:
        print("no1 power no2: ", no1**no2)
        continue
    elif enter_choice == 6:
        print("Subtraction : ", no1-no2)
        continue
    else:
        break
print("Thank you")

# 56. l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4] find out how many even numbers are there
# and how many odd numbers are there and how many positive numbers are there and how many negative numbers are
# there and how many prime numbers are there and how many perfect numbers are there and how many Armstrong numbers are
# there and how many palindrome numbers are there.

l=[1,2,3,5,7,8,9,10,11,12,13,20,22,23,24,25,26,27,20,21,22,4]
even_count = 0
odd_count = 0
negative_count = 0
positive_count = 0
prime_count = 0
perfect_count = 0
arm_count = 0
palindrome_count = 0
for i in l:
    fact = 0
    if i % 2 == 0:
        print("Even: ", i)
        even_count += 1
    else:
        odd_count += 1
        print("ODD: ", i)
    if i < 0 :
        negative_count += 1
        print("Negative: ", i)
    else:
        positive_count += 1
        print("Positive: ", i)
    for j in range(2,i):
        if i % j == 0:
            fact = fact + j
    if fact == 0:
        prime_count += 1
        print("Prime: ", i)
    if (fact+1) == i:
        perfect_count += 1
        print("Perfect: ", i)
    arm_formula = ((i % 10)**3)+((i-(i%10))**3)
    if i == arm_formula:
        arm_count += 1
        print("Armstrong: ", i)
    str_i = str(i)
    if str_i == str_i[::-1]:
        palindrome_count += 1
        print("Palindrome: ", i)
print(f"Even count: {even_count}, Odd count: {odd_count}, Positive Count: {positive_count}, Negative count: {negative_count},"
      f"Prmie count: {prime_count}, Perfect count: {perfect_count}, Armstrong count: {arm_count}, Palindrome count: {palindrome_count}")

# 57. Take a string from the user and find out how many digits are there, how many special symbols are there,
# how many small letters are there, how many caps are there.

string = input("Enter a string: ")
lower_count = 0
upper_count = 0
digit_count = 0
special_count = 0
for i in string:
    if i.isalpha():
        if i.islower():
            lower_count += 1
        else:
            upper_count += 1
    elif i.isdigit():
        digit_count += 1
    else:
        special_count += 1
print(f"Lower count: {lower_count}, Upper count: {upper_count}, Digit count: {digit_count}, Special count: {special_count}")



# 58. Take a char from the user and find out how many number of occurrences are there in given string

string = input("Enter a string: ")
find_char = input(("Input the character to find: "))
char_count = 0
for i in string:
    if i == find_char:
        char_count += 1
print(char_count)


# 59. Take a element from the user and find out how many times the  element occurred in given list

l = [122,23,44,44,55,667,4,44,44,44,56,67]
n = 44
count = 0
for i in l:
    if i == n:
        count += 1
print(count)

# 60. Take a element from the user and find out how many number of occurrences are there in given tuple


# 61. Reverse the string without effecting the special symbols. It involves three variations. Write code for three variations.
# 62.Input: abc123,#$45def6%$^789$%^, output: $%^987%$^6fed54,#$321cba

s = "abc123,#$45def6%$^789$%^"
temp = s[::-1]
print
rev = ""
temp1 = ""
for i in temp:

    if i.isalnum() == False:
        temp1 = temp1 + i
        continue
    temp1 = temp1[::-1]
    rev = rev + temp1
    temp1 = ""
    if i.isalnum():
        rev = rev + i
        continue
print("The expected reverse string is: ",rev)


#63.Input: abc123,#$45def6%$^789$%^, output: 9876fe,#$d54321%$^cba$%^

s = "abc123,#$45def6%$^789$%^"
temp = s[::-1]
temp1 = ""
res = ""
for i in temp:
    if i.isalnum():
        temp1 += i
j = 0
for i in s:
    if i.isalnum():
        res += temp1[j]
        j += 1
    else:
        res += i
print("The required string is: ", res)

# 64.Inout: "123,#$456%$^789$%^", Output: 321,#$654%$^987$%^

s = "123,#$456%$^789$%^"
temp = ""
res = ""
for i in s:
    if i.isalnum():
        temp += i
        continue
    res += temp[::-1]
    temp = ""
    if i.isalnum() == False:
        res += i
print("The expexted string is: ", res)



# coding challenge
# from collections import defaultdict
# def blockStorageRewrites(blockCount, writes, threshold):
#     hset = set()
#     hmap = defaultdict(int)
#     temp = []
#     for write in writes:
#         for i in range(write[0], write[1]+1):
#             if hmap[i] < threshold - 1:
#                 hmap[i] += 1
#                 print(f"hmap[{i}]= {hmap[i]}")
#
#             else:
#                 if i not in hset:
#                     hset.add(i)
#     j = 0
#     while j < blockCount:
#         if j in hset:
#             start = j
#             while j in hset:
#                 j += 1
#             end = j-1
#             temp.append([start,end])
#         else:
#             j += 1
#     return temp
# b = 10
# w = [[0, 4], [3, 5], [2, 6]]
# t = 2
# print(blockStorageRewrites(b, w, t))







