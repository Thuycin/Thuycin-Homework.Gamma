# pi = 3.14159265
# print(f"Pi rounded to 2 decimal places: {pi:.2f}")
# print("Pi rounded to 2 decimal places: P{:.2f}".format(pi))

# text = input("How are you today?: ")
# tim = text.find("shit")
# tem = text.find("bad")
# print(f"Today/'s mood is ok" if {tim} == -1 and {tem} == -1 else "fuck!!!")

# text = input("How are you today? ").lower()
# bad_word = ["bad", "shit", "gloomy", "dark", "doomed", "dull"]
# if any(word in text for word in bad_word):
#     print("Sleep more, don/'t get out of the bed")
# else:
#     print("Fine, fund day to explore. Go, slay!")
bad_word = ["bad", "shit", "gloomy", "dark", "doomed", "dull"]
print("Ready for Mood survey? Type quit to exit anytime.\n")
while True:
    text = input("How are you today? ").lower()
    if text.lower() == "quit":
        break
    if any(word in text for word in bad_word):
        print("Sleep more, don/'t get out of the bed")
    else:
        print("Fine, fund day to explore. Go, slay!")