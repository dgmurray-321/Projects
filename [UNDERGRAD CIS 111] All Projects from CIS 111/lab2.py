print("Part 1:")
print() 
feet = int(input("Enter the portion of your height in (whole) feet: "))
inches = int(input("Enter the poriton of your height in (whole) inches: "))
total_inches = feet*12+inches
centi=total_inches*2.54 
print("Your are", feet,"feet","and",inches,"inches, this is", centi, "centimeters" )

print("Part 2:")
print()
weight = int(input("Enter your weight in (whole) pounds: "))
kilo = weight/2.2046
print("Your weight is", kilo,"kilograms")