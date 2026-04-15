a, b = map(int, input().split())

start = min(a, b)
end = max(a, b)

n = end - start + 1

print(n * (start + end) // 2)