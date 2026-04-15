import sys
primes=[0]*10005
M=int(input())
N=int(input())
sum=0
ans=10005
primes[0]=1
primes[1]=1
for i in range(2,int((N+1)**0.5)+2):
    for j in range(i**2,N+1,i):
        primes[j]=1
for i in range(M,N+1):
    if not primes[i]:
        sum+=i
        ans=min(ans,i)
if not sum:print(-1)
else:print(sum,ans,sep='\n')