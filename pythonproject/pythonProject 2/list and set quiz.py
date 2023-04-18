brands = ["Vivo", "Apple", "Google", "Microsoft", "BMW"]

# add "BYD"
# replace "BMW" by "Ferrari"
# remove "BMW"
# remove "Google"
# count how much brands in this list
# how many "Apple" in this list 
# print from Apple to Microsoft and then print from Apple to BMW

# brands.insert(3, "BYD")
# brands[-1] = "Ferrari"
# brands.pop(2)
# print(brands)
# print(len(brands))
# print(brands.count("Apple"))
# print(brands[1:4])
# print(brands[1:])

brands_set = {'Volvo'}

brands_set.update(brands)

# print(brands_set)

# add "Samsung"
# sort brands_set
# remove "Microsoft"
# count how much brands in this set
# remove "Samsung"
# add "Samsung and Twitter and Meta and Uber"


brands_set.add("Samsung")
sorted(brands_set)
brands_set.discard("Microsoft")
print(len(brands_set))
brands_set.remove("Samsung")
brands_set.update(["Samsung, Twitter, Meta, Uber"])

print(brands_set)
