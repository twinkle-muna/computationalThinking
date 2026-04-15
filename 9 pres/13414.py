import sys
K,L = map(int,sys.stdin.readline().split())
dict={}
for i in range(L):
    ipt = str(sys.stdin.readline())
    dict[ipt]=i
dict=sorted(dict.items(), key=lambda x: x[1])
if K>len(dict):K=len(dict)
res=[]
for i in range(K):res.append(dict[i][0])
sys.stdout.write(''.join(res))