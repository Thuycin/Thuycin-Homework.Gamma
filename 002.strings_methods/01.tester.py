# string1 = "hello"
# string2 = "hello"
# string3 = 'My favourite book is "Metro 2033"'
# string4 = 'That\'s is'
# # escapte symbol if needed
# string5 = "My favourite book is \"Metro 2033\""
# string6 = 'user\\new_folder'
# print("String1", string1)
# print("String2", string2)
# print(string6)

# string7 = "Hello" \
#     "World"
# print("String7: ", string7)

# string8 = '''Hello
# World
#         123123
#                         124
#                                 ASDG'''
# print(string8)

example1 = "Hello world world"

# start to count from 0
# print(len(example1))
# print(len(str(1647488)))
# print(example1[1])
# print(example1[-1])
# print(example1[17])
# print(example1[6:10])
# print(example1[-11:-3])
# print(example1[:-1])
# print(example1[6:])
# print(example1[::2])
# print(example1[::-1])
# print(example1.lower())

example2 = "firSt LEtTEr is NoT uPPERcaSE"

example4 = "der Fluß"
# string methods
# print(example4.casefold())
# print(example4.lower())
# print(len('that\s'))
# print(example2.title())

example3 = "  *  extra spaces in front and back *     "
# print(example3.strip())
# print(example3.strip(' *'))

# print(example1.replace("world", "planet"))
# print(example1.replace("world", "planet", 1))
# print(example1.replace("world", "", 1).replace(" ", "",1).upper()[6:11])
# print(example1[:12] + example1[:12] + )
# print(example1[:-1].replace("world"[::-1],"planet"[::-1],1)[::-1])
# print(example1.find("world"))
# print(example1.find("world",7))
# print(example1.find("world",7,15))
# print(example1.count("world"))
# print(example1.count("wwww"))
# print(example1[example1.find("world"):])
#HOMEWORK play with string method

a = "hello"
b = "world"
print(a, 123, 32.456, True, sep=", ", end="")
print()

name = "John"
salary = 2000
# template = "{}s salary is {}"
# print(template.format(name, salary))

# template = "{0}s {2}salary is {1},{0}{0}{1}"
# print(template.format(name, salary, 2026))

# product = "computer"
# price = 999
# template = "This {prod} costs {pr:.2f}$"
# print(template.format(pr=price,prod=product))

name = "Sarah"
salary = 3000
print(f"Highest salary of {name.upper()}'s is {salary:.2f}")

