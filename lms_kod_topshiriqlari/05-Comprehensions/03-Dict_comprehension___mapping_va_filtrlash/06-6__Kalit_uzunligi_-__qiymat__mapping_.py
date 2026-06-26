n = int(input())

d = [input().split() for _ in range(n)]

r = {len(key): int(value) for key, value in d}

print(r)