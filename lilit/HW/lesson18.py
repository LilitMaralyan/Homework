"""Create new dictionary where you have
10 students and each of them have 
rating(1-10)."""

# newdict = {'st1':10, 'st2':8, 'st3':3, 'st4':5, 'st5':9, 'st6':8, 'st7':9, 'st8':8, 'st9':10, 'st10':2}
# print(newdict)

"""Create python program which will
calculate the arithmetic average of 
rating students."""

# newdict = {'st1':10, 'st2':8, 'st3':3, 'st4':5, 'st5':9, 'st6':8, 'st7':9, 'st8':8, 'st9':10, 'st10':2}
# summ = 0
# for i in newdict.values():
#     summ += i
# arithm = summ / 10
# print(arithm)

# newdict = {'st1':10, 'st2':8, 'st3':3, 'st4':5, 'st5':9, 'st6':8, 'st7':9, 'st8':8, 'st9':10, 'st10':2}
# print((sum(newdict.values())) / len(newdict)) 

"""Create a python program which will say
you who they are good and bad students."""

# newdict = {'st1':10, 'st2':8, 'st3':3, 'st4':5, 'st5':9, 'st6':8, 'st7':9, 'st8':8, 'st9':10, 'st10':2}
# for i in newdict.values():
#     if i > 7:
#         print('Good')
#     else:
#         print('Bad')

# newdict = {'st1':10, 'st2':8, 'st3':3, 'st4':5, 'st5':9, 'st6':8, 'st7':9, 'st8':8, 'st9':10, 'st10':2}
# new = {}
# for i in newdict.values():
#     if i >= 5:
#         new.setdefault(newdict.get, newdict.values)
# print(new)

"""Create a python program which will say
who have 5 or great rating in your 
Students."""

# newdict = {'st1':10, 'st2':8, 'st3':3, 'st4':5, 'st5':9, 'st6':8, 'st7':9, 'st8':8, 'st9':10, 'st10':2}

# for i in newdict.values():
#     if i >= 5:
        
"""Create a python program which will say
who have 5 or little rating in your 
Students."""

# newdict = {'st1':10, 'st2':8, 'st3':3, 'st4':5, 'st5':9, 'st6':8, 'st7':9, 'st8':8, 'st9':10, 'st10':2}
# for i in newdict.values():
#     if i <= 5:

"""Create a python program which will say
if your dictionary have this name 
print name and rating."""

# newdict = {'st1':10, 'st2':8, 'st3':3, 'st4':5, 'st5':9, 'st6':8, 'st7':9, 'st8':8, 'st9':10, 'st10':2}
# if 'st1' in newdict:
#     print('st1 :', newdict['st1'])
        
"""Create a new dictionary:
For example...
s = 'a,2,b,5,c,8,a,4,e,11'
{“a”:6,”b”:5,”c”:8,”e”:11}"""

# s = 'a,2,b,5,c,8,a,4,e,11'
# alpha = []
# digit = []
# for i in s:
#     if i.isalpha():
#         alpha.append(i)
# print(alpha)
# for j in s:
#     if j.isdigit():
#         digit.append(j)
# print(digit)

"""Create a dictionary from a string.
Track the count of the letters from the string. 
word = ‘exercises’
output: {“e”:3,”x”:1,”r”:1,”c”:1,”s”:2}"""

# word = 'exercises'
# temp_list = []
# for i in temp_list():
#     x = temp_list.count(i)
#     print(x)

"""Remove all duplicate items in list
input:
old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}] 
output:
new_list = [{'key1':'value1'},{},{'key2':'value2'}]"""

"""Create a python game Millionaire."""

print('Voxjuyn, eterum ov e uzum darnal milionater shown e! :D')
score = 0
while True:
    Q1 = input('harc a) b) c) d)---->')
    if Q1 == 'a':
        score += 500
        print(score)
        Q2 = input('harc a) b) c) d)---->')
        if Q2 == 'a':
            score += 500
            print(score)
            Q3 = input('harc a) b) c) d)---->')
            if Q3 == 'a':
                score += 1000
                print(score)
                Q4 = input('harc a) b) c) d)---->')
                if Q4 == 'a':
                    score += 2000
                    print(score)
                    Q5 = input('harc a) b) c) d)---->')
                    if Q5 == 'a':
                        score += 4000
                        print(score)
                        money = input('Do you want to continue or take your money? Print C for continue and T for taking the money ---> ')
                        if money == 'C':
                            Q6 = input('harc a) b) c) d)---->')
                            if Q6 == 'a':
                                score += 8000
                                print(score)
                                Q7 = input('harc a) b) c) d)---->')
                                if Q7 == 'a':
                                    score += 16000
                                    print(score)
                                    Q8 = input('harc a) b) c) d)---->')
                                    if Q8 == 'a':
                                        score += 32000
                                        print(score)
                                        Q9 = input('harc a) b) c) d)---->')
                                        if Q9 == 'a':
                                            score += 64000
                                            print(score)
                                            Q10 = input('harc a) b) c) d)---->')
                                            if Q10 == 'a':
                                                score += 128000
                                                print(score, 'And You Won The GAME!!! YOOHOO!!!!')
                                                break
                                            else:
                                                print('You lose!')
                                                break
                                        else:
                                            print('You lose!')
                                            break
                                    else:
                                        print('You lose!')
                                        break
                                else:
                                    print('You lose!')
                                    break
                            else:
                                print('You lose!')
                                break
                        elif money == 'T':
                            print('You won 8000!')
                            break
                    else:
                        print('You lose!')
                        break
                else:
                    print('You lose!')
                    break
            else:
                print('You lose!')
                break
        else:
            print('You lose!')
            break
    else:
        print('You lose!')
        break




















