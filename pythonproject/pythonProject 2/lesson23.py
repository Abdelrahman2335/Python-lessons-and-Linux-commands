# Python Errors and Exceptions

# try:
#     """
#     The code which can give rise to an exception is written here.
#     """

#     x = "Hello"
#     y = int(x)
#     print("y =",y)
#     print("I'm DoDo here") # This line is unreachable CUZ there is an exception or error
# except:
#     print("There is an error here, please try again.")

#Catchiong specific exception

# counter = 0
# out = False
# while(counter <= 3 and not out ):
#     try:
#         a = int(input("Enter number:"))
#         b = int(input("Enter number:"))
#         c = a/b
#         if c < 0:
#             raise TypeError
#         # print("c =",c) # or 
#         print("{} / {} = {}".format(a,b,c))
#         out = True

    # except ZeroDivisionError:
    #     print("Division by zero is not possible")
    # except ValueError:
    #     print("Please enter only numbers")
    # except TypeError:
    #     print("The data is out of range")
    # counter += 1

#Exceptions can be raised also
# try:
    # raise TypeError
# except TypeError:
    # print("TypeError Exception caught!")

# Try..finally
# try:
#     print("In try block")
    #raise TypeError #If you raise this line except will got printed
# except:
#     print("In except block")
# finally:
#     print("In the finally block")