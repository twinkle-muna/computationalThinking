import datetime

ct = datetime.datetime.now()

if ct.hour < 12 : print("현재 시간은 %d시로 오전입니다." %ct.hour)
else : print("현재 시간은 %d시로 오후입니다." %ct.hour)