# return "Hero" from a given string
example_string1 = "Hello bro"
print(example_string1[:1] + example_string[-2:])

# return ""Jack is my name"
example_string2 = "jack Is My NAME"
print((example_string2).capitalize())

#return "Get rid of junk please"
example_string3 = "%-Get rid of *junk* please*-L%*"
print(example_string3.replace("*","").strip("%-L"))

#return "Hello my name is Jack"
example_string4 = "hello my name is jack"
greeting = example_string4[0:example_string4.find("s")+1].capitalize()
name = (example_string4[example_string4.rfind(" ")+1:]).capitalize()
print(f"{greeting} {name}")
print(example_string4.capitalize().replace("jack", "Jack"))

#all occurrences of “Estonia” in a given string ignoring the case
example_string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."
print(example_string5.lower().count("estonia"))
print(example_string5.title().count("Estonia"))

#f-string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(f"{var2.capitalize()}, {var3.lower()} {var1.capitalize()}")

# Write a code to return byte_string text value

byte_string = b"\316\273"
print(byte_string.decode("utf-8")) # return lambda in Greek