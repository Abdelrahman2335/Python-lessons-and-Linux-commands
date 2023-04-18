def maxnum(a,b):
    if a > b:
        return "a is the beggest num and it's",a
    elif a < b:
        return "b is the beggest num and it's",b
    else:
        print("the input is equal")

print(maxnum(50,50))


def x(*a): 
    sum = 0
    for i in a:
        sum += i
    return sum

print(x(4,5,2,3,6,3,9,1))

# * Here is very very important becuase it allows you to write many numbers in print(xt()) 