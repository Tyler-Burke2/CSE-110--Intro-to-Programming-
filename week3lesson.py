name = "Tyler"  # String
age = 20        # Integer
height = 5.10   # Float

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type}")
print(f"Height {height}, Type: {type(height)}")

a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
exponentiation = a ** b

print(f"Addition: {a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")
print(f"Exponentiation: {a} ** {b} = {exponentiation}")

print(f"The sum of {a} and {b} is {a + b}")

pi = 3.14159
print(f"Pi to two decimal places: {pi:.2f}")

def square(n):
    return n * n

number = 7
print(f"The square of {number} is {square(number)}.")