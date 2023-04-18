# https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=false
# n = int(input("Enter something: "))

# x = 0

# while x < n:
#     print(x * x)
#     x += 1

# n = int(input("Enter Number: "))
# x = n / 4

# if n % 4 == 0:
#     print(True,"and the divination is:",x)
# else:
#     print(False)

# def is_leap(year):
#     leap = True
# #
# #     # Write your logic here
# #
# #
# #
#     if (year % 4 != 0) and (year % 400 != 0) or (year % 100 == 0):
#         leap = False

#     else:
#         leap = True

#     if (year % 4 != 0) or (year % 100 == 0) and (year % 400 !=0):
#         leap = False
#     else:
#         leap = True

#     return leap
# year = int(input("Enter num: "))
# print(is_leap(year))


# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=false
# r = []
# for x in [1,2,3,4,5]:
#     for y in [6,7,8,9,10]:
#         r.append([x,y])

# x = int(input("num1:"))
# y = int(input("num2:"))
# z = int(input("num3:"))
# n = int(input("num4:"))
# r = []
# for i1 in range (0,x+1):
#     for i2 in range(0,y+1):
#         for i3 in range(0,z+1):
#             if i1+i2+i3 != n:
#                 r.append([i1, i2, i3])

# print(r)

# x = [1, 4, 10, 15, 42, 53, 46, 67, 23, 45, 77]
# x.sort()
# print(x[-2])
# y = max(x)
# z = min(x)
# print(y)
# print(z)
# print(x)


#The second bigest number: 

# n = int(input()) # Who many numbers you will enter

# arr = map(int, input().split()) # map object which is a lazy iterable, meaning it does not 
    # calculate the values until they are needed.

# we can't use max or print(arr[1]) cuz of map so we change it to [list]

# my_list = list(arr)


# max_num1 = max(my_list)

# max_num2 = []

# second_max = []

# for num in my_list:
#     if num != (max_num1):
#         second_max.append(num)
#     else:
#         max_num2.append(num)

# print(max(second_max))




students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# Find the second lowest grade
grades = sorted(set([student[1] for student in students]))
second_lowest_grade = grades[1]

# Find the students with the second lowest grade
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# Print the result
print(second_lowest_students)



# print(students[1][0])