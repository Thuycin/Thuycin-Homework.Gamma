from pprint import pprint
from pprint import pp
empty = {}
empty = dict()
print(type(empty))

student = {
    "name": "Jack",
    "surname": "Jack",
    "age": 18,
    "email": "jack@example.com",
    "courses": ["Art","Math","Physics","PE"],
    "information": {
        "eye_colour": "blue",
        "hair_colour": "brown",
        "height": 178,
        "weight": 90,
    },
    "name": "Bob"
}

print(student["name"])

list_of_numbers = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]
count = {}
for num in list_of_numbers:
    count[num] = list_of_numbers.count(num)
print(count[1])
print(student)
print(student["courses"][1])
print(student["information"]["hair_colour"])
print(student.get("car_type"))

student["age"] = 20
student["car"] = {
    "make": "VW",
    "model": "Golf",
    "year": "2016",
}
student["car"].update(
 {"make": "Honda",
    "model": "Civic",
    "year": "2020",
    }
)
print(student)

student["car"].update(
 { "model": "Civic",
    "year": "2020",
    }
)
print(student)

student["car"].update(
    year=2020,
    make="Lambaghini")
print(student)
pprint(student)
deleted = student.pop("car")
deleted = student.popitem()
print(deleted)

del student["name"]
pp(student)
print(student.keys())
print(student.values())
print(student.items())
print(dict([("one", 1), "two", 2, "three", 3])) 