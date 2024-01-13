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
