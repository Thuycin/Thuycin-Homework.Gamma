# Difference
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print('Set A unique items:', set_a.difference(set_b))
print('Set B unique items:',set_b.difference(set_a))

# Create a string from a list and save it to variable
# Each name one new line
names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']
print(*names, sep="\n")
print('\n'.join(names))

# sum of all numbers in a list
numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]
print(sum(numbers))

# sum of all unique numbers in a list
print(sum(set(numbers)))

# create a new list from studentsA and studentsB
# make sure there is no duplicates in a new lists
studentsA = ['Jack', 'Bob', 'Mary']
studentsB = ['Bob', 'Sarah', 'Simon']
studentsC = list(set([*studentsA, *studentsB]))
print(studentsC)
# What elements are common for both tuples?
numbersA = (23, 52, 12, 75, 42)
numbersB = (75, 22, 42, 94, 70)
SetA = set(numbersA)
SetB = set(numbersB)
elements = SetA.intersection(SetB)
print(*elements)

# add 5 to correct index
a = (1, 2, 3, 4, 6, 7, 8)
lst = list(a)
lst.append(5)
lst.sort
a = tuple(lst)
print(a)
# b = a[:4] + (5,) + a[4:]
# print(b)
# a = list(a)
# a.insert(4,5)
# a = tuple(a)
# print(a)