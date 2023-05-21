# QUESTION 3
'''Program to calculate the area of a triangle using heron’s formula. (check condition if 
the combination of sides is possible).'''

import math
# first checking whether triangle is possible or not
side1 = float(input("enter the length of first side:"))
side2 = float(input("enter the length of second side:"))
side3 = float(input("enter the length of third side:"))
# side1,side2,side3 are variables declared for sides of traingles

if(side1>=side2+side3) or (side2>=side1+side3) or (side3>=side2+side1):
    print("traingle is not possible with given sides")
else:
    print("triangle is possible")

# herons formula =root(s(s-a)(s-b)(s-c))
# where s(semi perimeter)=(a+b+c)/2 #where a,b,c are sides of triangle
s=float((side1+side2+side3)/2)
area = float(s*(s-side1)*(s-side2)*(s-side3))
x = float(math.sqrt(area))
if("triangle is possible"):
    print("area of triangle is:",x)
