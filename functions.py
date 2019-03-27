# FUNCTIONS:
# 	65. rewrite above assignments by functions. Can use string functions to solve the string related assignments
# STRINGS
# 66. take a number from the user and check whether it is prime?


def getprime(user_no):
    for i in range(2, user_no):
        if user_no % i == 0:
            return print("It's not a prime no.")
    else:
        return print("It's a prime no.")


# 67. take a string from the user and check contains only digits or not?


def check_digits(string):
    for i in string:
        if i.isdigit():
            continue
        else:
            return print("The string doesnt contain all digits.")
    return print("The string contains all digits.")


# 68. take a string from the user and check contains only  alphabets or not?


def check_alpha(string):
    for i in string:
        if i.isalpha():
            continue
        else:
            return print("The string doesnt contain all alphabets.")
    return print('The string contains all alphabets.')


# 69. take a string from the user and check contains only  special chars or not?


def check_special(string):
    for i in string:
        if i.isalnum() == False:
            continue
        else:
            return print("not all special chars.")
    return print("all special chars.")


# 70. take a string from the user and check contains only  capital letters or not?


def check_upper(string):
    for i in string:
        if i.isupper():
            continue
        else:
            return print("Not all capitals.")
    return print("All uppercase letters.")


# 71. take a string from the user and check contains only  small letters or not?


def check_lower(string):
    for i in string:
        if i.islower():
            continue
        else:
            return print("Not all lower case.")
    return print("All lowercase.")


#  72. WAP to replace last n occurrence.
#  76.replace last two occurrences of given source string with destination string
#  preserve the delimiter after split.


def replace_substring(string, source_string, dest_string, n):
    temp = string.rsplit(source_string, n)
    return print(dest_string.join(temp))


# 73. WAP to check given string contains numbers or not. it should consider float numbers also.


def contain_no(string):
    for i in string:
        if i.isdigit():
            return print("It does contain numbers.")
        else:
            return print("IT doesnt contain numbers.")


# 74. Convert the total string in to lower case.
# Convert the total string in to upper case.

def convert_lower(string):
    return print(string.lower())


# 75. Convert every word start letter into caps. Some how title not working
# if it contains numbers and special symbols in the word


# 77. write a program to chcek given substring is there in actual string or not? (search should be case insensitive)
# example: act="python is a pure object oriented programing language"
# 78.check whether “pure” is there in act or not.
# Note: Use in operator

def string_present(string, sub_string):
    if sub_string in string:
        return print("Yes its present in the string.")
    else:
        return print("Its not present in the string.")




