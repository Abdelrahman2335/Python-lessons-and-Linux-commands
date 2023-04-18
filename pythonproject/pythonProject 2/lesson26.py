students = {1: {"Name": "Ahmed", "Student ID": "22230571", "Level": "1", "GPA": "3.60"},
            2: {"Name": "Salma", "Student ID": "22230478", "Level": "1", "GPA": "3.50"}}

students[3] = {}

# Nested Dictionary

# adding data to students[3]...

# students[3]["Name"] = input("Name: ") This is the coolest one :D

students[3]["Name"] = "Khalid"
students[3]["Student ID"] = "22230544"
students[3]["Level"] = "1"
students[3]["GPA"] = "3.50"

# print(students.items())

# Here python understand that x is the id or the number of the dict and y is the information ^O^

# for x_id,y_info in students.items():
#     print("\nStudent",x_id)

#     for key in y_info:
#         print(key + ":", y_info[key])

print(type(students))

for key in students:
    students[key]["GPA"]