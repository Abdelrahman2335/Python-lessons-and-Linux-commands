x = """Welcome
to the world of
python programming"""

#You can't do this with one "".

# print(x)

name = "Abdelrahman"

# print(name[-1])
# print(name[0])
# print(name[:3])
# print(name[3:])

# print(name[15]) Why this is an error ? This is TypeError.

# x = "Welcome"
# y = "Welcome "
# print(x * 3)
# print(y * 3)

#Did you see the different ?

word = "Hello World"
# count = 0
# for Letter in word:
#     if Letter == "l":
#         count += 1
# print(count, "times letter l has been found")
    

My_str = "University"
x = list(enumerate(My_str))
y = enumerate(My_str)
# print('enumerate(My_str)',y)
# print('list(enumerate(My_str))', x)
# print(len(x))
#Did you see the different between x and y ?

#print("Tell me "what's your name?"") # this case an error.

# print("Tell me 'what's your name?'")
#OR

# print('''Tell me "what's your name?"''')
#OR

# print('Tell me "what\'s your name?"')
#OR

#print("Tell me \"what's your name?\"")

#print('C:\\Users\\dodom\\PycharmProjects\\pythonProject1')
#print("This line have a new line \n character \n:)")
#print("This line is having a tap \t character")
# print("ABC written in \x41\x42\x43 (HEX) representation ") # I didn't understand this one. :(

# day = "{} {} ^^ {}".format("Today", "is", "Sunday")
# day = "{2} {1} ^^ {0}".format("Today", "is", "Sunday")
# day = "{c} {a} ^^ {b}".format(a="Today", b="is", c="Sunday")

# print(day)

# print("Required binary representation of {0} is {0:b}".format(20))

# print("Exponent representation: {0:e}".format(1653.324))

# print("One third is:{0:.3f}".format(1/3))

x = "Good Morning Everyone!"
#print(x.lower())
#print(x.upper())
#print(x.find("E"))