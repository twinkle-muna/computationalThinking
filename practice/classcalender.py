month = int(input())

daysmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

january = 3

start = january

for i in range(month -1):
    start = (start + daysmonth[i]) %7

days = daysmonth[month-1]
print("Mo Tu We Th Fr Sa Su")

for i in range(start):
    print("  ", end="")

day =1

for i in range (days):
    print(f"{day:2d}", end=" ")
    day += 1

    if(start + i + 1) % 7 == 0:

