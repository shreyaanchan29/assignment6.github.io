#. Write a Python program to check a triangle is equilateral, isosceles or scalene
x = int(input("Input length of the first side: "))
y = int(input("Input length of the second side: "))
z = int(input("Input length of the third side: "))
if x == y == z:
 print("Equilateral triangle")
elif x != y and y != z and x != z:
 print("Scalene triangle")
else:
 print("Isosceles triangle")