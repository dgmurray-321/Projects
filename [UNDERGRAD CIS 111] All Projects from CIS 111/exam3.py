sweet_matrix = [10,20,30],[5,15,25],[1,2,3]
print(sweet_matrix)
sweet_matrix[1][1]=45
print(sweet_matrix)
a = sweet_matrix[0][0]+sweet_matrix[0][0]
print(a)
print(sweet_matrix)

def big_sum(sweet_matrix):
    list_sum = 0
    for little_list in sweet_matrix:
        for i in little_list:
            list_sum = list_sum + i 
    return list_sum
x = big_sum(sweet_matrix)
print(x)
