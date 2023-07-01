# if...elif..else
age = int(input("Enter the age of the person..."))
if age < 5:
    print("Too young")
elif age == 5:
    print("Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade)) # this is old way to writ 
    print(f"Go to{grade} grade") # this is easiast way to writ 
else:
    print("Go to collage")
    
    
print(f'you are {age} years old')


# num = float(input("Please enter number:"))
# if num == 0:
#     print("Zero")
# elif num > 0:
#     print("Positive number")
# else:
#     print("Negative number")