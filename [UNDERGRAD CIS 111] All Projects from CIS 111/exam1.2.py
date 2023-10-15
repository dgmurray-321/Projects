square_nums = []
v1 = int(input("Enter the first number: "))
square_nums.append(v1)
v2 = int(input("Enter the second number: "))
square_nums.append(v2)
v3 = int(input("Enter the third number:"))
square_nums.append(v3)
perfect_cube = [27,125,216]
square_cube = square_nums+perfect_cube
sum = min(square_cube)+max(square_cube)
print("//square_nums will contain: %f" %square_nums)
print("//sqaure cube will contain: %f" %square_cube)
print("Sums of first and last numbers:%f" %sum) 