people, max = 0,0
for _ in range(4):
    a, b = map(int, input().split())
    people += b-a
    max = max(people, max)
print(max)

