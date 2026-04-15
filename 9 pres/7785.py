N=int(input())
dit=set()
for _ in range(N):
    k,a=map(str,input().split())
    if(a=="leave") and k in dit:dit.remove(k)
    else:dit.add(k)
dit=sorted(dit,reverse=True)
for i in dit:
    print(i)