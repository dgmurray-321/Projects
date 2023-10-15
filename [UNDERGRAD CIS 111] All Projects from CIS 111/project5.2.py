#Project 5
#CIS 111
#Drew Murray

# Function Name: get_hours
#Function description: Finds the hours in a single job duration, and turns the value into an integer
def get_hours(list):
    string=list.split(":")
    return int(string[0])
#Function Name: get_minutes
#Function description: Finds the minutes in a single duration and turns the value into an integer
def get_minutes(list):
    string = list.split(":")
    return int(string[1])
#Function Name: get_minutes
#Function description: Finds the seconds in a single duration and turns the value in a integer
def get_seconds(list):
    string = list.split(":")
    return int(string[2])
#Function Name: get_shortest
#Function description: finds the shortest time in the list of job durations 
def get_shortest(job_list):
    short = job_list[0]
    for i in job_list:
        if get_hours(short) > get_hours(i):
            short = i
        elif get_hours(short) == get_hours(i):
            if get_minutes(short) > get_hours(i):
                short = i 
            elif get_minutes(short) == get_minutes(i):
                if get_seconds(short) > get_seconds(i):
                    short = i
    return short
#Function Name: get_longest
#Function description: Finds the longest time in the list of job durations
def get_longest(job_list):
    long = job_list[0]
    for i in job_list:
        if get_hours(long) < get_hours(i):
            long = i
        elif get_hours(long) == get_hours(i):
            if get_minutes(long) < get_hours(i):
                long = i 
            elif get_minutes(long) == get_minutes(i):
                if get_seconds(long) < get_seconds(i):
                    long = i
    return long
#Function Name: get_average
#Funcion description: Finds the average time for the list of job durations
def get_average(job_list):
    sum_seconds = 0
    for i in job_list:
        hours = get_hours(i)
        minutes = get_minutes(i)
        seconds = get_seconds(i)
        sum_seconds+=(hours*60*60)+(minutes*60)+(seconds)
    avg = sum_seconds//len(job_list)
    hours = avg//3600
    minutes = (avg%3600)//60
    seconds = (avg%3600)%60
    return "%d:%d:%d" %(hours,minutes,seconds)

#main code
print("Working with multiple functions in Python")
print()
time = input("Enter a list of job durations (hours:minutes:seconds), seperated by commas: ")
time_list= time.split(",") 
shortest = get_shortest(time_list)
longest = get_longest(time_list)
time_avg = get_average(time_list)
print()
print("Shortest time of the job:", shortest)
print()
print("Longest time of the job:", longest)
print()
print("Average job length:", time_avg)
