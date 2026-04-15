# 1월 1일이 목요일인 윤년이 아닌 해의 한달 달력을 이쁘게 출력하기 (not 2024년)
# 월을 입력받고 아래 그림의 예와 같이 줄을 맞춰 한달 달력을 출력하라
month_start = [4, 0, 0, 3, 5, 1, 4, 6, 2, 4, 0, 2]
user_month = int(input())
loopday =1
start_day = month_start[user_month - 1]
printday = 0
print(" \t", end= "")
print(str(user_month) + " 월")
print("일 월 화 수 목 금 토")
if user_month == 2:
    day = 28
elif user_month in [1, 3, 5, 7, 8, 10, 12]:
    day = 31
else:
    day = 30
# moth start 시작 하는요일
# #공백을 출력하면서 시작
for i in range(0, start_day):
        print("  ", end =" ")
for i in range(start_day, 7):
        print(f"{i-start_day+1:2d}", end = " ")
        loopday += 1
print("")
weekday = start_day
while loopday <= day:
    print(f"{loopday:2d}", end=" ")
    loopday += 1
    weekday += 1
    printday +=1

    if printday == 7:
         weekday = 0
         print("")
         printday = 0