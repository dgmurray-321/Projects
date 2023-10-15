sale = float(input("Enter the amount spent: "))
print("Part 1: ")
print()
if sale > 50: 
    s = sale - 50 
    sw = sale - (s- (s*.6))
    ss = sw + (sw*.095)
    print("Amount after sale: $%.2f" %sw)
    print("Final amount afer tax: $%.2f" %ss)
else: 
    s2 = sale + (sale*.095)
    print("Amount after sale: $%.2f" %sale)
    print("Final amount after tax: $%.2f" %s2)
print()
print("Part 2:")
print()
age = int(input("Enter your age: "))
if age >= 60: 
    asw = sw-(sw*.1)
    asw2 = asw + (asw*.095)
    print("Amount after discount: $%.2f" %asw)
    print("Final amount after tax: $%.2f" %asw2)
else: 
    print("No discount applied.")
    print("Final amount after taxes: $%.2f" %ss)
