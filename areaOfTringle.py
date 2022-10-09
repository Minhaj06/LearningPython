import math

a = float(input("Enter the first length of tringle: "))
b = float(input("Enter the second length of tringle: "))
c = float(input("Enter the third length of tringle: "))

if a+b > c and b+c > a and c+a > b:

    s = (a+b+c)/2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("The are of tringle is : ", area)

else:
    print("Tringle is not possible!")

# Alternative Rule:
# if a+b <= c or b+c <= a or a+c <= b:
#     print("Tringle is not possible!")
# else:
#     s = (a+b+c)/2

#     area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#     print("The are of tringle is : ", area)
