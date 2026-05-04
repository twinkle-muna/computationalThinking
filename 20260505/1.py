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

def mul(a, b, n):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]
    return res

def plus(a, b, n):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = a[i][j] + b[i][j]
    return res

n = int(input("N (2~5): "))

a = make(n)
b = make(n)
c = make(n)

print("A:")
show(a)

print("B:")
show(b)

print("C:")
show(c)

ans = plus(mul(a, b, n), c, n)

print("A*B + C:")
show(ans)