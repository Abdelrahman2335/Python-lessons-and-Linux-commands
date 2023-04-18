# Name (also called identifier) is simply a name given to objects.

# We can get the address (in RAM) of some object through the built-in function, id().
# Note: You may get different value of id.

# a = 2
# print('id(2) =',id(2))
# print('id(a) =',id(a))

# print('\nid(3) =',id(3))
# print('id(a+1) =',id(a+1))

# Scope

def outer_function():
   global x
   x = 20


def inner_function():
    global x
    x = 30
    # print("x =",x)

inner_function()
print("x =",x)
x = 10
print("x =", x)
outer_function()
print("x =", x)
