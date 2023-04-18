# def hello1():
    # print("Hello! I love code in python.")
# 
# def hello2():
    # '''
    # Test
    # multiline 
    # text'''
    # return "Hello! I love code in python."
# 
# hello1()
# print(hello2())
# print(hello2.__doc__)

def myaddition(x,y):
    print("Performing the addition operation...")
    return (x+y)
def mysubraction(x,y):
    print("Performing the subtraction operation...")
    return(x-y)
def mymultiplication(x,y):
    print("Performing the multiplication operation...")
    return(x*y)
def mydivision(x,y):
    print("Performing the division operation...")
    return(x/y)
def mymenu():
    print("Main Menu")
    print('''1 > Addition operation
2 > Subtraction operation
3 > Multiplication operation
4 > Dividision operation''')
    choice = int(input("Enter the number of the operation:"))
    return choice
def calculation():
    x = mymenu()
    num1 = int(input("Please enter the first number:"))
    num2 = int(input("Please enter the second number: "))
    if x == 1:
        result = myaddition(num1,num2)
    elif x == 2:
        result = mysubraction(num1,num2)
    elif x == 3:
        result = mymultiplication(num1,num2)
    elif x == 4:
        result = mydivision(num1,num2)
    else:
        print("Erorr")
    print("The output is:", result)


    
calculation()