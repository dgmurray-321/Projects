def find_scores(dict):
    print("Part 1: ")
    grade = {}
    for i in range(10):
        name = input("Enter name: ")
        score = int(input("Enter score: "))
        print()
        grade[name]=score
    print()
    print("Students with at least a score of 80: ")
    for x in grade:
         if grade[x] >= 80:
            print(x)
#Url: https://realpython.com/sort-python-dictionary/
# The sorted function sorts the dictionary by it's key, however using the key parameter, it makes the computer select the value
#that the element is comparing to. It goes by ascending order, so you would have to set the reverse parameter to true
# to sort the dictionary to descending order
    print()
    print("Part 2: ")
    print()
    print("Students with the highest scores (highest to lowest): ")
    h= sorted(grade.items(), key = lambda x: x[1], reverse=True)
    print(h)

find_scores({})

