# Add name in original names list to sub-list (long and short) based on name length (5 chr)
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']
long_name = list()
short_name = []
for name in names:
    if len(name) > 5:
        long_name.append(name)
        print(long_name)
    else:
        short_name.append(name)
        print(short_name)

# find LEAP year (%4 = 0 %100 != 0)
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]
leap_year = list()
for year in years_list:
    if year % 400 == 0:
        leap_year.append(year)
    elif year % 4 == 0 and year % 100 != 0:
        leap_year.append(year)
print(leap_year)

# Ask user to input string then check if containing 1 unique chr
while True:
    thought = input("Please enter whatever is your first thought. (If stop, type E): ")
    a = thought.strip()

# break point
    if a.lower() == "e":
        print("BYE for now. SEE YOU NEXT TIME!")
        break
# main loop condition
    if len(a) == 1:
        print("Checked: thought has only one unique character. Very CONCISE thought!")
    else:
        print("Checked: NOT A SOLITUDE string")

# NESTED LIST - gender check
# Print "This is NAME SURNAME. S(he) is AGE years old"
people = [
    ('Jane', 'Smith', 26, 'Female'),
    ('Jack', 'Green', 30, 'male'),
    ('Maria', 'Gold', 29, 'female'),
    ('Simon', 'Bloom', 35, 'Male'),
]
num = len(people)
for num in range(len(people)):
    if people[num][3].strip().lower() == "female":
        print(f"This is {people[num][0].upper()} {people[num][1].upper()}. She is {people[num][2]} years old")
    else:    
        print(f"This is {people[num][0].upper()} {people[num][1].upper()}. He is {people[num][2]} years old")

# DICTIONARY - print name and courses for each student
students = [
    {
        "name": "Jack",
        "surname": "Smith",
        "courses": [
            "Math",
            "Physics",
            "Chemistry",
        ],
    },
    {
        "name": "Sarah",
        "surname": "Brown",
        "courses": [
            "Art",
            "Spanish",
            "Geography",
        ],
    },
    {
        "name": "Maria",
        "surname": "Gold",
        "courses": [
            "Englis",
            "Literature",
            "History",
        ],
    },
]
for num in range(len(students)):
    x = students[num]["name"]
    y = students[num]["courses"]
    print(f"Students name: {x}. Students courses: {y}.")