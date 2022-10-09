n = float(input("Enter an integer : "))

p = n * (-1)

result = n+p

if n == 0:
    print("0 is always positive")
else:
    if result == 0:
        print("The opposite number of", n, "is", p)
    else:
        print("Something went wrong!")
