def subt_tree(x,y,z):
    q = x-y-z
    return q
def count_between(list1, upper, lower):
    count = 0
    for x in list1:
        if lower <= x<=upper: 
            count+=1
    return count
     
#list2 = [10,20,30,40,50,60]
#answer = count_between(list2,15,50)
#print(answer)

def split_num():
    num = input("Enter a number: ")
    s = num.split(",")
    a = int(s[0])+int(s[-2])
    return a 
#
lines = [[0,0,0],[1,1,1],[2,2,2]]
er = lines[0].append(10)
lines[1].append(10)
lines[2].append(10)
lines[0].append(10)
lines[0].pop(0)
lines[1].pop(0)
lines[2].pop(0)

for i in lines:
    for j in i:
        e+=i

#t = split_num()
#print(t)
#num_1 = int(input("Enter value: "))
#num_2 = int(input("Enter a value: "))
#num_3 = int(input("Enter a value: "))

#answer = subt_tree(num_1, num_2, num_3)

