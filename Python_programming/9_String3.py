# !String format
fname = "John"
lname = "Doe"
age = 21

print(f"Name:{fname} {lname} ")

value = 42
print("{:04d}".format(value))

person = {'name': 'Alice', 'age': 30}
print("Name: {name}, Age: {age}".format(**person))


fname = "John"
lname = "Doe"
age = 21

print(f"Name:{fname:>{10}} {lname:>{20}}")