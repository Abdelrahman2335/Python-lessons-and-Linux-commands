email = "ali"
password = "123"
count = 0
limit = 2
out = False
x = input("Enter your email: ")
y = input("Enter your password:")
while x != email and y != password and not out:
    if count < limit:
        x = input("Try enter your email again: ")
        y = input("Try enter your password again: ")
        count += 1
    else:
        out = True

if out:
    print("Out of try")
else:
    print("Hello " + x)
#while y != password and not out:
#    if count < limit:
#        y = input("Try enter your password again:")
#        count += 1
#    else:
#        out = True

#if out:
#    print("Out of try")
#else:
#    print("Hello " + email)