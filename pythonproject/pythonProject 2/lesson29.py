# Python Generators

def my_generator():

    n = 1
    print('This is printed first')
    # Genetator finction yield statements
    yield n 

    n += 1
    print('This is printed secind')
    yield n

    n += 1
    print('This is printed at last')
    yield n


genr = my_generator()

# iterrating using next
next(genr)
next(genr)
next(genr)

print("Using for loop...")
# iterrationg using for loop

 # Here we write my_generator not genr because 
 # if you use genr you will note get the value of n.
for item in my_generator():
    print(item)

# another example:

def my_generator():
    for i in range(10):
        yield i

gen = my_generator()
for i in gen:
    print(i)

