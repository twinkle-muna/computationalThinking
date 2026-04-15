scores = []

for _ in range(5):
    n = int(input())
    if n < 40:
        n = 40
    scores.append(n)

print(sum(scores) // 5)