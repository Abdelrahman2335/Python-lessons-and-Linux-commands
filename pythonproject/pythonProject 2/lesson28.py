'''
Sometimes, when writing a Python function, you may not have the actual implementation 
ready yet, but you still need to define the function so that you can call it later. 
In such cases, you can use the 'pass' statement as a placeholder for the function body,
 like this:
'''
def my_function():
    pass

# you can also use pass in loop for example: 

for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)

x = 15

if x < 10:
    pass
else:
    print("x is greater than or equal to 10")
