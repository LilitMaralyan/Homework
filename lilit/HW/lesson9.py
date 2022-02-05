"""Take two int values from user and print greatest among them."""
# user1 = int(input('Print your number______'))
# user2 = int(input('Print your number______'))
# if user1 > user2:
#     print('User1 is greater')
# else:
#     print('User2 is greater')

"""Take input of age of 3 people by user and determine oldest 
and youngest among them.""" 
"""Albert jan sa stacvec ete 2 paymann el 
if-ov enq sarqum, bayc duq asel eiq vor karanq nayev elifi u elsei 
mej entapaymanner dnenq ifi elifi elsei tesqov... es depqum chashxatec.. 
mi hat dasi jamanak aseq eli vor pahn enq sxalvel"""

# person1 = int(input('Print your age_____'))
# person2 = int(input('Print your age_____'))
# person3 = int(input('Print your age_____'))
# Average_arith = (person1 + person2 + person3) / 3
# print('The arithmetic average is equal to', Average_arith)
# if person1 > person2 and person1 > person3 or person2 > person1 and person2 > person3 or person3 > person1 and person3 > person2:
#     if person1 > person2 and person1 > person3:
#         print("The first person is the oldest")
#     elif person2 > person1 and person2 > person3:
#         print('The second person is the oldest')
#     else:
#         print('The third person is the oldest')
# if person1 < person2 and person1 < person3 or person2 < person1 and person2 < person3 or person3 < person1 and person3 < person2:
#     if person1 < person2 and person1 < person3:
#         print('The first person is the youngest')
#     elif person2 < person1 and person2 < person3:
#         print('The second person is the youngest')
#     else:
#         print('The third person is the youngest')

"""You have number. Write a python program which to print a 
new number with digits reversed as of original one.
For example:
INPUT : 1234
INPUT : 5982
OUTPUT : 4321
OUTPUT : 2895"""

# number = int(input('Write a 4-digit number!_______'))
# d_4 = number % 10
# d_3 = (number // 10) % 10
# d_2 = (number // 100) % 10
# d_1 = number // 1000
# print(str(d_4) + str(d_3) + str(d_2) + str(d_1))

"""Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using 
following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in 
anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban 
areas only.
And any other input of age should print "ERROR"."""
"""sra verjin paymany kananc vra el petq a gorci?? es paymany chi ashxatum mots"""

user_age = int(input('Write your age!_____'))
user_sex = input('Are you a female or a male?_____')
# user_marital_status = input('Are you married?_____')
if user_sex == 'female' and user_age >= 20 and user_age <= 60:
    print('You will work in urban areas.')
elif user_sex == 'male':
    if user_age >= 20 and user_age <= 40:
        print('You can work everywhere.')
    elif user_age >= 40 and user_age <= 60:
        print('You will work only in urban areas.')
elif user_age < 20 or user_age > 60:
    print('Error!')

"""Rock, Paper, Scissors"""

# import random
# user_choice = input('Enter Rock, Paper or Scissors!_____')
# choice = ('Rock', 'Paper', 'Scissors')
# PC_choice = random.choice(choice)
# print(PC_choice)
# user_points = 0
# PC_points = 0






"""You (input) and pc have followers (pc have 
random followers) if your followers
is great 20 % than pc you are blogger otherwise 
pc is blogger."""

# import random
# You = int(input('Print the number of your followers!'))
# PC = random.randint(0, 10000000000)
# if You > 1.2 * PC:
#     print('You are a blogger!')
# else:
#     print('PC is a blogger!')

"""You and the Pc take part in the rally, You must 
pass 12 km. PC passed in 3 minutes and You are 
10% later than Pc. how much is the speed of 
your car."""

# S = 12
# PC_t = 3 / 60
# I_t = 1.1 * (3 / 60)
# I_speed = S / I_t
# print('My speed is', I_speed)


"""You should create two good new exercises using your ideas."""



"""Խնդիր֊֊֊֊֊֊֊֊Write a Python program to count the number of even and odd
numbers from a series of numbers(1-100)  ----- գիրք մինչև 80 էջ։"""

"""Հասկանալ թե ինչես են աշխատում split և join  ֆունկցիաները։"""

"""1.Մուտքագրել տարի,ամիս,ամսաթիվ,ինքը արտածի հաջորդ օրը(նույն կերպ)։
2.Մուտքագրել թիվ։Եթե թիվը բաժանվում է 2-ի,թող արտածի "yes",եթե 9-ի թող արտածի "no",եթե և՛ 2-ի,և՛ 9-ի"""


# number = float(input('Print your number!....'))
# if number % 2 == 0:
#     print('YES')
# if number % 9 ==0:
#     print('NO')
# elif number % 2 == 0 and number % 9 == 0:
#     print('YESNO')


"""write a python program where we have a rectangular find it’s area
2. write a python program which takes the age of 5 people and find the oldest the youngest and erkrachapakan mijin@
ogtagorcelov random"""

# length = float(input('print the number...'))
# width = float(input('Print the number...'))
# S = length * width
# print(S)

# import random
# age1 = random.randint(1, 105)
# print(age1)
# age2 = random.randint(1, 105)
# print(age2)
# age3 = random.randint(1, 105)
# print(age3)
# age4 = random.randint(1, 105)
# print(age4)
# age5 = random.randint(1, 105)
# print(age5)
# geom_mean = (age1 * age2 * age3 * age4 * age5) ** (1 / 5)
# print('The geometrical mean is equal to', geom_mean)
# if age1 > age2 and age1 > age3 and age1 > age4 and age1 > age5 or age2 > age1 and age2 > age3 and age2 > age4 and age2 > age5 or age3 > age1 and age3 > age2 and age3 > age4 and age3 > age5 or age4 > age1 and age4 > age2 and age4 > age3 and age4 > age5 or age5 > age1 and age5 > age2 and age5 > age3 and age5 > age4:
#     if age1 > age2 and age1 > age3 and age1 > age4 and age1 > age5:
#         print('The first person is the oldest')
#     if age2 > age1 and age2 > age3 and age2 > age4 and age2 > age5:
#         print('The second person is the oldest')
#     if age3 > age1 and age3 > age2 and age3 > age4 and age3 > age5:
#         print('The third person is the oldest')
#     if age4 > age1 and age4 > age2 and age4 > age3 and age4 > age5:
#         print('The forth person is the oldest')
#     if age5 > age1 and age5 > age2 and age5 > age3 and age5 > age4:
#         print('The fifth person is the oldest')
# if age1 < age2 and age1 < age3 and age1 < age4 and age1 < age5 or age2 < age1 and age2 < age3 and age2 < age4 and age2 < age5 or age3 < age1 and age3 < age2 and age3 < age4 and age3 < age5 or age4 < age1 and age4 < age2 and age4 < age3 and age4 < age5 or age5 < age1 and age5 < age2 and age5 < age3 and age5 < age4:
#     if age1 < age2 and age1 < age3 and age1 < age4 and age1 < age5:
#         print('The first person is the youngest')
#     if age2 < age1 and age2 < age3 and age2 < age4 and age2 < age5:
#         print('The second person is the youngest')
#     if age3 < age1 and age3 < age2 and age3 < age4 and age3 < age5:
#         print('The third person is the youngest')
#     if age4 < age1 and age4 < age2 and age4 < age3 and age4 < age5:
#         print('The forth person is the youngest')
#     if age5 < age1 and age5 < age2 and age5 < age3 and age5 < age4:
#         print('The fifth person is the youngest')



"""Խնդիր՝ Create python program where you want to check if input word is
palindrome or no .if yes print Open otherwise Trash
Sample Input:  RACECAR"""






























