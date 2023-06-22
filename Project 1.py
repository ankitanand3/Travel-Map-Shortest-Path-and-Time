import random


month_travel = random.randint(15,25) # Choosing month travel random from 15 to 25
def one_step(x,y): # This function lets user to travel on step from current position, either right ot straight depending on the leeser wait time
    """This function lets user to travel on step from current position, either right ot straight depending on the leeser wait time"""
    x_wait_time = random.uniform(0, 75) # Choosing random wait time for x
    y_wait_time = random.uniform(0, 75) # Choosing random wait time for y
    wait_time = min(x_wait_time, y_wait_time) # Choosing minimum wait time out of x  and y
    if y_wait_time > x_wait_time: # Checking if y wait time is greater than x wait time 
        x = x + 1 # Increasing x so that it can go straight

    elif x_wait_time > y_wait_time: # Checking if x wait time is greater than y wait time
        y = y + 1 # Increasing y so that it can go right


    step_set = (x,y,wait_time) # setting x and y present position with the wait time
    return step_set

def one_commute(x, y): # Computes the successive wait_times for a given set of (x, y)
    """Computes the successive wait_times for a given set of (x, y)."""
    wait_times = []  # Creating an empty list

    while x < 5 or y < 5:  # Set the loop condition

        x_, y_, wait_time = one_step(x, y)  # Get the right values from 'one_step'
        if x_ <= 5 and y_ <= 5:  # Check for any overrun
            x, y = x_, y_  # Increment the variables
            wait_times.append(wait_time)  # Append the list with the wait_time

    return x, y, wait_times  # Return the coordinates and the wait_times


def month_max():
    """Runs previous function month_max times and returns max travel time of that month"""
    wait_times = []  # Creating an empty list

    for i in range(month_travel):
        x, y, wait_time = one_commute(0, 0)  # Get the right values from 'one_step'
        sum_wait_times = sum(wait_time)
        wait_times.append(sum_wait_times)  # Append the list with the wait_time
    return max(wait_times) # Getting maximum wait time of the month
wait_times_new = [] # Creating an empty list
def ave_max(n):
    """This function runs previous function n number of times and takes the average of all maximum travel times"""
   

    for i in range(n):
        x = month_max()
        wait_times_new.append(x)  # Append the list with the wait_times_new
        
    return sum(wait_times_new)/len(wait_times_new) # Getting average
n = int(input("Enter number of months: "))
x = int(input("Enter x position: "))
y = int(input("Enter y position: "))
aver = ave_max(n) # Calling function ave_max
sec_to_min = aver/60 # Converting seconds to minute
sec_to_min_round = round(sec_to_min,1) # Rounding off value

X, Y, TIMES = one_commute(x, y) # Calling function one_commute
sum_wait_time = sum(TIMES)
sec_to_min_round_str = str(sec_to_min_round) # Converting sec_to_min_round to string

sec_to_min_round_str_list = list(sec_to_min_round_str) # Converting sec_to_min_round_str to a list
min_time = sec_to_min_round_str_list[0]
sec_time = sec_to_min_round_str_list[-1]
print("The average maximum travel time was", min_time, "minutes and", sec_time, "seconds")

