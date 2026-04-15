cnt=0
def hanoi(n,start,mid,end):
    global cnt
    if(n==1):
        print(n,":",start,"->",end)
        cnt+=1
    else:
        hanoi(n-1,start,end,mid)
        print(n,":",start,"->",end)
        cnt+=1
        hanoi(n-1,mid,start,end)
hanoi(2,"A","B","C")
print(cnt)