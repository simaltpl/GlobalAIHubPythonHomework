FirstName = input("First name: ")
LastName = input("Last name: ")
Age = int(input("Age: "))
DateOfBirth = int(input("Date of Birth (just year): "))

Information = [FirstName,LastName,Age,DateOfBirth]

if Age < 18:
    print("You can't go out because it's too dangerous.")

elif Age > 18:
    print("You can go out to the street.")

for i in Information:
    print(i)
