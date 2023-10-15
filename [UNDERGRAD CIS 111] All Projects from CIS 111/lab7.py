print("Part 1: ")
print()
height = int(input("Enter your height in inches: "))
feet = height//12 
inches = height%12 
if inches >1: 
    print("You are " ,feet, "feet,", inches, "inches tall")
if inches ==1: 
    print("You are ", feet,"foot," ,inches, "inch tall")
if inches==0:
    print("Your are", feet, "foot tall")
print()
print("Part 2: ")
print()
grade = float(input("Enter your GPA: "))
if grade >=3.95 and grade <= 4.0:
    print("Academic Honors: Summa cum laude")
elif grade >= 3.85 and grade <= 3.949: 
    print("Academic Honors: Magma cum Laude")
elif grade >= 3.75 and grade <= 3.849: 
    print("Academic Honors: Cum Laude")
elif grade > 0 and grade <= 3.749: 
    print("No distinction")
else: 
    print("Error! Must be between 0-4.0") 


