#this is a different ways how you can write the result of class

class Number:
    def __init__(self,real = 0, image = 0):
        print("Number constructor executing...")
        self.real_part = real
        self.image_part = image
    def displayNumber(self):
        print("{0},{1}".format(self.real_part,self.image_part))

x = Number(50,10)

x.displayNumber()

# x2 = Number(60,10)
# x2.new_attribute = 80

#print(x2.real_part,x2.image_part,x2.new_attribute)

# ask yourself why python didn't gave me result? print(x.new_attribute)

#To delete object attributes or the object:

# del x.real_part
# print(x.real_part)

#del x
#print(x.image_part)
#print(x.real_part)
#del Number