my_list = [1, 2, 3, 4, 5]

print(my_list)

# create an iterator for my_list
my_iter = iter(my_list)

# use the iterator to get each element of the list
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # 4
print(next(my_iter))  # 5


# list = [44,77,11,55]

#Get an iterator using iter() method

# list2 = iter(list)

# print(type(list2))

#iterate through it using next() method


# print(next(list2))
# print(next(list2))

# we can use for loop here

# for i in list2:
#     print(i)

# print(list2) # you can't use it like this CUZ it will give you the location in memory.

# next(obj) is same as calling obj.__next__() method

# print(list2.__next__())
# print(list2.__next__())

# next(list2)  # this one will case an error because there is no more elements

# print(next(list2))

# Why the output dont't include 11 ? CUZ we give it to the red point and we did't print it.

#Creating a custom iterrator

# class Pow_Of_Tow:
#     """Class to implement an iterator of power of tow"""

#     def __init__(self,max=0):
#         self.max = max

#     def __iter__(self):
#         self.n = 0
#         return self

#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration

# print(Pow_Of_Tow.__doc__)
# a = Pow_Of_Tow(4)
# i = iter(a)
# print(i.__next__())
# print(next(i))
# print(next(i))


#Creating a infinite custom iterrator

class Infinite_Iter:
    """Infinite iterator to return all odd numbers"""

    def __iter__(self):
        self.num = 0
        return self
    def __next__(self):
        num = self.num
        self.num += 5
        return num

i = Infinite_Iter()
a = iter(i)
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# we can use for loop here

# x = 0
# for y in i:
#     if(x <= 5 ):
#         print(y)
#         x += 1
#     else:
#         break