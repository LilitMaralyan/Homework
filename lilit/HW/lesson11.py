"""Write a Python program to find the smallest number which are 
divisible by 12 and 15."""

# number1 = int(input('Print the number---->'))
# number2 = int(input('Print the number---->'))
# ref = range(number1, (number1 * number2) + 1)
# for i in ref:
#     if i % number1 == 0 and i % number2 == 0:
#         print(i)
#         break

"""Write a Python program to count the number of even and odd 
numbers from a series of numbers(1-100)."""

# even = 0
# odd = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f'The quantity of even and odd numbers are accordingly {even} and {odd}.')

"""Write a Python program to get the Fibonacci series between 0 
to 40:
Fib_num = 0,1,1,2,3,5,8 ....."""

# num = int(input('Print the series --->'))
# a1 = 0
# a2 = 1
# i = 0
# while num <= 0:
#     num = int(input('Enter the positive one --->'))
#     continue
# while num == 1:
#     print(a1)
#     print(num)
#     break
# else:
#     print('Fibonaaci --->')
#     for i in range(num):
#         print(a1)
#         gumar = a1 + a2
#         a1 = a2
#         a2 = gumar
#         # i += 1

        

"""Write a Python program that accepts a string and calculate 
the number of digits and letters.
string = ‘python 3.9’"""

# word = input('Print a word --->')
# gumar = 0
# for i in str(word):
#     if i.isdigit():
#         gumar += int(i)
# print(gumar)

# word = input('Print a word --->')
# gumar = 0
# for i in str(word):
#     if i.isdigit():
#         gumar += int(i)
# print(f"{gumar}")

"""Albert jan es meky nayeq ha, en pahn em uzum anel vor 
21 + 23 ani voch te arandzin tvnashanner.. bayc mek inputov 
chi lini vonc patkeracnum em"""


        

"""Write a Python program which have number (73421):
You should calculate (7 + 3 + 4 ....):"""

# num = int(input('Print the number --->'))
# gumar = 0
# for i in str(num):
#     if i.isdigit():
#         gumar += int(i)
# print(gumar)

"""Write a loop to find the factorial of any number. You have one 
input."""

# num = int(input('Print the number --->'))
# fac = 1
# if num == 0:
#     print(1)
# else:
#     while num >= 1:
#         fac *= num
#         num -= 1
#     print(fac)

"""Write a python program to check if user age in (18-20) and if 
sex is male."""

# age = int(input('Print your age, please! --->'))
# sex = input('Are you male or female? --->')
# if 18 <= age <= 20 and sex == 'male':
#     print('OK')
# else:
#     print('ERROR!')


"""You should create four good new exercises
using your ideas."""

"""Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 2        OUTPUT: 2
INPUT: -2       OUTPUT: 2"""

# number = float(input('Enter the number --->'))
# if number < 0:
#     print(number * (-1))
# elif number == 0:
#     print(0)
# else:
#     print(number)

"""Write a program to print first 10 integers and their squares using while loop."""

# number = 1
# print('numbers \t\t\t\tsquares')
# while number <= 10:
#     print(number, '\t\t\t\t', number ** 2)
#     number += 1

"""Write a program to find the sum of following series"""
"""1 + 4 + 9 + 16 + 25 ... + n"""

# number = int(input('Print your number --->'))
# i = 1
# s = 0
# while i <= number:
#     s += (i ** 2)
#     i += 1
# print(s)



"""others' problems"""
"""գրել Python ծրագիր, որը կհաշվի 1-ից n թվերի թվաբանական միջինը։

գրել Python ծրագիր, որը կհաշվի աճող երկրաչափական պրոգրեսիայի 
(b1>0, q>1) n անդամների գումարը։"""

n = int(input('Print your number --->'))
gumar = 0
for i in range(1, n + 1):
    gumar += int(i)
    tv_mijin = gumar / n
print(gumar)
print(tv_mijin)

# b1 = int(input('Enter your first positive number --->'))
# if b1 <= 0:
#     b1 = int(input('Error! Enter the positive one, please! --->'))
# q = int(input('Enter the positive ratio --->'))
# if q <= 0:
#     q = int(input('Error! Enter the positive one, please! --->'))
# n = int(input('What\'s the quantity of your numbers? --->'))
# if n <= 0:
#     n = int(input('Error! Enter the positive one, please! --->'))
# S_n = (b1 * (q ** n - 1)) / (q - 1)
# print(S_n)

"""FizzBuzz is a well known programming assignment, asked during 
interviews.
The given code solves the FizzBuzz problem and uses the words 
"Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers which are multiples of both 3 and 5, output "SoloLearn"."""

# n = int(input('Enter your number --->'))
# if n % 3 == 0 and n % 5 == 0:
#     print('SoloLearn')
# elif n % 3 == 0 or n % 5 == 0:
#     if n % 3 == 0:
#         print('Solo')
#     elif n % 5 == 0:
#         print('Learn')

"""python""" """sa der chi stacvum :("""

# str = "PYTHON"
# i = 0
# for i in len(str):
#     while i < len(str):
#         print(str[i])
#         i = i + 1
#         continue

"""խնդիր 1
11:37
Write a Python program to create the multiplication table (from 1 to 10) of a number, by using input.
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20 (edited) """

# num = int(input('your num ---'))
# i = 1
# while i <= 10:
#     print(f'{num} x {i} = {i * num}')
#     i += 1

"""A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade."""

# mark = float(input('Print your mark, please --->'))
# if mark < 25:
#     print('F')
# elif 25 <= mark < 45:
#     print('E')
# elif 45 <= mark < 50:
#     print('D')
# elif 50 <= mark < 60:
#     print('C')
# elif 60 <= mark < 80:
#     print('B')
# else:
#     print('A')




