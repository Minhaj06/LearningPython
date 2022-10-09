import datetime

currentYear = datetime.date.today().year
print(currentYear)

birthYear = int(input("Enter your date of birth: "))

curretnAge = currentYear - birthYear

# print("Your current age is : ", curretnAge)

if curretnAge <= 18:
    print("Hey, you are under 18 and your current age is", currentYear)
else:
    print("Hey, you are over 18 and your current age is", curretnAge)
