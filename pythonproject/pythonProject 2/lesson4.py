x = (["a", "b", "c", "d", "e","e","e"])

# To know the type of x:
print(type(x))

y = {5,10,15,25,20,30}

z = {40,45,50}

#You can't use this functions to add something in the set{} you usually use this function in the list[]
# y.append(35)
#y.insert(1,0)
#y.extend(z)
#print(y)

#You can use add to add only one argument in the (set):
# y.add(0)

#To add more you can use update function:

# y.update([0,1,2,3,4])

#We can use it also to add list or set:

# y.update([40,45,50,55], {60,65,75,80})

#This function do the same job of extend function in the list[]

#w = y.union(x)
#print(w)
#print(y.union(x))

# please know that union you have to gave it a variable or use print() to use it 
# but if you use it to do some changes in the value of the set it would not work 
# so you can use update rather than it.
y.union(x)
print(y)

#To sort in set we use sorted function:
# print(sorted(y))

#To delete any element we can use this functions, note that if you use "discard" and you 
# gave it element not exist in the set no error will appear, but if you use "remove" and 
# the element not exist it will return with error, otherwise there is no different.

# y.discard(0)
# y.remove(0)

#This one will delete the set but it will still exist.
# y.clear()
# print(y)
