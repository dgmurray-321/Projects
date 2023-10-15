time = input("Enter a list of job durations (hours:minutes:seconds), separated by commas:")
colon_time = time.replace(":", ",")
#print(colon_time)
time_list = colon_time.split(",")
for i in range(0,len(time_list)): 
    time_list[i]= int(time_list[i])
print(time_list)

#first = time_list[0]
#print(first[0])


def get_hours(): 
    print("The hours are: ")
    for i in range(0, len(time_list), 4):
        hours = time_list[i:i+2]
    print(hours)
get_hours()
#max(get_hours())
#5:35:25,1:05:00,2:15:45,1:00:00,5:35:30