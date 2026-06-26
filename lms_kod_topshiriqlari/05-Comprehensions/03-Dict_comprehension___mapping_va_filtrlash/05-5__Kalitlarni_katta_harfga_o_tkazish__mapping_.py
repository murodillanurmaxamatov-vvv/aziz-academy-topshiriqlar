n = int(input())
d = [input().split() for _ in range(n)]

r = {key.upper(): int(value) for key, value in d}

print(r)