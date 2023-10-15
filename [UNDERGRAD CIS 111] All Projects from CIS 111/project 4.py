#Project 4 
#CIS 111
#Drew Murray
print("Grouping ten (10) names into Alphabetical Categories")
print()
name = []

for i in range(1,11):
    n = input("Enter name %d: " %i).lower()
    name.append(n)
print()
print("Names beginning with letters (A-H):")
for a_H in name:
    if a_H[0] == 'a' or a_H[0] =='b' or a_H[0] =='c' or a_H[0] =='d' or a_H[0] =='e' or a_H[0] =='f' or a_H[0] == 'g' or a_H[0] =='h': 
        print(a_H)
print()
print("Names beginning with Letters (I-O): ")
for i_O in name: 
    if i_O[0] == 'i' or i_O[0] =='j' or i_O[0] =='k' or i_O[0] =='l' or i_O[0] =='m' or i_O[0] =='n' or i_O[0] =='o':
        print(i_O)
print()
print("Names beginning with Letters (P-Z): ")
for z in name: 
    if z[0] == 'p' or z[0] == 'q'or z[0] =='r' or z[0] =='s'or z[0] =='t' or z[0] =='u' or z[0] =='v' or z[0] == 'w' or z[0] =='y' or z[0] =='z':
        print (z)


