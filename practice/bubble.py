e = int(input())
array = list(map(int,input().split()))
for i in range(e):
    for j in range(i,e):
        if(array[j]<array[i]):
            array[i],array[j]=array[j],array[i]
print(array)