import time
import os

hours = int(input("Welcome to Timer.\nEnter hours:\n"))
minutes = int(input("\nEnter minutes:\n"))
seconds = int(input("\nEnter seconds:\n"))
start = str(input("\nPress S to start:\n"))

hours2 = 0
seconds2 = 0
minutes2 = 0

if seconds >= 60:
    m = seconds % 60
    seconds -= m
    n = seconds / 60
    minutes += n
    seconds += m
    seconds = seconds - (n * 60)
if minutes >= 60:
    k = minutes % 60
    minutes -= k
    j = minutes / 60
    hours += j
    minutes += k
    minutes = minutes - (j * 60)

while start == 's' or start == 'S':
    x = 6
    if x == 6:
        os.system('clear')
    print(hours2,":", minutes2, ":", seconds2, "\n")
    time.sleep(1)
    seconds2 += 1
    os.system('clear')
    while seconds2 >= 60:
        minutes2 += 1
        seconds2 = 0
    while minutes2 >= 60:
        hours2 += 1
        minutes2 = 0
    if hours2 == hours and minutes2 == minutes and seconds2 == (seconds + 1):
        print("Time's up")
        break
    
    
