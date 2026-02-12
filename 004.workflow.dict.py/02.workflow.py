# a = 7
# b = 10
# print(a > b)
# print('a' > 'A')
# print('a -', ord('a'), 'A -', ord('A'))
# # print(chr(97), chr(65))
# # print('world' in 'hello world')
# # print(123 in [123, 456, 678])
# # x = -100
# # if x > 0:
# #     print("X is greater than 0")
# # name = input("Enter a name: ")
# # if len(name) > 0:
# #     print("Hello", name)
# # else:
# #     print("Hello stranger")
# idcode = '38803160272'
# if len(idcode) == 11:
#     print(idcode, 'is correct')
# else:
#     if len(idcode) < 11:
#         print(idcode, 'is too short')
#     else:
#         print(idcode, 'is too long')
# age = 20
# if age > 0 and age <= 12:
#     print("Child")
# elif age < 18:
#     print("Teenager")
# elif age < 65:
#     print("Adult")
# else:
#     print("Senior")
# If number divisible by 3 without remainder, print number and "FIZZ"
# If number divisible by 5 without remainder, print number and "BUZZ"
# If number divisible by 3 and by 5 without remainder, print number and "FIZZBUZZ"
# for num in range(101):
#     if num%3 == 0 and num%5 == 0:
#         print(num, "FIZZBUZZ")
#     elif num%5 == 0:
#         print(num, "BUZZ")
#     elif num%3 == 0:
        # print(num, "FIZZ")
# name = input("Enter name: ")
# if name.strip():
#     print("Hello,", name)
# else:
#     print("Hello, stranger")
# print(list(range(3, 10, 2)))
# for num in range(1, 11):
#     print(num)
# for num in [5, 6, 7, 8, 1, 2, 3, 4, 9, 10]:
#     print(num)
# print("Good bye")
# for letter in "Hello Python":
#     print(letter)
# number = [0, 2, 6, 3, 8, 77, 20, 1143, 85, 93, 12]
# evens = []
# odds = []
# for num in number:
#     if num = 1143:
#         continue
#     elif num == 93:
#         break
#     elif num % 2 == 0:
#         print(num, "EVEN")
#         evens.append(num)
#     else:
#         print(num, "ODD")
#         odds.append(num)
#     print(odds)
#     print(evens)
for num1 in range(10):
    for num2 in range(10):
        for num3 in range(10):
            print(num1, num2, num3)