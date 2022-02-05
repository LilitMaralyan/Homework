"""Write a Python program to check if pc
number is great than 10. random(1,20)
when True break."""

# import random
# while True:
#     number = random.randint(1, 20)
#     if number >10:
#         print(number)
#         break
#     else:
#         print(number)
#         continue

"""chinga chung"""

import random

possibles = 'Rock', 'Paper', 'Scissors'
user_points = 0
pc_points = 0
while True:
    user = input('Print \n\tRock \n\tPaper \n\tScissors ---->')
    pc = random.choice(possibles)
    print(pc)
    if user == 'Rock' and pc == 'Scissors' or user == 'Paper' and pc == 'Rock' or user == 'Scissors' and pc == 'Paper':
        user_points += 1
        print(f'User point is {user_points} and pc point is {pc_points}')
        if user_points == 2 and user_points < 3 and user_points > 0:
            print('User WIN')
            break
        else: continue
    elif user == 'Rock' and pc == 'Paper' or user == 'Paper' and pc == 'Scissors' or user == 'Scissors' and pc == 'Rock':
        pc_points += 1
        print(f'Pc point is {pc_points} and user point is {user_points}')
        if pc_points == 2 and pc_points < 3 and pc_points > 0:
            print('PC WIN')
            break
        else:
            continue
    elif user == pc:
        user_points += 0
        pc_points += 0
        print(f'Pc point is {pc_points} and user point is {user_points}')
        continue






































