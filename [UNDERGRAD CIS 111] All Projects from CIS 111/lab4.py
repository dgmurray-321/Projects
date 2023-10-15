print("Part 1: ")
print()
slices = int(input("How many slices of pizzas are there?: "))
eat = int(input("How many people are eating?: "))
leftover = slices%eat
each = slices//eat
print()
print("Each person gets", each,"slices")
print("There will be", leftover,"leftover slices")
print()
print("Part 2:")
many = int(input("How many pizzas are there?: "))
cost = float(input("What is the cost of each pizza?:"))
total = many*cost
per_slice=total/(8*many)
print()
print("Total cost: ", total)
print("Cost per slice:", per_slice)

