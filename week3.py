import math

print("Please enter the lenght and width of a rectangle or the radius of a circle. ")
choice = input("Enter 'Rectangle' or 'Circle' or 'Square': ")
 
if choice.lower() == 'Rectangle':
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")
 
elif choice.lower() == 'circle':
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print(f"The area of the circle is: {area:.2f}")

elif choice.lower() == 'square':
    side = float(input("Enter the length of a side of the square: "))
    area = side * side
    print(f"The area of the square is: {area}")
 
else:
    print("Invalid choice. Please try again.")