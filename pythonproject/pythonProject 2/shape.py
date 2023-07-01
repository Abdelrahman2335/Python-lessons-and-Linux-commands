# A program to display a pattern using loops

# n = int(input("Enter number:"))
# i = 1 
# while i <= n:
#     j = 1
#     while j <= (n - i):
#         print(" ",end="")
#         j += 1
#     j = 1 
#     while j <= (2*i - 1):
#         print("*",end="")
#         j += 1
#     i += 1
#     print()


n = int(input("Enter number:"))
m = (n+1)/2
i = 1 
while i <= n:
    if(i > m):
        b = n - i
        s = 2 * (i - m) + 1
    else:
        b = i - 1
        s = 2 * (m - i) + 1
    j = 1
    while j <= b:
        print(" ",end="")
        j += 1
    j = 1 
    while j <= s:
        print("*",end="")
        j += 1
    i += 1
    print()


# . => n - i
# * => 2 * i - m) + 1

#  . => i - 1
#  * => 2 * (m - i) + 1

#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#  *********
#   *******
#    *****
#     ***
#      *