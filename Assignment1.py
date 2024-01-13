#1
"""a = float(input("Enter the height of rectangle: "))
if a % 1==0:
    a = int(a);
print("output the perimeter = " + str(4*a))
print("output the  area = " + str(a**2) )"""
#2
"""a = float(input("  enter any first number: "))
b = float(input(" enter any second number: "))
if a % 1 and b % 1 ==0:
    a = int(a);
    b = int(b);
print("output the perimeter = " + str(a*b))
print("output the  area = " + str(2*a+2*b))"""
#3
"""a = float(input(" enter any first number: "))
b = float(input(" enter any second number: "))
c = float(input(" enter any third number: "))
if a % 1 and b % 1 and c%1 ==0:
    a = int(a);
    b = int(b);
    c = int(c);
print("output the volume = " + str(a*b*c))
print("output the  area = " + str(2*(a*b+b*c+a*c)))"""
#4
"""import math
a = float(input(" enter any first number: "))
b = float(input(" enter any second number: "))
Raiymbek = math.sqrt(a*b)
if  Raiymbek%1 == 0:
    Raiymbek = int(Raiymbek)
print("output the square = " + str(Raiymbek) )"""
#5
"""import math
a = float(input(" enter any first number: "))
b = float(input(" enter any second number: "))
c = math.sqrt(a**2 + b**2)
der = a+b+c
if der % 1 and c % 1==0:
    c = int(c)
    der = int(der)
print("output the perimetr = " + str(der))
print("output the perimetr = " + str(c))"""
#6
"""a = int(input(" enter any number: "))
b = int(input(" enter any number: "))
c = int(input(" enter any number: "))
a,b,c=b,c,a
print()
print(a)
print(b)
print(c)"""
#7
"""a = int(input(" enter any number: "))
b = int(input(" enter any number: "))
c = int(input(" enter any number: "))
a,b,c = c,a,b
print()
print(a)
print(b)
print(c)"""
#8
"""def calculate_function_value(x):
    result = 3 * x**2 - 6 * x + 7
    return result
x_value = 2
result = calculate_function_value(x_value)

print(f"The value of the function for x = {x_value} is: {result}")

"""
#9
"""def calculate_function_value(x):
    result = 4 * (x - 3)**2 + 7 * (x - 2) + 2
    return result

# Example: Find the value of the function for x = 5
x_value = 5
result = calculate_function_value(x_value)

print(f"The value of the function for x = {x_value} is: {result}")
"""
#10
"""name = input("Enter your name: ")
print(f"Hello, {name}!")
"""
#11
"""number = int(input("Enter a four-digit integer: "))
digit_sum = sum(map(int, str(number)))
print(f"The sum of the digits is: {digit_sum}")
"""
#12
"""seconds = int(input("Enter a number of seconds: "))
days, remainder = divmod(seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"{days} days, {hours:02}:{minutes:02}:{seconds:02}")
"""
#13
"""K = int(input("Enter a day of the year (1-365): "))
day_of_week = (K - 1) % 7
print(f"The day of the week for day {K} is: {day_of_week}")
"""
#14
"""# Get input from the user
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
c = float(input("Enter the third number (c): "))

# Sort the values
sorted_values = sorted([a, b, c])

# Display the result
print(f"The numbers in increasing order: {sorted_values}")
"""
#15
"""# Get input from the user
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
c = float(input("Enter the third number (c): "))
d = float(input("Enter the fourth number (d): "))

# Calculate sum, difference, and product
sum_result = a + b + c + d
difference_result = a - b - c - d
product_result = a * b * c * d

# Display the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
"""
#16
"""# Get input from the user
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

# Calculate the expression
result = (|x| + |y|) / (1 + |x*y|)

# Display the result
print(f"The result of (|x| + |y|) / (1 + |x*y|) is: {result}")
"""
#17
"""def calculate_cube_properties(edge_length):
    volume = edge_length**3
    surface_area = 6 * edge_length**2
    return volume, surface_area

# Example: Input edge length of the cube
edge_length = float(input("Enter the edge length of the cube: "))

volume, surface_area = calculate_cube_properties(edge_length)

print(f"The volume of the cube is: {volume}")
print(f"The surface area of the cube is: {surface_area}")
"""
#18
"""def calculate_mean_geometric(numbers):
    arithmetic_mean = sum(numbers) / len(numbers)
    geometric_mean = (numbers[0] * numbers[1])**0.5
    return arithmetic_mean, geometric_mean

# Example: Input two positive real numbers
num1 = float(input("Enter the first positive real number: "))
num2 = float(input("Enter the second positive real number: "))

arithmetic_mean, geometric_mean = calculate_mean_geometric([num1, num2])

print(f"The arithmetic mean is: {arithmetic_mean}")
print(f"The geometric mean is: {geometric_mean}")
"""
#19
"""import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

top = math.sqrt(abs(x - 1)) - abs(y)**(1/3)
bottom = 1 + (x**2/2) + (y**2/4)
a = top / bottom

b = x * (math.atan(z) + math.exp(-(x + 3)))

print(f"a = {a}")
print(f"b = {b}")"""
#20
"""import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

top = 3 + math.exp(y - 1)
bottom = 1 + x**2 * abs(y - math.tan(z))
a = top / bottom

b = 1 + abs(y - x) + ((y - x)**2/2) + (abs(y - x)**3/3)

print(f"a = {a}")
print(f"b = {b}")"""
#21
"""import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

top = (1 + y) * (x + y / (x**2 + 4))
bottom = math.exp(-x - 2) + (1/(x**2 + 4))
a = top / bottom

btop = 1 + math.cos(y - 2)
bbottom = (x**4/2) + math.sin(z) ** 2
b = btop / bbottom

print(f"a = {a}")
print(f"b = {b}")"""
#22
"""import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

bottom = y**2 + abs(x**2/(y + (x**3/3)))
a = y + (x/bottom)

b = 1 + math.tan(z/2)**2

print(f"a = {a}")
print(f"b = {b}")"""
#23
"""import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

top = 2 * math.cos(x - (math.pi/6))
bottom = (1/2) + math.sin(y)**2
a = top / bottom

bbottom = 3 + (z**2/5)
b = 1 + (z**2/bbottom)

print(f"a = {a}")
print(f"b = {b}")"""
#24
"""import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

top = 1 + math.sin(x + y)**2
bottom = 2 + abs((x - 2 * x) / (1 + (x**2 * y**2)))
a = (top / bottom) + x

b = math.cos(math.atan(1/z))**2

print(f"a = {a}")
print(f"b = {b}")"""
#25
"""import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

a = math.log(abs(y-math.sqrt(abs(x)) * (x - y/(z + x**2/4))))

b = x - (x**2/(2*3)) + (x**5/(2*3*4*5))

print(f"a = {a}")
print(f"b = {b}")"""
#26
"""import math
x1 = float(input('Enter x1: '))
y1 = float(input('Enter y1: '))
x2 = float(input('Enter x2: '))
y2 = float(input('Enter y2: '))
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print('The distance between points = ' + str(d))"""
#27
"""import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    side1 = calculate_distance(x1, y1, x2, y2)
    side2 = calculate_distance(x2, y2, x3, y3)
    side3 = calculate_distance(x3, y3, x1, y1)

    perimeter = side1 + side2 + side3
    return perimeter

# Example: Input vertices (x1, y1), (x2, y2), (x3, y3)
x1, y1 = map(float, input("Enter coordinates of vertex 1 (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of vertex 2 (x2 y2): ").split())
x3, y3 = map(float, input("Enter coordinates of vertex 3 (x3 y3): ").split())

perimeter = calculate_triangle_perimeter(x1, y1, x2, y2, x3, y3)

print(f"The perimeter of the triangle is: {perimeter}")
"""
