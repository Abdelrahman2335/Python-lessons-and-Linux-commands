# iterating a string through a for loop and adding the letters to a list 

# h_letters = []

# for x in 'human':
    # h_letters.append(x)
    # print(h_letters)

# watch the different when you put print(h_letters on the loop)
# print(h_letters)


# using comprehension

# h_letters = [letter for letter in 'human']
# print(h_letters)

# list comprehensions vs lambda function

# h_letters = list(map(lambda x: x, 'human'))
# print(h_letters)

# if with list comprehension

# number_list = [x for x in range(20) if x % 2 == 0 and x != 0]
# print(number_list)

# nested if with list comprehension 

# num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
# print(num_list)

# if...else with list comprehension

# obj = ["Even" if  i%2==0 else "Odd" for i in range(10)]
# print(obj)

# transposing a matrix using list comprehension

matrix = [[1, 2],[3, 4],[5, 6],[7, 8]]
transpose = [[row[i] for row in matrix]for i in range(2)]
print(transpose)