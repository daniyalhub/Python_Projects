import math

#   -----------FUNCTIONS----------  #
def circle():
    Radius = float(input("Enter the radius of circle: "))
    area = math.pi * (Radius**2)
    
    if Radius<=0:
        print("Radius must be positive number \n")
        return 
    
    area = math.pi * (Radius**2)
    print(f"The area of circle is {area}")

def square():
    lenght = float(input("Enter the lenght of one side of square: "))
    
    if lenght <= 0 :
        print("Lenght must be positive number \n")
        return
    
    area = lenght**2
    print(f"The area of square is {area}")

def triangle():
    base = float(input("Enter the base of one side of triangle: "))
    height = float(input("Enter the height of one side of triangle: "))
    
    if base <= 0 or height <= 0:
        print("Base and Height must be positive number \n")
        return
    
    area = 0.5 * base * height
    print(f"The area of triangle is {area}")

def rectangle():
    lenght = float(input("Enter the lenght of one side of rectangle: "))
    width = float(input("Enter the width of one side of rectangle: "))
    
    if lenght <= 0 or width <= 0:
        print("Lenght and width must be positive number \n")
        return 
    
    area = lenght * width
    print(f"The area of Rectangle is {area}")


def parallelogram():
    base = float(input("Enter the base of one side of Parallelogram: "))
    height = float(input("Enter the height of one side of Parallelogram: "))
    
    if base <= 0 or height <= 0:
        print("Base must be positive number \n")
        return
    
    area = base * height
    print(f"The area of Parallelogram is {area}")    

def trapezium():
    base1 = float(input("Enter the first base of one side of Trapezium: "))
    base2 = float(input("Enter the second base of one side of Trapezium: "))
    height = float(input("Enter the height of one side of Trapezium: "))
    
    if base1 <= 0 or base2 <= 0 or height <= 0:
        print("Base and Height must be positive number \n")
        return
    
    area = 0.5 * (base1 + base2) * height
    print(f"The area of Trapezium is {area}")

def rhombus():
    diagonal1 = float(input("Enter diagonal 1: "))
    diagonal2 = float(input("Enter diagonal 2: "))
    
    if diagonal1 <= 0 or diagonal2 <= 0:
        print("Diagonal must be positive number \n")
        return
    
    area = 0.5 * diagonal1 * diagonal2
    print(f"The area of Rombus is {area}")

def ellipse():
    axis_a = float(input("Enter semi-major axis (a): "))
    axis_b = float(input("Enter semi-minor axis (b): "))
    
    if axis_a <= 0 or axis_b <= 0:
        print("Values must be positive\n")
        return
    
    area = math.pi * axis_a * axis_b
    print(f"The area of Ellipse is {area}")

# ------ CLI interface ------

#   -----------BANNER----------  #

print("="*24)
print("="*24)
print("             AREA FINDER")
print("="*24)
print("="*24)

print("\nTHIS A SIMPLE AREA FINDER\n")


#   -----------MENU----------  #

print("You can find area of any of these")
print("1. Circle")
print("2. Square ")
print("3. Triangle")
print("4. Rectangle")
print("5. Parallelogram")
print("6. Trapezium")
print("7. Rhombus")
print("6. Ellipse")
print("0. Exit")
print("")

#   -----------MAIN LOOP----------  #
while True:
    try:
        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Thanks for using this program!\n")
            break

        elif choice == 1:
            circle()
        elif choice == 2:
            square()
        elif choice == 3:
            triangle()
        elif choice == 4 :
            rectangle()
        elif choice == 5 :
            parallelogram()
        elif choice == 6:
            trapezium()    
        elif choice == 7:
            rhombus()
        elif choice == 8:
            ellipse()
        else:
            print("Invalid choice! Please enter 0, 1, 2, or 3.\n")
    except:
        print("Invalid choice! Please enter a number between 0 to 6 \n")