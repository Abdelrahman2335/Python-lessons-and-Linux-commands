# Declaring and defining a nested dictionary

people = {1: {'name':'John','age':'27','gender': 'male'},
        2:{'name':'Maria','age':'27','gender': 'female'}}
people[3] = {}

#adding elements to a dictionary

people[3]['name'] = 'Shen'
people[3]['age'] = '25'
people[3]['gender'] = 'male'
people[3]['married'] = 'no'

#Iterationg through a nested dictionary
print(people.items())

for x_id, y_info in people.items():
    print("\nperson ID",x_id)

    for key in y_info:
        print(key + ':', y_info[key])
# print(people.items())


# This maybe difficult but you can do it ;)