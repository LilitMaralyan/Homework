"""dog"""
# dog_age = int(input("enter dog's age..."))
# if dog_age <= 2:
#     man_age = dog_age * 10.5
#     print(man_age)
# else:
#     man_age = (dog_age - (dog_age - 2)) * 10.5 + (dog_age - 2) * 4
#     print(man_age)

"""man"""
# man_age = int(input("enter man's age..."))
# if man_age == 10.5 or man_age == 21:
#     dog_age = man_age / 10.5
#     print(dog_age)
# elif man_age > 21:
#     dog_age = (man_age - 21) / 4 + 2
#     print(dog_age)

"""alphabet"""
# alphabet = input('Print a letter.....')
# vowel = 'aeiou'
# if alphabet in vowel:
#     print(alphabet, 'is a vowel')
# elif alphabet == 'y':
#     print(alphabet, 'sometimes is a vowel, sometimes not')
# else:
#     print(alphabet, 'is a consonent')

"""leap year"""
# year = int(input('print a year....'))
# if year % 4 == 0 or year % 400 == 0:
#     print(year, 'is a leap year')
# else:
#     print(year, 'is not a leap year')


"""odd or even"""
# number = int(input('print your number...'))
# if number % 2 == 0:
#     print('Your number is even')
# else:
#     print('Your number is odd')


"""game"""
import random
pc = random.randint(0, 5)
user = int(input('Enter your number in (0, 5) range'))
user_point = 0
pc_point = 0
if user is pc:
    user_point += 1
    print(user_point, '-', pc_point)
else:
    pc_point += 1
    print(pc_point, '-', user_point)

if user_point == 2:
    print('You win!')
elif pc_point > user_point and pc_point == 2:
    print('You lose!')











