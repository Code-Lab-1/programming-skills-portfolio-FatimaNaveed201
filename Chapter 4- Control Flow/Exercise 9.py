#checking if a triangle is isosceles, equilateral or scalene

print("Enter the lengths of the sides of the triangle: ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == b == c:
    print("The triangle is an equilateral triangle.")
elif a == b or b == c or c == a:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")