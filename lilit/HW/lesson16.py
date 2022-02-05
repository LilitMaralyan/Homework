"""Write a Python program to sort a dictionary 
by value."""

# mydict = {'year1':1996, 'year2':1998, 'year3':1875}
# mydict.values()
# x = []
# for i in mydict.values():
#     x.append(i)
# x.sort()
# print(x)

"""Write a Python program to add a key to a 
dictionary."""

# mydict = {'year1':1996, 'year2':1998, 'year3':1875}
# mydict['year4'] = 2018
# print(mydict)

"""Write a Python program to check whether a 
given key already exists in a dictionary."""

# mydict = {'year1':1996, 'year2':1998, 'year3':1875}
# if 'year1' in mydict:
#     print('OK')
# else:
#     print('OH NO')

"""Write a Python program to merge two 
Python dictionaries.
dict1 = {'a': 50, 'b': 700}
dict2 = {'c': 400, 'd': 600}
output: {'a': 50, 'b': 700, 'c': 400, 'd': 600}"""

# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)
# print(dict1)

"""Write a Python program to multiply all the 
values in a dictionary.
For example:
mydict = {'a':1,'b':2,'c':12} output: 24"""

# mydict = {'a':1,'b':2,'c':12}
# c = 1
# for i in mydict.values():
#     c *= i
# print(c)

"""Create a Python program to find the highest 
3 values in a dictionary.
{'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
output: {'F': 69, 'A': 67, 'D': 56}"""

mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
newdict = {}
mykeys = sorted(mydict, key = mydict.get, reverse = True) [:3]
myvalues = sorted(mydict.values(), reverse = True) [:3]
for i, j in zip(mykeys, myvalues):
    newdict.setdefault(i, j)
print(newdict)












