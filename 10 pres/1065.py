import sys
def ispr(num):
    dif=num%10-(num//10)%10
    ck=0
    while num//10:
        if(num%10-(num//10)%10)!=dif:
            ck=1
            break
        num//=10
    if not ck:return True
    else:return False
N=int(sys.stdin.readline())
cnt=0
for i in range(1,N+1):
    if ispr(i):cnt+=1
print(cnt)