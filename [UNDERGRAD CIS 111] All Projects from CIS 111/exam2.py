email = [] 

for i in range(3): 
    email.append(input("Enter an email: "))
l = len(email)
count = 0
c = 0
while count > len(list[email]): 
    if count % 2 == 0:
        print("length:", l)
        print("Even length")
    count+=1
    if count %2 ==1: 
        print("Length:",l)
        print("Odd length")
    count+=1
 