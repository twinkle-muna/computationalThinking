from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))

count = defaultdict(int)

for num in cards:
    count[num] += 1

m = int(input())
queries = list(map(int, input().split()))

result = []

for q in queries:
    result.append(str(count[q]))

print(" ".join(result))