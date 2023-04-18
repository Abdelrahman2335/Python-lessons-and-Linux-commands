#x = 20
#y = "40"
#z = 30

# print(type(y))
#print(type(x))
#print(type(z))

#y = int(y)
#print(type(y))

#result = x + z
#result2 = x + y  #This is cool!
#print(result)
#print(result2)

# file = open("lesson11.py","r+")
# print(file.read())
# print(file.write("""x = 20 
# y = "40" 
# z = 30 

# print(type(y))
# print(type(x)) 
# print(type(z)) 

# y = int(y) 
# print(type(y)) 

# result = x + z 
# result2 = x + y  
# print(result) 
# print(result2)
# """))


import os
a = os.getcwdb()
print(a)
os.chdir('/home/kali/pythonproject')
print(os.listdir())

