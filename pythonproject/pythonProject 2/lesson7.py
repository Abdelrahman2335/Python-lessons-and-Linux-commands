dict = {1:"Hello", 2:"Hi", 3:"Hole"}
#print(dict)

#Her if you enter number not exist it will return error:
#print(dict[1])
#Her if you enter number not exist it will return none:
#print(dict.get(2))

#dict[3] = "Hey"
#print(dict)

x = {1:1, 2:4, 3:9, 4:16, 5:25}

#print(x.popitem())
#print(x)

#print(sorted(dict))

x = int(input("Enter number: "))
y = {v:v * v for v in range(x)}
print(y)