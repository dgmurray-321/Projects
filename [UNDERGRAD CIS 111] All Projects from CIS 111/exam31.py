email = []
for i in range(3): 
    email.append(input("Enter email: "))
for x in len(email):
    if x %2  == 0: 
        print("Length", x)
        print("Even length")
    if x % 2 ==1:
        print("Length", x)
        print("Odd length") 

