n = int(input())
count = {}
for _ in range(n):
    title = input().strip()
    
    if title in count:
        count[title] += 1
    else:
        count[title] = 1
max_count = max(count.values())
result = sorted([title for title in count if count[title] == max_count])
print(result[0])