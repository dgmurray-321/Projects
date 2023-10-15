print("Part 1: ")
word = input("Enter a word: ")
length = int(input("Enter the length: "))
def divide_word():
    for i in range(0, len(word), length): 
        piece = word[i:i+length]
        print(piece) 

def inside_out(): 
    left =(length/2)-1
    right = (length/2)+1
    for i in range(0,len(word), length): 
        if left != 0: 
            print(word[i:i+left])
            left+=-1
        if right != word[word(len)]:
            print(word[i:i+right])
            right +=1
divide_word()
print("Part 2: ")
inside_out()




