import math
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
print(f"b = {b}")