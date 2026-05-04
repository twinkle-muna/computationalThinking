import random

def make(n):
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(1, n*n*10 - 1))
        m.append(row)
    return m

def show(m):
    for r in m:
        for x in r:
            print(f"{x:4}", end="")
        print()
    print()

def t(m, n):
    res = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m[j][i])
        res.append(row)
    return res

n = int(input("N (2~5): "))

m = make(n)

print("Original:")
show(m)

tm = t(m, n)

print("Transposed:")
show(tm)