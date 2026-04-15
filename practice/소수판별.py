import time
n = int(input("자연수 >"))
start_time = time.time()
check = 0
for i in range(1,int(n**0.5)):
    if not (n%(i+1)):
        check+=1
        break
if check : print("소수아님")
else : print("소수임")
print("걸린 시간 :", time.time() - start_time)