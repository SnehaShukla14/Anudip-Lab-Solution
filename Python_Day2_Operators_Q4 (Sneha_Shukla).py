# 4. Python program to find the area of a triangle whose sides are given.

# Three sides of the triangle is a, b and c:  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)


""" OUTPUT:
Enter first side: 8
Enter second side: 6
Enter third side: 4
The area of the triangle is 11.62."""
