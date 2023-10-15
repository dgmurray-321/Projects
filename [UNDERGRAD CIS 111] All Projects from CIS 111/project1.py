#Project 1 
#CIS 111
#Drew Murray
print("Program to compute the area of a trapezoid")
print()
top= float(input("Enter the length of the top-base of the trapezoid: "))
bottom = float(input("Enter the length of the bottom=base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))
area = ((top+bottom)/2)*height
print("The area of the trapezoid with a top-base of", top,", a bottom base of", bottom, ",and a height of", height,
"is", area,"square units!")
