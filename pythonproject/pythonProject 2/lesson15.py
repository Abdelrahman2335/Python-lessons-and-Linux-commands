# Global and Local variable with different name.
# Global variable can be accessed from any where.

a = 5
def function_2():
   a = 10
   print("Local a =",a)  # Local variables are accessed from the block where it is defined only.
function_2()
print("Global a =",a)

# Creating and using a Non-local variable.

def outer():
   x = "local"

   def inner():
       nonlocal x  # See the different when you # this one.
       x = "Nonlocal"
       print("inner:", x)
   inner()

   print("outer:", x)
outer()