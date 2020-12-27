name = input("Please enter a name:")
surname = input("Please enter a surname:")
age = int(input("Please enter an age:"))
decimal = float(input("Please enter a decimal number:"))
value = int(input("Please enter a value:"))

print(type(name))
print(type(surname))
print(type(age))
print(type(decimal))
print(type(value))

print("Hello {}".format(name))
print(f'Your name is {name} and your surname is {surname}.')
print("You are {} years old.".format(age))
print(f'Your value: {value} and Your decimal: {decimal}')

