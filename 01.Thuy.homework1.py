# NUMBER 1 - Age calculator
year_of_birth = input("Please enter your YoB (yyyy): ")
current_year = 2026
age = current_year - int(year_of_birth)
print(age)

# NUMBER 2 - Code Missing Part
x = 152
y = 132
print(x / y)
print(13*(x / y))
print(13*(x / y)**0.5)
print(int(float(13*(x / y)**0.5)))

# NUMBER 3 - Combine code into a separable variable
code_1 = '354'
code_2 = int(float(13*(x / y)**0.5))
code_3 = 132
new_code = code_1 + '-' + str(code_2) + '-' + str(code_3)
print(new_code)

# NUMBER 4 - Output a string using available variables
name = input("Please enter your name: ")
print("Hello ", name, "." "You are ", age, "years old. Your secret code is ", new_code, ".")