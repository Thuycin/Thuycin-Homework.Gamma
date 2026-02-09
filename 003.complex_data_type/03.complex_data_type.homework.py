# Difference
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.difference(set_b))
print(set_b.difference(set_a))

# Create a string from a list and save it to variable
# Each name one new line
names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']
print(*names, sep="\n")

# sum of all numbers in a list
numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]
print(sum(numbers))

# sum of all unique numbers in a list
print(sum(set(numbers)))

# create a new list from studentsA and studentsB
# make sure there is no duplicates in a new lists
studentsA = ['Jack', 'Bob', 'Mary']
studentsB = ['Bob', 'Sarah', 'Simon']
A = set(studentsA)
B = set(studentsB)
print(A.union(B))

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