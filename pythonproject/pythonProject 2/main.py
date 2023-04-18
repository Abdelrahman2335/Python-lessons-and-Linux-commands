n = int(input("Enter number:"))
i = 1 
while i <= n:
    j = 1
    while(j <= n - i):
        print(".",end="")
        j += 1
    j = 1 
    while j <= 2*i - 1:
        print("*",end="")
        j += 1
    print()
    i += 1