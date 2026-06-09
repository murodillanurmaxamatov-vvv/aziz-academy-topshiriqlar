x = list(map(int, input().split()))

n = sorted(set(x))
print(*n)